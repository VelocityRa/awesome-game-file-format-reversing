"""MkDocs hooks for the site build (see ``hooks:`` in mkdocs.yml)."""

from __future__ import annotations

# mkdocs is installed only in the docs build env (requirements-docs.txt), not the
# dev venv, so ty cannot resolve it here.
from mkdocs.structure.files import Files, InclusionLevel  # ty: ignore[unresolved-import]

NAV_FILE = "SUMMARY.md"


def on_files(files: Files, config) -> Files:
    """Drop the generated nav file from the build output.

    ``gen_pages.py`` writes ``SUMMARY.md`` for mkdocs-literate-nav, which reads it
    in its own ``on_files`` and then marks it ``NOT_IN_NAV`` -- excluded from the
    nav but still rendered, leaving a stray ``/SUMMARY/`` page that turns up in
    search results. Hooks run after plugins, so by the time this executes the nav
    has already been resolved and the file is safe to remove.
    """
    nav_file = files.get_file_from_path(NAV_FILE)
    if nav_file is not None:
        nav_file.inclusion = InclusionLevel.EXCLUDED
    return files
