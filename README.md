# 🎮 Awesome Game File Format Reversing

> A collection of documentation, code, tools, and resources for reverse engineering and working with video game file formats.

<!-- site:skip-start -->
> [!TIP]
> ### 🌐 [Browse this list as a website](https://velocityra.github.io/awesome-game-file-format-reversing/)
>
> *(recommended for easier navigation)*
<!-- site:skip-end -->

## 📖 About

Video games store their assets in specialized, usually undocumented formats for models, textures, animations, audio, archives, scripts, and level data.

This list is for developers and modders working with such formats. It provides tools and knowledge to understand, extract, convert, and work with them across many games and engines.

**Contributions are welcome!** Submit pull requests to add new tools, documentation, or corrections.

## 🗺️ How to Use This List

- **Newcomers**: Start with [Learning Resources & Tutorials](#-learning-resources--tutorials) and [General Tools](#️-general-tools)
- **Looking for a specific game**: Use Ctrl+F or check the [Contents](#-contents) for studio/game-specific sections
- **Working with an engine**: See [Engines](#️-engines) and [Middleware & SDKs](#-middleware--sdks)
- **Need help**: Join the communities in [Forums & Communities](#forums--communities) and [Discord Servers](#discord-servers)

<!-- START doctoc -->
## 📑 Contents

- [👥 Communities](#-communities)
  - [Forums & Communities](#forums--communities)
  - [Discord Servers](#discord-servers)
- [📚 Reference & Learning](#-reference--learning)
  - [Knowledge Bases & Format Databases](#knowledge-bases--format-databases)
  - [Platform & SDK Documentation](#platform--sdk-documentation)
  - [Game-Specific Wikis](#game-specific-wikis)
  - [📚 Learning Resources & Tutorials](#-learning-resources--tutorials)
  - [Asset Databases](#asset-databases)
- [🛠️ General Tools](#️-general-tools)
  - [🎨 Asset Viewers & Converters](list/general-tools.md#-asset-viewers--converters)
  - [📦 Archive Extractors](list/general-tools.md#-archive-extractors)
  - [🔊 Audio Tools](list/general-tools.md#-audio-tools)
  - [🌐 Translation & Localization](list/general-tools.md#-translation--localization)
  - [🔍 Hex Editors](list/general-tools.md#-hex-editors)
  - [🔬 Format Analysis & Reverse Engineering](list/general-tools.md#-format-analysis--reverse-engineering)
  - [💻 Development Libraries](list/general-tools.md#-development-libraries)
  - [📂 Script Collections & Multi-Game Tools](list/general-tools.md#-script-collections--multi-game-tools)
- [⚙️ Engines](#️-engines)
  - [Major & General-Purpose Engines](list/engines.md#major--general-purpose-engines)
  - [Legacy & Specialized Engines](list/engines.md#legacy--specialized-engines)
  - [RPG, Visual Novel & Adventure Engines](list/engines.md#rpg-visual-novel--adventure-engines)
  - [Interactive Fiction & Dialogue Systems](list/engines.md#interactive-fiction--dialogue-systems)
  - [Other Authoring Runtimes](list/engines.md#other-authoring-runtimes)
- [🔧 Middleware & SDKs](#-middleware--sdks)
  - [Graphics, Animation & Asset Technology](list/middleware.md#graphics-animation--asset-technology)
  - [Audio Technology](list/middleware.md#audio-technology)
  - [Platform SDKs & Hardware](list/middleware.md#platform-sdks--hardware)
  - [Runtimes, Services & Toolkits](list/middleware.md#runtimes-services--toolkits)
- [Game & Studio Tools](#game--studio-tools)
  - [0–9](list/games-0-9-a.md#09)
  - [A](list/games-0-9-a.md#a)
  - [B](list/games-b-c.md#b)
  - [C](list/games-b-c.md#c)
  - [D](list/games-d-f.md#d)
  - [E](list/games-d-f.md#e)
  - [F](list/games-d-f.md#f)
  - [G](list/games-g-h.md#g)
  - [H](list/games-g-h.md#h)
  - [I](list/games-i-l.md#i)
  - [J](list/games-i-l.md#j)
  - [K](list/games-i-l.md#k)
  - [L](list/games-i-l.md#l)
  - [M](list/games-m.md#m)
  - [N](list/games-n-o.md#n)
  - [O](list/games-n-o.md#o)
  - [P](list/games-p-r.md#p)
  - [Q](list/games-p-r.md#q)
  - [R](list/games-p-r.md#r)
  - [S](list/games-s.md#s)
  - [T](list/games-t-z.md#t)
  - [U](list/games-t-z.md#u)
  - [V](list/games-t-z.md#v)
  - [W](list/games-t-z.md#w)
  - [X](list/games-t-z.md#x)
  - [Y](list/games-t-z.md#y)
  - [Z](list/games-t-z.md#z)
  - [Other / Non-Latin](list/games-t-z.md#other--non-latin)
- [🔗 Related Lists](#-related-lists)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)
<!-- END doctoc -->

## 👥 Communities

*Forums and Discord servers for reverse engineering and file formats. For knowledge bases and learning resources, see [Reference & Learning](#-reference--learning).*

### Forums & Communities

- [ZenHAX](https://zenhax.com/) - Game hacking and reverse engineering forum.
- [ResHax](https://reshax.com/) - Game Reversing Archives and Formats.
- [XeNTaX Forum (defunct)](https://web.archive.org/web/20231024043128/https://forum.xentax.com/) - Game archive and format research forum.

### Discord Servers

- [REGames](https://discord.com/invite/regames-760531247704702996) - Community for game reverse engineering and file format research.
- [The VG Resource](https://discord.com/invite/tsr) - Community for The VG Resource asset databases (models, textures, sprites, sounds).
- [The Cutting Room Floor (TCRF)](https://discord.com/invite/SGeE8dcWR6) - Community for discovering and documenting unused and debug game content.
- [Reverse Engineering](https://discord.com/invite/reverse-engineering-391398885819547652) - General reverse engineering community and resources.
- [noclip.website](https://discord.com/invite/bkJmKKv) - Community for the noclip.website in-browser game viewer project.

*Note: Many game-specific and studio-specific Discord servers exist for individual games and franchises. This list includes only general-purpose reverse engineering communities.*

## 📚 Reference & Learning
### Knowledge Bases & Format Databases

- [Just Solve the File Format Problem](http://fileformats.archiveteam.org/wiki/Game_data_files) - ArchiveTeam's wiki for file formats.
- [XeNTaX Wiki (defunct)](https://web.archive.org/web/20230822181840/https://wiki.xentax.com/index.php/Game_File_Format_Central) - Massive database of file format specifications.
- [XeNTaXBackup](https://github.com/XeNTaXBackup/XeNTaXBackup.github.io) - Public backup of the XeNTaX game file format reverse engineering forum and wiki, preserving community knowledge on game format documentation, QuickBMS scripts, and format research.
- [RetroReversing](https://github.com/RetroReversing/retroReversing) - Curated list of retro game development and reverse-engineering resources, tools, and documentation, published as the RetroReversing.com website/wiki.
- [oldgamescracking.github.io](https://github.com/OldGamesCracking/oldgamescracking.github.io) - Community knowledge base documenting cracking and format-preservation notes for old games.
- [arcade-docs](https://codeberg.org/shiz/arcade-docs) - Open documentation repository for arcade system hardware, network protocols, and file formats across many manufacturers. Migrated from the archived [GitHub mirror](https://github.com/shizmob/arcade-docs).
- [Galgame-Engine-Collect (galWiki)](https://github.com/2439905184/Galgame-Engine-Collect) - Extensive community knowledge base cataloging Japanese visual novel/galgame engines, their file formats, and associated extraction/translation tools.

### Platform & SDK Documentation

- [Psy-Q SDK Documentation](https://psx.arthus.net/sdk/Psy-Q/DOCS/) - Official PlayStation SDK documentation archive. Includes file format references, development guides, and API documentation.
  - [File Format Reference](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Filefrmt.pdf) - Official Psy-Q SDK file format documentation.
- [PSX-SPX Console Dev](https://psx-spx.consoledev.net/) - Comprehensive PlayStation technical documentation and reference. Covers hardware specifications, BIOS functions, and development resources.
  - [CD-ROM File Formats](https://psx-spx.consoledev.net/cdromfileformats/) - Detailed documentation on PlayStation CD-ROM file formats and structures.
- [psx-guide](https://github.com/simias/psx-guide) - In-depth guide to writing a PlayStation emulator from scratch, covering the CPU/MIPS instruction set and memory interconnect, DMA ordering tables, GPU internals and rendering, and building a debugger with breakpoints/watchpoints.
- [rom-properties](https://github.com/GerbilSoft/rom-properties) - Shell extension for Windows and Linux that shows information about ROM and disc image files. Supports over 500 game and system file formats across dozens of consoles and handhelds.
  - Features: Metadata viewing (title, publisher, region), icon/boxart extraction, save game management, and explorer integration.
- [pif_rom_dumper](https://github.com/hcs64/pif_rom_dumper) - Tool for extracting N64 PIF ROM (system firmware) from Nintendo 64 hardware.
- [Awesome PlayStation Vita](https://github.com/MuxaJlbl4/Awesome-PlayStation-Vita) - Comprehensive PS Vita resource list including reverse engineering tools, file format decompilers (.rco, .rcs), and RE utilities.
- [ps4libdoc](https://github.com/idc/ps4libdoc) - PS4 library documentation for game development and reverse engineering reference.
- [PSVita-RE-tools](https://github.com/TeamFAPS/PSVita-RE-tools) - Collection of PlayStation Vita reverse-engineering tools.
- [awesome-gbdev](https://github.com/gbdev/awesome-gbdev) - Curated list of Game Boy development resources, including reverse-engineering tools, hardware/format documentation, disassemblers, and emulators.
- [awesome-megadrive](https://github.com/And-0/awesome-megadrive) - Curated list of Sega Mega Drive/Genesis development resources, including hardware documentation, disassemblers, and format tools.
- [Pan Docs](https://github.com/gbdev/pandocs) - The single, most comprehensive technical reference to the Game Boy hardware available to the public, including cartridge header, memory bank controller, and save format documentation.
- [gb-ctr](https://github.com/Gekkio/gb-ctr) - Game Boy: Complete Technical Reference, an in-depth document covering Game Boy console hardware internals.
- [gb-bootroms](https://codeberg.org/ISSOtm/gb-bootroms) - Disassembled and annotated Game Boy family boot ROMs.
- [gbadoc](https://github.com/gbadev-org/gbadoc) - Community-driven Game Boy Advance technical documentation effort.
- [Architecture of consoles](https://github.com/flipacholas/Architecture-of-consoles) - Series of technical articles on console hardware architecture, covering CPU, graphics, and file/memory layout across many platforms.
- [SiliconRE](https://github.com/furrtek/SiliconRE) - Traces, schematics, and technical writeups from silicon-level reverse engineering of custom game console/arcade chips.
- [ay-3-8910_reverse_engineered](https://github.com/lvd2/ay-3-8910_reverse_engineered) - Transistor-level reverse engineering of the AY-3-8910 sound chip used in many arcade and home computer systems, with transistor-level schematics, a Verilog model, and a testbench that renders register dumps into audio.
- [awesome-gbadev](https://github.com/gbadev-org/awesome-gbadev) - Curated list of Game Boy Advance development resources, including documentation, tools, and libraries relevant to GBA file formats and homebrew.
- [Free60 Wiki Archive](https://github.com/Free60Project/wiki) - Archived MediaWiki dump of free60.org, the community reference for Xbox 360 hardware, firmware, and file format reverse engineering.
- [awesome-dreamcast](https://github.com/dreamcastdevs/awesome-dreamcast) - Curated list of Sega Dreamcast development resources, including tutorials, homebrew tools, engines, and frameworks; see also [dreamcast.wiki](https://dreamcast.wiki/Dreamcast.wiki) linked within for hardware/format documentation.
- [gbdoc](https://github.com/msinger/gbdoc) - Documents from original Game Boy hardware research.
- [Cart Reader (OSCR)](https://github.com/sanni/cartreader) (archived) - Firmware for an Arduino Mega/Nano-based shield that backs up ROM and save data from game cartridges without a PC, natively supporting NES, SNES, N64, Game Boy/Color/Advance, Sega Mega Drive/Genesis, and Master System, plus dozens more systems (Virtual Boy, PC Engine, WonderSwan, NeoGeo Pocket, Intellivision, ColecoVision, and others) via adapters.
- [n64cartreader](https://github.com/jgazeley/n64cartreader) - N64-focused fork/adaptation of the Sanni Open Source Cartridge Reader (OSCR), a Raspberry Pi Pico-based hardware dumper for reading Nintendo 64 ROM and cartridge save data over USB, with web-browser or command-line dump tools.

### Game-Specific Wikis

- [The Cutting Room Floor](https://tcrf.net/Help:Contents/Finding_Content) - Community for discovering and documenting unused and debug game content.
- [Nintendo File Formats](https://nintendo-formats.com/) - Documentation for Wii U and Switch games.
- [Custom Mario Kart Wiiki](https://mkwiiki.org/wiki/List_of_File_Formats) - Formats used in Mario Kart Wii and related games.
- [Mario Kart 8 Wiki](https://mk8.tockdom.com/wiki/Main_Page) - Documentation for Mario Kart 8 formats and modding.
- [Luma's Workshop](https://www.lumasworkshop.com/wiki/Category:File_formats) - Nintendo modding wiki.
- [Splatoon Technical Wiki](https://wiki.oatmealdome.me/index.php/Special:AllPages) - Technical documentation for Splatoon game formats.
- [Souls Modding Wiki](https://www.soulsmodding.com/doku.php?id=start) - Documentation for FromSoftware formats.
- [MGSV Modding and Research Wiki](https://mgsvmoddingwiki.github.io/) - Community wiki documenting Metal Gear Solid V: The Phantom Pain's Fox Engine file formats and modding workflows.
- [Ragnarok Research Lab](https://ragnarokresearchlab.github.io/) - Technical documentation covering Ragnarok Online's file formats, rendering systems, and game mechanics. Active continuation of the archived [RagnarokFileFormats](https://github.com/rdw-archive/RagnarokFileFormats) manifest.
- [Persona Modding Wiki](https://persona-modding.github.io/) - Community-driven documentation for modding Persona series games. Continuation of the archived [AnimatedSwine37/persona-modding-docs](https://github.com/AnimatedSwine37/persona-modding-docs).
- [RSDK Modding Wiki](https://rsdkmodding.com) - Community wiki for Retro Engine (RSDK) modding, covering Sonic CD, Sonic 1 & 2 (2013 mobile), and Sonic Mania.

### 📚 Learning Resources & Tutorials

- **[DGTEFF](https://web.archive.org/web/20230817151933/http://wiki.xentax.com/index.php/DGTEFF) - Definitive Guide To Exploring File Formats.**
- [The VG Resource Wiki](https://wiki.vg-resource.com/Main_Page) - Wiki with tutorials for ripping and creating sprites, models, textures, and sounds across gaming platforms.
- [Compression Deep Dive](https://chronovore.dev/posts/2023-01-25-1234P-compression-deepdive.html) - Technical analysis of compression algorithms used in games.
- [How to Crack a Binary File Format](https://www.iwriteiam.nl/Ha_HTCABFF.html) - Classic tutorial on reverse engineering file formats.
- [kovidomi/game-reversing](https://github.com/kovidomi/game-reversing) - Beginner learning materials on reverse engineering video games.
- [How to Grab Models and Textures](https://aknavj.github.io/3d/2019/06/10/Grabbing-models-and-textures-from-game-or-3D-application.html) - Guide on extracting models and textures from games.
- [ReWolf's Retrogaming Blog](http://blog.rewolf.pl/blog/?cat=23) - Blog posts on retrogaming and reverse engineering.
- [vgmdocs](https://github.com/loveemu/vgmdocs) - Resources and documentation for video game music formats. Includes guides for GBA sound drivers, FM synth presets, conversion tools, and format documentation.
- [Inazuma-Eleven-GO-Modding](https://github.com/SxncYT/Inazuma-Eleven-GO-Modding) - Documentation regarding the functions of Inazuma Eleven GO Light/Shadow. Covers game scripting, format specifications, and modding techniques.
- [Crazy Taxi Reverse Engineering](https://wretched.computer/post/crazytaxi) - Detailed retrospective series on reverse engineering the GameCube version of Crazy Taxi, covering archive (.all), model (.shp), texture (.tex), and audio (.adp) formats.

#### 🎥 Video Tutorials

- [Binary File Format Engineering and Reverse Engineering](https://www.youtube.com/watch?v=8OxtBxXfJHw) - Peter Bindels - ACCU 2023 conference talk on binary file format analysis and reverse engineering techniques.
- [Reverse engineering game formats for fun and profit! (or just fun)](https://www.youtube.com/watch?v=MXbo6y6MCPE) - Spencer Alves - !!Con West 2020 talk on reverse engineering game file formats.
- [What's In A Bit - Designing, Using And Reverse-engineering Binary File Formats](https://www.youtube.com/watch?v=QEIGc3tXGmM) - Peter Bindels - cpponsea talk on binary file format design and reverse engineering.
- [File Format Reverse Engineering 1 - Intro, target, and tools](https://www.youtube.com/watch?v=_zCekiF5aBQ) - CO/DE tutorial series introduction to file format reverse engineering.
- [Reverse Engineered old Compression Algorithm for Frogger](https://www.youtube.com/watch?v=BwoOB2QFXvw) - LiveOverflow - Case study on reverse engineering compression algorithms in classic games.
- [retrore](https://github.com/realdmx/retrore) - Curated list of original and reverse-engineered vintage 6502 game source code, tracking disassembly projects across many classic 8-bit titles.
- [dsasmblr/game-hacking](https://github.com/dsasmblr/game-hacking) - Large curated collection of tutorials, tools, and resources for reverse engineering video games.

### Asset Databases

- [The VG Resource (archived)](https://archive.vg-resource.com/index.php) - Models, Textures, Sounds, and Sprite databases and forums.
  - [The Spriters Resource](https://www.spriters-resource.com/) - Dedicated sprite and pixel art database.
  - [The Models Resource](https://models.spriters-resource.com/) - Dedicated 3D model database.
  - [The Textures Resource](https://textures.spriters-resource.com/) - Dedicated texture database.
  - [The Sounds Resource](https://sounds.spriters-resource.com/) - Dedicated audio and music database.

## 🛠️ General Tools

*Multi-format tools that support a wide variety of unrelated games.*

<!-- site:skip-start -->
**This section lives in [list/general-tools.md](list/general-tools.md).**
<!-- site:skip-end -->

<!-- part: list/general-tools.md -->

## ⚙️ Engines

*Tools specific to widespread third-party game engines.*

<!-- site:skip-start -->
**This section lives in [list/engines.md](list/engines.md).**
<!-- site:skip-end -->

<!-- part: list/engines.md -->

## 🔧 Middleware & SDKs

*Game development middleware, libraries, and SDK-provided formats used across multiple titles and platforms.*

<!-- site:skip-start -->
**This section lives in [list/middleware.md](list/middleware.md).**
<!-- site:skip-end -->

<!-- part: list/middleware.md -->

## Game & Studio Tools

<!-- site:skip-start -->
**This section is split by letter:** [0–9 · A](list/games-0-9-a.md) · [B–C](list/games-b-c.md) · [D–F](list/games-d-f.md) · [G–H](list/games-g-h.md) · [I–L](list/games-i-l.md) · [M](list/games-m.md) · [N–O](list/games-n-o.md) · [P–R](list/games-p-r.md) · [S](list/games-s.md) · [T–Z](list/games-t-z.md)
<!-- site:skip-end -->

<!-- part: list/games-0-9-a.md -->

<!-- part: list/games-b-c.md -->

<!-- part: list/games-d-f.md -->

<!-- part: list/games-g-h.md -->

<!-- part: list/games-i-l.md -->

<!-- part: list/games-m.md -->

<!-- part: list/games-n-o.md -->

<!-- part: list/games-p-r.md -->

<!-- part: list/games-s.md -->

<!-- part: list/games-t-z.md -->

## 🔗 Related Lists

- [Awesome Modding](https://github.com/loicreynier/awesome-modding.bak) - Resources for game modding and customization.
- [Awesome Game Decompilations](https://github.com/CharlotteCross1998/awesome-game-decompilations) - A curated list of awesome game decompilations.
- [Awesome Game Datasets](https://github.com/leomaurodesenv/game-datasets) - Datasets and resources for game research.
- [Awesome Reverse Engineering](https://github.com/tylerha97/awesome-reversing) - List of reverse engineering resources.
- [Awesome Software Reverse Engineering](https://github.com/ReversingID/Awesome-Reversing/blob/master/software-reversing.md) - Comprehensive list of reverse engineering software and tools.
- [Awesome Gamedev](https://github.com/ellisonleao/magictools) - Curated list of game development resources.
- [Game-Decompilations](https://github.com/SamidyFR/Game-Decompilations) - Curated list of video game decompilation projects, documenting reverse-engineered game source code and asset parsing.
- [Awesome Unofficial PC Ports](https://github.com/Sebastrion/awesome-unofficial-pc-ports) - Curated list of fan-made, reverse-engineering-driven PC ports and static recompilations of console-only games.
- [Awesome-Game-Boy-Camera-and-Game-Boy-Printer-projects](https://github.com/Raphael-Boichot/Awesome-Game-Boy-Camera-and-Game-Boy-Printer-projects) - Curated meta-list of Game Boy Camera and Game Boy Printer projects across the internet.

## 📄 License

[CC0](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.

## 🙏 Acknowledgments

Shoutout to [MeltyPlayer/awesome-game-file-formats](https://github.com/MeltyPlayer/awesome-game-file-formats) - this started as a fork of it with my own bookmark collection, but I eventually decided to add more sections and reorganize it.





