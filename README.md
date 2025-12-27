# 🎮 Awesome Game File Format Reversing

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

> A collection of documentation, code, tools, and resources for reverse engineering and working with video game file formats.

## 📖 About

Video games store their assets in specialized, usually undocumented formats for models, textures, animations, audio, archives, scripts, and level data.

This list is for developers and modders working with such formats. It provides tools and knowledge to understand, extract, convert, and work with them across many games and engines.

**Contributions are welcome!** Submit pull requests to add new tools, documentation, or corrections.

## 🗺️ How to Use This List

- **Newcomers**: Start with [Learning Resources & Tutorials](#-learning-resources--tutorials) and [General Tools](#️-general-tools)
- **Looking for a specific game**: Use Ctrl+F or check the [Contents](#-contents) for studio/game-specific sections
- **Working with an engine**: See [Engines](#️-engines) and [Middleware & SDKs](#-middleware--sdks)
- **Need help**: Join the communities in [Forums & Communities](#forums--communities) and [Discord Servers](#discord-servers)

## 📑 Contents

- [🎮 Awesome Game File Format Reversing](#-awesome-game-file-format-reversing)
  - [📖 About](#-about)
  - [🗺️ How to Use This List](#️-how-to-use-this-list)
  - [📑 Contents](#-contents)
  - [👥 Communities \& Wikis](#-communities--wikis)
    - [Forums \& Communities](#forums--communities)
    - [Discord Servers](#discord-servers)
    - [Knowledge Bases \& Format Databases](#knowledge-bases--format-databases)
    - [Game-Specific Wikis](#game-specific-wikis)
    - [📚 Learning Resources \& Tutorials](#-learning-resources--tutorials)
      - [🎥 Video Tutorials](#-video-tutorials)
    - [Asset Databases](#asset-databases)
  - [🛠️ General Tools](#️-general-tools)
    - [🎨 Model, Texture \& Animation](#-model-texture--animation)
    - [📦 Archive \& Asset Extraction](#-archive--asset-extraction)
    - [🔊 Audio Tools](#-audio-tools)
    - [🌐 Translation \& Localization](#-translation--localization)
    - [🔍 Binary Analysis \& Hex Editors](#-binary-analysis--hex-editors)
    - [💻 Libraries \& Development Tools](#-libraries--development-tools)
    - [Decompilation Tools](#decompilation-tools)
    - [Blender Addons](#blender-addons)
  - [⚙️ Engines](#️-engines)
    - [GameMaker](#gamemaker)
    - [Source (Valve)](#source-valve)
    - [Unity](#unity)
    - [Unreal Engine](#unreal-engine)
  - [🔧 Middleware \& SDKs](#-middleware--sdks)
    - [Fast3d/F3dex (N64)](#fast3df3dex-n64)
    - [JSYSTEM (GameCube/Wii)](#jsystem-gamecubewii)
    - [Sappy (GBA Audio)](#sappy-gba-audio)
  - [Formats by Studio / Game](#formats-by-studio--game)
    - [Activision / Infinity Ward / Treyarch](#activision--infinity-ward--treyarch)
      - [Call of Duty](#call-of-duty)
    - [Angel Studios / Rockstar San Diego](#angel-studios--rockstar-san-diego)
    - [Ape, Inc](#ape-inc)
    - [Argonaut Games](#argonaut-games)
    - [Arkane Studios](#arkane-studios)
    - [Atlus](#atlus)
    - [Asobo Studio](#asobo-studio)
    - [Bandai Namco](#bandai-namco)
    - [Capcom](#capcom)
      - [Monster Hunter](#monster-hunter)
      - [Devil May Cry](#devil-may-cry)
    - [CCP Games](#ccp-games)
    - [CD Projekt Red](#cd-projekt-red)
      - [The Witcher 3 / REDEngine 3](#the-witcher-3--redengine-3)
      - [Cyberpunk 2077 / REDEngine 4](#cyberpunk-2077--redengine-4)
    - [Cygames](#cygames)
    - [Clover Studio](#clover-studio)
    - [Double Fine](#double-fine)
    - [EA Black Box](#ea-black-box)
      - [Need for Speed Series](#need-for-speed-series)
    - [FromSoftware](#fromsoftware)
    - [Game Freak](#game-freak)
      - [Gen I \& II](#gen-i--ii)
      - [Gen III](#gen-iii)
    - [Genius Sonority](#genius-sonority)
    - [Grezzo](#grezzo)
    - [Guerrilla Games](#guerrilla-games)
    - [Gust (Koei Tecmo)](#gust-koei-tecmo)
    - [HAL Laboratory](#hal-laboratory)
    - [Heavy Iron Studios](#heavy-iron-studios)
    - [Hudson Soft](#hudson-soft)
    - [Insomniac Games](#insomniac-games)
    - [Intelligent Systems](#intelligent-systems)
      - [Paper Mario 64](#paper-mario-64)
      - [Paper Mario: TTYD / Super Paper Mario](#paper-mario-ttyd--super-paper-mario)
    - [Interactive Studios](#interactive-studios)
      - [Glover](#glover)
    - [iNiS](#inis)
    - [Jupiter](#jupiter)
    - [Jagex](#jagex)
    - [Konami](#konami)
      - [Metal Gear Solid](#metal-gear-solid)
      - [Silent Hill](#silent-hill)
    - [Kuju London](#kuju-london)
    - [Larian Studios](#larian-studios)
      - [Baldur's Gate 3](#baldurs-gate-3)
      - [Divinity: Original Sin 2](#divinity-original-sin-2)
    - [Level-5](#level-5)
    - [Mario Artist](#mario-artist)
    - [Microsoft Studios / Bungie / Turn 10](#microsoft-studios--bungie--turn-10)
      - [Halo](#halo)
      - [Forza](#forza)
    - [Mobius Digital](#mobius-digital)
    - [Midway](#midway)
      - [Gauntlet](#gauntlet)
      - [NFL Blitz](#nfl-blitz)
    - [Naughty Dog](#naughty-dog)
      - [Crash Bandicoot 1-3 \& CTR](#crash-bandicoot-1-3--ctr)
      - [Jak and Daxter](#jak-and-daxter)
    - [NanaOn-Sha](#nanaon-sha)
    - [Nintendo EAD](#nintendo-ead)
      - [Animal Crossing](#animal-crossing)
      - [AST](#ast)
      - [Luigi's Mansion](#luigis-mansion)
      - [Pikmin](#pikmin)
      - [Pikmin 2](#pikmin-2)
      - [Mario Kart: Double Dash](#mario-kart-double-dash)
      - [Super Mario 64](#super-mario-64)
      - [Super Mario 64 DS](#super-mario-64-ds)
      - [Super Mario (Other)](#super-mario-other)
      - [Zelda](#zelda)
      - [Wii Sports](#wii-sports)
      - [Star Fox Adventures](#star-fox-adventures)
      - [Super Monkey Ball](#super-monkey-ball)
      - [New Super Mario Bros DS](#new-super-mario-bros-ds)
      - [Metroid Prime](#metroid-prime)
      - [Pokemon](#pokemon)
    - [Nintendo SDKs \& Hardware](#nintendo-sdks--hardware)
    - [Ntreev Soft](#ntreev-soft)
    - [Panic](#panic)
    - [PlatinumGames](#platinumgames)
      - [Bayonetta](#bayonetta)
      - [Nier: Automata / Replicant](#nier-automata--replicant)
    - [Polytron](#polytron)
    - [Punchline](#punchline)
    - [Polyphony Digital](#polyphony-digital)
    - [RAD Game Tools](#rad-game-tools)
    - [Rare](#rare)
    - [Radical Entertainment](#radical-entertainment)
    - [Reflections Interactive](#reflections-interactive)
    - [Riot Games](#riot-games)
    - [Santa Monica Studio](#santa-monica-studio)
    - [Sega](#sega)
    - [Sonic Team](#sonic-team)
      - [Sonic Adventure](#sonic-adventure)
      - [Sonic Heroes / Shadow](#sonic-heroes--shadow)
      - [Other Sonic Games](#other-sonic-games)
    - [Sony (First Party)](#sony-first-party)
    - [Square Enix](#square-enix)
    - [Sucker Punch](#sucker-punch)
      - [Sly Cooper](#sly-cooper)
    - [Thekla Inc](#thekla-inc)
    - [Visceral Games](#visceral-games)
    - [Wargaming](#wargaming)
    - [Ubisoft](#ubisoft)
      - [Anno 1800](#anno-1800)
    - [Angel Matrix](#angel-matrix)
    - [Bethesda](#bethesda)
    - [Blizzard Entertainment](#blizzard-entertainment)
  - [🔗 Related Lists](#-related-lists)
  - [📄 License](#-license)
  - [🙏 Acknowledgments](#-acknowledgments)

## 👥 Communities & Wikis

*Knowledge bases, forums, and learning resources for reverse engineering and file formats.*

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

### Knowledge Bases & Format Databases

- [Just Solve the File Format Problem](http://fileformats.archiveteam.org/wiki/Game_data_files) - ArchiveTeam's wiki for file formats.
- [XeNTaX Wiki (defunct)](https://web.archive.org/web/20230822181840/https://wiki.xentax.com/index.php/Game_File_Format_Central) - Massive database of file format specifications.
- [AVSYS Wiki](http://ww38.avsys.xyz/wiki/Category:File_Formats) - Audio/visual formats wiki (site currently parked).

### Game-Specific Wikis

- [The Cutting Room Floor](https://tcrf.net/Help:Contents/Finding_Content) - Community for discovering and documenting unused and debug game content.
- [Nintendo File Formats](https://nintendo-formats.com/) - Documentation for Wii U and Switch games.
- [Custom Mario Kart Wiiki](https://wiki.tockdom.com/wiki/List_of_File_Formats) - Formats used in Mario Kart Wii and related games.
- [Luma's Workshop](https://www.lumasworkshop.com/wiki/Category:File_formats) - Nintendo modding wiki.
- [Souls Modding Wiki](http://www.soulsmodding.com/doku.php?id=start) - Documentation for FromSoftware formats.

### 📚 Learning Resources & Tutorials

- **[DGTEFF](https://web.archive.org/web/20230817151933/http://wiki.xentax.com/index.php/DGTEFF) - Definitive Guide To Exploring File Formats.**
- [The VG Resource Wiki](https://wiki.vg-resource.com/Main_Page) - Wiki with tutorials for ripping and creating sprites, models, textures, and sounds across gaming platforms.
- [Compression Deep Dive](https://chronovore.dev/posts/2023-01-25-1234P-compression-deepdive.html) - Technical analysis of compression algorithms used in games.
- [How to Crack a Binary File Format](https://www.iwriteiam.nl/Ha_HTCABFF.html) - Classic tutorial on reverse engineering file formats.
- [kovidomi/game-reversing](https://github.com/kovidomi/game-reversing) - Beginner learning materials on reverse engineering video games.
- [How to Grab Models and Textures](https://aknavj.github.io/3d/2019/06/10/Grabbing-models-and-textures-from-game-or-3D-application.html) - Guide on extracting models and textures from games.
- [ReWolf's Retrogaming Blog](http://blog.rewolf.pl/blog/?cat=23) - Blog posts on retrogaming and reverse engineering.

#### 🎥 Video Tutorials

- [Binary File Format Engineering and Reverse Engineering](https://www.youtube.com/watch?v=8OxtBxXfJHw) - Peter Bindels - ACCU 2023 conference talk on binary file format analysis and reverse engineering techniques.
- [Reverse engineering game formats for fun and profit! (or just fun)](https://www.youtube.com/watch?v=MXbo6y6MCPE) - Spencer Alves - !!Con West 2020 talk on reverse engineering game file formats.
- [What's In A Bit - Designing, Using And Reverse-engineering Binary File Formats](https://www.youtube.com/watch?v=QEIGc3tXGmM) - Peter Bindels - cpponsea talk on binary file format design and reverse engineering.
- [File Format Reverse Engineering 1 - Intro, target, and tools](https://www.youtube.com/watch?v=_zCekiF5aBQ) - CO/DE tutorial series introduction to file format reverse engineering.
- [Reverse Engineered old Compression Algorithm for Frogger](https://www.youtube.com/watch?v=BwoOB2QFXvw) - LiveOverflow - Case study on reverse engineering compression algorithms in classic games.

### Asset Databases

- [The VG Resource (archived)](https://archive.vg-resource.com/index.php) - Models, Textures, Sounds, and Sprite databases and forums.
  - [The Spriters Resource](https://www.spriters-resource.com/) - Dedicated sprite and pixel art database.
  - [The Models Resource](https://models.spriters-resource.com/) - Dedicated 3D model database.
  - [The Textures Resource](https://textures.spriters-resource.com/) - Dedicated texture database.
  - [The Sounds Resource](https://sounds.spriters-resource.com/) - Dedicated audio and music database.

## 🛠️ General Tools

*Multi-format tools that support a wide variety of games.*

### 🎨 Model, Texture & Animation

- [Noesis](http://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91) - Popular all-in-one tool for previewing and converting 500+ model, texture, and animation formats. Supports batch conversion, has a rich plugin ecosystem, and can handle most common game formats out of the box.
  - [Noesis Plugins (Rich Whitehouse)](http://richwhitehouse.com/index.php?content=inc_projects.php#prjmp91) - Official plugin collection by the creator of Noesis.
  - [Noesis Plugins (HimeWorks)](https://himeworks.com/noesis-plugins/) - Community plugin collection including Tales series and Midnight Club 2 support.
  - [Noesis Plugins (Durik256)](https://github.com/Durik256/Noesis-Plugins) - Community plugins for various game formats.
  - [Noesis Plugins (mrpostiga)](https://github.com/mrpostiga/noesis-plugins-official) - Additional community-maintained plugin collection.
  - [Noesis Plugins (RoadTrain)](https://github.com/RoadTrain/noesis-plugins) - Community plugins for additional game formats.
  - [Noesis Plugins (Zheneq)](https://github.com/Zheneq/Noesis-Plugins) - Community plugin collection with various format support.
- [TexViewer](https://github.com/Puxtril/TexViewer) - Tool to help discover unknown texture formats.
- [binviz](https://github.com/VelocityRa/binviz) - Binary visualization tool for identifying patterns and structure in unknown files. Creates visual representations showing potential compression/encryption, structured data and padding at a glance. Helpful for spotting where assets begin/end in unstructured archives.
- [DDS.Tools](https://github.com/BoBoBaSs84/DDS.Tools) - Command line bulk PNG to DDS (and vice versa) conversion tool with duplicate detection.
- [BodySlide and Outfit Studio](https://github.com/ousnius/BodySlide-and-Outfit-Studio) - Tool to convert, create, and customize outfits and bodies for The Elder Scrolls and Fallout games.
- [Cathedral Assets Optimizer](https://www.nexusmods.com/skyrimspecialedition/mods/23316) - Tool to automatically optimize BSAs, meshes, textures and animations for Bethesda games.

### 📦 Archive & Asset Extraction

- [QuickBMS](https://aluigi.altervista.org/quickbms.htm) - Universal archive extractor and reimporter with extensive script database covering thousands of games. Uses BMS scripting language to describe archive formats.
- [AssetRipper](https://github.com/AssetRipper) - Tool for extracting assets from Unity and other engines.
- [Switch Toolbox](https://github.com/KillzXGaming/Switch-Toolbox) - Tool to edit many video game file formats (Nintendo focus).
- [MeltyTool](https://github.com/MeltyPlayer/MeltyTool) - Multitool for viewing/extracting assets from various N64/GCN/3DS/PC games.
- [bartlomiejduda/Tools](https://github.com/bartlomiejduda/Tools) - Set of tools to manage and modify files from many various games.
- [BAE](https://www.nexusmods.com/starfield/mods/165) - Bethesda Archive Extractor application for BSA/BA2 archives.
- [BSA Browser](https://github.com/AlexxEG/BSA_Browser) - Bethesda Archive (BSA and BA2) browser & extractor application.
- [LSLib](https://github.com/Norbyte/lslib) - Tools for manipulating Divinity Original Sin and Baldur's Gate 3 files including archive extraction.

### 🔊 Audio Tools

- [vgmstream](https://github.com/vgmstream/vgmstream) - Audio playback library supporting 1000+ game audio formats including looping, multi-channel streams, and console-specific codecs. Works as a standalone player or Winamp/foobar2000 plugin. If a game audio file exists, vgmstream probably plays it.
- [vgm_ripping](https://github.com/hcs64/vgm_ripping) - Sources for game music ripping tools.

### 🌐 Translation & Localization

- [Kuriimu](https://github.com/IcySon55/Kuriimu) - General purpose game translation toolkit.
- [Kuriimu2](https://github.com/FanTranslatorsInternational/Kuriimu2) - Next-gen version of Kuriimu.

### 🔍 Binary Analysis & Hex Editors

- [010 Editor](https://www.sweetscape.com/010editor/) - Professional hex editor with powerful template system for analyzing binary file structures (paid).
- [ImHex](https://github.com/WerWolv/ImHex) - Modern, open-source hex editor with pattern language for reverse engineering file formats (free).
- [Kaitai Struct](https://kaitai.io/) - Declarative language for describing binary data structures with code generation for multiple programming languages.
- [Veles](https://codisec.com/veles/) - Binary analysis and visualization tool for reverse engineering (open-source).
- [010 Templates / ImHex Patterns](https://github.com/neptuwunium/bt) - Templates for binary analysis.
- [010GameTemplates](https://github.com/Nenkai/010GameTemplates) - Collection of 010 Editor templates for various games.

### 💻 Libraries & Development Tools

- [DragonLib](https://github.com/neptuwunium/DragonLib) - Common library for file format research.
- [gclib](https://github.com/LagoLunatic/gclib) - Python implementations of several GameCube file formats for ROM hacking.
- [XeNTaXTools-Legacy](https://github.com/XeNTaXTools/XeNTaXTools-Legacy) - Legacy tools scraped from the XeNTaX forums.
- [EdnessP/scripts](https://github.com/EdnessP/scripts) - Various scripts for game file formats.

### Decompilation Tools

- [decomp-toolkit](https://github.com/encounter/decomp-toolkit) - GameCube & Wii decompilation toolkit.
- [splat](https://github.com/ethteck/splat) - Binary splitting tool to assist with decompilation and modding projects.
- [objdiff](https://github.com/encounter/objdiff) - Local diffing tool for decompilation projects.
- [decomp-permuter](https://github.com/simonlindholm/decomp-permuter) - Randomly permute C files to better match a target binary.
- [m2c](https://github.com/matt-kempster/m2c) - MIPS and PowerPC decompiler.
- [vutrace](https://github.com/chaoticgd/vutrace) - PS2 VU tracing debugger.

### Blender Addons

- [NifTools Blender Addon](https://github.com/niftools/blender_niftools_addon) - Blender addon for NetImmerse File Formats (.nif, .kf, .egm).
- [NaomiLib Blender Addon](https://github.com/NaomiMod/blender-NaomiLib) - Blender addon for importing NaomiLib files.
- [PyNifly](https://github.com/BadDogSkyrim/PyNifly) - Blender addon to import/export NIF files with support for Skyrim LE, Skyrim SE, Fallout 4, Fallout New Vegas, Fallout 76, and Fallout 3.

## ⚙️ Engines

*Tools specific to widespread third-party game engines.*

### GameMaker

- [UndertaleModTool](https://github.com/UnderminersTeam/UndertaleModTool) - Tool for modding/decompiling GameMaker games.
- [GMS-Explorer](https://github.com/puggsoy/GMS-Explorer) - Game Maker Studio `data.win` explorer.

### Source (Valve)

- [noclip.website (Source Engine)](https://github.com/magcius/noclip.website/tree/main/src/SourceEngine) - In-browser Source engine map viewer supporting Counter-Strike: Source, Half-Life 2, Half-Life 2: Deathmatch, Half-Life 2: Lost Coast, Half-Life 2: Episode 1, Half-Life 2: Episode 2, Team Fortress 2, Portal, Portal 2, Counter-Strike: Global Offensive, Left 4 Dead 2, The Stanley Parable, Infra, Neo Tokyo, and Estranged: Act I.
- [noclip.website (GoldSrc)](https://github.com/magcius/noclip.website/tree/main/src/GoldSrc) - In-browser Half-Life (GoldSrc) viewer.
- [studiomodel](https://github.com/Galaco/studiomodel) - Go library for loading Valve studiomodel formats (.mdl, .vtx, .vvd).
- [VTFLib](https://github.com/NeilJed/VTFLib) - C/C++ library for reading/writing VTF and VMT texture/material files.
- [srctools](https://github.com/TeamSpen210/srctools) - Python modules for working with Source Engine file formats (VMF, BSP, VPK, etc).
- [vdf-parser](https://github.com/lukezbihlyj/vdf-parser) - Parser for Valve Data Format (VDF) files used in Source games.
- [go-valve](https://github.com/handsomematt/go-valve) - Go library for querying A2S server information from Source servers.
- [valve-vrm](https://github.com/UnBeatWaterGH/valve-vrm) - Documentation and converter for Valve's experimental VRM model format.
- [sledge-formats](https://github.com/LogicAndTrick/sledge-formats) - C# parsers and formats for Half-Life 1 and related engines.
- [corvid](https://github.com/KILLTUBE/corvid) - Source Engine level converter for Call of Duty.

### Unity

- [AssetStudio (Perfare)](https://github.com/Perfare/AssetStudio) - Explorer/exporter for Unity assets and assetbundles (original version).
- [AssetStudio (aelurum fork)](https://github.com/aelurum/AssetStudio) - Actively maintained fork with UI optimization and enhancements.
- [AssetStudio (zhangjiequan fork)](https://github.com/zhangjiequan/AssetStudio) - Continuation of Perfare's AssetStudio with support for new Unity versions and additional improvements.
- [UABEA (Unity Asset Bundle Extractor Avalonia)](https://github.com/nesrak1/UABEA) - Cross-platform Unity asset bundle and serialized file editor/extractor built with Avalonia.
- [UnityExplorer](https://github.com/sinai-dev/UnityExplorer) - In-game UI for exploring, debugging and modifying IL2CPP and Mono Unity games.

### Unreal Engine

- [UEViewer (UModel)](https://github.com/gildor2/UEViewer) - Viewer and exporter for Unreal Engine 1-4 assets.
  - [Compatibility Table](https://www.gildor.org/projects/umodel/compat) - Official compatibility list.
- [FModel](https://fmodel.app/) - Open-source software for data-mining UE4-5 games.
- [CUE4Parse](https://github.com/FabianFG/CUE4Parse) - C# Parser for UE archives.
- [UnrealExporter](https://github.com/luk-gg/UnrealExporter) - Batch file exporter.
- [UE-Modding-Tools](https://github.com/Buckminsterfullerene02/UE-Modding-Tools) - Databank of generic UE modding tools.
- [Snooper](https://github.com/FModel/Snooper/tree/opengl) - OpenGL based 3D viewer for cooked UE packages.

## 🔧 Middleware & SDKs

*Game development middleware, libraries, and SDK-provided formats used across multiple titles and platforms.*

### Fast3d/F3dex (N64)

*SGI's microcode format for defining 3D graphics on the Nintendo 64. Used in [Super Mario 64](#super-mario-64), [Paper Mario 64](#paper-mario-64), [Banjo-Kazooie](#rare), and many other N64 titles.*

- [n64-fast3d-engine](https://github.com/Emill/n64-fast3d-engine) - N64 Fast3D engine implementation.
- [noclip.website (Banjo)](https://github.com/magcius/noclip.website/blob/main/src/BanjoKazooie/f3dex.ts) - F3DEX implementation for Banjo-Kazooie viewer.
- [MeltyTool (F3dzex2)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/F3dzex2) - F3DZEX2 format support.
- [F3DEX2Decoder](https://github.com/Mr-Wiseguy/F3DEX2Decoder) - Decoder for F3DEX2 display lists.
- [F3D2F3DEX](https://github.com/Trenavix/F3D2F3DEX) - Converter between F3D variants.
- [Hack64 Fast3D Commands](https://hack64.net/wiki/doku.php?id=super_mario_64:fast3d_display_list_commands) - Documentation for Fast3D display list commands.
- [CloudModding F3DZEX2](https://wiki.cloudmodding.com/oot/F3DZEX2) - Documentation for F3DZEX2 format.

### JSYSTEM (GameCube/Wii)

*Nintendo's in-house middleware used to develop GameCube and Wii era games. Used in [Pikmin](#pikmin), [Pikmin 2](#pikmin-2), [Luigi's Mansion](#luigis-mansion), [Super Mario Sunshine](#super-mario-other), [Super Mario Galaxy](#super-mario-other), [Wind Waker](#zelda), [Twilight Princess](#zelda), [Mario Kart: Double Dash](#mario-kart-double-dash), and many other first-party GameCube/Wii titles.*

- [Amnoid GC Resources](http://amnoid.de/gc/) - Documentation and resources for GameCube file formats.
- [JStudio (LordNed)](https://github.com/LordNed/JStudio) - Classes for Wind Waker J* tools.
- [J3D-Model-Viewer](https://github.com/LordNed/J3D-Model-Viewer) - Viewer for J3D models.
- [Hack.io](https://github.com/SuperHackio/Hack.io) - Libraries for J3D Era formats.
- [noclip.website (JSYSTEM)](https://github.com/magcius/noclip.website/tree/main/src/Common/JSYSTEM) - In-browser viewer for JSYSTEM formats.
- [MeltyTool (JSystem)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/JSystem) - JSystem format viewer/exporter.
- [SuperBMD](https://github.com/Sage-of-Mirrors/SuperBMD) - BMD/BDL model converter for GameCube/Wii games.
- [p2setoolkit](https://github.com/NerduMiner/p2setoolkit) - Toolkit for disassembling/reassembling Pikmin 2 BMS sequenced music files.
- [Rain336/JSystem](https://github.com/Rain336/JSystem) - Rust libraries for parsing Nintendo Wii/GameCube file formats (BCSV, RARC, U8).
- [Luma's Workshop (BMD)](https://lumasworkshop.com/wiki/BMD/BDL_(File_Format)) - BMD/BDL format documentation.
- [Wiki.CloudModding (JSYSTEM)](https://wiki.cloudmodding.com/zgcn/JSYSTEM) - JSYSTEM format documentation.
- [blojob](https://github.com/arookas/blojob) - J2DGraph BLO format tool.
- [pyblo2-gui](https://github.com/RenolY2/pyblo2-gui) - GUI for working with BLO files.
- [j3dview](https://github.com/blank63/j3dview) - J3DGraph viewer.
- [blemd](https://github.com/Sage-of-Mirrors/blemd) - Blender addon for J3D models.
- [J3DUltra](https://github.com/Sage-of-Mirrors/J3DUltra) - Advanced J3D model tool.
- [Jekyll](https://github.com/Sage-of-Mirrors/Jekyll) - J3D animation tool.
- [RiiStudio](https://github.com/snailspeed3/RiiStudio) - Modern editor for J3D models.
- [Tockdom BMD/BDL](https://wiki.tockdom.com/wiki/BMD_and_BDL_(File_Format)) - BMD/BDL format documentation.
- [ibnktool](https://github.com/XAYRGA/ibnktool) - JAudio instrument bank tool.
- [pyjmap](https://github.com/SunakazeKun/pyjmap) - JMap format library.
- [jpc_conv](https://github.com/PikHacker/jpc_conv) - JParticle converter.
- [pikmin2-stb](https://github.com/RenolY2/pikmin2-stb) - JStudio format tool.
- [Yaz0Decoder](https://github.com/Cuyler36/Yaz0Decoder) - Yaz0 compression decoder.
- [rarc-rs](https://github.com/gcnhax/rarc-rs) - Rust library for RARC archives.
- [WArchive-Tools](https://github.com/LordNed/WArchive-Tools) - Tools for working with RARC archives.
- [RARClib.py](https://github.com/RenolY2/RARClib.py) - Python library for RARC format.
- [yaz0-decode-encode](https://github.com/RenolY2/yaz0-decode-encode) - Yaz0 compression tool.
- [BTITool](https://github.com/Sage-of-Mirrors/BTITool) - BTI texture tool.
- [GCFontTool](https://github.com/Sage-of-Mirrors/GCFontTool) - GameCube font tool.
- [libbti](https://github.com/Sage-of-Mirrors/libbti) - BTI texture library.
- [RarcPack](https://github.com/Sage-of-Mirrors/RarcPack) - RARC archive packer.
- [pyjkernel](https://github.com/SunakazeKun/pyjkernel) - Python library for JKernel formats.
- [WiiExplorer](https://github.com/SuperHackio/WiiExplorer) - Wii filesystem explorer.
- [ARCTool](https://github.com/tpwrules/ARCTool) - Tool for ARC/RARC archives.

### Sappy (GBA Audio)

*SDK-provided formats for the Game Boy Advance sound engine. Used in [Pokémon Gen III](#gen-iii) and many other GBA titles.*

- [gba-mus-ripper](https://github.com/berg8793/gba-mus-ripper) - GBA music ripper.
- [SapPy](https://github.com/hfmkwi/SapPy) - Python-based GBA sound tool.
- [agbplay](https://github.com/ipatix/agbplay) - Music player and music ripper for GBA.
- [sappy](https://github.com/maddievision/sappy) - GBA sound tool.
- [Sappy (Touched)](https://github.com/Touched/Sappy) - Fork with additional features.

## Formats by Studio / Game

### Activision / Infinity Ward / Treyarch

#### Call of Duty

- [blender-cod](https://github.com/CoDEmanX/blender-cod) - Blender Add-On for Call of Duty modding.
- [WraithXArchon](https://github.com/dtzxporter/WraithXArchon/) - Asset extraction tool.
- [Cordycep](https://github.com/Scobalula/Cordycep) - Tool to load and parse Call of Duty fast files.
- [zonebuilder](https://github.com/RagdollPhysics/zonebuilder) - Fastfile Generator for IW4 (Modern Warfare 2).
- [iw4-open-formats](https://github.com/iw4x/iw4-open-formats/blob/main/src/iw4-of/assets/assets.cpp) - Asset conversion system for MW2 formats.
- [C2M](https://github.com/sheilan102/C2M) - Map exporter for Call of Duty.

### Angel Studios / Rockstar San Diego

- [AngelStudiosBlenderAddon](https://github.com/Dummiesman/AngelStudiosBlenderAddon) - Blender addon for importing models from Angel Studios games (~1999-2006).
- [MidnightClub2 (Noesis)](https://himeworks.com/noesis-plugins/) - Noesis plugin for Midnight Club 2 model formats.
- [Sollumz](https://docs.sollumz.org) - GTA V modding suite for Blender (RAGE engine formats).
- [pyrpfiv](https://github.com/gmroder/pyrpfiv) - Python library for parsing and manipulating GTA IV's RPF (Resource Package Format) archives.
- [noclip.website (Grand Theft Auto III)](https://github.com/magcius/noclip.website/tree/main/src/GrandTheftAuto3) - In-browser Grand Theft Auto III viewer.
- [noclip.website (Grand Theft Auto: Vice City)](https://github.com/magcius/noclip.website/tree/main/src/GrandTheftAuto3) - In-browser Grand Theft Auto: Vice City viewer.
- [noclip.website (Grand Theft Auto: San Andreas)](https://github.com/magcius/noclip.website/tree/main/src/GrandTheftAuto3) - In-browser Grand Theft Auto: San Andreas viewer.
- [MidtownExtractor](https://github.com/0x1F9F1/MidtownExtractor) - Midtown Madness 1/2 and Midnight Club 2 File Extractor
- [MeltyTool](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/AngelStudios) - Multitool for viewing/extracting assets from various N64/GCN/3DS/PC games en-masse.

### Ape, Inc

- [earthbound-script-dumper](https://github.com/CataLatas/earthbound-script-dumper) - Script dumper for EarthBound.
- [ebtexted](https://github.com/PKHackers/ebtexted) - Text editor for EarthBound.
- [EBME](https://github.com/Supremekirb/EBME) - EarthBound Map Editor.

### Argonaut Games

- [PS1-BRender-Reverse](https://github.com/OverSurge/PS1-Argonaut-Reverse) - Reverse engineering tools for PlayStation 1 BRender engine games like Harry Potter and Croc 2.

### Arkane Studios

- [disrev](https://github.com/chipolux/disrev) - Python tools for extracting and modifying Dishonored 2 assets.
- [dishonored2_scripts](https://github.com/usernametoolo/dishonored2_scripts/blob/master/tools/scripts/unpack_resources.py) - Resource extraction script for unpacking .pak archives.
- [Obscura](https://github.com/Mikompilation/Obscura) - Modding toolkit for Dishonored games.

### Atlus

- [DDS3-Model-Studio](https://github.com/tge-was-taken/DDS3-Model-Studio) - WIP Model editing tools for DDS3 engine based SMT games (SMT: Nocturne, DDS 1 & 2, Raidou 1 & 2).

### Asobo Studio

- [fmtk](https://github.com/widberg/fmtk) - FUEL Modding Toolkit.

### Bandai Namco

- [BinarySerializer.Klonoa](https://github.com/BinarySerializer/BinarySerializer.Klonoa) - Serializer for Klonoa games.
- [TalesOfFantasy (Noesis)](https://himeworks.com/noesis-plugins/) - Noesis plugins for Tales series.
- [ARC](https://github.com/Bigchillghost/ARC) - Animation Recipe Cracker for Bandai Namco games.
- [noclip.website (Klonoa)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Klonoa viewer.
- [noclip.website (Katamari Damacy)](https://github.com/magcius/noclip.website/tree/main/src/KatamariDamacy) - In-browser Katamari Damacy viewer.

### Capcom

#### Monster Hunter

- [Mod3-MHW-Importer](https://github.com/AsteriskAmpersand/Mod3-MHW-Importer) - Blender Import-Exporter for Monster Hunter World Mod3 model format.

#### Devil May Cry

- [dmc_hd_tools](https://github.com/Kerilk/dmc_hd_tools) - Toolkit for Devil May Cry HD Collection including Noesis plugins and binary templates.

### CCP Games

- [yretenai/Jackdaw](https://github.com/neptuwunium/Jackdaw) - Research project for Carbon Engine file formats used in EVE Online.

### CD Projekt Red

#### The Witcher 3 / REDEngine 3

- [WolvenKit (legacy)](https://github.com/WolvenKit/WolvenKit-7) - REDEngine 3 file editor designed to simplify and accelerate modding workflow for The Witcher 3.

#### Cyberpunk 2077 / REDEngine 4

- [WolvenKit](https://github.com/WolvenKit/WolvenKit) - REDEngine 4 file editor designed to simplify and accelerate modding workflow for Cyberpunk 2077.
- [Cyber Engine Tweaks](https://github.com/maximegmd/CyberEngineTweaks) - Framework to script mods using Lua with access to all the internal scripting features.

### Cygames

- [GBFRBlenderTools](https://github.com/WistfulHopes/GBFRBlenderTools) - Blender addon for importing Granblue Fantasy Relink mesh models.
- [GBFR2Blender2GBFR](https://github.com/WistfulHopes/GBFR2Blender2GBFR) - Tools for importing/exporting animations and collision data for Granblue Fantasy Relink.

### Clover Studio

- [noclip.website (Okami)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Okami viewer.

### Double Fine

- [noclip.website (Psychonauts)](https://github.com/magcius/noclip.website/tree/main/src/psychonauts) - In-browser Psychonauts viewer.

### EA Black Box

#### Need for Speed Series

- [Binary](https://github.com/NFSCO/Binary) - Tool for editing Black Box Need for Speed binary .BIN, .BUN, .LZC files.
- [Icebreaker](https://github.com/R-033/icebreaker) - NIS (NFS Most Wanted cutscene files) editing tool.
- [MAD x VP6 x MPC x MPV x WMV Compiler](https://github.com/bluesky-dev12/MAD-x-VP6-x-MPC-x-MPV-x-WMV-Compiler) - Compilation of tools for compiling WMV, MAD, VP6, MPC and MPV video formats for Black Box games.
- [NFS.BIN.Tool](https://github.com/Ekey/NFS.BIN.Tool) - Tool for extracting ZZDATA archives from NFS console games.
- [NFS Carbon PDFData Compiler](https://github.com/bluesky-dev12/PFDataCompiler) - Helper to convert music to NFS Carbon format.
- [NFS SPEECHTOOL](https://github.com/TheUnpunished/SpeechTool) - Speech audio files editor for NFS ProStreet, Undercover & World.
- [NFS TMXTOOL](https://github.com/TheUnpunished/tmxtool) - TMX audio files encoder for NFS ProStreet, Undercover & World.
- [UCGT](https://github.com/NI240SX/UCGT) - NFS Undercover geometry editor (file compiler/decompiler).
- [Vivianne](https://github.com/TheXDS/Vivianne) - NFS 3/4 All-in-one VIV and FSH/QFS editor that aims to provide you with tools to edit textures, car performance and fedata files.
- [noclip.website (Need for Speed: Most Wanted)](https://github.com/magcius/noclip.website/tree/main/src/NeedForSpeedMostWanted) - In-browser Need for Speed: Most Wanted viewer.

### FromSoftware

*Demon's Souls, Dark Souls, Bloodborne, Sekiro, Elden Ring.*

- [Souls Modding Wiki](http://www.soulsmodding.com/doku.php?id=start) - Documentation for FromSoftware formats.
- [Awesome Elden Ring](https://github.com/sovietspaceship/awesome-elden-ring) - Curated list of resources and tools for Elden Ring.
- [Sekiro Modding Wiki](https://github.com/SekiroResurrection/modding-wiki) - Documentation for Sekiro modding.
- [DSMapStudio](https://github.com/soulsmods/DSMapStudio) - Map/level editor for Souls/Bloodborne/Elden Ring.
- [DSMSPortable](https://github.com/mountlover/DSMSPortable/tree/main) - Portable version of DSMapStudio.
- [FLVER_Editor](https://github.com/asasasasasbc/FLVER_Editor) - Editor for FLVER 3D model format.
- [BinderTool](https://github.com/Atvaark/BinderTool) - Tool for extracting and repacking BND/BHD archives.
- [dark-souls-map-viewer](https://github.com/colevk/dark-souls-map-viewer) - Web-based Dark Souls map viewer.
- [blender-flver](https://github.com/elizagamedev/blender-flver) - Blender addon for importing/exporting FLVER models.
- [FromSoftware-Blender-Importer](https://github.com/FelixBenter/FromSoftware-Blender-Importer) - Blender importer for FromSoftware formats.
- [soulstruct](https://github.com/Grimrukh/soulstruct) - Python library for Dark Souls file formats and modding.
- [soulstruct-blender](https://github.com/Grimrukh/soulstruct-blender) - Blender plugin for soulstruct.
- [SoulsTemplates](https://github.com/JKAnderson/SoulsTemplates) - 010 Editor templates for Souls formats.
- [noclip.website (DarkSouls)](https://github.com/magcius/noclip.website/tree/main/src/DarkSouls) - In-browser Dark Souls map viewer.
- [DSAnimStudio](https://github.com/Meowmaritus/DSAnimStudio) - Animation and cutscene editor for Souls games.
- [ESDLang](https://github.com/thefifthmatt/ESDLang) - Decompiler for ESD event script format.
- [Gibbed.DarkSouls](https://github.com/gibbed/Gibbed.DarkSouls) - Tools & code for use with Dark Souls.
- [DS2Template](https://github.com/LordRadai/DS2Template) - Collection of 010 .bt templates specifically made for Dark Souls II

### Game Freak

*Pokémon games across various generations.*

#### Gen I & II

- [map-editor](https://github.com/KernelEquinox/map-editor) - Map editor for Generation I/II Pokémon games.
- [polished-map](https://github.com/Rangi42/polished-map) - Polished map editor for Gen II.

#### Gen III

*See also [Sappy (GBA Audio)](#sappy-gba-audio) for audio tools used in these games.*

- [blue-spider](https://github.com/cosarara/blue-spider) - Map editor for Pokémon Ruby/Sapphire/Emerald.
- [porymap](https://github.com/huderlem/porymap) - Modern map editor for Gen III Pokémon games.
- [MEH](https://github.com/shinyquagsire23/MEH) - Map editor for Gen III.
- [AwesomeMapEditor](https://github.com/Sierraffinity/AwesomeMapEditor) - Alternative map editor for Gen III.
- [Bulbapedia (Gen I)](https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_I)) - Save data structure documentation for Generation I.
- [Bulbapedia (Gen II)](https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_II)) - Save data structure documentation for Generation II.
- [Bulbapedia (Gen III)](https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_III)) - Save data structure documentation for Generation III.

### Genius Sonority

*Pokémon Colosseum, Pokémon XD: Gale of Darkness.*

- [pokemon_fsys_tool](https://github.com/gamemasterplc/pokemon_fsys_tool) - Tool for FSYS archive format used in Pokémon Colosseum/XD.
- [PokemonFSYSConverter](https://github.com/vgmoose/PokemonFSYSConverter) - Converter for FSYS archive format.

### Grezzo

*Ocarina of Time 3D, Majora's Mask 3D, Luigi's Mansion remake.*

- [io_scene_cmb](https://github.com/M-1-RLG/io_scene_cmb) - Blender add-on for Grezzo's "Ctr Model Binary" (CMB) format.
- [noclip.website (OoT3D)](https://github.com/magcius/noclip.website/tree/main/src/OcarinaOfTime3D) - In-browser Ocarina of Time 3D viewer.
- [MeltyTool (Grezzo)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/Grezzo) - Grezzo format viewer/exporter.
- [N3DSCmbViewer](https://github.com/xdanieldzd/N3DSCmbViewer) - Viewer for 3DS CMB models.
- [Scarlet](https://github.com/xdanieldzd/Scarlet) - General purpose 3DS/Vita game tool.
- [Gar/Zar UnPacker](https://gbatemp.net/threads/release-gar-zar-unpacker-v0-1.385264/) - Archive unpacker for Ocarina of Time 3D and Majora's Mask 3D.
- [Switch-Toolbox](https://github.com/KillzXGaming/Switch-Toolbox/tree/master/File_Format_Library/FileFormats/Grezzo) - A tool to edit many video game file formats

### Guerrilla Games

- [ProjectZeroDawn](https://github.com/neptuwunium/ProjectZeroDawn) - File format research and tools for Horizon Zero Dawn.

### Gust (Koei Tecmo)

- [gust_stuff](https://github.com/eArmada8/gust_stuff) - Modding toolkit for G1M model files used in Gust games (Atelier series).
- [Project-G1M](https://github.com/Joschuka/Project-G1M) - Noesis plugin for importing G1M 3D model format used in Gust and Bandai Namco games.

### HAL Laboratory

*Kirby, Super Smash Bros series.*

- [Smash-Forge](https://github.com/jam1garner/Smash-Forge) - Editor for Super Smash Bros 4 file formats.
- [HSDLib](https://github.com/Ploaj/HSDLib) - Library for HAL's HSD format (used in Super Smash Bros Melee).
- [MeleeMedia](https://github.com/Ploaj/MeleeMedia) - Media extractor for Super Smash Bros Melee.
- [noclip.website (Melee)](https://github.com/magcius/noclip.website/tree/main/src/SuperSmashBrosMelee) - In-browser Melee stage viewer.
- [noclip.website (Super Smash Bros Brawl)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Super Smash Bros Brawl viewer.
- [noclip.website (SYSDOLPHIN)](https://github.com/magcius/noclip.website/tree/main/src/SYSDOLPHIN) - In-browser SYSDOLPHIN format viewer.
- [noclip.website (Kirby Air Ride)](https://github.com/magcius/noclip.website/tree/main/src/KirbyAirRide) - In-browser Kirby Air Ride viewer.
- [noclip.website (Kirby's Return to Dream Land)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Kirby's Return to Dream Land viewer.
- [MeltyTool (Sysdolphin)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/Sysdolphin) - Sysdolphin format viewer/exporter.
- [Melee DAT format](https://smashboards.com/threads/melee-dat-format.292603/) - Documentation for Melee's DAT format.
- [DATReaderC](https://github.com/EstevanBR/DATReaderC) - A C program that reads a .dat file (Super Smash Bros. Melee)

### Heavy Iron Studios

- [IndustrialPark](https://github.com/igorseabra4/IndustrialPark) - Viewer and editor for SpongeBob SquarePants: Battle for Bikini Bottom and Scooby-Doo games.
- [noclip.website (SpongeBob Battle for Bikini Bottom)](https://github.com/magcius/noclip.website/tree/main/src/HeavyIron) - In-browser SpongeBob BFBB viewer.
- [noclip.website (SpongeBob The Movie)](https://github.com/magcius/noclip.website/tree/main/src/HeavyIron) - In-browser SpongeBob The Movie viewer.
- [noclip.website (SpongeBob Revenge of the Flying Dutchman)](https://github.com/magcius/noclip.website/tree/main/src/SpongebobRevengeOfTheFlyingDutchman) - In-browser SpongeBob ROTFD viewer.

### Hudson Soft

*Mario Party series (Nintendo 64).*

- [PartyPlanner64](https://github.com/PartyPlanner64/PartyPlanner64) - Full-featured board editor and modding tool for Mario Party (N64) games.
- [symbols](https://github.com/PartyPlanner64/symbols) - Debug symbol maps for reverse engineering Mario Party games.

### Insomniac Games

- [rivet](https://github.com/neptuwunium/rivet) - File format research project for Ratchet & Clank: Rift Apart.
- [ripped_apart](https://github.com/chaoticgd/ripped_apart) - Modding toolkit for Ratchet & Clank: Rift Apart.
- [insomniac-model](https://github.com/sleepyzay/insomniac-model) - Research and tools for Insomniac Games model formats.
- [DDLParser](https://github.com/macton/DDLParser) - Parser for Insomniac's Data Definition Language (DDL) format.
- [replanetizer](https://github.com/RatchetModding/replanetizer) - Full-featured level editor for PS3 Ratchet & Clank games.
- [RaCTrilogy-PS3-Tools](https://github.com/thtrandomlurker/RaCTrilogy-PS3-Tools) - Python scripts for extracting armor and model meshes from Ratchet & Clank PS3 Trilogy.
- [wrench](https://github.com/chaoticgd/wrench) - Set of modding tools for the Ratchet & Clank PS2 games.
- [horizon-forge](https://github.com/Horizon-Private-Server/horizon-forge) - Map editor for Ratchet: Deadlocked Multiplayer (PS2).
- [Overstrike](https://github.com/Tkachov/Overstrike) - Open-source mod manager for PC ports of Insomniac Games' games.

### Intelligent Systems

#### Paper Mario 64

*See also [Fast3d/F3dex (N64)](#fast3df3dex-n64) for graphics format tools used in this game.*

- [noclip.website (PM64)](https://github.com/magcius/noclip.website/tree/main/src/PaperMario64) - In-browser Paper Mario 64 map viewer.
- [star-rod](https://github.com/z64a/star-rod) - Modding tool for Paper Mario 64 including map editor and script tools.
- [Hack64 Paper Mario](https://hack64.net/wiki/doku.php?id=paper_mario) - Documentation for Paper Mario 64 file formats and data structures.

#### Paper Mario: TTYD / Super Paper Mario

*See also [JSYSTEM](#jsystem-gamecubewii) for additional format tools used in these games.*

- [SpmViewer](https://github.com/follyfoxe/SpmViewer) - Viewer for Super Paper Mario assets.
- [ttyd-utils](https://github.com/jdaster64/ttyd-utils) - Utilities for modding Paper Mario: TTYD.
- [noclip.website (TTYD)](https://github.com/magcius/noclip.website/tree/main/src/PaperMarioTTYD) - In-browser TTYD map viewer.
- [MeltyTool (TTYD)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/PaperMarioTheThousandYearDoor) - Model viewer/exporter.
- [PistonMiner/ttyd-tools](https://github.com/PistonMiner/ttyd-tools) - Development tools including Blender exporter, disassembler, and REL linker.
- [PaperMarioModelViewer](https://github.com/uyjulian/PaperMarioModelViewer) - Model viewer for Paper Mario games.
- [CollisionSceneBinary](https://github.com/KillzXGaming/CollisionSceneBinary) - A library and tool for handling csb and ctb collision files found in paper mario games.

### Interactive Studios

#### Glover

- [noclip.website (Glover)](https://github.com/magcius/noclip.website/tree/main/src/Glover) - In-browser Glover level viewer.
- [libgarib](https://github.com/naclomi/libgarib) - Library for Glover asset formats.

### iNiS

- [Murugo/Misc-Game-Research (Gitaroo Man)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Gitaroo%20Man) - Reverse engineering notes for Gitaroo Man (PS2).

### Jupiter

*Mario's Picross (Game Boy).*

- [MarioPicrossRipper](https://github.com/AkagitsuneYuki/MarioPicrossRipper) - Asset extraction tool for Mario's Picross.
- [MeltyTool (Picross)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/MariosPicross/MariosPicross) - Format viewer and exporter for Mario's Picross.
- [cgrr-mariospicross](https://github.com/sopoforic/cgrr-mariospicross) - Graphics extraction tool for Mario's Picross.
- [MarioPicrossLoader3000](https://github.com/T0biasCZe/MarioPicrossLoader3000) - Asset loader and viewer for Mario's Picross.
- [Picross Level Data](https://www.zophar.net/fileuploads/3/21546xutra/picrossleveldata.txt) - Technical documentation for Mario's Picross level data format.

### Jagex

*Old School RuneScape / RuneScape.*

- [CacheModelTools](https://github.com/Bloodspawns/CacheModelTools) - Tools for extracting and viewing OSRS cache models.
- [OSRS-Environment-Exporter](https://github.com/ConnorDY/OSRS-Environment-Exporter) - Environment and map exporter for Old School RuneScape.
- [modelviewer](https://github.com/waleedyaseen/modelviewer) - Model viewer for RuneScape cache files.

### Konami

#### Metal Gear Solid

- [MGS-MDL-Noesis](https://github.com/Jayveer/MGS-MDL-Noesis) - Noesis plugin for importing Metal Gear Solid 3 MDL models and MTAR animations.
- [Rex](https://github.com/Jayveer/Rex) - A tool to extract the Stage Dir and Dar files from the game Metal Gear Solid on PS1

#### Silent Hill

- [Sparagas/Silent-Hill](https://github.com/Sparagas/Silent-Hill) - Reverse engineering research and documentation for Silent Hill file formats.
- [Murugo/Misc-Game-Research (Silent Hill 2)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Silent%20Hill%202%2B3) - Reverse engineering notes for Silent Hill 2 & 3 (PS2).
- [Silent Hill Museum](https://silenthillmuseum.org/) - Website dedicated to Silent Hill series with file format documentation.
- [laura-a-n-n/silent-hill-museum](https://github.com/laura-a-n-n/silent-hill-museum) - Repository for Silent Hill Museum website with technical documentation.
- [Silent-Hill-2-Enhancements](https://github.com/elishacloud/Silent-Hill-2-Enhancements) - Project to enhance Silent Hill 2 (PC) graphics and audio, includes scripts to build or modify SH2 audio files (SFX, BGM, Dialog).
- [MGS-KMD-Noesis](https://github.com/Jayveer/MGS-KMD-Noesis) - Noesis Plugin for Metal Gear Solid PS1 Model (KMD) and Animation (OAR) files

### Kuju London

- [PF2-BMP-Editor](https://github.com/htimsnhoj543678/PF2-BMP-Editor) - Editor for PF2 BMP texture format used in Kuju games.
- [Battalion-Wars-SFX-Editor](https://github.com/JasperZebra/Battalion-Wars-SFX-Editor) - Sound effects editor for Battalion Wars.
- [MeltyTool (BattalionWars)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/BattalionWars) - Battalion Wars format viewer/exporter.
- [battalion-level-editor](https://github.com/RenolY2/battalion-level-editor) - Level editor for Battalion Wars.
- [battalion-tools](https://github.com/RenolY2/battalion-tools) - Collection of tools for working with Battalion Wars files.
- [bw-model-viewer](https://github.com/RenolY2/bw-model-viewer) - Model viewer for Battalion Wars.
- [bwterrain-blender](https://github.com/RenolY2/bwterrain-blender) - Blender addon for Battalion Wars terrain.
- [bw-restool](https://github.com/RenolY2/bw-restool) - Resource tool for Battalion Wars files.
- [bw-texture-conv](https://github.com/RenolY2/bw-texture-conv) - Texture converter for Battalion Wars.

### Larian Studios

#### Baldur's Gate 3

- [Norbyte's Baldur's Gate 3 Script Extender](https://github.com/Norbyte/bg3se) - Baldur's Gate 3 Script Extender.
- [Native Mod Loader](https://www.nexusmods.com/baldursgate3/mods/944) - Native DLL plugin loader for Baldur's Gate 3.

#### Divinity: Original Sin 2

- [Norbyte's Divinity Script Extender](https://github.com/Norbyte/ositools) - Divinity: Original Sin 2 script extender toolkit adding features to the scripting language of the game.

### Level-5

- [Metanoia](https://github.com/Ploaj/Metanoia) - Model viewer and research tool for Level-5 games.
- [MeltyTool (Level5)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/Level5) - Level-5 format viewer/exporter for games like Dark Cloud and Professor Layton.
- [CfgBinEditor](https://github.com/Tiniifan/CfgBinEditor) - Level 5 Bin Editor
- [Fougere](https://github.com/Tiniifan/Fougere) - Level-5 games tool.
- [GetNPCPos](https://github.com/Tiniifan/GetNPCPos) - Converting minimap coordinates to real NPC positions in Level-5 games
- [level5_material](https://github.com/Tiniifan/level5_material) - Convert .mtr to .json and back
- [Level5ResourceEditor](https://github.com/Tiniifan/Level5ResourceEditor) - Level-5 Resource Editor (RES.bin)
- [Nyanko](https://github.com/Tiniifan/Nyanko) - Level 5 Text Editor
- [Pingouin](https://github.com/Tiniifan/Pingouin) - Level 5 Archive File Manager
- [StudioElevenLib](https://github.com/Tiniifan/StudioElevenLib) - Additional C# library for files supported by the Studio Eleven Blender Addon

### Mario Artist

*Mario Artist series (Nintendo 64DD Disk Drive).*

- [leotools](https://github.com/jkbenaim/leotools) - Toolkit for extracting and working with 64DD disk images.
- [leo64dd_python](https://github.com/LuigiBlood/leo64dd_python) - Python-based tools for 64DD disk manipulation.
- [mfs_manager](https://github.com/LuigiBlood/mfs_manager) - Manager for MFS (Multi File System) used on 64DD disks.
- [MeltyTool (MarioArtist)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/MarioArtist) - Format viewer and exporter for Mario Artist series.
- [ma3d1toOBJ](https://github.com/LuigiBlood/ma3d1toOBJ) - Mario Artist Polygon Studio Model File to OBJ

### Microsoft Studios / Bungie / Turn 10

#### Halo

- [KSoft](https://github.com/KornnerStudios/KSoft) - Toolkit for working with Halo engine file formats.
- [HaloWarsDocs](https://github.com/HaloMods/HaloWarsDocs) - Documentation and 010 Editor templates for modding Halo Wars 1 and 2.
- [noclip.website (Halo: Combat Evolved)](https://github.com/magcius/noclip.website/tree/main/src/Halo1) - In-browser Halo: Combat Evolved viewer.

#### Forza

- [ForzaTech-extraction-tools](https://github.com/Doliman100/ForzaTech-extraction-tools) - Documentation and tools for ForzaTech .carbin and .modelbin file structures.

### Mobius Digital

- [noclip.website (Outer Wilds)](https://github.com/magcius/noclip.website/tree/main/src/OuterWilds) - In-browser Outer Wilds viewer.

### Midway

#### Gauntlet

- [gdl-tools (haekb)](https://github.com/haekb/gdl-tools) - Toolkit for Gauntlet Dark Legacy files.
- [gdl_wad_decoder](https://github.com/haekb/gdl_wad_decoder) - WAD archive decoder for Gauntlet Dark Legacy.
- [gdl_vbnk_decoder](https://github.com/haekb/gdl_vbnk_decoder) - Voice bank decoder for Gauntlet Dark Legacy.
- [gl_rom_decoder](https://github.com/haekb/gl_rom_decoder) - ROM decoder for Gauntlet Legends.
- [io_scene_gdl](https://github.com/haekb/io_scene_gdl) - Blender addon for Gauntlet Dark Legacy scene format.
- [gdl_tools (MosesofEgypt)](https://github.com/MosesofEgypt/gdl_tools) - Alternative toolkit for Gauntlet Dark Legacy.
- [MeltyTool (Gauntlet)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/GauntletDarkLegacy) - Gauntlet Dark Legacy format viewer/exporter.

#### NFL Blitz

- [NFL-Blitz-File-Editor](https://github.com/thompjake/NFL-Blitz-File-Editor) - File editor for NFL Blitz game data.
- [NFL-Blitz-Play-Maker](https://github.com/thompjake/NFL-Blitz-Play-Maker) - Playbook editor for NFL Blitz.
- [NFL_Blitz_Roster_Manager](https://github.com/thompjake/NFL_Blitz_Roster_Manager) - Roster management tool for NFL Blitz.
- [NFLBlitzDataEditor.Core](https://github.com/thompjake/NFLBlitzDataEditor.Core) - Core library for editing NFL Blitz data files.

### Naughty Dog

#### Crash Bandicoot 1-3 & CTR

- [CTR-tools](https://github.com/CTR-tools/CTR-tools) - Toolkit for Crash Team Racing (PlayStation 1) file formats.
- [CrashEdit](https://github.com/cbhacks/CrashEdit) - Level and graphics editor for PlayStation 1 Crash Bandicoot games.
- [drnsf](https://github.com/cbhacks/drnsf) - Format research tool for Naughty Dog games including Crash.
- [crash-bandicoot-nsf](https://github.com/dehodson/crash-bandicoot-nsf) - NSF (Naughty Dog Streaming File) format tools for Crash Bandicoot.
- [Crash-Bandicoot-2-Modelexport](https://github.com/warenhuis/Crash-Bandicoot-2-Modelexport) - Model exporter for Crash Bandicoot 2.
- [crashutils](https://github.com/wurlyfox/crashutils) - Collection of utilities for Crash Bandicoot file formats.
- [noclip.website (Crash Bandicoot: Warped)](https://github.com/magcius/noclip.website/tree/main/src/CrashWarped) - In-browser Crash Bandicoot: Warped viewer.

#### Jak and Daxter

- [jak1-vag-splitter](https://github.com/blahpy/jak1-vag-splitter) - Tool for splitting VAG audio files from Jak and Daxter 1.
- [JakAndDaxter1Sound](https://github.com/efimandreev0/JakAndDaxter1Sound) - Sound extraction and playback tool for Jak and Daxter 1.
- [Blender-Script-JaD-Actors](https://github.com/innocentmiau/Blender-Script-JaD-Actors) - Blender script for importing Jak and Daxter actor models.
- [JakAudioTools](https://github.com/jwetzell/JakAudioTools) - Audio extraction and conversion tools for Jak and Daxter series.
- [JakAudioTool](https://github.com/LuminarLight/JakAudioTool) - GUI tool for working with Jak and Daxter audio files.

### NanaOn-Sha

- [Murugo/Misc-Game-Research (Vib-Ribbon)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS1/Vib-Ribbon) - Reverse engineering notes for Vib-Ribbon (PS1).

### Nintendo EAD

*First-party Nintendo titles. Many GameCube/Wii games use [JSYSTEM](#jsystem-gamecubewii) middleware.*

#### Animal Crossing

*See also [JSYSTEM](#jsystem-gamecubewii) for additional format tools used in this game.*

- [010Editor-AnimalCrossing-Templates](https://github.com/Cuyler36/010Editor-AnimalCrossing-Templates) - Binary templates for analyzing Animal Crossing file formats in 010 Editor.
- [AC-Audiobank-Dumper](https://github.com/Cuyler36/AC-Audiobank-Dumper/tree/main/AC%20Audiobank%20Dumper) - Tool for extracting audio from Animal Crossing audio banks.
- [ACNESCreator](https://github.com/Cuyler36/ACNESCreator) - NES ROM editor for Animal Crossing.
- [ACSE](https://github.com/Cuyler36/ACSE) - Animal Crossing Save Editor for GameCube.
- [Animal-Crossing-Model-Editor](https://github.com/Cuyler36/Animal-Crossing-Model-Editor) - 3D model editor for Animal Crossing.
- [Animal-Crossing-Texture-Editor](https://github.com/Cuyler36/Animal-Crossing-Texture-Editor) - Texture editing tool for Animal Crossing.
- [Cross-View](https://github.com/Cuyler36/Cross-View) - Model viewer for Animal Crossing.
- [RELDumper](https://github.com/Cuyler36/RELDumper) - Tool for dumping REL files from Animal Crossing.

#### AST

*PCM audio format used in various Nintendo games.*

- [Nintendo-AST-Creator](https://github.com/gheskett/Nintendo-AST-Creator) - Tool for creating AST audio files for Nintendo games.
- [ast_to_wav](https://github.com/jdflyer/ast_to_wav) - Converter for AST audio files to WAV format.
- [MeltyTool (AST)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Formats/Ast) - AST audio format viewer/converter.
- [jatast](https://github.com/XAYRGA/jatast) - JAudio AST format tool.

#### Luigi's Mansion

*See also [JSYSTEM](#jsystem-gamecubewii) for additional format tools used in this game.*

- [Luigis-Mansion-Blender-Toolkit](https://github.com/Astral-C/Luigis-Mansion-Blender-Toolkit) - Blender toolkit for Luigi's Mansion models.
- [Dolhouse](https://github.com/opeyx/Dolhouse) - Level editor for Luigi's Mansion (GameCube).
- [Booldozer](https://github.com/Sage-of-Mirrors/Booldozer) - Collision editor for Luigi's Mansion.
- [noclip.website (Luigi's Mansion)](https://github.com/magcius/noclip.website/tree/main/src/LuigisMansion) - In-browser Luigi's Mansion viewer.

#### Pikmin

*See also [JSYSTEM](#jsystem-gamecubewii) for additional format tools used in this game.*

- [MODConv](https://github.com/intns/MODConv) - MOD model format converter for Pikmin 1.
- [Pikmin1Toolset](https://github.com/NerduMiner/Pikmin1Toolset) - Collection of modding tools including mod2obj converter for Pikmin 1.
- [PikBinGen](https://github.com/RenolY2/PikBinGen) - Binary file generator for creating custom Pikmin levels.
- [MeltyTool (Pikmin1)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/Pikmin1) - Pikmin 1 format viewer/exporter.
- [piki-tools](https://github.com/Minty-Meeo/piki-tools) - Collection of tools for working with Pikmin file formats.

#### Pikmin 2

*See also [JSYSTEM](#jsystem-gamecubewii) for additional Pikmin 2 tools.*

- [PikminEnemyParms](https://github.com/AntonioAntonio-ai/PikminEnemyParms) - GUI editor for modifying enemy parameters in Pikmin 2.
- [MeltyTool (Pikmin2)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/Pikmin2) - Pikmin 2 format viewer/exporter.
- [Pikmin-2-Symbol-Maps](https://github.com/Minty-Meeo/Pikmin-2-Symbol-Maps) - Debug symbol maps for Pikmin 2 reverse engineering.
- [pikmin-tools](https://github.com/RenolY2/pikmin-tools) - Collection of various tools for working with Pikmin 2 files.
- [noclip.website (Pikmin 2)](https://github.com/magcius/noclip.website/tree/main/src/j3d) - In-browser Pikmin 2 viewer.

#### Mario Kart: Double Dash

*See also [JSYSTEM](#jsystem-gamecubewii).*

- [MeltyTool (MarioKartDoubleDash)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/MarioKartDoubleDash) - Format viewer/exporter for Mario Kart Double Dash.
- [mkdd-collision](https://github.com/RenolY2/mkdd-collision) - Tool for viewing and editing collision data in Mario Kart Double Dash.
- [mkdd-track-editor](https://github.com/RenolY2/mkdd-track-editor) - Full-featured track editor for Mario Kart Double Dash.
- [DouBOL-Dash](https://github.com/shibbo/DouBOL-Dash) - BOL file format tool for editing race course layouts in Mario Kart Double Dash.
- [noclip.website (Mario Kart: Double Dash)](https://github.com/magcius/noclip.website/tree/main/src/j3d) - In-browser Mario Kart Double Dash viewer.

#### Super Mario 64

*See also [Fast3d/F3dex](#fast3df3dex-n64).*

- [Quad64](https://github.com/DavidSM64/Quad64) - Level editor for Super Mario 64.
- [MeltyTool (SuperMario64)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/SuperMario64) - Super Mario 64 format viewer/exporter.
- [SM64Paint](https://github.com/Trenavix/SM64Paint) - Texture editor for Super Mario 64.
- [Hack64 Super Mario 64](https://hack64.net/wiki/doku.php?id=super_mario_64) - Documentation for Super Mario 64 formats.

#### Super Mario 64 DS

- [SM64DSe](https://github.com/Arisotura/SM64DSe) - Level editor for Super Mario 64 DS.
- [SM64DSe-Ultimate](https://github.com/Gota7/SM64DSe-Ultimate) - Enhanced version of SM64DSe.
- [noclip.website (SM64DS)](https://github.com/magcius/noclip.website/tree/main/src/SuperMario64DS) - In-browser Super Mario 64 DS viewer.
- [MeltyTool (SuperMario64Ds)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/SuperMario64Ds) - Super Mario 64 DS format viewer/exporter.

#### Super Mario (Other)

*See also [JSYSTEM](#jsystem-gamecubewii) for Super Mario Sunshine and Galaxy.*

- [smstools](https://github.com/impiaaa/smstools) - Toolkit for decoding and working with Super Mario Sunshine data files.
- [Track-Studio](https://github.com/MapStudioProject/Track-Studio) - Full-featured track and course editor for Mario Kart 8.
- [CTR-Studio](https://github.com/MapStudioProject/CTR-Studio) - Editor for 3DS BCH/BCRES formats used in Mario Kart 7 and other 3DS games.
- [noclip.website (Super Mario Sunshine)](https://github.com/magcius/noclip.website/tree/main/src/j3d) - In-browser Super Mario Sunshine viewer.
- [noclip.website (Super Mario Galaxy)](https://github.com/magcius/noclip.website/tree/main/src/SuperMarioGalaxy) - In-browser Super Mario Galaxy viewer.
- [noclip.website (Super Mario Galaxy 2)](https://github.com/magcius/noclip.website/tree/main/src/SuperMarioGalaxy) - In-browser Super Mario Galaxy 2 viewer.
- [noclip.website (Mario Kart 64)](https://github.com/magcius/noclip.website/tree/main/src/MarioKart64) - In-browser Mario Kart 64 viewer.
- [noclip.website (Mario Kart DS)](https://github.com/magcius/noclip.website/tree/main/src/nns_g3d) - In-browser Mario Kart DS viewer.
- [noclip.website (Mario Kart Wii)](https://github.com/magcius/noclip.website/tree/main/src/MarioKartWii) - In-browser Mario Kart Wii viewer.
- [noclip.website (Mario Kart 8 Deluxe)](https://github.com/magcius/noclip.website/tree/main/src/MarioKart8Deluxe) - In-browser Mario Kart 8 Deluxe viewer.

#### Zelda

*See also [JSYSTEM](#jsystem-gamecubewii) for Wind Waker and Twilight Princess.*

- [WindEditor](https://github.com/Sage-of-Mirrors/WindEditor) - Map viewer/editor for The Legend of Zelda: The Wind Waker.
- [noclip.website (Ocarina of Time)](https://github.com/magcius/noclip.website/tree/main/src/zelview) - In-browser Ocarina of Time viewer.
- [noclip.website (Ocarina of Time Beta)](https://github.com/magcius/noclip.website/tree/main/src/zelview) - In-browser Ocarina of Time Beta viewer.
- [noclip.website (Majora's Mask 3D)](https://github.com/magcius/noclip.website/tree/main/src/OcarinaOfTime3D) - In-browser Majora's Mask 3D viewer.
- [noclip.website (Wind Waker)](https://github.com/magcius/noclip.website/tree/main/src/ZeldaWindWaker) - In-browser Wind Waker viewer.
- [noclip.website (Twilight Princess)](https://github.com/magcius/noclip.website/tree/main/src/ZeldaTwilightPrincess) - In-browser Twilight Princess viewer.
- [noclip.website (Skyward Sword)](https://github.com/magcius/noclip.website/tree/main/src/ZeldaSkywardSword) - In-browser Skyward Sword viewer.

#### Wii Sports

- [noclip.website (Wii Sports)](https://github.com/magcius/noclip.website/tree/main/src/WiiSports) - In-browser Wii Sports viewer.
- [noclip.website (Wii Sports Resort)](https://github.com/magcius/noclip.website/tree/main/src/WiiSports) - In-browser Wii Sports Resort viewer.

#### Star Fox Adventures

- [noclip.website (Star Fox Adventures)](https://github.com/magcius/noclip.website/tree/main/src/StarFoxAdventures) - In-browser Star Fox Adventures viewer.

#### Super Monkey Ball

- [noclip.website (Super Monkey Ball)](https://github.com/magcius/noclip.website/tree/main/src/SuperMonkeyBall) - In-browser Super Monkey Ball viewer.

#### New Super Mario Bros DS

- [noclip.website (New Super Mario Bros DS)](https://github.com/magcius/noclip.website/tree/main/src/nns_g3d) - In-browser New Super Mario Bros DS viewer.

#### Metroid Prime

- [noclip.website (Metroid Prime)](https://github.com/magcius/noclip.website/tree/main/src/MetroidPrime) - In-browser Metroid Prime viewer.
- [noclip.website (Metroid Prime 2)](https://github.com/magcius/noclip.website/tree/main/src/MetroidPrime) - In-browser Metroid Prime 2: Echoes viewer.
- [noclip.website (Metroid Prime 3)](https://github.com/magcius/noclip.website/tree/main/src/MetroidPrime) - In-browser Metroid Prime 3: Corruption viewer.
- [noclip.website (Metroid Prime Hunters)](https://github.com/magcius/noclip.website/tree/main/src/MetroidPrimeHunters) - In-browser Metroid Prime Hunters viewer.

#### Pokemon

- [noclip.website (Pokemon Snap)](https://github.com/magcius/noclip.website/tree/main/src/PokemonSnap) - In-browser Pokemon Snap viewer.
- [noclip.website (Pokemon Platinum)](https://github.com/magcius/noclip.website/tree/main/src/nns_g3d) - In-browser Pokemon Platinum viewer.
- [noclip.website (Pokemon HeartGold/SoulSilver)](https://github.com/magcius/noclip.website/tree/main/src/nns_g3d) - In-browser Pokemon HeartGold/SoulSilver viewer.
- [amnoid.de/gc](http://amnoid.de/gc/) - GameCube file format documentation and tools.
- [BMS-Analyzer](https://github.com/3e2j/BMS-Analyzer) - Nintendo Wii/Gamecube BMS to MIDI converter
- [CaveGenerator](https://github.com/Fizz14/CaveGenerator) - A tool to generate caves for Pikmin 2.
- [NintyFont](https://github.com/hadashisora/NintyFont) - Nintendo binary font editor
- [MarioKartToolbox](https://github.com/HaroohiePals/MarioKartToolbox) - New version of Mario Kart Toolbox, a fully fledged Mario Kart DS editor.
- [picori](https://github.com/Julgodis/picori) - Picori (ピッコル) is a library for decompilation, modding, and rom-hacking with focus on GameCube and Wii games.
- [MasterOcarina](https://github.com/mzxrules/MasterOcarina) - Collection of Zelda 64 programs
- [zelda-internal-file-extractor](https://github.com/politerust/zelda-internal-file-extractor) - A command-line utility that extracts the internal files of Zelda 64 ROMs.
- [Zelda64Loader](https://github.com/Random06457/Zelda64Loader) - Ghidra loader for Zelda 64 ROMs
- [zcamedit](https://github.com/sauraen/zcamedit) - Zelda 64 (OoT/MM) cutscene camera editor Blender plugin
- [OoT-Anim-Copy](https://github.com/skawo/OoT-Anim-Copy) - Copies a Zelda OoT animation between ZOBJ files
- [OoT-NPC-Maker](https://github.com/skawo/OoT-NPC-Maker) - An NPC creation tool for The Legend of Zelda: Ocarina of Time.
- [PyZelda64-Text-Editor](https://github.com/skawo/PyZelda64-Text-Editor) - Cross-platform Zelda 64 Text Editor
- [pycgfx](https://github.com/skyfloogle/pycgfx) - A program for converting glTF models into the Nintendo 3DS's CGFX format.
- [zev](https://github.com/wareya/zev) - ZEV, a ZElda 64 level Viewer
- [ozmav](https://github.com/xdanieldzd/ozmav) - Legacy N64 emulation and game modding tools (unmaintained).
- [SceneNavi](https://github.com/xdanieldzd/SceneNavi) - Level editor for The Legend of Zelda: Ocarina of Time (N64)
- [sharpocarina](https://github.com/xdanieldzd/sharpocarina) - Automatically exported from code.google.com/p/sharpocarina - UNMAINTAINED.
- [z64font](https://github.com/z64dev/z64font) - The first font editor for Zelda games on the Nintendo 64
- [z64viewer](https://github.com/z64dev/z64viewer) - HLE Zelda 64 model rendering in modern OpenGL
- [zzrtl](https://github.com/z64dev/zzrtl) - the lightweight Zelda 64 filesystem management utility
- [z64audio](https://github.com/z64tools/z64audio) - Somewhat flexible audio converter.
- [Z64Utils](https://github.com/zeldaret/Z64Utils) - Asset viewer for the Zelda64 Engine
- [NSMBHD Wiki (BCRES)](https://nsmbhd.net/wiki/BCRES/) - BCRES format documentation for 3DS games.
- [CloudModding Wiki (OoT Animation)](https://wiki.cloudmodding.com/oot/Animation_Format) - Animation format documentation for Ocarina of Time.

### Nintendo SDKs & Hardware

*Formats and tools generic to Nintendo consoles or SDKs.*

- [Nintendo-File-Formats](https://github.com/kinnay/Nintendo-File-Formats) - Documentation for Wii U and Switch file formats.
- [Nitro Files](https://wiki.vg-resource.com/Nitro_Files) - Documentation for Nintendo DS file formats.
- [narchive](https://github.com/nickworonekin/narchive) - Tool for extracting and creating NARC archives used in DS games.
- [apicula](https://github.com/scurest/apicula) - Converter for Nintendo DS .nsbmd 3D model format.
- [apicula/wiki/FILETYPES](https://github.com/scurest/apicula/wiki/FILETYPES) - Documentation for Nintendo DS file types.
- [nitro-fs](https://github.com/DanielPXL/nitro-fs) - Nintendo DS filesystem tools.
- [nitro-g3d-tools](https://github.com/Ermelber/nitro-g3d-tools) - Tools for Nintendo DS 3D graphics.
- [nitroefx](https://github.com/Fexty12573/nitroefx) - Nintendo DS effect tools.
- [NitroEffectMaker](https://github.com/HaroohiePals/NitroEffectMaker) - Effect editor for Nintendo DS.
- [narc](https://github.com/lhearachel/narc) - NARC archive tool for Nintendo DS.
- [NitroSDK](https://github.com/ntrtwl/NitroSDK) - Official Nintendo DS SDK.
- [NitroSystem](https://github.com/ntrtwl/NitroSystem) - Nintendo DS system library.
- [NTRGhidra](https://github.com/pedro-javierf/NTRGhidra) - Ghidra plugin for Nintendo DS.
- [NitroSharp](https://github.com/PlatinumMaster/NitroSharp) - Nintendo DS file format library.
- [nitrog3d](https://github.com/red031000/nitrog3d) - Nintendo DS 3D tools.
- [nitrogfx](https://github.com/red031000/nitrogfx) - Nintendo DS graphics tools.
- [Ekona](https://github.com/SceneGate/Ekona) - Nintendo DS file format library.
- [Nds4j](https://github.com/turtleisaac/Nds4j) - Java library for Nintendo DS formats.
- [Cafe-Shader-Studio](https://github.com/KillzXGaming/Cafe-Shader-Studio) - Shader editor and viewer for Wii U games.
- [REGames Editor](https://www.reddit.com/r/REGames/comments/12o004k/a_friend_and_i_made_a_full_editor_for_a_nintendo/) - Full-featured editor for Nintendo DS games.

### Ntreev Soft

- [PangLib](https://github.com/retreev/PangLib) - Series of tools to interact with Pangya PC MMO game files.
- [Pangya .iff formats](https://pixelde.su/blog/reverse-engineering-pangya-file-formats-2-iff/) - Blog post detailing the IFF file format used in Pangya.
- [Pangya .dat formats](https://desu.blog/reverse-engineering-pangya-file-formats-1-dat) - Blog post explaining the DAT file format used in Pangya.

### Panic

- [playdate-reverse-engineering](https://github.com/cranksters/playdate-reverse-engineering) - Reverse engineering notes and tools for Playdate handheld console.
- [noclip.website (A Short Hike)](https://github.com/magcius/noclip.website/tree/main/src/AShortHike) - In-browser A Short Hike viewer.

### PlatinumGames

#### Bayonetta

- [bayonetta_patch](https://github.com/Kerilk/bayonetta_patch) - Patching system for modifying Bayonetta executable.
- [noesis_bayonetta_pc](https://github.com/Kerilk/noesis_bayonetta_pc) - Noesis plugin for PlatinumGames models/animations (Bayonetta, Nier, MGR).
- [bayonetta_tools](https://github.com/Kerilk/bayonetta_tools) - Ruby toolkit for extracting/converting Bayonetta assets (models, textures, animations).

#### Nier: Automata / Replicant

- [kaine](https://github.com/neptuwunium/kaine) - C# library for working with Nier Replicant 1.22 file formats.
- [Blender2NieR](https://github.com/WoefulWolf/NieR2Blender2NieR) - Blender addon for exporting WMB/WTP/WTA/DAT/DTT formats to NieR games.
- [NieR2Blender](https://github.com/WoefulWolf/NieR2Blender_2_8) - Blender addon for importing NieR Automata and Replicant models.

### Polytron

- [noclip.website (Fez)](https://github.com/magcius/noclip.website/tree/main/src/Fez) - In-browser Fez viewer.

### Punchline

- [Murugo/Misc-Game-Research (Rule of Rose)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Rule%20of%20Rose) - Reverse engineering notes for Rule of Rose (PS2).

### Polyphony Digital

- [PDTools](https://github.com/Nenkai/PDTools) - Utilities for extracting and modifying Gran Turismo game files.

### RAD Game Tools

- [Knit](https://github.com/neptuwunium/Knit) - Managed C# library for reading Granny 2 3D model files used in many games.

### Rare

*Banjo-Kazooie, Donkey Kong, GoldenEye 007.*

- [noclip.website (Banjo-Kazooie)](https://github.com/magcius/noclip.website/tree/main/src/BanjoKazooie) - In-browser Banjo-Kazooie viewer.
- [noclip.website (Banjo-Tooie)](https://github.com/magcius/noclip.website/tree/main/src/BanjoTooie) - In-browser Banjo-Tooie viewer.
- [noclip.website (Diddy Kong Racing)](https://github.com/magcius/noclip.website/tree/main/src/DiddyKongRacing) - In-browser Diddy Kong Racing viewer.
- [noclip.website (Donkey Kong 64)](https://github.com/magcius/noclip.website/tree/main/src/DonkeyKong64) - In-browser Donkey Kong 64 viewer.
- [noclip.website (GoldenEye 007)](https://github.com/magcius/noclip.website/tree/main/src/GoldenEye007) - In-browser GoldenEye 007 viewer.
- [GoldEditor](https://github.com/carnivoroussociety/GoldEditor) - Setup editor for GoldenEye 007 game configurations.
- [DK64MapGenerator](https://github.com/GloriousLiar/DK64MapGenerator) - Tool for generating Donkey Kong 64 map and floor files from 3D meshes.
- [Banjo-Kazooie-Floor-Tool](https://github.com/oohnahleevay/Banjo-Kazooie-Floor-Tool) - Tool to modify floor collision properties in Banjo-Kazooie.
- [Banjo-s-Backpack](https://github.com/RareExports/Banjo-s-Backpack) - Level editor for Banjo-Kazooie (map and object editing).
- [Bottles_Glasses](https://github.com/RareExports/Bottles_Glasses) - Model and map renderer for Banjo-Kazooie and Banjo-Tooie.
- [DK64-Viewer](https://github.com/RareExports/DK64-Viewer) - Model and map viewer for Donkey Kong 64.
- [WumbasWigwam](https://github.com/RareExports/WumbasWigwam) - Level exporter for Banjo-Tooie (Blender import support).
- [dk64_lib](https://github.com/ThomasJRyan/dk64_lib) - Library for extracting data from Donkey Kong 64 ROMs.

### Radical Entertainment

- [scarface-p3d](https://github.com/aap/scarface-p3d) - P3D format tools for "Scarface: The World is Yours".

### Reflections Interactive

- [driver-tools](https://github.com/Fireboyd78/driver-tools) - Modding tools for DRIV3R, Driver: Parallel Lines, and Driver: San Francisco.
- [REDRIVER2](https://github.com/OpenDriver2/REDRIVER2) - Driver 2 Playstation game reverse engineering effort.

### Riot Games

- [yordle](https://github.com/neptuwunium/yordle) - File format research project for League of Legends.
- [MindCorpViewer](https://github.com/autergame/MindCorpViewer?tab=readme-ov-file) - Model viewer for League of Legends SKN/SKL/DDS files [archived].
- [MindCorpViewer-Rust](https://github.com/autergame/MindCorpViewer-Rust) - Modern Rust rewrite of League of Legends model viewer with improved performance.

### Santa Monica Studio

- [god_of_war_browser](https://github.com/mogaika/god_of_war_browser) - WebGL-based in-browser viewer for God of War I/II (PS2/PS3/Vita) models and textures.
- [God of War 2018 PS4 Tools](https://forum.xentax.com/viewtopic.php?f=16&t=22897) - XeNTaX forum discussion and extraction tools for God of War (2018) on PlayStation 4. *(Link archived/dead)*

### Sega

- [Aqua-Toolset](https://github.com/Shadowth117/Aqua-Toolset) - Toolkit primarily for Phantasy Star Online 2 file formats.
- [PCSX2 Patches](https://github.com/PCSX2/pcsx2_patches) - Game patches for PCSX2 emulator including widescreen and interlacing fixes.
- [noclip.website (Jet Set Radio)](https://github.com/magcius/noclip.website/tree/main/src/JetSetRadio) - In-browser Jet Set Radio viewer.

### Sonic Team

#### Sonic Adventure

- [SCHG:Sonic_Adventure](https://info.sonicretro.org/SCHG:Sonic_Adventure) - Sonic Community Hacking Guide documentation for Sonic Adventure.
- [sadtools](https://github.com/FraGag/sadtools) - Command-line tools for Sonic Adventure file formats.
- [sa_tools](https://github.com/X-Hax/sa_tools) - Modding toolkit for Sonic Adventure games.

#### Sonic Heroes / Shadow

- [HeroesPowerPlant](https://github.com/igorseabra4/HeroesPowerPlant/wiki/Level-Editor) - Full-featured level editor for Sonic Heroes and Shadow the Hedgehog.

#### Other Sonic Games

- [HedgeLib](https://github.com/Radfordhound/HedgeLib) - C++ library and collection of tools that aims to make modding games in the Sonic the Hedgehog franchise easier.
- [Marathon](https://github.com/hyperbx/Marathon) - Toolkit and library for Sonic The Hedgehog file formats.
- [Sonic-1-2-2013-Decompilation](https://github.com/RSDKModding/RSDKv4-Decompilation) - Complete decompilation of Sonic 1 & Sonic 2 (2013) & Retro Engine (v4).
- [UnleashedRecomp](https://github.com/hedge-dev/UnleashedRecomp) - Unofficial PC port of the Xbox 360 version of Sonic Unleashed created through static recompilation.
- [noclip.website (Sonic Colors)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Sonic Colors viewer.
- [Sonic Retro (SA2 Hacking Guide)](https://info.sonicretro.org/SCHG:Sonic_Adventure_2) - Sonic Hacking Guide for Sonic Adventure 2.

### Sony (First Party)

- [LibreFios](https://github.com/neptuwunium/LibreFios) - C# library for working with PlayStation PSARC archive format.

### Square Enix

- [WOFFington](https://github.com/neptuwunium/WOFFington) - File format research and tools for World of Final Fantasy.
- [heretic](https://github.com/adamrt/heretic) - Modding toolkit for Final Fantasy Tactics.
- [KH-ReCOM-Tools](https://github.com/Murugo/KH-ReCOM-Tools) - Set of experimental tools for Kingdom Hearts Re:Chain of Memories (PS2).
- [Murugo/Misc-Game-Research (Kingdom Hearts II)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Kingdom%20Hearts%20II%20Final%20Mix) - Reverse engineering notes for Kingdom Hearts II Final Mix (PS2).
- [Murugo/Misc-Game-Research (Musashi: Samurai Legend)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Musashi%20Samurai%20Legend) - Reverse engineering notes for Musashi: Samurai Legend (PS2).
- [kh1](https://github.com/ethteck/kh1) - WIP Decompilation of Kingdom Hearts (PS2, JP).
- [noclip.website (Final Fantasy X)](https://github.com/magcius/noclip.website/tree/main/src/FinalFantasyX) - In-browser Final Fantasy X viewer.
- [noclip.website (Kingdom Hearts)](https://github.com/magcius/noclip.website/tree/main/src/KingdomHearts) - In-browser Kingdom Hearts viewer.
- [noclip.website (Kingdom Hearts II Final Mix)](https://github.com/magcius/noclip.website/tree/main/src/KingdomHearts2FinalMix) - In-browser Kingdom Hearts II Final Mix viewer.
- [noclip.website (Dragon Quest VIII)](https://github.com/magcius/noclip.website/tree/main/src/DragonQuest8) - In-browser Dragon Quest VIII viewer.
- [kh2mdlx](https://github.com/GovanifY/kh2mdlx) - Tool for importing and exporting Kingdom Hearts 2 3D models.
- [kh2vif](https://github.com/GovanifY/kh2vif) - Model importer for Kingdom Hearts 2 (OBJ to VIF format converter).
- [KH2-Anm-Generator](https://github.com/Kite2810/KH2-Anm-Generator) - Automated animation cutscene generator for Kingdom Hearts 2 custom character models.
- [Hypercrown](https://github.com/Some1fromthedark/Hypercrown) - Model converter for Kingdom Hearts 1 (converts models to common formats and back).

### Sucker Punch

#### Sly Cooper

- [SlyTools](https://github.com/VelocityRa/SlyTools) - Sly Cooper (PS2/PS3 games) modding tools & research
- [Sly2ModelRE](https://github.com/froggestspirit/Sly2ModelRE) - Researching the model format in Sly 2: Band of Thieves.
- [sly_dec.py](https://github.com/yukinogatari/Reverse-Engineering/blob/573fc1c20796fb40a982f11dfda4039eb480a34e/Sly%20Cooper/sly_dec.py) - Python script for decrypting Sly Cooper files.
- [PS23DFormat (Sly 2)](https://web.archive.org/web/20160205080914/http://ps23dformat.wikispaces.com/Sly+2+Band+of+Thieves) - Archived documentation for Sly 2 3D format.
- [PS23DFormat Wiki Archive](https://archive.org/details/wiki-ps23dformat.wikispaces.com) - Complete archive of PS23DFormat wiki covering PS2 3D formats.
- [SlyCineTrainer](https://github.com/slynders/SlyCineTrainer) - Trainer for creating camera animations in Sly Cooper games.

### Thekla Inc

- [noclip.website (The Witness)](https://github.com/magcius/noclip.website/tree/main/src/TheWitness) - In-browser The Witness viewer.

### Visceral Games

- [Gibbed.Visceral](https://github.com/gibbed/Gibbed.Visceral) - File format tools for Dante's Inferno and Dead Space 2.
- [Noesis-Plugins (Durik256)](https://github.com/Durik256/Noesis-Plugins) - Community Noesis plugins collection including Visceral Games support.
- [MeltyTool (Visceral)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/VisceralGames) - Format viewer/exporter for Visceral Games titles.
- [ZenHAX Thread](https://zenhax.com/viewtopic.php?t=15376) - Forum discussion and research on Visceral Games file formats. *(Link archived/dead)*
- [VisceralToolkit](https://github.com/Greavesy1899/VisceralToolkit) - Toolkit for editing games by EA Redwood Shores/Visceral Games (The Godfather, Dead Space, Dante's Inferno).

### Wargaming

- [yretenai/Akizuki](https://github.com/neptuwunium/Akizuki/tree/csharp) - File format research project for World of Warships.

### Ubisoft

- [Jormungandr](https://github.com/neptuwunium/Jormungandr) - File format research and tools for Ubisoft's Anvil Engine (Assassin's Creed series).
- [Ubitunedec](https://github.com/ldeon/Ubitunedec) - Program for decoding and exporting SPK audio files found in Ubisoft game .dat files.

#### Anno 1800

- [Anno 1800 Mod Loader](https://github.com/magicalcookie/anno1800-mod-loader) - Mod loader for Anno 1800 that supports loading of unpacked RDA files, XML auto merging and DLL based mods.
- [Modding Tools for Anno](https://marketplace.visualstudio.com/items?itemName=JakobHarder.anno-modding-tools) - Visual Studio Code extension with utilities to build Anno 1800 mods.

### Angel Matrix

- [noclip.website (Neon White)](https://github.com/magcius/noclip.website/tree/main/src/NeonWhite) - In-browser Neon White viewer.

### Bethesda

*The Elder Scrolls, Fallout series, and Starfield.*

- [xEdit](https://tes5edit.github.io) - Advanced graphical module editor and conflict detector for Bethesda games.
- [Wrye Bash](https://wrye-bash.github.io) - Swiss army knife for modding Bethesda games with features including mod installation, conflict manager, load order manager and automatic merging.
- [Synthesis](https://github.com/Mutagen-Modding/Synthesis) - Framework and GUI to empower people to create mods via code instead of by hand, mainly used to create patches.
- [Spriggit](https://github.com/Mutagen-Modding/Spriggit) - Tool to facilitate converting Bethesda plugin files to a text based format that can be stored in Git.
- [ck-cmd](https://github.com/aerisarn/ck-cmd) - Command-line helper for executing some Creation Kit/Engine commands.
- [hkxc](https://www.nexusmods.com/skyrimspecialedition/mods/126214) - CLI tool to convert between x86/x64 HKX and XML animation files.
- [HKX Conversion Tool](https://www.nexusmods.com/skyrimspecialedition/mods/128839) - hkxc Windows GUI for converting between HKX and XML animations files.
- [hkxPoser](https://www.nexusmods.com/skyrimspecialedition/mods/11783) - .hkx animation file editor.
- [DDS Texture Converter](https://www.nexusmods.com/skyrimspecialedition/mods/111378) - Application for bulk conversion and resizing of DDS textures.
- [DDS Texture Scanner](https://github.com/niston/TextureScan) - Application scanning for DDS textures with abnormal dimensions.
- [noclip.website (Morrowind)](https://github.com/magcius/noclip.website/tree/main/src/Morrowind) - In-browser Morrowind viewer.

### Blizzard Entertainment

- [OWLib](https://github.com/overtools/OWLib) - Toolkit for extracting and working with Overwatch game files.
- [noclip.website (World of Warcraft - Vanilla, The Burning Crusade, Wrath of the Lich King)](https://github.com/magcius/noclip.website/tree/main/src/WorldOfWarcraft) - In-browser World of Warcraft (Vanilla) viewer.

## 🔗 Related Lists

- [Awesome Modding](https://github.com/loicreynier/awesome-modding) - Resources for game modding and customization.
- [Awesome Game File Formats](https://github.com/MeltyPlayer/awesome-game-file-formats) - The inspiration for this list - another excellent such collection.
- [Awesome Game Datasets](https://github.com/leomaurodesenv/game-datasets) - Datasets and resources for game research.
- [Awesome Reverse Engineering](https://github.com/tylerha97/awesome-reversing) - List of reverse engineering resources.
- [Awesome Software Reverse Engineering](https://github.com/ReversingID/Awesome-Reversing/blob/master/_software.md) - Comprehensive list of reverse engineering software and tools.
- [Awesome Gamedev](https://github.com/ellisonleao/magictools) - Curated list of game development resources.

## 📄 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.

## 🙏 Acknowledgments

Shoutout to [MeltyPlayer/awesome-game-file-formats](https://github.com/MeltyPlayer/awesome-game-file-formats) - this started as a fork of it with my own bookmark collection, but I eventually decided to add more sections and reorganize it.
