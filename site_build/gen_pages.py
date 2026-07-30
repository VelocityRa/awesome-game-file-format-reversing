"""Split README.md into the MkDocs page tree at build time.

Run by ``mkdocs-gen-files`` (see ``mkdocs.yml``). Nothing this script writes is
ever committed: pages are handed to MkDocs through the plugin's virtual
filesystem, so ``README.md`` stays the single source of truth for the list.

Pipeline
--------
1. ``annotate_headings`` computes every heading's **GitHub** anchor over the
   whole README -- including the headings inside the doctoc block, so the
   ``-1``/``-2`` duplicate counters match GitHub exactly -- and re-emits each
   heading with that anchor as an explicit ``attr_list`` id
   (``### Nintendo EAD {#nintendo-ead}``). Python-Markdown's ``toc`` extension
   honours explicit ids verbatim, so the site's anchors *are* GitHub's anchors
   with no slugifier configuration and no possibility of drift.
2. ``strip_doctoc`` drops the generated Contents block; the nav and the per-page
   ToCs replace it. It stays in README.md for GitHub.
3. ``build_pages`` splits the body into one page per ``##`` section, with the
   333 KB ``Game & Studio Tools`` section bucketed into fixed alphabetical
   ranges, plus a ``full.md`` holding the entire list on one page.
4. ``rewrite_links`` turns in-document ``](#anchor)`` links into relative
   ``.md`` links through the slug -> page map. Writing them as source paths
   rather than URLs means MkDocs resolves them *and* ``--strict`` with
   ``validation.anchors`` fails the build on a dead one.
5. ``write_summary`` emits ``SUMMARY.md`` for ``mkdocs-literate-nav``, so the nav
   tree is derived from the README rather than maintained by hand.
"""

from __future__ import annotations

import posixpath
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

# mkdocs_gen_files is imported lazily in write_pages/write_summary, so everything
# above them stays importable from the plain dev environment -- which is what lets
# tests and scripts/verify_site.py exercise the splitter without the docs
# toolchain installed.

REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"

GITHUB_BLOB = "https://github.com/VelocityRa/awesome-game-file-format-reversing/blob/master"

DOCTOC_START = "<!-- START doctoc -->"
DOCTOC_END = "<!-- END doctoc -->"

# Content between these markers is for GitHub readers only and is dropped from the
# site. HTML comments, so they stay invisible in the rendered README. Used for the
# "browse this as a website" pointer, which would be self-referential on the site.
SITE_SKIP_START = "<!-- site:skip-start -->"
SITE_SKIP_END = "<!-- site:skip-end -->"

# The `## Game & Studio Tools` section is split into these fixed first-letter
# ranges. Fixed -- rather than byte-balanced -- boundaries keep page URLs stable
# as studios are added; balanced buckets would shift and rot external links.
# The cost is unevenness (S is the heaviest at ~50 KB: Sega, Square Enix, Sony,
# Sierra, Spike Chunsoft), which is still a seventh of the un-split section.
GAME_BUCKETS: list[tuple[str, str, str]] = [
    # (page slug, nav label, inclusive upper bound on the studio's first letter)
    ("0-9-a", "0–9 · A", "A"),
    ("b-c", "B–C", "C"),
    ("d-f", "D–F", "F"),
    ("g-h", "G–H", "H"),
    ("i-l", "I–L", "L"),
    ("m", "M", "M"),
    ("n-o", "N–O", "O"),
    ("p-r", "P–R", "R"),
    ("s", "S", "S"),
    ("t-z", "T–Z", "Z"),
]

# Anchors whose heading is deliberately absent from the site, mapped to the page
# that replaces them (no fragment -- the whole page is the target). The doctoc
# Contents block is stripped since the nav supersedes it, but README.md's "How to
# Use This List" still points readers at it; the A-Z studio index is the site's
# equivalent.
ANCHOR_ALIASES: dict[str, str] = {"-contents": "games/index.md"}

# `##` sections the splitter places by hand. Renaming one of these headings in
# README.md changes its slug and must be reflected here; the build fails loudly
# rather than silently dropping the section.
SECTION_ABOUT = "-about"
SECTION_HOW_TO_USE = "️-how-to-use-this-list"
SECTION_COMMUNITIES = "-communities--wikis"
SECTION_GENERAL_TOOLS = "️-general-tools"
SECTION_ENGINES = "️-engines"
SECTION_MIDDLEWARE = "-middleware--sdks"
SECTION_GAMES = "game--studio-tools"
SECTION_RELATED = "-related-lists"
SECTION_LICENSE = "-license"
SECTION_ACKNOWLEDGMENTS = "-acknowledgments"

HEADING_RE = re.compile(r"^(#{1,6}) +(.+?)\s*$")
ANNOTATED_RE = re.compile(r"^(#{1,6}) +(.*?) \{#(.+)\}$")
# The target of a markdown link, when that target is an in-document anchor.
ANCHOR_LINK_RE = re.compile(r"(?<=\]\()#([^)\s]*)(?=\))")


# --------------------------------------------------------------------------
# GitHub slugs
# --------------------------------------------------------------------------
def _strip_for_slug(text: str) -> str:
    """Drop every character GitHub's slugger drops.

    Ports ``github-slugger``'s character class: keep letters, numbers, marks and
    connector punctuation, plus hyphen and space; drop everything else.

    U+FE0F VARIATION SELECTOR-16 is category ``Mn``, so it is *kept* -- which is
    why ``## 🛠️ General Tools`` slugifies to ``#️-general-tools`` with a leading
    invisible character. That is GitHub's behaviour, not a bug here.
    """
    kept = []
    for ch in text:
        if ch in "- ":
            kept.append(ch)
        else:
            cat = unicodedata.category(ch)
            if cat[0] in "LNM" or cat == "Pc":
                kept.append(ch)
    return "".join(kept)


class GithubSlugger:
    """Stateful slugger matching ``github-slugger``, dedupe counters included."""

    def __init__(self) -> None:
        self._seen: dict[str, int] = {}

    def slug(self, text: str) -> str:
        base = _strip_for_slug(text.strip().lower()).replace(" ", "-")
        if base not in self._seen:
            self._seen[base] = 0
            return base
        self._seen[base] += 1
        return f"{base}-{self._seen[base]}"


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class Heading:
    level: int
    text: str
    slug: str
    line: int


@dataclass
class Page:
    """One generated markdown file."""

    path: str  # e.g. "games/b-c.md"
    title: str  # nav label
    lines: list[str] = field(default_factory=list)
    slugs: set[str] = field(default_factory=set)  # heading anchors this page owns
    exclude_from_search: bool = False


def read_readme() -> list[str]:
    return README.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")


def annotate_headings(lines: list[str]) -> tuple[list[str], dict[str, str]]:
    """Append ``{#slug}`` to every heading. Returns (lines, slug -> heading text).

    Run against the *whole* README, before the doctoc block is stripped, so the
    slugger sees the same heading sequence GitHub does.
    """
    slugger = GithubSlugger()
    titles: dict[str, str] = {}
    out = list(lines)
    in_fence = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        hashes, text = m.group(1), m.group(2)
        slug = slugger.slug(text)
        titles[slug] = text
        out[i] = f"{hashes} {text} {{#{slug}}}"
    return out, titles


def strip_doctoc(lines: list[str]) -> list[str]:
    """Remove the generated Contents block, and the blank lines trailing it."""
    start = next((i for i, ln in enumerate(lines) if ln.startswith(DOCTOC_START)), None)
    end = next((i for i, ln in enumerate(lines) if ln.startswith(DOCTOC_END)), None)
    if start is None or end is None:
        raise SystemExit(
            "gen_pages: README.md is missing the doctoc markers "
            f"({DOCTOC_START!r} / {DOCTOC_END!r})."
        )
    if end < start:
        raise SystemExit("gen_pages: doctoc END marker precedes START marker in README.md.")
    tail = end + 1
    while tail < len(lines) and not lines[tail].strip():
        tail += 1
    return lines[:start] + lines[tail:]


def strip_site_skip(lines: list[str]) -> list[str]:
    """Drop every ``<!-- site:skip-start -->`` .. ``<!-- site:skip-end -->`` block.

    Runs *after* ``annotate_headings``, so removing a block can never shift the
    GitHub slug counters of the headings that remain. A heading inside a skipped
    block therefore keeps its slug but has no page — a link to it then fails the
    build in ``rewrite_links``, which is the intended loud failure.
    """
    out: list[str] = []
    depth = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == SITE_SKIP_START:
            depth += 1
            continue
        if stripped == SITE_SKIP_END:
            if depth == 0:
                raise SystemExit(
                    f"gen_pages: README.md line {i + 1} has {SITE_SKIP_END} with no "
                    f"matching {SITE_SKIP_START}."
                )
            depth -= 1
            continue
        if depth == 0:
            out.append(line)
    if depth:
        raise SystemExit(f"gen_pages: README.md has an unclosed {SITE_SKIP_START}.")
    # Collapse the blank-line pair a removed block leaves behind.
    return _collapse_blank_runs(out)


def _collapse_blank_runs(lines: list[str]) -> list[str]:
    out: list[str] = []
    for line in lines:
        if not line.strip() and out and not out[-1].strip():
            continue
        out.append(line)
    return out


def scan_headings(lines: list[str]) -> list[Heading]:
    """Re-derive heading positions and slugs from the annotated lines."""
    found: list[Heading] = []
    in_fence = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = ANNOTATED_RE.match(line)
        if m:
            found.append(Heading(len(m.group(1)), m.group(2), m.group(3), i))
    return found


# --------------------------------------------------------------------------
# Page splitting
# --------------------------------------------------------------------------
def bucket_for(studio: str) -> str:
    """Which GAME_BUCKETS page a studio heading belongs on."""
    first = studio.strip()[0].upper()
    if not first.isalpha():  # digits: "11 bit studios", "1C Company", "2K Games", ...
        return GAME_BUCKETS[0][0]
    for slug, _label, upper in GAME_BUCKETS:
        if first <= upper:
            return slug
    return GAME_BUCKETS[-1][0]


def build_pages(lines: list[str], headings: list[Heading]) -> list[Page]:
    h2s = [h for h in headings if h.level == 2]
    if not h2s:
        raise SystemExit("gen_pages: README.md has no '##' sections to split on.")

    # Each `##` section runs to the next `##` (the last one to EOF).
    ends = [h2s[i + 1].line if i + 1 < len(h2s) else len(lines) for i in range(len(h2s))]
    by_slug = {h.slug: (h.line, end) for h, end in zip(h2s, ends, strict=True)}

    missing = [
        s
        for s in (
            SECTION_ABOUT,
            SECTION_HOW_TO_USE,
            SECTION_COMMUNITIES,
            SECTION_GENERAL_TOOLS,
            SECTION_ENGINES,
            SECTION_MIDDLEWARE,
            SECTION_GAMES,
            SECTION_RELATED,
            SECTION_LICENSE,
            SECTION_ACKNOWLEDGMENTS,
        )
        if s not in by_slug
    ]
    if missing:
        raise SystemExit(
            "gen_pages: expected '##' section(s) not found in README.md: "
            + ", ".join(repr(s) for s in missing)
            + ".\nIf a heading was renamed its slug changed too -- update the SECTION_* "
            "constants in site_build/gen_pages.py to match."
        )

    def slugs_in(start: int, end: int) -> set[str]:
        return {h.slug for h in headings if start <= h.line < end}

    def page(path: str, title: str, *sections: str, promote: bool = True) -> Page:
        body: list[str] = []
        owned: set[str] = set()
        for s in sections:
            start, end = by_slug[s]
            body.extend(lines[start:end])
            owned |= slugs_in(start, end)
        if promote:
            body = promote_first_heading(body)
        return Page(path, title, body, owned)

    pages: list[Page] = []

    # index.md -- H1, badges, the intro blockquote, About and How to Use. No
    # promotion: README.md's own `# 🎮 Awesome ...` is already this page's h1.
    home = page("index.md", "Home", SECTION_ABOUT, SECTION_HOW_TO_USE, promote=False)
    home.lines = lines[: h2s[0].line] + home.lines
    home.slugs |= slugs_in(0, h2s[0].line)
    pages.append(home)

    pages.append(page("communities.md", "Communities & Wikis", SECTION_COMMUNITIES))
    pages.append(page("general-tools.md", "General Tools", SECTION_GENERAL_TOOLS))
    pages.append(page("engines.md", "Engines", SECTION_ENGINES))
    pages.append(page("middleware.md", "Middleware & SDKs", SECTION_MIDDLEWARE))

    # --- Game & Studio Tools: a section index page plus alphabetical buckets ---
    games_start, games_end = by_slug[SECTION_GAMES]
    studios = [h for h in headings if h.level == 3 and games_start < h.line < games_end]
    if not studios:
        raise SystemExit(
            "gen_pages: no '###' studio headings found under Game & Studio Tools."
        )
    studio_end = {
        h.line: (studios[i + 1].line if i + 1 < len(studios) else games_end)
        for i, h in enumerate(studios)
    }

    buckets: dict[str, list[Heading]] = {slug: [] for slug, _, _ in GAME_BUCKETS}
    for h in studios:
        buckets[bucket_for(h.text)].append(h)

    bucket_pages: list[Page] = []
    for slug, label, _upper in GAME_BUCKETS:
        members = buckets[slug]
        if not members:
            continue
        body = [f"# Games & Studios: {label} {{#games-{slug}}}", ""]
        owned: set[str] = set()
        for h in members:
            end = studio_end[h.line]
            body.extend(lines[h.line : end])
            owned |= slugs_in(h.line, end)
        bucket_pages.append(Page(f"games/{slug}.md", label, body, owned))

    # games/index.md: the section heading, its intro prose, and an A-Z directory
    # of every studio, linking into the bucket pages.
    gi = [lines[games_start], *lines[games_start + 1 : studios[0].line]]
    gi += ["", f"{len(studios)} studios and publishers, split alphabetically.", ""]
    for slug, label, _upper in GAME_BUCKETS:
        members = buckets[slug]
        if not members:
            continue
        gi += [f"## {label} {{#index-{slug}}}", ""]
        gi += [", ".join(f"[{h.text}]({slug}.md#{h.slug})" for h in members), ""]
    pages.append(
        Page(
            "games/index.md",
            # Not a `navigation.indexes` section landing page -- that flag is
            # incompatible with toc.integrate -- so it needs a title that does not
            # duplicate the "Games & Studios" section heading above it in the nav.
            "All Studios (A–Z)",
            promote_first_heading(gi),
            {headings_slug(lines, games_start)},
        )
    )
    pages.extend(bucket_pages)

    pages.append(page("related-lists.md", "Related Lists", SECTION_RELATED))
    pages.append(page("license.md", "License", SECTION_LICENSE))
    pages.append(page("acknowledgments.md", "Acknowledgments", SECTION_ACKNOWLEDGMENTS))

    # full.md -- the entire list on one page, the way GitHub renders it. Excluded
    # from search so its 621 headings do not double every result. `anchor_page_map`
    # skips it, since it duplicates every anchor and so is never a link *target*;
    # its own slug set is still needed to resolve its own in-page links.
    full = Page("full.md", "Full List", exclude_from_search=True)
    full.lines = ["# Full List {#full-list}", "", *lines[1:]]
    full.slugs = slugs_in(1, len(lines)) | {"full-list"}
    pages.append(full)

    return pages


def promote_first_heading(body: list[str]) -> list[str]:
    """Turn a page's leading ``##`` into an ``#``, keeping its explicit anchor.

    Material renders the page's nav title as an ``<h1>`` when the markdown has
    none, so a section page starting at ``##`` shows its title twice ("Games &
    Studios" above "Game & Studio Tools"). Promoting the first heading gives the
    page a real ``h1`` and drops the duplicate. The ``{#slug}`` id rides along, so
    GitHub anchors are unaffected.
    """
    out = list(body)
    for i, line in enumerate(out):
        m = ANNOTATED_RE.match(line)
        if m:
            if m.group(1) == "##":
                out[i] = f"# {m.group(2)} {{#{m.group(3)}}}"
            break
    return out


def headings_slug(lines: list[str], line: int) -> str:
    """The explicit anchor on an already-annotated heading line."""
    m = ANNOTATED_RE.match(lines[line])
    if not m:
        raise SystemExit(f"gen_pages: line {line + 1} is not an annotated heading.")
    return m.group(3)


# --------------------------------------------------------------------------
# Link rewriting
# --------------------------------------------------------------------------
def anchor_page_map(pages: list[Page]) -> dict[str, str]:
    """slug -> owning page path, for every heading that landed on a page.

    ``full.md`` is skipped: it holds a copy of every anchor, so treating it as an
    owner would send cross-page links to the 505 KB page instead of the small one.
    """
    mapping: dict[str, str] = {}
    for p in pages:
        if p.path == "full.md":
            continue
        for slug in p.slugs:
            mapping.setdefault(slug, p.path)
    return mapping


def rewrite_links(page: Page, mapping: dict[str, str]) -> list[str]:
    """Repoint in-document anchors at the page that now owns them.

    Emits *source-relative* ``.md`` links so MkDocs resolves them itself and
    ``validation.anchors`` can check the fragment.
    """
    here = posixpath.dirname(page.path) or "."
    unresolved: list[str] = []

    def repl(m: re.Match[str]) -> str:
        slug = m.group(1)
        if slug in page.slugs:
            return m.group(0)  # target is on this page
        target = mapping.get(slug)
        if target is not None:
            return f"{posixpath.relpath(target, here)}#{slug}"
        alias = ANCHOR_ALIASES.get(slug)
        if alias is not None:
            return posixpath.relpath(alias, here)  # whole page is the target
        unresolved.append(slug)
        return m.group(0)

    out = [
        ANCHOR_LINK_RE.sub(repl, line).replace("](LICENSE)", f"]({GITHUB_BLOB}/LICENSE)")
        for line in page.lines
    ]
    if unresolved:
        raise SystemExit(
            f"gen_pages: {page.path} links to anchor(s) with no matching heading: "
            + ", ".join(f"#{s}" for s in sorted(set(unresolved)))
            + ".\nFix the link in README.md, or add an ANCHOR_ALIASES entry if the "
            "heading is intentionally absent from the site."
        )
    return out


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------
def write_pages(pages: list[Page], mapping: dict[str, str]) -> None:
    import mkdocs_gen_files  # ty: ignore[unresolved-import]  # docs-env only

    for p in pages:
        body = rewrite_links(p, mapping)
        front = "---\nsearch:\n  exclude: true\n---\n\n" if p.exclude_from_search else ""
        with mkdocs_gen_files.open(p.path, "w") as fh:
            fh.write(front + "\n".join(body).rstrip() + "\n")


def write_summary(pages: list[Page]) -> None:
    """Nav for mkdocs-literate-nav. Top-level entries become Material's tabs."""
    import mkdocs_gen_files  # ty: ignore[unresolved-import]  # docs-env only

    have = {p.path for p in pages}
    titles = {p.path: p.title for p in pages}
    out: list[str] = []

    def link(path: str, indent: int = 0) -> None:
        out.append(f"{'    ' * indent}- [{titles[path]}]({path})")

    for path in ("index.md", "communities.md", "general-tools.md", "engines.md", "middleware.md"):
        link(path)

    # A section whose first child is its own index.md is what Material's
    # `navigation.indexes` turns into a clickable section landing page.
    out.append("- Games & Studios")
    link("games/index.md", 1)
    for slug, _label, _upper in GAME_BUCKETS:
        path = f"games/{slug}.md"
        if path in have:
            link(path, 1)

    link("full.md")

    out.append("- About")
    for path in ("related-lists.md", "license.md", "acknowledgments.md"):
        link(path, 1)

    with mkdocs_gen_files.open("SUMMARY.md", "w") as fh:
        fh.write("\n".join(out) + "\n")


def build() -> list[Page]:
    """Everything except writing, so tests can inspect the result."""
    lines, _titles = annotate_headings(read_readme())
    lines = strip_site_skip(strip_doctoc(lines))
    return build_pages(lines, scan_headings(lines))


def main() -> None:
    pages = build()
    write_pages(pages, anchor_page_map(pages))
    write_summary(pages)


# mkdocs-gen-files runs this file with `runpy.run_path`, which sets __name__ to
# "<run_path>" rather than "__main__". Guarding on both keeps the module safe to
# import from tests (where mkdocs_gen_files.open would fail outside a build).
if __name__ in ("__main__", "<run_path>"):
    main()
