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
    - [📂 Script Collections \& Multi-Game Tools](#-script-collections--multi-game-tools)
  - [⚙️ Engines](#️-engines)
    - [GameMaker](#gamemaker)
    - [Source (Valve)](#source-valve)
    - [Unity](#unity)
    - [Unreal Engine](#unreal-engine)
    - [CryEngine](#cryengine)
    - [Hedgehog Engine](#hedgehog-engine)
    - [Northlight Engine](#northlight-engine)
    - [Build Engine](#build-engine)
    - [Raven Software](#raven-software)
      - [Heretic II](#heretic-ii)
      - [Soldier of Fortune](#soldier-of-fortune)
  - [🔧 Middleware \& SDKs](#-middleware--sdks)
    - [Fast3d/F3dex (N64)](#fast3df3dex-n64)
    - [Havok](#havok)
    - [JSYSTEM (GameCube/Wii)](#jsystem-gamecubewii)
    - [MikuMikuDance](#mikumikudance)
    - [RenderWare](#renderware)
    - [Sappy (GBA Audio)](#sappy-gba-audio)
  - [Formats by Studio / Game](#formats-by-studio--game)
    - [Activision / Infinity Ward / Treyarch](#activision--infinity-ward--treyarch)
      - [Call of Duty](#call-of-duty)
      - [Tony Hawk's Pro Skater](#tony-hawks-pro-skater)
    - [Angel Matrix](#angel-matrix)
    - [Angel Studios / Rockstar San Diego](#angel-studios--rockstar-san-diego)
    - [Ape, Inc](#ape-inc)
    - [11 bit studios](#11-bit-studios)
    - [Remedy Entertainment](#remedy-entertainment)
      - [Max Payne](#max-payne)
    - [Argonaut Games](#argonaut-games)
    - [Arkane Studios](#arkane-studios)
    - [Atlus](#atlus)
    - [Asobo Studio](#asobo-studio)
    - [Black Element Software](#black-element-software)
    - [Bandai Namco](#bandai-namco)
    - [EA DICE](#ea-dice)
      - [Battlefield Series](#battlefield-series)
      - [Star Wars: Battlefront](#star-wars-battlefront)
    - [Capcom](#capcom)
      - [Resident Evil](#resident-evil)
      - [Monster Hunter](#monster-hunter)
      - [Devil May Cry](#devil-may-cry)
      - [Gregory Horror Show](#gregory-horror-show)
    - [CCR](#ccr)
    - [CCP Games](#ccp-games)
    - [CD Projekt Red](#cd-projekt-red)
      - [The Witcher 3 / REDEngine 3](#the-witcher-3--redengine-3)
      - [The Witcher](#the-witcher)
      - [Cyberpunk 2077 / REDEngine 4](#cyberpunk-2077--redengine-4)
    - [Clover Studio](#clover-studio)
    - [Cygames](#cygames)
    - [Disney Interactive](#disney-interactive)
      - [Toontown Online](#toontown-online)
    - [Double Fine](#double-fine)
    - [8monkey Labs](#8monkey-labs)
    - [Crystal Dynamics / Eidos Interactive](#crystal-dynamics--eidos-interactive)
    - [Ion Storm](#ion-storm)
      - [Anachronox](#anachronox)
      - [Deus Ex](#deus-ex)
    - [Massive Entertainment](#massive-entertainment)
      - [AquaNox](#aquanox)
      - [World in Conflict](#world-in-conflict)
    - [Surreal Software](#surreal-software)
    - [Dynamix / Sierra](#dynamix--sierra)
      - [Tribes Series](#tribes-series)
    - [EA Black Box](#ea-black-box)
      - [Need for Speed Series](#need-for-speed-series)
    - [FromSoftware](#fromsoftware)
    - [Gearbox Software](#gearbox-software)
      - [MechWarrior 4](#mechwarrior-4)
    - [Game Freak](#game-freak)
      - [Gen I \& II](#gen-i--ii)
      - [Gen III](#gen-iii)
    - [Genius Sonority](#genius-sonority)
    - [Genki](#genki)
    - [Grezzo](#grezzo)
    - [Human Head Studios](#human-head-studios)
    - [Grezzo](#grezzo-1)
    - [id Software](#id-software)
    - [Grezzo](#grezzo-2)
    - [Guerrilla Games](#guerrilla-games)
    - [LucasArts](#lucasarts)
    - [Gust (Koei Tecmo)](#gust-koei-tecmo)
    - [Harmonix](#harmonix)
    - [HAL Laboratory](#hal-laboratory)
    - [Heavy Iron Studios](#heavy-iron-studios)
    - [Hudson Soft](#hudson-soft)
    - [Insomniac Games](#insomniac-games)
    - [Intelligent Systems](#intelligent-systems)
      - [Paper Mario 64](#paper-mario-64)
      - [Paper Mario: TTYD / Super Paper Mario](#paper-mario-ttyd--super-paper-mario)
    - [Interactive Studios](#interactive-studios)
      - [Glover](#glover)
    - [Illusion](#illusion)
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
    - [Metropolis Software](#metropolis-software)
      - [Gorky 17](#gorky-17)
    - [Microsoft Studios / Bungie / Turn 10](#microsoft-studios--bungie--turn-10)
      - [Halo](#halo)
      - [Gears of War](#gears-of-war)
      - [Forza](#forza)
      - [Age of Empires](#age-of-empires)
    - [Mobius Digital](#mobius-digital)
    - [Midway](#midway)
      - [Gauntlet](#gauntlet)
      - [NFL Blitz](#nfl-blitz)
    - [Monolith Productions](#monolith-productions)
      - [F.E.A.R.](#fear)
      - [Trespasser](#trespasser)
      - [Blood](#blood)
      - [Blood 2: The Chosen](#blood-2-the-chosen)
      - [No One Lives Forever](#no-one-lives-forever)
      - [Shogo: Mobile Armor Division](#shogo-mobile-armor-division)
    - [Oddworld Inhabitants](#oddworld-inhabitants)
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
      - [New Super Mario Bros Wii](#new-super-mario-bros-wii)
      - [Zelda](#zelda)
      - [Wii Sports](#wii-sports)
      - [Star Fox Adventures](#star-fox-adventures)
      - [Super Monkey Ball](#super-monkey-ball)
      - [New Super Mario Bros DS](#new-super-mario-bros-ds)
      - [Metroid Prime](#metroid-prime)
      - [Pokemon](#pokemon)
    - [Nintendo SDKs \& Hardware](#nintendo-sdks--hardware)
    - [Ntreev Soft](#ntreev-soft)
    - [BioWare](#bioware)
      - [Dragon Age: Origins](#dragon-age-origins)
      - [Knights of the Old Republic](#knights-of-the-old-republic)
    - [Obsidian Entertainment](#obsidian-entertainment)
      - [Neverwinter Nights 2](#neverwinter-nights-2)
    - [Panic](#panic)
    - [Petroglyph Games](#petroglyph-games)
    - [PlatinumGames](#platinumgames)
      - [Bayonetta](#bayonetta)
      - [Nier: Automata / Replicant](#nier-automata--replicant)
    - [Primal Software](#primal-software)
      - [The I of the Dragon](#the-i-of-the-dragon)
    - [Polytron](#polytron)
    - [Mithis Entertainment](#mithis-entertainment)
      - [Nexus: The Jupiter Incident](#nexus-the-jupiter-incident)
    - [Punchline](#punchline)
    - [People Can Fly](#people-can-fly)
      - [Painkiller](#painkiller)
    - [Polyphony Digital](#polyphony-digital)
    - [RAD Game Tools](#rad-game-tools)
    - [Rebel Act](#rebel-act)
    - [Rebellion Developments](#rebellion-developments)
      - [Aliens vs. Predator 2](#aliens-vs-predator-2)
      - [Aliens vs. Predator (2010)](#aliens-vs-predator-2010)
    - [Rare](#rare)
    - [Runic Games](#runic-games)
      - [Torchlight](#torchlight)
      - [Torchlight II](#torchlight-ii)
    - [1C Company / Best Way](#1c-company--best-way)
      - [Men of War](#men-of-war)
    - [Ironclad Games / Stardock](#ironclad-games--stardock)
      - [Sins of a Solar Empire](#sins-of-a-solar-empire)
    - [Radical Entertainment](#radical-entertainment)
    - [Reflections Interactive](#reflections-interactive)
    - [Riot Games](#riot-games)
    - [Santa Monica Studio](#santa-monica-studio)
    - [Sega](#sega)
      - [Creative Assembly](#creative-assembly)
        - [Alien: Isolation](#alien-isolation)
        - [Total War Series](#total-war-series)
    - [Sonic Team](#sonic-team)
      - [Sonic Adventure](#sonic-adventure)
      - [Sonic Heroes / Shadow](#sonic-heroes--shadow)
      - [Other Sonic Games](#other-sonic-games)
    - [Sony (First Party)](#sony-first-party)
    - [Square Enix](#square-enix)
      - [Hitman](#hitman)
    - [Sucker Punch](#sucker-punch)
      - [Sly Cooper](#sly-cooper)
    - [Supercell](#supercell)
    - [SuperTuxKart](#supertuxkart)
    - [Telltale Games](#telltale-games)
    - [GSC Game World](#gsc-game-world)
      - [S.T.A.L.K.E.R.](#stalker)
    - [Terminal Reality](#terminal-reality)
      - [BloodRayne](#bloodrayne)
    - [THQ / Rainbow Studios](#thq--rainbow-studios)
      - [Cars](#cars)
      - [MX vs ATV](#mx-vs-atv)
    - [3D Realms](#3d-realms)
      - [Duke Nukem 3D](#duke-nukem-3d)
      - [Duke Nukem: Manhattan Project](#duke-nukem-manhattan-project)
      - [Duke Nukem Forever (2001)](#duke-nukem-forever-2001)
      - [The Outforce](#the-outforce)
    - [Techland](#techland)
    - [Thekla Inc](#thekla-inc)
    - [Slitherine / Proxy Studios](#slitherine--proxy-studios)
    - [Visceral Games](#visceral-games)
    - [Wargaming](#wargaming)
    - [Ubisoft](#ubisoft)
      - [Anno 1800](#anno-1800)
    - [Bethesda](#bethesda)
    - [2K Games / Firaxis Games](#2k-games--firaxis-games)
    - [Bohemia Interactive](#bohemia-interactive)
    - [Blizzard Entertainment](#blizzard-entertainment)
    - [Westwood Studios / EA Los Angeles](#westwood-studios--ea-los-angeles)
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

### Game-Specific Wikis

- [The Cutting Room Floor](https://tcrf.net/Help:Contents/Finding_Content) - Community for discovering and documenting unused and debug game content.
- [Nintendo File Formats](https://nintendo-formats.com/) - Documentation for Wii U and Switch games.
- [Custom Mario Kart Wiiki](https://wiki.tockdom.com/wiki/List_of_File_Formats) - Formats used in Mario Kart Wii and related games.
- [Mario Kart 8 Wiki](https://mk8.tockdom.com/wiki/Main_Page) - Documentation for Mario Kart 8 formats and modding.
- [Luma's Workshop](https://www.lumasworkshop.com/wiki/Category:File_formats) - Nintendo modding wiki.
- [Splatoon Technical Wiki](https://wiki.oatmealdome.me/index.php/Special:AllPages) - Technical documentation for Splatoon game formats.
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
  - [Noesis Plugins (HimeWorks)](https://himeworks.com/noesis-plugins/) - Community plugin collection for 100+ games, primarily MMORPGs and action games.
    Games include Tales series, Midnight Club 2, Dragon Nest, Dark Souls, League of Legends, C9, Cabal Online, Monster Hunter 3, Hyperdimension Neptunia, Ys series, and many more.
  - [Noesis Plugins (Durik256)](https://github.com/Durik256/Noesis-Plugins) - Community collection with 150+ plugins for various games including Final Fantasy series, Dark Souls 2, Dead Rising 4, Ridge Racer, NHL 21, and many others.
  - [Noesis Plugins (mrpostiga)](https://github.com/mrpostiga/noesis-plugins-official) - Additional community-maintained plugin collection.
  - [Noesis Plugins (RoadTrain)](https://github.com/RoadTrain/noesis-plugins) - LS3D engine plugin (.4ds format) supporting Mafia: The City of Lost Heaven, Chameleon, Hidden & Dangerous 2, War of Wings.
  - [Noesis Plugins (Zheneq)](https://github.com/Zheneq/Noesis-Plugins) - Community plugins for Megaman X8 (PC), Fatal Frame 4 (Wii), Star Wars: The Force Unleashed (Wii), Planet 51 (Wii), Silent Hill: Shattered Memories (Wii), Fire Emblem (Wii), MT Framework (3DS).
  - [noesis_dukemdx](https://github.com/DaZombieKiller/noesis_dukemdx) - Noesis plugin for Duke Nukem Extended Model (MDX) format.
  - [noesis_iqe](https://github.com/viciious/noesis_iqe) - Noesis plugin for exporting models to Inter-Quake Export (IQE) format.
- [TexViewer](https://github.com/Puxtril/TexViewer) - Tool to help discover unknown texture formats.
- [ImageHeat](https://github.com/bartlomiejduda/ImageHeat) - Texture viewing tool for encoded textures. Supports RGBA8888, RGB888, RGB565, DXT1, ASTC, indexed formats (PAL4/8/16), platform-specific unswizzling (PSP, PS2, PS3, PS4, Xbox), and decompression (RLE, PackBits, ZLIB). Exports as DDS, PNG, or BMP.
- [binviz](https://github.com/VelocityRa/binviz) - Binary visualization tool for identifying patterns and structure in unknown files. Creates visual representations showing potential compression/encryption, structured data and padding at a glance. Helpful for spotting where assets begin/end in unstructured archives.
- [DDS.Tools](https://github.com/BoBoBaSs84/DDS.Tools) - Command line bulk PNG to DDS (and vice versa) conversion tool with duplicate detection.
- [Sprite Sheet Addon for Blender](https://www.moddb.com/engines/blender-game-engine/downloads/sprite-sheet-addon-for-blender) - Blender addon for working with sprite sheets.
- [Sprite Sheet Addon for Blender VSE](https://www.moddb.com/groups/blender-game-engine/downloads/sprite-sheet-addon-for-blender-vse) - Blender VSE (Video Sequence Editor) addon for working with sprite sheets.
- [BodySlide and Outfit Studio](https://github.com/ousnius/BodySlide-and-Outfit-Studio) - Tool to convert, create, and customize outfits and bodies for The Elder Scrolls and Fallout games.
- [Cathedral Assets Optimizer](https://www.nexusmods.com/skyrimspecialedition/mods/23316) - Tool to automatically optimize BSAs, meshes, textures and animations for Bethesda games.
- [blender_magicavoxel](https://github.com/AstrorEnales/blender_magicavoxel) - MagicaVoxel `.vox` importer for Blender with hierarchy/greedy meshing, voxel hull reduction, and UV-aware material modes.
  - Options: multiple meshing modes (voxel-as-model, simple cubes/quads, greedy), UV unwrapping, vertex colors, texture baking, and voxel hull pruning.
  - Material modes: ignore, vertex colors, per-color materials, palette textures, and UV-unwrapped textured models.
- [Blender MD3 Import-Export Tool](https://www.moddb.com/games/quake-iii-arena/downloads/blender-md3-import-export-tool) - Blender script for importing and exporting MD3 model format used in Quake III Arena and other id Tech 3 games. Supports animation frame export and shader path configuration.
- [Blender - MD3 Import and Export](https://www.moddb.com/groups/blender-artist/downloads/blender-md3-import-and-export-download) - Blender addon for importing and exporting MD3 model format.
- [3DS MAX 5 and 3DS MAX 6 converter](https://www.moddb.com/engines/3dstate/downloads/3ds-max-5-and-3ds-max-6-converter) - Converter tool for 3DS Max 5 and 6 file formats (3DSTATE engine).
- [Vampire the Masquerade Bloodlines Blender 2.42 plugin](https://www.moddb.com/games/vampire-the-masquerade-bloodlines/downloads/vampire-the-masquerade-bloodlines-blender-242-plugin) - Blender 2.42 plugin for Vampire: The Masquerade - Bloodlines.
- [NOD Noesis Plugin (Vampire: The Masquerade – Redemption)](https://www.moddb.com/games/vampire-the-masquerade-redemption/downloads/nod-noesis-plugin) - Noesis plugin for NOD model format used in Vampire: The Masquerade – Redemption.
- [Blender samples (Vampire: The Masquerade – Redemption)](https://www.moddb.com/games/vampire-the-masquerade-redemption/downloads/blender-samples) - Blender sample files for Vampire: The Masquerade – Redemption.
- [Dreamkiller Mapping Tools for 3ds Max](https://www.moddb.com/games/dreamkiller/downloads/dreamkiller-mapping-tools) - Mapping tools for Dreamkiller in 3DS Max.

### 📦 Archive & Asset Extraction

- [QuickBMS](https://aluigi.altervista.org/quickbms.htm) - Universal archive extractor and reimporter with extensive script database covering thousands of games. Uses BMS scripting language to describe archive formats.
- [AssetRipper](https://github.com/AssetRipper) - Tool for extracting assets from Unity and other engines.
- [Switch Toolbox](https://github.com/KillzXGaming/Switch-Toolbox) - Multi-format editor for Nintendo Switch, Wii U, and 3DS games. Supports Mario Kart 8 Deluxe, Sonic Forces, Team Sonic Racing, Zelda (OoT 3D, MM 3D, Twilight Princess HD, Hyrule Warriors), Luigi's Mansion (3DS, Dark Moon), Crash Bandicoot N. Sane Trilogy, Crash Team Racing, and many more.
- [BAE](https://www.nexusmods.com/starfield/mods/165) - Bethesda Archive Extractor application for BSA/BA2 archives.
- [BSA Browser](https://github.com/AlexxEG/BSA_Browser) - Bethesda Archive (BSA and BA2) browser & extractor application.
- [LSLib](https://github.com/Norbyte/lslib) - Tools for manipulating Divinity Original Sin and Baldur's Gate 3 files including archive extraction.

### 🔊 Audio Tools

- [vgmstream](https://github.com/vgmstream/vgmstream) - Audio playback library supporting 1000+ game audio formats including looping, multi-channel streams, and console-specific codecs. Works as a standalone player or Winamp/foobar2000 plugin. If a game audio file exists, vgmstream probably plays it.
- [VGAudio](https://github.com/Thealexbarney/VGAudio) - .NET library for encoding, decoding, and manipulating audio files from video games. Supports many Nintendo formats (BRSTM, BCSTM, BFSTM, IDSP, HPS, DSP, etc.).
- [vgm_ripping](https://github.com/hcs64/vgm_ripping) - Sources for game music ripping tools.
- [wwiseutil](https://github.com/hpxro7/wwiseutil) - Tool for manipulating Wwise SoundBank (.bnk, .nbnk) and File Package (.pck, .npck) files. Supports unpacking WEM audio files, replacing audio with automatic metadata updates, and editing loop points. Works with any game using Wwise audio middleware.
- [soundbank-editor](https://github.com/t1f7/soundbank-editor) - Python-based editor for Wwise soundbank files (.bnk). List, extract, and replace WEM sounds while preserving headers, events, and metadata. Works with any game using Wwise audio middleware.
- [Wwise-Unpacker](https://github.com/Vextil/Wwise-Unpacker) - Windows tool for extracting audio from Wwise PCK and BNK containers to OGG or MP3 format. Works with any game using Wwise audio middleware.
- [Wwise-BNKExtract](https://github.com/rickvg/Wwise-BNKExtract) - Extraction utility for Wwise soundbank files (BNK format, file version 113 and earlier). Extracts WEM audio files for conversion to OGG Vorbis format.
- [ww2ogg](https://github.com/hcs64/ww2ogg) - Converts Wwise RIFF/RIFX Vorbis audio (.wem files) to standard Ogg Vorbis format. Command-line tool with packed codebook support for various encoding variants. Note: vgmstream is recommended for playback, but ww2ogg is useful when Ogg Vorbis output is specifically required.

### 🌐 Translation & Localization

- [Kuriimu](https://github.com/IcySon55/Kuriimu) - General purpose game translation toolkit.
- [Kuriimu2](https://github.com/FanTranslatorsInternational/Kuriimu2) - Next-gen version of Kuriimu.

### 🔍 Binary Analysis & Hex Editors

- [010 Editor](https://www.sweetscape.com/010editor/) - Professional hex editor with powerful template system for analyzing binary file structures (paid).
- [ImHex](https://github.com/WerWolv/ImHex) - Modern, open-source hex editor with pattern language for reverse engineering file formats (free).
- [Kaitai Struct](https://kaitai.io/) - Declarative language for describing binary data structures with code generation for multiple programming languages.
- [Veles](https://codisec.com/veles/) - Binary analysis and visualization tool for reverse engineering (open-source).
- [010 Templates / ImHex Patterns](https://github.com/neptuwunium/bt) - Templates for binary analysis.
- [010GameTemplates](https://github.com/Nenkai/010GameTemplates) - Collection of 010 Editor templates for various games including Gran Turismo, Forza, Project Cars, Ridge Racer 7, Tales of Vesperia, Xenoblade Chronicles, Granblue Fantasy: Relink, Driveclub, WWE 2K, and many others.
- [JSC-PyDecrypt-Tool](https://github.com/bartlomiejduda/JSC-PyDecrypt-Tool) - Decrypts JSC (JavaScript Compiled) files from Cocos2d games. Requires valid encryption key extracted via Frida from running game instances.

### 💻 Libraries & Development Tools

- [ReverseBox](https://github.com/bartlomiejduda/ReverseBox) - Python library for reverse engineering with utilities for checksums (Adler32, CRC variants, Fletcher, XOR), compression (BZIP2, LZ4, LZMA, MIO0, PackBits, RLE variants), encryption (ROT13, XOR cipher), hashing (FNV, DJB2, MD5, SHA, Murmur3), and image processing (100+ pixel formats including DXT, PVRTC, ETC, ASTC, BC formats, swizzling for multiple platforms).
- [DragonLib](https://github.com/neptuwunium/DragonLib) - Common library for file format research.
- [GL Editor Framework](https://github.com/jupahe64/GL_EditorFramework) - OpenGL-based framework for creating 3D game editors.
- [SFGraphics](https://github.com/ScanMountGoat/SFGraphics) - OpenGL graphics library for rendering game formats, used in various format viewers.
- [ooz](https://github.com/powzix/ooz) - Open-source decompressor for Oodle compression formats (Kraken, Mermaid, Selkie, Leviathan, LZNA, Bitknit) used in many modern games including Warframe and other titles using RAD Game Tools compression.
- [Syroot.BinaryData](https://gitlab.com/Syroot/BinaryData) - .NET library for easy binary data reading/writing with support for various endianness and encodings.
- [XeNTaXTools-Legacy](https://github.com/XeNTaXTools/XeNTaXTools-Legacy) - Legacy tools scraped from the XeNTaX forums.

### Decompilation Tools

- [decomp-toolkit](https://github.com/encounter/decomp-toolkit) - GameCube & Wii decompilation toolkit.
- [splat](https://github.com/ethteck/splat) - Binary splitting tool to assist with decompilation and modding projects.
- [objdiff](https://github.com/encounter/objdiff) - Local diffing tool for decompilation projects.
- [decomp-permuter](https://github.com/simonlindholm/decomp-permuter) - Randomly permute C files to better match a target binary.
- [m2c](https://github.com/matt-kempster/m2c) - MIPS and PowerPC decompiler.
- [vutrace](https://github.com/chaoticgd/vutrace) - PS2 VU tracing debugger.

### 📂 Script Collections & Multi-Game Tools

- [noclip.website](https://github.com/magcius/noclip.website) - In-browser 3D viewer for 60+ games across multiple platforms and studios.
  - Games: Source Engine games (17 titles including Half-Life 2, Portal 1 & 2, Team Fortress 2, CS:GO, L4D2),
    Nintendo games (Mario 64, Mario Kart series, Zelda series, Pikmin, Luigi's Mansion, Super Mario Galaxy 1 & 2, Paper Mario series, Kirby, Smash Bros Melee/Brawl), Rare games (Banjo-Kazooie, DKC), GTA series (III, Vice City, San Andreas), Crash Bandicoot, Dark Souls, Katamari Damacy, Okami, Psychonauts, Need for Speed: Most Wanted, SpongeBob games, Outer Wilds, Halo CE, and more.
- [GameArchives](https://github.com/PikminGuts92/GameArchives) - C# library for reading 14+ video game archive formats.
  - Games: Harmonix titles (Frequency, Amplitude, Guitar Hero series, Rock Band series 1-4, Beatles, Green Day, Lego, VR, Karaoke Revolution, Disney Fantasia),
    Konami rhythm games (DDR Universe 1-3, DDR 2010, Dance Masters), FreeStyleGames (DJ Hero series, Guitar Hero Live, Sing Party), Psychonauts, Power Gig.
  - Formats: Ark, PSARC, PACKAGE, PFS, STFS, XDVDFS, U8. See also [maxton's fork](https://github.com/maxton/GameArchives) with FSAR support for Sing Party.
- [MeltyTool](https://github.com/MeltyPlayer/MeltyTool) - Multitool for viewing/extracting assets from various N64/GCN/3DS/PC games.
  - Games: Super Mario 64, Mario Artist (Polygon Studio, Talent Studio), Paper Mario TTYD, Super Paper Mario, Mario Kart Double Dash, Pikmin 1 & 2, Super Mario Sunshine, Chibi-Robo, Super Smash Bros. Melee, Battalion Wars 1 & 2, Super Mario 64 DS, Luigi's Mansion 3D, Majora's Mask 3D, Ocarina of Time 3D, Professor Layton vs. Phoenix Wright, Dead Space, Glover, Halo Wars, Celeste 64, Pokemon Colosseum, and more.
- [Noesis Plugins](http://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91) - Community plugin collections extending Noesis support to hundreds more games.
  - See [6 major plugin collections](http://richwhitehouse.com/index.php?content=inc_projects.php#prjmp91) including Tales series, Midnight Club 2, Visceral Games titles, and many more formats.
- [EdnessP/scripts](https://github.com/EdnessP/scripts) - Collection of scripts for various game file formats.
  - Games: Bully series, Burnout series (1, 2, 3, Legends, CRASH!), Call of Duty: Finest Hour, Jak & Daxter series (1, II, 3, X), Midnight Club series (2, 3), Saints Row series (2, Undercover), The Sims series (Bustin' Out, Urbz, 2, Pets, Castaway), The Simpsons Game, Tomb Raider (Wii), Need for Speed: Shift (PSP), Activision/Atari Anthology, Adventure Time, Bomberman Act:Zero, Big Rigs, Castle Strike, Driver: San Francisco, Epic Mickey, Exit, Freaky Flyers, Ready 2 Rumble Boxing, SpongeBob's Surf & Skate Roadtrip, Strike Suit Zero/Infinity, Yakuza 1 & 2 (PS2), and more.
- [bartlomiejduda/Tools](https://github.com/bartlomiejduda/Tools) - Collection of tools to manage and modify files from many various games. Includes archive tools, binary templates, and format-specific utilities.
  - Games: 150+ titles including Harry Potter series, Bully, Crash Bandicoot series, Tony Hawk's Underground, Sonic 2006/Unleashed, Resident Evil 7, Silent Hill series, Just Cause, Splinter Cell, SimCity 3000, LEGO games, The Sims series, Super Mario Sunshine, Star Wars Jedi Academy, Tekken 5, Transformers, Beyond Good & Evil, and many more.
- [Murugo/Misc-Game-Research](https://github.com/Murugo/Misc-Game-Research) - Research artifacts and tools for various games.
  - Games: Vib-Ribbon (PS1), Gitaroo Man (PS2), Silent Hill 2 & 3 (PS2), Kingdom Hearts series (PS2), Rule of Rose (PS2), Musashi: Samurai Legend (PS2).
- [EA-Graphics-Manager](https://github.com/bartlomiejduda/EA-Graphics-Manager) - Handles FSH, SSH, XSH, PSH, GSH, ASH, QFS and MSH files from EA games. Parse, preview, and export/import graphics as DDS/PNG/BMP.
  - Games: FIFA series (97, 2000, 06, 09, 14, Street, UEFA Euro 2004), Need For Speed series (1994, II, High Stakes, Hot Pursuit 2, Porsche Unleashed, Carbon, Undercover), Medal of Honor series (Frontline, Rising Sun, Vanguard, European Assault), Madden NFL (06, 08), NHL series (2001, 2002, 2005, 07), NBA Live 97, MVP Baseball/NCAA Baseball (2005, 2007), SSX series, Cricket (2005, 2007), Harry Potter (Chamber of Secrets, Quidditch World Cup), Def Jam: Fight For New York, Fight Night Round 3, GoldenEye, SimCity 4 Deluxe, Triple Play 2000, ReBoot, F.A. Premier League Football Manager 2000, EA Playground (Wii), and more across PS1, PS2, PSP, PC, Xbox, Wii, and Zeebo platforms.
- [EA-Font-Manager](https://github.com/bartlomiejduda/EA-Font-Manager) - Handles EA font files (FFN, PFN, XFN, MFN, SFN formats). Preview, decode flags, edit character tables, and convert font images.
  - Games: FIFA 97, Need for Speed series (2, High Stakes, Hot Pursuit, Undercover), NBA Live 06-07, SSX series, MVP Baseball 2005, Medal of Honor: European Assault,
    NHL series, Def Jam: Fight for NY, Harry Potter and the Chamber of Secrets, The Sims, and more.
- [EA-Loc-Manager](https://github.com/bartlomiejduda/EA-Loc-Manager) - Extract and import localization files (LOC format) from EA games. Supports UTF-8, UTF-16, and Latin-1 encodings.
  - Games: Harry Potter and the Chamber of Secrets (PS2), Medal of Honor: European Assault (Xbox), SSX On Tour, SSX Tricky (PS2), NHL 07 (PSP), and more.
- [TTG-Tools](https://github.com/zenderovpaulo95/TTG-Tools) - Translation utility for Telltale Games titles ([original version here](https://github.com/bartlomiejduda/TTG_Tools)). Supports texture conversion (d3dtx to dds/pvr), bitmap font editing/export to ttf, archive building/unpacking (ttarch/ttarch2), lua/lenc decryption/encryption, and extended game support including Sam & Max remasters and The Walking Dead: Definitive Series.
  - Games: Telltale Texas Hold'em, Bone (Out from Boneville, The Great Cow Race), Sam & Max (Save the World, Beyond Time and Space, The Devil's Playhouse), Strong Bad's Cool Game for Attractive People, Wallace & Gromit's Grand Adventures, Tales of Monkey Island, Hector: Badge of Carnage, Nelson Tethers: Puzzle Agent, Poker Night at the Inventory, Back to the Future: The Game, Puzzle Agent 2, Jurassic Park: The Game, Law & Order: Legacies, The Walking Dead (Season One, Season Two, Michonne, A New Frontier), Poker Night 2, The Wolf Among Us, Tales from the Borderlands, Game of Thrones, Minecraft: Story Mode, Batman: The Telltale Series.
- [RTB-3DSMax-Scripts](https://github.com/RandomTBush/RTB-3DSMax-Scripts) - Comprehensive collection of 3ds Max scripts for importing models from dozens of games and engines.
  - Games: Pokémon (Switch/3DS), Zelda (BOTW/TOTK/Wind Waker HD), Mario (Odyssey/Kart 8/3D World), Splatoon (1-3), Hyperdimension Neptunia series, Crash Bandicoot N. Sane Trilogy, Sonic (Unleashed/Riders), Telltale Games (Walking Dead/Batman), and many more.
  - Highlights: Support for ISM2, IGZ, MDL, D3DMesh, and Nintendo BFRES/BCH formats across PS1, PS3, Wii, Wii U, and Switch.

## ⚙️ Engines

*Tools specific to widespread third-party game engines.*

### GameMaker

- [UndertaleModTool](https://github.com/UnderminersTeam/UndertaleModTool) - Tool for modding/decompiling GameMaker games.
- [GMS-Explorer](https://github.com/puggsoy/GMS-Explorer) - Game Maker Studio `data.win` explorer.

### Source (Valve)

- [Blender Source Tools](https://github.com/Artfunkel/BlenderSourceTools) - Blender addon for importing and exporting Source Engine model and animation formats. Enables 3D asset creation and modification for all Source Engine games in Blender.
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
- [Plumber](https://github.com/lasa01/Plumber) - Blender add-on for importing Source 1 engine maps, models, materials and textures from CS:GO, TF2, CS:S, and other titles.
  - Features: full map import (brushes, overlays, lights, props, skyboxes), MDL/material/texture import with color options, and embedded file browser.
- [3D Studio Max SMD Import Plugin](https://www.moddb.com/games/half-life/downloads/3d-studio-max-smd-import-plug-in-import-smd-mode) - 3DS Max plugin for importing SMD (Studiomodel) format files from Half-Life and other Source Engine games.
- [Blender SMD Import and Export](https://www.moddb.com/groups/blender-artist/downloads/blender-smd-import-and-export-download) - Blender addon for importing and exporting SMD (Studiomodel) format files used in Source Engine games.
- [3D Studio Max SMD Export Plug-in](https://www.moddb.com/games/half-life/downloads/3d-studio-max-smd-export-plug-in) - 3DS Max plugin for exporting SMD (Studiomodel) format files for Half-Life and other Source Engine games.
- [Dvondrake's SMD exporter for Blender](https://www.moddb.com/groups/source-developers/downloads/dvondrake-smd-blender) - Blender SMD exporter for Source Engine models.
- [Autodesk Softimage Mod Tool 7.5 (Source Developers)](https://www.moddb.com/groups/source-developers/downloads/autodesk-softimage-mod-tool-75) - Softimage mod tool for Source Engine development (v7.5).
- [Blender3D SMD Exporter (Half-Life 2)](https://www.moddb.com/games/half-life-2/downloads/blender3d-smd-exporter) - Blender3D SMD exporter for Half-Life 2.
- [Hammer Units Conversion Tool](https://www.moddb.com/engines/source/downloads/hammer-units-conversion-tool) - Tool for converting Hammer units in Source Engine.
- [Hammer Units Converter 2.2](https://www.moddb.com/groups/level-design-group/downloads/hammer-units-converter-22) - Hammer units converter for Source Engine (v2.2).
- [Goldsrc Model Viewer (V 0.3a Beta2)](https://www.moddb.com/games/half-life/downloads/goldsrc-model-viewer-v-03a-beta2-archived-for-other-use) - Model viewer for GoldSrc engine (Half-Life) models (v0.3a Beta2).
- [Half-Life Model Viewer 1.25](https://www.moddb.com/games/half-life/downloads/half-life-model-viewer-125) - Model viewer for Half-Life MDL format (v1.25).
- [Half-Life Model Viewer 2.10](https://www.moddb.com/games/half-life/downloads/half-life-model-viewer-210) - Model viewer for Half-Life MDL format (v2.10).
- [Half Life 2 MDL (v37) Importer V 0.9 Beta for 3DS](https://www.moddb.com/games/half-life-2/downloads/half-life-2-mdl-v37-importer-v-0-9-beta-for-3ds) - 3DS Max plugin for importing Half-Life 2 MDL models (v37 format, v0.9 Beta).
- [Jed's Half-Life Model Viewer 1.36](https://www.moddb.com/games/half-life/downloads/jeds-half-life-model-viewer-136) - Model viewer for Half-Life MDL format (v1.36).
- [Source Model Viewer [Build: 2019-04-23] (Half-Life 2)](https://www.moddb.com/games/half-life-2/downloads/source-model-viewer-build-2019-04-23) - Model viewer for Source Engine models (build 2019-04-23).
- [VTF-2-TGA Convertor Utility (Half-Life 2)](https://www.moddb.com/games/half-life-2/downloads/vtf-2-tga-convertor-utility) - Converter for VTF (Valve Texture Format) to TGA format used in Half-Life 2.
- [Texture Tool v1.2.1 (Half-Life)](https://www.moddb.com/mods/half-life-episode-two/downloads/texture-tool) - Texture tool for Half-Life (v1.2.1).
- [BSP Decompiler by 005 (Half-Life)](https://www.moddb.com/games/half-life/downloads/bsp-decompiler-by-005) - BSP decompiler for Half-Life maps.
- [Bloody Knife + Addon DB Skin Tutorial (Counter-Strike: Source)](https://www.moddb.com/games/counter-strike-source/downloads/bloody-knife-addon-db-skin-tutorial) - Tutorial and tools for creating custom knife skins in Counter-Strike: Source.
- [Bloodlines Character Search Tool v1.0 (Vampire: The Masquerade – Bloodlines)](https://www.moddb.com/games/vampire-the-masquerade-bloodlines/downloads/bloodlines-character-search-tool-v10) - Character search tool for Vampire: The Masquerade – Bloodlines (v1.0).
- [Detail Tool v1.0 (Half-Life)](https://www.moddb.com/mods/half-life-episode-two/downloads/detail-tool-v10) - Detail tool for Half-Life modding (v1.0).
- [fixed bhop addon + more (Half-Life 2)](https://www.moddb.com/games/half-life-2/downloads/fixed-bhop-addon-more) - Bunny hop addon and additional tools for Half-Life 2.
- [Forsaken Assets & Source Code (Half-Life 2)](https://www.moddb.com/mods/forsaken/downloads/forsaken-assets-source-code) - Assets and source code for Forsaken mod for Half-Life 2.
- [Game Server Browser & Admin Tool 1.2.1 (Half-Life 2)](https://www.moddb.com/games/half-life-2/downloads/game-server-browser-admin-tool-1-2-1) - Server browser and admin tool for Half-Life 2 (v1.2.1).
- [GMad Extractor (Garry's Mod)](https://www.moddb.com/mods/garrys-mod-11-half-life-rebuilt/downloads/gmad-extractor) - Extractor for GMad archive files used in Garry's Mod.
- [Half Life 1 Modding Kit Addon 2](https://www.moddb.com/games/half-life/downloads/half-life-1-modding-kit-addon-2) - Modding kit addon for Half-Life (addon 2).
- [Half-Life Asset Manager V3.0.0](https://www.moddb.com/games/half-life/downloads/half-life-asset-manager-v300) - Asset manager for Half-Life (v3.0.0).
- [Half-Life DLL Decompiler](https://www.moddb.com/games/half-life/downloads/half-life-dll-decompiler) - DLL decompiler for Half-Life.
- [Half-Life: Insecure - Mapping Tools and Source Code v1.3](https://www.moddb.com/mods/half-life-insecure/downloads/half-life-insecure-mapping-tools-and-source-code-version-13) - Mapping tools and source code for Half-Life: Insecure mod (v1.3).
- [Half-Life Quick Mod Creation tool](https://www.moddb.com/games/half-life/downloads/half-life-quick-mod-creation-tool) - Quick mod creation tool for Half-Life.
- [Half-Life to Quake 3 .MAP converter](https://www.moddb.com/games/half-life/downloads/half-life-to-quake-3-map-converter) - Tool for converting Half-Life maps to Quake 3 MAP format.
- [Half-Life Unified SDK Map Decompiler (Counter-Strike)](https://www.moddb.com/games/counter-strike/downloads/half-life-unified-sdk-map-decompiler) - Unified SDK map decompiler for Half-Life and Counter-Strike.
- [Keybinder Source Tool (Counter-Strike: Source)](https://www.moddb.com/games/counter-strike-source/downloads/keybinder-source-tool) - Key binding tool for Source Engine games.
- [Jed's Half-Life Model Viewer 1.36 (Counter-Strike)](https://www.moddb.com/games/counter-strike/downloads/jeds-half-life-model-viewer-1361) - Model viewer for Counter-Strike MDL format (v1.36).
- [Xash studioMDL Goldsrc Large Model Compiler (Counter-Strike)](https://www.moddb.com/games/counter-strike/downloads/xash-studiomdl-goldsrc-large-model-compiler) - Large model compiler for GoldSrc engine used in Counter-Strike.
- [Half-Life Studio Model Decompiler v1.2.1 (Win32, Linux, Mac)](https://www.moddb.com/games/half-life/downloads/half-life-studio-model-decompilerwin32-linux-mac) - Studio model decompiler for Half-Life supporting multiple platforms (v1.2.1).
- [Valve Batch Compile Tool](https://www.moddb.com/engines/source/downloads/valve-batch-compile-tool) - Batch compilation tool for Source Engine.
- [XSI Valve Source Tools](https://www.moddb.com/downloads/valve-source-tools) - XSI tools for working with Source Engine formats.
- [Wedge MDL Compiler (QC Generator) 1.0.1](https://www.moddb.com/company/wedge/downloads/wedge-mdl-compiler-qc-generator-1-0-1) - MDL compiler with QC generator for Source Engine (v1.0.1).
- [Windows Vista/7 Phoneme Extractor 1.2](https://www.moddb.com/groups/source-developers/downloads/windows-vista7-phoneme-extractor-11) - Phoneme extraction tool for Source Engine (v1.2).
- [Windows Vista/7 Phoneme Extractor 1.3](https://www.moddb.com/groups/source-developers/downloads/windows-vista7-phoneme-extractor-13) - Phoneme extraction tool for Source Engine (v1.3).

### Unity

- [AssetStudio (Perfare)](https://github.com/Perfare/AssetStudio) - Explorer/exporter for Unity assets and assetbundles (original version).
- [Unity Asset Editor v0.2 (7 Days To Die)](https://www.moddb.com/games/7-days-to-die/downloads/unity-asset-editor) - Unity asset editor for 7 Days To Die (v0.2).
- [AssetStudio (aelurum fork)](https://github.com/aelurum/AssetStudio) - Actively maintained fork with UI optimization and enhancements.
- [AssetStudio (zhangjiequan fork)](https://github.com/zhangjiequan/AssetStudio) - Continuation of Perfare's AssetStudio with support for new Unity versions and additional improvements.
- [UABEA (Unity Asset Bundle Extractor Avalonia)](https://github.com/nesrak1/UABEA) - Cross-platform Unity asset bundle and serialized file editor/extractor built with Avalonia.
- [UnityExplorer](https://github.com/sinai-dev/UnityExplorer) - In-game UI for exploring, debugging and modifying IL2CPP and Mono Unity games.

### Unreal Engine

- [io_scene_psk_psa](https://github.com/DarklightGames/io_scene_psk_psa) - Blender addon for importing and exporting PSK (skeletal mesh) and PSA (animation) formats used in Unreal Engine. Supports PSK/PSKX mesh import with vertex normals, extra UV channels, vertex colors, and shape keys.
- [io_scene_ase](https://github.com/DarklightGames/io_scene_ase) - Blender exporter for the legacy ASE (ASCII Scene Export) format used by Unreal Engine 1 & 2 games (e.g., Unreal Tournament 2004).
- [UEViewer (UModel)](https://github.com/gildor2/UEViewer) - Viewer and exporter for Unreal Engine 1-4 assets.
  - [Compatibility Table](https://www.gildor.org/projects/umodel/compat) - Official compatibility list.
- [FModel](https://fmodel.app/) - Open-source software for data-mining UE4-5 games.
- [CUE4Parse](https://github.com/FabianFG/CUE4Parse) - C# Parser for UE archives.
- [UnrealExporter](https://github.com/luk-gg/UnrealExporter) - Batch file exporter.
- [UE-Modding-Tools](https://github.com/Buckminsterfullerene02/UE-Modding-Tools) - Databank of generic UE modding tools.
- [Snooper](https://github.com/FModel/Snooper/tree/opengl) - OpenGL based 3D viewer for cooked UE packages.
- [ActorX Tools](https://www.moddb.com/groups/unreal-tournament-3-mod-developers/downloads/actorx-tools-for-maya-85-3dsmax-9) - Plugin for Maya 8.5 and 3DS Max 9 for importing skeletal meshes and animations in Unreal Engine games.
- [ActorX Softimage Exporter](https://www.moddb.com/downloads/actorx-softimage-exporter) - Softimage exporter for ActorX format used in Unreal Engine games.
- [U3D](https://www.moddb.com/games/unreal-tournament/downloads/u3d-v10-unreal-model-conversion-tool) - Unreal model conversion tool for converting 3DS files to Unreal .3D format. Supports uniform/XYZ scaling, clipping bounds, and animation frame conversion.
- [Unreal to Deus Ex mesh converter](https://www.moddb.com/games/deus-ex/downloads/unreal-to-deus-ex-mesh-converter) - Tool for converting Unreal Engine mesh formats to Deus Ex format.
- [DUT TOOL-2.0.2.0 (Unreal Tournament 3)](https://www.moddb.com/mods/defend-unreal-territories/downloads/dut-tool-2020) - Tool for Defend Unreal Territories mod for Unreal Tournament 3.
- [UEd Style Tools for Maya (Unreal Tournament)](https://www.moddb.com/games/unreal-tournament/downloads/ued-style-tools-for-maya) - Maya tools for working with Unreal Tournament assets in UEd style.
- [Unreal Unit Converter (Source Code)](https://www.moddb.com/downloads/unreal-unit-converter-source-code) - Unit converter for Unreal Engine (source code).
- [UShock - Unreal level viewer (Unreal Tournament)](https://www.moddb.com/games/unreal-tournament/downloads/ushock-unreal-level-viewer) - Level viewer for Unreal Tournament maps.
- [Unreal Unit Converter](https://www.moddb.com/downloads/unreal-unit-converter1) - Unit converter tool for Unreal Engine.
- [PS3 Mod Tools version 2.1 (Unreal Tournament 3)](https://www.moddb.com/games/unreal-tournament-3/downloads/ps3-mod-tools-version-21) - PlayStation 3 modding tools for Unreal Tournament 3 (v2.1).
- [WOTgreal Package Exporter (Unreal Tournament)](https://www.moddb.com/games/unreal-tournament/downloads/wotgreal-package-exporter) - Package exporter for Unreal Tournament using WOTgreal.
- [Advanced Model Support SDK (Unreal Tournament)](https://www.moddb.com/mods/ut-skins-voices-mods-fixes/downloads/advanced-model-support-sdk) - Advanced model support SDK for Unreal Tournament.
- [Web Admin Tools (Unreal Tournament 3)](https://www.moddb.com/games/unreal-tournament-3/downloads/web-admin-tools) - Web-based administration tools for Unreal Tournament 3.
- [Blender 2.49 Scripts for UT2004](https://www.moddb.com/games/unreal-tournament-2004/downloads/blender-249-scripts-for-ut2004) - Blender 2.49 scripts for Unreal Tournament 2004.
- [Defend Unreal Territories Launcher (Unreal Tournament 3)](https://www.moddb.com/mods/defend-unreal-territories/downloads/defend-unreal-territories-launcher) - Launcher for Defend Unreal Territories mod for Unreal Tournament 3.
- [February 2015 Unreal Development Kit (UDK)](https://www.moddb.com/engines/unreal-development-kit/downloads/february-2015-unreal-development-kit-udk) - Unreal Development Kit release from February 2015.

### CryEngine

- [Far Cry 1 Noesis import plugin](https://www.moddb.com/games/far-cry/downloads/far-cry-1-noesis-import-plugin) - Noesis plugin for importing Far Cry 1 (CryEngine 1) models. Supports model import but not export.
- [Far Cry 1 3dsmax 9 plugin](https://www.moddb.com/games/far-cry/downloads/far-cry-1-3dsmax-9-plugin) - 3DS Max 9 plugin for Far Cry 1.
- [CryEngine 2 3d archive](https://www.moddb.com/games/crysis/downloads/cryengine-2-3d-archive) - Tool for working with CryEngine 2 3D archive files from Crysis.
- [CryENGINE 2 Resources (Crysis)](https://www.moddb.com/games/crysis/downloads/cryengine-2-resources1) - Resources for CryENGINE 2 used in Crysis.
- [CryEngine2 Archive (Crysis)](https://www.moddb.com/games/crysis/downloads/cryengine2-archive) - Archive tool for CryEngine2 used in Crysis.
- [Crysis Benchmarking Tool 1.05](https://www.moddb.com/games/crysis/downloads/crysis-benchmarking-tool-1-05) - Benchmarking tool for Crysis (v1.05).
- [Cryengine Mod SDK 1.4 (Far Cry)](https://www.moddb.com/games/far-cry/downloads/cryengine-mod-sdk-14) - Mod SDK for CryEngine used in Far Cry (v1.4).
- [Enhanced Gibbed Tools with Hash Decoder (Far Cry 2)](https://www.moddb.com/games/far-cry-2/downloads/enhanced-gibbed-tools-with-hash-decoder) - Enhanced Gibbed tools with hash decoder for Far Cry 2.
- [Far Cry 2 Mod Tools](https://www.moddb.com/mods/far-cry-2-redux/downloads/far-cry-2-mod-tools) - Mod tools for Far Cry 2.
- [Far Cry 3 Mod Tools](https://www.moddb.com/mods/far-cry-3-redux/downloads/far-cry-3-mod-tools) - Mod tools for Far Cry 3.
- [FCMAP Tool v0.3B-0.5B (Far Cry)](https://www.moddb.com/mods/fcmap-tool/downloads/fcmap-tool-v03b-05b) - Map tool for Far Cry (v0.3B-0.5B).
- [FCMAP Tool v1.0 (Far Cry)](https://www.moddb.com/mods/fcmap-tool/downloads/fcmap-tool-v05-10) - Map tool for Far Cry (v1.0).

### Hedgehog Engine

- [HedgeLib](https://github.com/Radfordhound/HedgeLib) - C++ library and collection of tools for modding Hedgehog Engine games (Sonic series).
- [Hedgehog Engine Blender I/O](https://github.com/hedge-dev/HedgehogEngineBlenderIO) - WIP Blender add-on for Hedgehog Engine assets including import/export and animation editing.

### Northlight Engine

- [BlenderNorthlight](https://github.com/OpenAWE-Project/BlenderNorthlight) - Blender plugin for loading `binmsh` and `binfbx` files from Northlight Engine games (Control, Alan Wake 2, Quantum Break).

### Build Engine

- [BUILD Map Importer](https://github.com/jensnt/io_import_build_map) - Blender add-on for BUILD-format maps (Blood, Duke Nukem 3D, etc.) that can auto-extract textures from `.ART`, `.GRP`, and `.RFF` files.
  - Import options: split sectors/walls/sky, preserve sprite offsets, reuse materials, shade to vertex colors, and store original map data in custom properties.
- [Build palette editing tools (Duke Nukem 3D)](https://www.moddb.com/mods/black-shadow/downloads/build-palette-editing-tools) - Palette editing tools for BUILD Engine games like Duke Nukem 3D.

### Raven Software

#### Heretic II

- [Quake Model to FlexModel Converter](https://www.moddb.com/games/heretic-ii/downloads/quake-model-to-flexmodel-converter-aka-convert) - Tool for converting Quake model formats to FlexModel format used in Heretic II.
- [FlexModel to Wavefront Object Converter (FM2OBJ)](https://www.moddb.com/games/heretic-ii/downloads/flexmodel-to-wavefront-object-converter-aka-fm2obj) - Converter for FlexModel format to Wavefront OBJ format used in Heretic II.
- [Heretic II Toolkit v1.06](https://www.moddb.com/games/heretic-ii/downloads/heretic-ii-toolkit-v106) - Comprehensive toolkit for working with Heretic II file formats (v1.06).

#### Soldier of Fortune

- [Official 3dsmax 3x plugin (Soldier of Fortune)](https://www.moddb.com/games/soldier-of-fortune/downloads/official-3dsmax-3x-plugin) - Official 3DS Max 3.x plugin for Soldier of Fortune.
- [.m32 to .tga/.adp to .wav file converters (Soldier of Fortune)](https://www.moddb.com/games/soldier-of-fortune/downloads/m32-to-tga-file-converter) - File format converters for Soldier of Fortune (.m32 to .tga, .adp to .wav).
- [.m32 tool (Soldier of Fortune)](https://www.moddb.com/games/soldier-of-fortune/downloads/m32-tool) - Tool for working with .m32 texture files from Soldier of Fortune.
- [.os script decompiler v2.0 (Soldier of Fortune)](https://www.moddb.com/games/soldier-of-fortune/downloads/os-script-decompiler-v20) - Script decompiler for Soldier of Fortune .os files (v2.0).

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

### Havok

*Physics and animation middleware used in hundreds of games across all platforms.*

- [Havok IO (Blender)](https://github.com/NewSkyLine-dev/havokmax-blender) - Blender add-on that imports `.hkx`, `.hkt`, `.hka`, `.igz`, and `.pak` files from Havok XML and binary archives. Replaces the legacy HavokMax 3ds Max plugin.
  - Capabilities: builds armatures and keyframed actions from animation data, constructs static meshes from geometry blocks, and unwraps PAK/IGZ containers.
- [HavokNoesis](https://github.com/PredatorCZ/HavokNoesis) - Noesis plugin for importing/exporting Havok physics engine formats.

### JSYSTEM (GameCube/Wii)

*Nintendo's in-house middleware used to develop GameCube and Wii era games. Used in [Pikmin](#pikmin), [Pikmin 2](#pikmin-2), [Luigi's Mansion](#luigis-mansion), [Super Mario Sunshine](#super-mario-other), [Super Mario Galaxy](#super-mario-other), [Wind Waker](#zelda), [Twilight Princess](#zelda), [Mario Kart: Double Dash](#mario-kart-double-dash), and many other first-party GameCube/Wii titles.*

- [gclib](https://github.com/LagoLunatic/gclib) - Python implementations of several GameCube file formats for ROM hacking.
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

### MikuMikuDance

*Freeware animation program and its associated model and motion formats (.pmx, .pmd, .vmd).*

- [MMD Tools](https://github.com/MMD-Blender/blender_mmd_tools) - Blender add-on for importing/exporting MikuMikuDance assets. Supports physics, bone constraints, and motion/pose data.
- [MMD Tools Append](https://github.com/MMD-Blender/blender_mmd_tools_append) - Companion extension for MMD Tools that provides material/scene controls, lighting presets, and Rigify helpers.

### RenderWare

*Cross-platform 3D engine and middleware developed by Criterion Games. Powering the Grand Theft Auto trilogy (III, Vice City, San San Andreas), Burnout series, and many other titles.*

- [DragonFF](https://github.com/Parik27/DragonFF) - Blender add-on for RenderWare `.dff` models, `.txd` textures, `.col` collisions, and `.ipl` map data.

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
- [IWI DDS Fast Converter V1.40 (Call of Duty 2)](https://www.moddb.com/games/call-of-duty-2/downloads/iwi-dds-fast-converter-v140) - Fast converter for IWI and DDS texture formats used in Call of Duty 2 (v1.40).
- [x to xmodel_export converter 1.6 cod5 Version (Call of Duty: World at War)](https://www.moddb.com/games/call-of-duty-world-at-war/downloads/x-to-xmodel-exporter-converter-16-cod5-version) - Converter for X model format to xmodel_export format for Call of Duty: World at War (v1.6).
- [iw4-open-formats](https://github.com/iw4x/iw4-open-formats/blob/main/src/iw4-of/assets/assets.cpp) - Asset conversion system for MW2 formats.
- [BSP Decompiler (Call of Duty)](https://www.moddb.com/games/call-of-duty/downloads/bsp-decompiler) - BSP decompiler for Call of Duty maps.
- [Call of Duty 1 Milkshape plugins](https://www.moddb.com/games/call-of-duty/downloads/call-of-duty-1-milkshape-plugins) - Milkshape 3D plugins for Call of Duty.
- [Call of Duty 1 Mod Tools No Installer Version](https://www.moddb.com/games/call-of-duty/downloads/call-of-duty-1-mod-tools-no-installer-version) - Mod tools for Call of Duty (no installer version).
- [Call of Duty 2 Mod Tools](https://www.moddb.com/games/call-of-duty-2/downloads/call-of-duty-2-mod-tools) - Mod tools for Call of Duty 2.
- [Call of Duty 2 Mod Tools No Installer](https://www.moddb.com/games/call-of-duty-2/downloads/call-of-duty-2-mod-tools-no-installer) - Mod tools for Call of Duty 2 (no installer version).
- [Call of Duty 4 Mod Tools (SDK)](https://www.moddb.com/games/call-of-duty-4-modern-warfare/downloads/call-of-duty-4-mod-tools-sdk) - Mod tools SDK for Call of Duty 4: Modern Warfare.
- [Iwi Converter (Call of Duty 2)](https://www.moddb.com/games/call-of-duty-2/downloads/iwi-converter) - Converter for IWI texture format used in Call of Duty 2.
- [KV Map Converter v2 Beta2 (Call of Duty 4: Modern Warfare)](https://www.moddb.com/games/call-of-duty-4-modern-warfare/downloads/kv-map-converter-v2-beta2) - Map converter for Call of Duty 4: Modern Warfare (v2 Beta2).

#### Tony Hawk's Pro Skater

- [WAD Tool v1.0 (Tony Hawk's Pro Skater)](https://www.moddb.com/games/tony-hawks-pro-skater/downloads/wad-tool-v10) - WAD archive tool for Tony Hawk's Pro Skater (v1.0).
- [C2M](https://github.com/sheilan102/C2M) - Map exporter for Call of Duty.
- [TOXEC (The Obj to Xmodel Export Converter)](https://www.moddb.com/games/call-of-duty-world-at-war/downloads/toxec-the-obj-to-xmodel-export-converter) - Tool for converting OBJ files to Call of Duty Xmodel format.
- [DDS/IWI Converter 1.5 (Call of Duty 2)](https://www.moddb.com/games/call-of-duty-2/downloads/dds-iwi-converter-1-5) - Converter for DDS and IWI texture formats used in Call of Duty 2.

### Angel Matrix

- [noclip.website (Neon White)](https://github.com/magcius/noclip.website/tree/main/src/NeonWhite) - In-browser Neon White viewer.

### Angel Studios / Rockstar San Diego

- [AngelStudiosBlenderAddon](https://github.com/Dummiesman/AngelStudiosBlenderAddon) - Blender addon for importing models from Angel Studios/Rockstar San Diego games. Supports multiple formats (BMS, DLP, MOD/XMOD, BND, SKEL, GEO) used in Midnight Club 2, Midtown Madness 1, and likely other Angel Studios titles from ~1999-2006.
- [MidnightClub2 (Noesis)](https://himeworks.com/noesis-plugins/) - Noesis plugin for Midnight Club 2 model formats.
- [Sollumz](https://github.com/Hancapo/Sollumz) - GTA V modding suite for Blender (RAGE engine formats). [Documentation here](https://docs.sollumz.org).
- [pyrpfiv](https://github.com/gmroder/pyrpfiv) - Python library for parsing and manipulating GTA IV's RPF (Resource Package Format) archives.
- [noclip.website (Grand Theft Auto III)](https://github.com/magcius/noclip.website/tree/main/src/GrandTheftAuto3) - In-browser Grand Theft Auto III viewer.
- [noclip.website (Grand Theft Auto: Vice City)](https://github.com/magcius/noclip.website/tree/main/src/GrandTheftAuto3) - In-browser Grand Theft Auto: Vice City viewer.
- [noclip.website (Grand Theft Auto: San Andreas)](https://github.com/magcius/noclip.website/tree/main/src/GrandTheftAuto3) - In-browser Grand Theft Auto: San Andreas viewer.
- [MidtownExtractor](https://github.com/0x1F9F1/MidtownExtractor) - Midtown Madness 1/2 and Midnight Club 2 File Extractor
- [MeltyTool](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/AngelStudios) - Multitool for viewing/extracting assets from various N64/GCN/3DS/PC games en-masse.
- [CLEO library v2.0.0.5 by Seemann (Grand Theft Auto III)](https://www.moddb.com/games/grand-theft-auto-3/downloads/cleo-library-by-seemann-for-gta-iii) - CLEO library for Grand Theft Auto III (v2.0.0.5).
- [CLEO library v2.0.0.5 by Seemann (Grand Theft Auto: Vice City)](https://www.moddb.com/games/grand-theft-auto-vice-city/downloads/cleo-library-v2005-by-seemann-for-gta-vc) - CLEO library for Grand Theft Auto: Vice City (v2.0.0.5).
- [CLEO library v4.3.22 by Seemann (Grand Theft Auto: San Andreas)](https://www.moddb.com/games/grand-theft-auto-san-andreas/downloads/cleo-library-v4322-by-seemann-for-gta-sa) - CLEO library for Grand Theft Auto: San Andreas (v4.3.22).
- [Epic GTA2 Script Decompiler Source Code (Grand Theft Auto 2)](https://www.moddb.com/games/grand-theft-auto-2/downloads/epic-gta2-script-decompiler-source-code) - Source code for GTA2 script decompiler.
- [GMP/STY file format descriptions (Grand Theft Auto 2)](https://www.moddb.com/games/grand-theft-auto-2/downloads/gmpsty-file-format-descriptions) - File format documentation for GMP and STY formats used in Grand Theft Auto 2.
- [GTA Font compiler (Grand Theft Auto)](https://www.moddb.com/games/grand-theft-auto/downloads/gta-font-compiler) - Font compiler for Grand Theft Auto.
- [GTA V Suspend Resume tool (Grand Theft Auto V)](https://www.moddb.com/games/grand-theft-auto-v/downloads/gta-v-suspend-resume-tool) - Tool for suspending and resuming Grand Theft Auto V.
- [IMG Tool v1.3 (Grand Theft Auto III)](https://www.moddb.com/games/grand-theft-auto-3/downloads/iii-img-tool-v13) - IMG archive tool for Grand Theft Auto III (v1.3).
- [IMG Tool 2.0 (Grand Theft Auto: San Andreas)](https://www.moddb.com/games/grand-theft-auto-san-andreas/downloads/img-tool-20) - IMG archive tool for Grand Theft Auto: San Andreas (v2.0).

### Ape, Inc

- [earthbound-script-dumper](https://github.com/CataLatas/earthbound-script-dumper) - Script dumper for EarthBound.
- [ebtexted](https://github.com/PKHackers/ebtexted) - Text editor for EarthBound.
- [EBME](https://github.com/Supremekirb/EBME) - EarthBound Map Editor.

### 11 bit studios

- [Frostract - Frostpunk idx and dat unpacker](https://www.moddb.com/games/frostpunk/downloads/frostract-frostpunk-idx-and-dat-unpacker) - Tool for unpacking IDX and DAT archive files from Frostpunk.

### Remedy Entertainment

#### Max Payne

- [Game Levels Importing plugin for Maya (Max Payne)](https://www.moddb.com/games/max-payne/downloads/game-levels-importing-plugin-for-maya) - Maya plugin for importing game levels from Max Payne.
- [MAX-FX Tools (Max Payne)](https://www.moddb.com/games/max-payne/downloads/max-fx-tools) - Tools for working with MAX-FX engine formats in Max Payne.
- [Max Payne 1-2 Packer](https://www.moddb.com/games/max-payne-2/downloads/max-payne-1-2-packer) - Archive packer for Max Payne 1 and 2.
- [MaxPayne Toolset](https://www.moddb.com/games/max-payne/downloads/maxpayne-toolset) - Toolset for working with Max Payne file formats.
- [Mod Tools (Max Payne 2)](https://www.moddb.com/games/max-payne-2/downloads/mod-tools) - Modding tools for Max Payne 2.

### Argonaut Games

- [PS1-BRender-Reverse](https://github.com/OverSurge/PS1-Argonaut-Reverse) - Reverse engineering tools for PlayStation 1 BRender engine games like Harry Potter and Croc 2.

### Arkane Studios

- [Arx Fatalis .PAK unpacker](https://www.moddb.com/games/arx-fatalis/downloads/arx-fatalis-pak-unpacker-v13) - Tool for unpacking PAK archive files from Arx Fatalis (v1.3).
- [disrev](https://github.com/chipolux/disrev) - Python tools for extracting and modifying Dishonored 2 assets.
- [dishonored2_scripts](https://github.com/usernametoolo/dishonored2_scripts/blob/master/tools/scripts/unpack_resources.py) - Resource extraction script for unpacking .pak archives.
- [Obscura](https://github.com/Mikompilation/Obscura) - Modding toolkit for Dishonored games.
- [Field Editor 0.5.1 \"Tautologist tool\" (Dishonored)](https://www.moddb.com/games/dishonored/downloads/field-editor-051-tautologist-tool) - Field editor for Dishonored (v0.5.1).

### Atlus

- [DDS3-Model-Studio](https://github.com/tge-was-taken/DDS3-Model-Studio) - WIP Model editing tools for DDS3 engine based SMT games (SMT: Nocturne, DDS 1 & 2, Raidou 1 & 2).

### Asobo Studio

- [fmtk](https://github.com/widberg/fmtk) - FUEL Modding Toolkit.

### Black Element Software

- [Alpha Prime RES Unpacker](https://www.moddb.com/mods/alpha-prime-dominus-prime/downloads/alpha-prime-res-unpacker-modding-tool) - Tool for unpacking RES archive files from Alpha Prime.

### Bandai Namco

- [BinarySerializer.Klonoa](https://github.com/BinarySerializer/BinarySerializer.Klonoa) - Serializer for Klonoa games.
- [TalesOfFantasy (Noesis)](https://himeworks.com/noesis-plugins/) - Noesis plugins for Tales series.
- [ARC](https://github.com/Bigchillghost/ARC) - Animation Recipe Cracker for Bandai Namco games.
- [noclip.website (Klonoa)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Klonoa viewer.
- [noclip.website (Katamari Damacy)](https://github.com/magcius/noclip.website/tree/main/src/KatamariDamacy) - In-browser Katamari Damacy viewer.

### EA DICE

#### Battlefield Series

- [BF1942 3dsmax 8 plugin](https://www.moddb.com/games/battlefield-1942/downloads/bf1942-3dsmax-8-plugin) - 3DS Max 8 plugin for importing Battlefield 1942 models.
- [BF2 Maya 4-6 Tools](https://www.moddb.com/games/battlefield-2/downloads/bf2-maya-4-6-tools) - Maya 4-6 tools for working with Battlefield 2 assets.
- [BF42 3dsMax plugins 2.762](https://www.moddb.com/mods/battlefield-2-play-for-free-mod/downloads/bf42-3dsmax-plugins-2762) - 3DS Max plugins for Battlefield 2 (v2.762).
- [BGF Heightmap Converter](https://www.moddb.com/games/battlefield-2/downloads/bgf-heightmap-converter-utility) - Heightmap converter utility for Battlefield 2 BGF format.
- [DDS Viewer Plugin (Battlefield Vietnam)](https://www.moddb.com/games/battlefield-vietnam/downloads/dds-viewer-plugin) - DDS texture viewer plugin for Battlefield Vietnam.
- [NVIDIA DDS Utilities (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/nvidia-dds-utilities) - NVIDIA DDS texture utilities for Battlefield 2.
- [NVIDIA Texture Atlas Tool (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/nvidia-texture-atlas-tool) - NVIDIA texture atlas tool for Battlefield 2.
- [POE2 3DS Max 6-8 BF2 Tools (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/poe2-3ds-max-6-8-tools) - 3DS Max 6-8 tools for Battlefield 2 (POE2).
- [POE2 3DS Max 9 BF2 Tools (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/poe2-3ds-max-9-bf2-tools) - 3DS Max 9 tools for Battlefield 2 (POE2).
- [Windows Texture Viewer v089b (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/windows-texture-viewer-v089b) - Texture viewer for Battlefield 2 (v0.89b).
- [Texture Tool 0.2 (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/texture-tool-0-2) - Texture editing tool for Battlefield 2 (v0.2).
- [Clan Tool (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/clan-tool) - Clan management tool for Battlefield 2.
- [Dragon UnPACKer (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/dragon-unpacker) - Archive unpacker tool for Battlefield 2.

#### Star Wars: Battlefront

- [StarWars Battlefront unpacker / decoder](https://www.moddb.com/games/star-wars-battlefront/downloads/starwars-battlefront-unpacker-decoder) - Archive unpacker and decoder for Star Wars: Battlefront.
- [Star Wars: Battlefront Modification Tools](https://www.moddb.com/games/star-wars-battlefront/downloads/star-wars-battlefront-modification-tools) - Comprehensive modification toolkit for Star Wars: Battlefront.
- [3D Object Converter (Star Wars Battlefront II)](https://www.moddb.com/games/star-wars-battlefront-ii/downloads/3d-object-converter) - 3D object format converter for Star Wars: Battlefront II.

### Capcom

#### Resident Evil

- [BioHazard File Archive Tool (Resident Evil 4)](https://www.moddb.com/games/resident-evil-4/downloads/biohazard-file-archive-tool) - File archive tool for Resident Evil 4 (2005).

#### Monster Hunter

- [Mod3-MHW-Importer](https://github.com/AsteriskAmpersand/Mod3-MHW-Importer) - Blender Import-Exporter for Monster Hunter World Mod3 model format.
- [RingingBloom](https://github.com/Silvris/RingingBloom) - WWise audio editing toolkit for Monster Hunter: World and other Capcom titles.
  - Features: BNK Editor (soundbanks), PCK Editor (packages), Loop Calculator, WEM Creator, WWCT/WWBK/WWPK/EPVSP editors.
  - Formats: .nbnk/.bnk, .npck/.pck, .wwct, .wwbk/.wwpk, .epvsp, .wem.

#### Devil May Cry

- [dmc_hd_tools](https://github.com/Kerilk/dmc_hd_tools) - Toolkit for Devil May Cry HD Collection including Noesis plugins and binary templates.
- [ARC Unpacker & Repacker](https://www.moddb.com/games/devil-may-cry-4/downloads/arc-unpacker-repacker-v09428) - Tool for unpacking and repacking ARC archive files from Devil May Cry 4.

#### Gregory Horror Show

- [GregoryHorrorShow-Blender-IO](https://github.com/boringhexi/GregoryHorrorShow-Blender-IO) - Imports PS2 Gregory Horror Show assets (`.ghs`, `.map-pm2`, `.pm2`) into Blender.

### CCR

- [RF Online Addon](https://github.com/Cardboard-box-a/cbb-rf-online-addon) - Blender 4.3 importer/exporter for RF Online `.msh`, `.bn`, `.ani`, and `.bsp` formats.

### CCP Games

- [yretenai/Jackdaw](https://github.com/neptuwunium/Jackdaw) - Research project for Carbon Engine file formats used in EVE Online.

### CD Projekt Red

#### The Witcher 3 / REDEngine 3

- [WolvenKit (legacy)](https://github.com/WolvenKit/WolvenKit-7) - REDEngine 3 file editor designed to simplify and accelerate modding workflow for The Witcher 3.

#### The Witcher

- [Blender 2.49 exporter for The Witcher](https://www.moddb.com/games/the-witcher/downloads/blender-exporter-for-the-witcher) - Blender 2.49 exporter for The Witcher.
- [twMax v1.2.3.2 -- mdb Importer for 3DSMax (The Witcher)](https://www.moddb.com/games/the-witcher/downloads/twmax-v1232-mdb-importer-for-3dsmax) - 3DS Max importer for The Witcher MDB model format (v1.2.3.2).
- [Extra tools (The Witcher)](https://www.moddb.com/games/the-witcher/downloads/extra-tools) - Additional tools for The Witcher.

#### Cyberpunk 2077 / REDEngine 4

- [WolvenKit](https://github.com/WolvenKit/WolvenKit) - REDEngine 4 file editor designed to simplify and accelerate modding workflow for Cyberpunk 2077.
- [Cyber Engine Tweaks](https://github.com/maximegmd/CyberEngineTweaks) - Framework to script mods using Lua with access to all the internal scripting features.

### Clover Studio

- [noclip.website (Okami)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Okami viewer.

### Cygames

- [GBFRBlenderTools](https://github.com/WistfulHopes/GBFRBlenderTools) - Blender addon for importing Granblue Fantasy Relink mesh models.
- [GBFR2Blender2GBFR](https://github.com/WistfulHopes/GBFR2Blender2GBFR) - Tools for importing/exporting animations and collision data for Granblue Fantasy Relink.

### Disney Interactive

#### Toontown Online

- [omUlette](https://github.com/lifelandman/omUlette) - Lightweight exporter for Panda3D `.egg` files (used in Toontown) that works without Panda3D installed.

### Double Fine

- [noclip.website (Psychonauts)](https://github.com/magcius/noclip.website/tree/main/src/psychonauts) - In-browser Psychonauts viewer.

### 8monkey Labs

- [Translation Tool (Darkest of Days)](https://www.moddb.com/games/darkest-of-days/downloads/darkest-of-days-translation-tool) - Translation tool for Darkest of Days.

### Crystal Dynamics / Eidos Interactive

- [Blood Omen 2 3D Rip Tools](https://www.moddb.com/games/blood-omen-2/downloads/blood-omen-2-3d-rip-tools) - Tools for extracting 3D models from Blood Omen 2.

### Ion Storm

#### Anachronox

- [Anachronox Modding Tools](https://www.moddb.com/games/anachronox/downloads/anachronox-modding-tools) - Modding tools for Anachronox.

#### Deus Ex

- [Gibbed's Deus Ex HR tools](https://www.moddb.com/games/deus-ex-3/downloads/gibbeds-deus-ex-hr-tools) - Gibbed's tools for Deus Ex: Human Revolution.

### Massive Entertainment

#### AquaNox

- [AquaNox 1-2 modding tools](https://www.moddb.com/games/aquanox/downloads/aquanox-1-2-modding-tools) - Modding tools for AquaNox 1 and 2.

#### World in Conflict

- [Broadcast Tool v6 (World in Conflict)](https://www.moddb.com/games/world-in-conflict/downloads/broadcast-tool-v6) - Broadcast tool for World in Conflict (v6).
- [Broadcast Tool v7 (World in Conflict)](https://www.moddb.com/games/world-in-conflict/downloads/broadcast-tool-v7) - Broadcast tool for World in Conflict (v7).
- [Broadcast Tool v8 (World in Conflict)](https://www.moddb.com/games/world-in-conflict/downloads/broadcast-tool-v8) - Broadcast tool for World in Conflict (v8).

### Surreal Software

- [Drakan Editing Tools v1.2](https://www.moddb.com/games/drakan-order-of-the-flame/downloads/drakan-editing-tools-v12) - Editing tools for Drakan: Order of the Flame (v1.2).
- [reo converter to obj (Drakan: Order of the Flame)](https://www.moddb.com/games/drakan-order-of-the-flame/downloads/reo-converter-to-obj) - Converter for REO model format to OBJ format used in Drakan: Order of the Flame.

### Dynamix / Sierra

#### Tribes Series

- [Tribes 2 3D Studio MAX Export Plug-in](https://www.moddb.com/games/tribes-2/downloads/tribes-2-3d-studio-max-export-plug-in) - 3DS Max export plugin for Tribes 2 model formats.
- [Tribes: Vengeance Editing Tools](https://www.moddb.com/games/tribes-vengeance/downloads/tribes-vengeance-editing-tools) - Editing tools for Tribes: Vengeance.
- [Tribes 1.40 LoDFix plugin](https://www.moddb.com/games/tribes/downloads/tribes-140-lodfix-plugin) - Level of Detail fix plugin for Tribes (v1.40).

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
- [blender-flver](https://github.com/elizagamedev/blender-flver) - Blender addon for importing/exporting FLVER models from FromSoftware games. Supports Dark Souls, Dark Souls: Remastered, Bloodborne, and Sekiro.
- [FromSoftware-Blender-Importer](https://github.com/FelixBenter/FromSoftware-Blender-Importer) - Blender importer for FromSoftware FLVER formats. Supports Dark Souls 1, 2, 3, and Sekiro: Shadows Die Twice (characters, partsbnds, and maps for DS1/DS3).
- [soulstruct](https://github.com/Grimrukh/soulstruct) - Python library for Dark Souls file formats and modding.
- [soulstruct-blender](https://github.com/Grimrukh/soulstruct-blender) - Blender plugin for soulstruct.
- [SoulsTemplates](https://github.com/JKAnderson/SoulsTemplates) - 010 Editor templates for Souls formats.
- [noclip.website (DarkSouls)](https://github.com/magcius/noclip.website/tree/main/src/DarkSouls) - In-browser Dark Souls map viewer.
- [DSAnimStudio](https://github.com/Meowmaritus/DSAnimStudio) - Animation and cutscene editor for Souls games.
- [dark_souls_hkx](https://github.com/Danilodum/dark_souls_hkx) - Noesis plugins for Dark Souls HKX (Havok animation) format with extra root bone and root motion support.
- [ESDLang](https://github.com/thefifthmatt/ESDLang) - Decompiler for ESD event script format.
- [Gibbed.DarkSouls](https://github.com/gibbed/Gibbed.DarkSouls) - Tools & code for use with Dark Souls.
- [DS2Template](https://github.com/LordRadai/DS2Template) - Collection of 010 .bt templates specifically made for Dark Souls II

### Gearbox Software

- [Borderlands 2 Texture Modding Tool for PC](https://www.moddb.com/games/borderlands-2/downloads/borderlands-2-texture-modding-tool-for-pc) - Texture modding tool for Borderlands 2 on PC.

#### MechWarrior 4

- [MW4 Sound Extractor (MechWarrior 4: Mercenaries)](https://www.moddb.com/games/mechwarrior-4-mercenaries/downloads/mw4-sound-extractor) - Sound extraction tool for MechWarrior 4: Mercenaries.

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

### Genki

*Jade Cocoon: Story of the Tamamayu, Jade Cocoon 2.*

- [Jade-Cocoon-Unpacker-Repacker](https://github.com/Meos4/Jade-Cocoon-Unpacker-Repacker) - Tool to unpack and repack DATA.001 archive files from Jade Cocoon (PS1).
- [Jade-Cocoon-2-Unpacker-Repacker](https://github.com/Meos4/Jade-Cocoon-2-Unpacker-Repacker) - Tool to unpack and repack archive files from Jade Cocoon 2 (PS2).
- [Tamamayu-Monogatari-Dennou-Bijutsukan-Unpacker](https://github.com/Meos4/Tamamayu-Monogatari-Dennou-Bijutsukan-Unpacker) - Unpacker for DATA.001 archives from Tamamayu Monogatari Dennou Bijutsukan demo (PS1).

### Grezzo

*Ocarina of Time 3D, Majora's Mask 3D, Luigi's Mansion remake.*

### Human Head Studios

- [Gwynhala's Model Exporter (Rune)](https://www.moddb.com/games/rune/downloads/gwynhalas-model-exporter) - Model exporter for Rune.

### Grezzo

### id Software

- [Doom 3 model import tutorial files](https://www.moddb.com/games/doom-iii/downloads/doom-3-model-import-tutorial-files) - Tutorial files for importing models into Doom 3.
- [Doom 3 Compatibility Tool Mod](https://www.moddb.com/games/doom-iii/downloads/doom-3-compatibility-tool-mod) - Compatibility tool mod for Doom 3.
- [Doom 3 - Quake 3 Map Converter](https://www.moddb.com/games/doom-iii/downloads/doom-3-quake-3-map-converter) - Tool for converting Quake 3 maps to Doom 3 format.
- [Doom 3: ROE (XBOX) .gfc extract](https://www.moddb.com/games/doom-iii/downloads/doom-3-roe-xbox-gfc-extract) - Tool for extracting GFC archive files from Doom 3: Resurrection of Evil (Xbox).
- [Doom maps Converter 1.4](https://www.moddb.com/games/doom-iii/downloads/doom-maps-converter-14) - Map converter for Doom 3 (v1.4).
- [DOOM Audio Tools](https://www.moddb.com/games/doom-4/downloads/doom-audio-tools) - Audio tools for DOOM (2016).
- [Export Font To Doom 3 v1.02](https://www.moddb.com/games/doom-iii/downloads/export-font-to-doom-3-v102) - Tool for exporting fonts to Doom 3 format (v1.02).
- [.GOB & global.d3tfull unpacker (Doom III)](https://www.moddb.com/games/doom-iii/downloads/gob-globald3tfull-unpacker) - Tool for unpacking GOB and global.d3tfull archive files from Doom III.
- [IdTech4 File Unpacker 1.5 (Doom III)](https://www.moddb.com/games/doom-iii/downloads/idtech4-file-unpacker-15) - File unpacker for id Tech 4 engine used in Doom III (v1.5).
- [Lightwave to MD5 converter (Doom III)](https://www.moddb.com/games/doom-iii/downloads/lightwave-to-md5-converter) - Tool for converting Lightwave models to MD5 format used in Doom III.
- [Daikatana to Quake 2 model converter](https://www.moddb.com/games/daikatana/downloads/daikatana-to-quake-2-model-converter) - Tool for converting Daikatana models to Quake 2 format.
- [Quake 1 Model Viewer v0.50 alpha](https://www.moddb.com/games/quake/downloads/quake-1-model-viewer-v050-alpha) - Model viewer for Quake 1 MDL format (v0.50 alpha).
- [Skyboxer - Map-to-Skybox Tool for Quake (1.0)](https://www.moddb.com/games/quake/downloads/skyboxer-a-map-to-skybox-tool-for-quake-10) - Tool for converting Quake maps to skybox format (v1.0).
- [Adjusted MD5 blender exporter (Quake III Arena)](https://www.moddb.com/mods/project-rdx/downloads/adjusted-md5-blender-exporter) - Blender exporter for MD5 model format used in Quake III Arena.
- [Q3-Games Model Tool v1.6.0 (Quake III Arena)](https://www.moddb.com/games/quake-iii-arena/downloads/q3-games-model-tool-v160) - Model tool for Quake III Arena (v1.6.0).
- [RtCW – SDK Editing Tools v1.1 (Return to Castle Wolfenstein)](https://www.moddb.com/mods/rtcw-classic-cooperative-campaign/downloads/rtcw-sdk-editing-tools-v11) - SDK editing tools for Return to Castle Wolfenstein (v1.1).
- [RTCW .bsp to .map Converter (Return to Castle Wolfenstein)](https://www.moddb.com/games/return-to-castle-wolfenstein/downloads/rtcw-bsp-to-map-converter) - BSP to MAP format converter for Return to Castle Wolfenstein.
- [Wolfenstein SPK & MPK Extractor v0.2](https://www.moddb.com/games/wolfenstein/downloads/wolfenstein-spk-mpk-extractor-v02) - Archive extractor for Wolfenstein SPK and MPK formats (v0.2).
- [Blender Terrain scripts (Quake III Arena)](https://www.moddb.com/mods/project-rdx/downloads/blender-terrain-scripts) - Blender terrain scripts for Project RDX mod for Quake III Arena.
- [Blocks II v0.2 Editing Package (Doom II)](https://www.moddb.com/mods/blocks-of-doom-ii/downloads/blocks-ii-v02-editing-package) - Editing package for Blocks of Doom II mod (v0.2).

### Grezzo

- [io_scene_cmb](https://github.com/M-1-RLG/io_scene_cmb) - Blender add-on for Grezzo's "Ctr Model Binary" (CMB) format.
- [noclip.website (OoT3D)](https://github.com/magcius/noclip.website/tree/main/src/OcarinaOfTime3D) - In-browser Ocarina of Time 3D viewer.
- [MeltyTool (Grezzo)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/Grezzo) - Grezzo format viewer/exporter.
- [N3DSCmbViewer](https://github.com/xdanieldzd/N3DSCmbViewer) - Viewer for 3DS CMB models.
- [Scarlet](https://github.com/xdanieldzd/Scarlet) - General purpose 3DS/Vita game tool.
- [Gar/Zar UnPacker](https://gbatemp.net/threads/release-gar-zar-unpacker-v0-1.385264/) - Archive unpacker for Ocarina of Time 3D and Majora's Mask 3D.
- [Switch-Toolbox](https://github.com/KillzXGaming/Switch-Toolbox/tree/master/File_Format_Library/FileFormats/Grezzo) - A tool to edit many video game file formats

### Guerrilla Games

- [ProjectZeroDawn](https://github.com/neptuwunium/ProjectZeroDawn) - File format research and tools for Horizon Zero Dawn.

### LucasArts

- [Grim Fandango model viewer](https://www.moddb.com/games/grim-fandango/downloads/grim-fandango-model-viewer) - Model viewer for Grim Fandango.
- [Easy Saber Editing Script 2.0 (Star Wars: Jedi Academy)](https://www.moddb.com/games/star-wars-jedi-academy/downloads/easy-saber-editing-script-2-0) - Script for editing lightsaber properties in Star Wars: Jedi Academy (v2.0).
- [JK editing manuals (Star Wars Jedi Knight: Dark Forces II)](https://www.moddb.com/games/star-wars-jedi-knight-dark-forces-ii/downloads/jk-editing-manuals) - Editing manuals for Star Wars Jedi Knight: Dark Forces II.
- [JKVersions Tool 3.0 by The_MAZZTer (Star Wars Jedi Knight: Dark Forces II)](https://www.moddb.com/mods/todoa/downloads/jkversions-tool-by-the-mazzter) - Version management tool for Star Wars Jedi Knight: Dark Forces II (v3.0).

### Gust (Koei Tecmo)

- [gust_stuff](https://github.com/eArmada8/gust_stuff) - Modding toolkit for G1M model files used in Gust games (Atelier series).
- [Project-G1M](https://github.com/Joschuka/Project-G1M) - Noesis plugin for importing G1M 3D model format used in Gust and Bandai Namco games.

### Harmonix

*Rock Band, Guitar Hero, Amplitude, Dance Dance Revolution Universe, Frequency, Karaoke Revolution.*

- [LibForge](https://github.com/maxton/LibForge) - Library for reading, writing, and converting Forge engine formats (Rock Band 4, Rock Band VR, FUSER). Handles MIDI, textures (PNG, BMP), models (FBX, OBJ), DTA/DTB, RBmid, RBsong, lipsync, and package files (CON, GP4, PKG). See also [PikminGuts92's fork](https://github.com/PikminGuts92/LibForge) with v2 RB MIDI support, MAGMA v1 milos support, and AMP/RBVR .mid_* file support.
- [pikaxe](https://github.com/PikminGuts92/pikaxe) - Milo engine modding tool for Harmonix games. Supports Guitar Hero 1-2, Guitar Hero Encore: Rocks the 80s, Rock Band series, Dance Central, and other Milo engine titles. Handles DTA, GLTF, and ARK formats across Xbox, Wii, and PS3. Evolution of Mackiloha.
- [DtxCS](https://github.com/maxton/DtxCS) - C# library for parsing and interpreting DTA/DTB scripting format used in Rock Band and Guitar Hero games.
- [CON-Tools](https://github.com/PikminGuts92/CON-Tools) - Create, modify, and combine Rock Band CON files. Convert to Phase Shift, Wii, and PS3 formats.
- [PyMilo](https://github.com/PikminGuts92/PyMilo) - Python library for managing milo files from Harmonix games. Includes GUI and archive extraction utilities. (Archived)
- [BFForever](https://github.com/PikminGuts92/BFForever) - Library for managing and creating game files for BandFuse (PS3, Xbox 360). Handles RIFF files, CELT audio encoding/decoding.
- [Beatles Rock Band Blender plugin](https://www.moddb.com/games/rock-band/downloads/beatles-rock-band-blender-plugin) - Blender plugin for working with Beatles Rock Band assets.
- [amplitools](https://github.com/PikminGuts92/amplitools) - Tools for Amplitude '03.
- [offbeat](https://github.com/PikminGuts92/offbeat) - Rust library for Dance Dance Revolution Universe. Includes DDM to glTF converter.
- [praise-mod](https://github.com/PikminGuts92/praise-mod) - Toolkit for creating Guitar Praise custom content. Converts Clone Hero songs to GP format. Supports ogg vorbis audio.
- [WorshipTools](https://github.com/PikminGuts92/WorshipTools) - Converts Jam Band songs to Clone Hero format. (Archived)
- [ghlcrypt](https://github.com/maxton/ghlcrypt) - C# tool for Guitar Hero Live.
- [re-notes](https://github.com/PikminGuts92/re-notes) - Reverse engineering notes and templates for Harmonix games (Dance Dance Revolution Universe, DJ Hero, Karaoke Revolution) and other titles. Includes 010 Editor templates, Python scripts, and data dumps for BlitzTech, Forge, and Milo engines.

### HAL Laboratory

*Kirby, Super Smash Bros series.*

- [BrawlLib](https://github.com/libertyernie/brawltools) - Library for reading/writing file formats from Super Smash Bros. Brawl and other Wii games.
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

- [ALERT](https://github.com/Tkachov/ALERT) - Amazing Luna Engine Research Tools. Python toolkit for researching and modifying Insomniac Games assets with dat1lib library and web-based Assets Browser.
  - Games: Sunset Overdrive, Marvel's Spider-Man (Remastered, Miles Morales, 2), Marvel's Wolverine, Ratchet & Clank: Rift Apart.
  - Features: Model conversions (.model/.ascii/.gltf), animation application, soundbank audio injection, DSAR archive compression, asset extraction.
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

### Illusion

- [KK-Blender-Porter-Pack](https://github.com/AnalogKnight/KK-Blender-Porter-Pack) - Collection of Koikatsu exporter/importer plugins for Blender covering meshes, armatures, and character data.

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

- [Rex](https://github.com/Jayveer/Rex) - A tool to extract the Stage Dir and Dar files from the game Metal Gear Solid on PS1
- [MGS-KMD-Noesis](https://github.com/Jayveer/MGS-KMD-Noesis) - Noesis Plugin for Metal Gear Solid PS1 Model (KMD) and Animation (OAR) files
- [MGS2 HZX Format](https://github.com/GirianSeed/mgs2/blob/trunk/source/include/fmt_hzx.h) - Documentation for Metal Gear Solid 2 HZX (Hazard) map navigation format including patrol routes, navmesh, triggers, cameras, and spatial zones.
- [MGS-MDL-Noesis](https://github.com/Jayveer/MGS-MDL-Noesis) - Noesis plugin for importing Metal Gear Solid 3 MDL models and MTAR animations.
- [DAR Archive Editor (Metal Gear Solid 2: Sons of Liberty)](https://www.moddb.com/games/metal-gear-solid-2-sons-of-liberty/downloads/dar-archive-editor) - Archive editor for DAR format used in Metal Gear Solid 2: Sons of Liberty.

#### Silent Hill

- [Sparagas/Silent-Hill](https://github.com/Sparagas/Silent-Hill) - Reverse engineering research and documentation for Silent Hill file formats.
- [Murugo/Misc-Game-Research (Silent Hill 2)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Silent%20Hill%202%2B3) - Reverse engineering notes for Silent Hill 2 & 3 (PS2).
- [Silent Hill Museum](https://silenthillmuseum.org/) - Website dedicated to Silent Hill series with file format documentation.
- [laura-a-n-n/silent-hill-museum](https://github.com/laura-a-n-n/silent-hill-museum) - Repository for Silent Hill Museum website with technical documentation.
- [Silent-Hill-2-Enhancements](https://github.com/elishacloud/Silent-Hill-2-Enhancements) - Project to enhance Silent Hill 2 (PC) graphics and audio, includes scripts to build or modify SH2 audio files (SFX, BGM, Dialog).

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
- [BG3-DialogsBinary-Node-Editor](https://github.com/kitmods/BG3-DialogsBinary-Node-Editor) - Node-based editor for Baldur's Gate 3 dialog binary files.

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

### Metropolis Software

#### Gorky 17

- [Gorky 17 *.dat and *.kdt extractor tool](https://www.moddb.com/games/gorky-17/downloads/gorky-17-dat-and-kdt-extractor-tool) - Tool for extracting DAT and KDT archive files from Gorky 17.

### Microsoft Studios / Bungie / Turn 10

#### Halo

- [KSoft](https://github.com/KornnerStudios/KSoft) - Toolkit for working with Halo engine file formats.
- [ekur](https://github.com/TheHaloArchive/ekur) - Blam! engine (Halo) format library and research tools.
- [Reclaimer](https://github.com/Gravemind2401/Reclaimer) - Halo asset extraction and analysis tool supporting Halo 1, 2, 3, 4, Reach, and Online.
- [HaloWarsDocs](https://github.com/HaloMods/HaloWarsDocs) - Documentation and 010 Editor templates for modding Halo Wars 1 and 2.
- [XTraction - Halo 3/ODST texture extractor](https://www.moddb.com/games/halo-3/downloads/xtraction-halo-3-odst-texture-extractor-tool) - Tool for extracting textures from Halo 3 and ODST.
- [Stream Ripping Tools - Halo 3/4/ODST/CEA/HR Game Asset Extractors Converters Kit](https://www.moddb.com/games/halo-2/downloads/stream-ripping-tools-game-asset-extractors-converters-kit) - Asset extraction and conversion toolkit for Halo 3, 4, ODST, CEA, and HR.
- [Halo2 Gravemind Tool Extractor v1.6B](https://www.moddb.com/games/halo-2/downloads/halo2-gravemind-tool-extractor) - Asset extractor for Halo 2 (v1.6B).
- [Bonobo [Version 1.0.0.3] Halo2/3/ODST/Reach Animation Extractor](https://www.moddb.com/games/halo-2/downloads/bonobo-version-1003) - Animation extractor for Halo 2, 3, ODST, and Reach (v1.0.0.3).
- [Composer Halo 4 Audio Extractor](https://www.moddb.com/games/halo-4/downloads/composer-halo-4-audio-extractor) - Audio extraction tool for Halo 4.
- [3ds Max GBX Importer (Halo CE)](https://www.moddb.com/downloads/3ds-max-gbx-importer-halo-ce) - 3DS Max plugin for importing Halo: Combat Evolved GBX model formats.
- [noclip.website (Halo: Combat Evolved)](https://github.com/magcius/noclip.website/tree/main/src/Halo1) - In-browser Halo: Combat Evolved viewer.
- [Halo 2 Xbox Modding Tools](https://www.moddb.com/games/halo-2/downloads/halo-2-xbox-modding-tools) - Modding tools for Halo 2 on Xbox.
- [Halo CE Batch Bitmap Extractor](https://www.moddb.com/downloads/halo-ce-batch-bitmap-extractor) - Batch bitmap extraction tool for Halo: Combat Evolved.

#### Gears of War

- [Gears of War Map Cooker Tool for Newbies](https://www.moddb.com/mods/gears-multiplayer-enhancement-mod/downloads/gears-of-war-map-cooker-tool-for-newbies) - Map cooker tool for Gears of War modding.

#### Forza

- [ForzaTech-extraction-tools](https://github.com/Doliman100/ForzaTech-extraction-tools) - Documentation and tools for ForzaTech .carbin and .modelbin file structures.

#### Age of Empires

- [Audio Modding Guide (AoE2DE)](https://steamcommunity.com/sharedfiles/filedetails/?id=1915891079) - Comprehensive tutorial for audio modding in Age of Empires II: Definitive Edition.
  - Topics: Scenario triggers, SFX replacement, music, voice-overs, taunts, data file editing with Wwise audio system.
  - Tools: Ravioli Tools, vgmstream, Advanced Genie Editor.

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

### Monolith Productions

#### F.E.A.R.

- [F.E.A.R. 3dsmax 7 model import plugin](https://www.moddb.com/games/fear/downloads/3dsmax-7-model-import-plugin) - 3DS Max 7 plugin for importing F.E.A.R. model formats.
- [F.E.A.R. 2 unofficial extraction tools](https://www.moddb.com/games/fear-2/downloads/fear-2-unofficial-extraction-tools) - Unofficial extraction tools for F.E.A.R. 2.
- [FEAR Online 3dsmax script (F.E.A.R. 2)](https://www.moddb.com/games/fear-2/downloads/fear-online-3dsmax-script) - 3DS Max script for F.E.A.R. 2.
- [Video Tutorial: 3DSMax Plugin (F.E.A.R.)](https://www.moddb.com/games/fear/downloads/video-tutorial-3dsmax-plugin) - Video tutorial for using 3DS Max plugin with F.E.A.R.
- [FEAR Database Extractor](https://www.moddb.com/games/fear/downloads/fear-database-extractor) - Database extraction tool for F.E.A.R.
- [FEAR Public Tools v2](https://www.moddb.com/games/fear/downloads/fear-public-tools-v2) - Public modding tools for F.E.A.R. (v2).
- [FEAR Tweaking Tool and Guide](https://www.moddb.com/games/fear/downloads/fear-tweaking-tool-and-guide) - Tweaking tool and guide for F.E.A.R.
- [Lithtech Jupiter Ex FX Decompiler (F.E.A.R.)](https://www.moddb.com/games/fear/downloads/lithtech-jupiter-ex-fx-decompiler) - Decompiler for Lithtech Jupiter Ex FX effects in F.E.A.R.

#### Trespasser

- [Blender 2.6 Trespasser Exporter](https://www.moddb.com/games/trespasser/downloads/blender-26-trespasser-exporter-10) - Blender 2.6 exporter for Trespasser (v1.0).
- [Blender3D Trespasser Exporter 1.0](https://www.moddb.com/games/trespasser/downloads/blender3d-trespasser-exporter-10) - Blender3D exporter for Trespasser models (v1.0).

#### Blood

- [BLOOD ULTIMATE BUNDLE TOOLS KIT](https://www.moddb.com/mods/blood-modern-voxels-pak-for-mappers-and-moders/downloads/blood-ultimate-bundle-tools-kit) - Comprehensive tools kit for Blood game formats.
- [BLOOD UNOFFICIAL TOOLS](https://www.moddb.com/games/blood/downloads/blood-unofficial-tools) - Unofficial tools collection for Blood.
- [Spill Some: The Blood Tool](https://www.moddb.com/games/blood/downloads/spill-some-the-blood-tool) - Tool for working with Blood game files.

#### Blood 2: The Chosen

- [Updated 3dsmax plugin (Blood 2: The Chosen)](https://www.moddb.com/games/blood-2-the-chosen/downloads/updated-3dsmax-plugin) - Updated 3DS Max plugin for Blood 2: The Chosen.
- [Blood 2 Modding tools](https://www.moddb.com/games/blood-2-the-chosen/downloads/blood-2-modding-tools) - Modding tools for Blood 2: The Chosen.
- [Blood 2 Toolset 64 bit fix](https://www.moddb.com/games/blood-2-the-chosen/downloads/blood-2-toolset-64-bit-fix) - 64-bit compatibility fix for Blood 2 toolset.
- [Milkshape ABC Plugin (Blood 2: The Chosen)](https://www.moddb.com/games/blood-2-the-chosen/downloads/milkshape-abc-plugin) - Milkshape 3D plugin for Blood 2: The Chosen ABC model format.

#### No One Lives Forever

- [Lithtech Jupiter Maya/3dsmax plugins (No One Lives Forever 2)](https://www.moddb.com/games/no-one-lives-forever-2-a-spy-in-harm/downloads/lithtech-jupiter-maya3dsmax-plugins) - Maya and 3DS Max plugins for Lithtech Jupiter engine used in No One Lives Forever 2.
- [Lithtech 2.2 toolset (No One Lives Forever)](https://www.moddb.com/games/no-one-lives-forever/downloads/lithtech-22-toolset) - Toolset for Lithtech 2.2 engine used in No One Lives Forever.
- [NOLF Tools (No One Lives Forever)](https://www.moddb.com/games/no-one-lives-forever/downloads/nolf-tools) - Tools for working with No One Lives Forever file formats.
- [No One Lives Forever 2 Toolkit](https://www.moddb.com/games/no-one-lives-forever-2-a-spy-in-harm/downloads/no-one-lives-forever-2-toolkit) - Toolkit for No One Lives Forever 2.

#### Shogo: Mobile Armor Division

- [Shogo Mobile Armor Division Modding Tools](https://www.moddb.com/games/shogo-mobile-armor-division/downloads/shogo-mobile-armor-division-modding-tools) - Modding tools for Shogo: Mobile Armor Division.
- [Shogo tools 64 bit](https://www.moddb.com/games/shogo-mobile-armor-division/downloads/shogo-tools-64-bit) - 64-bit tools for Shogo: Mobile Armor Division.

### Oddworld Inhabitants

- [Asset Tool (Oddworld: Abe's Exoddus)](https://www.moddb.com/games/oddworld-abes-exoddus/downloads/asset-tool) - Tool for working with assets from Oddworld: Abe's Exoddus.
- [Sprite / CAM Extractor (Oddworld: Abe's Exoddus)](https://www.moddb.com/games/oddworld-abes-exoddus/downloads/sprite-cam-extractor) - Extractor for sprite and CAM files from Oddworld: Abe's Exoddus.

### Naughty Dog

#### Crash Bandicoot 1-3 & CTR

- [Crash-Bandicoot-Resources](https://github.com/Helias/Crash-Bandicoot-Resources) - Comprehensive collection of resources for Crash Bandicoot file formats and reverse engineering. Covers N. Sane Trilogy, Twinsanity, Crash Team Racing, Crash Bash, and original PS1 trilogy. Includes documentation for extracting/modifying PAK archives, IGZ models, NSD/NSF files, plus links to 30+ specialized tools, character mods, decompilation projects, and modding frameworks.
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

#### New Super Mario Bros Wii

- [BerryBush](https://github.com/hayden0729/berrybush) - Blender addon focused on importing and exporting BRRES models.
  - Games: New Super Mario Bros. Wii (BRRES assets including characters, levels, props).
  - Features: BRRES importer/exporter, render engine, material editing interface, and verifier to catch malformed model data before export.

#### Zelda

*See also [JSYSTEM](#jsystem-gamecubewii) for Wind Waker and Twilight Princess.*

- [CloudModding OoT Wiki](https://wiki.cloudmodding.com/oot/Main_Page) - Comprehensive technical wiki for Ocarina of Time with 331+ articles covering actors, objects, scenes, file formats, animations, cutscenes, audio, textures, collision, decompilation project, and modding guides.
- [WindEditor](https://github.com/Sage-of-Mirrors/WindEditor) - Map viewer/editor for The Legend of Zelda: The Wind Waker.
- [bfntoolkit](https://github.com/NerduMiner/bfntoolkit) - Extract and repack BFN font files from The Legend of Zelda: The Wind Waker (GameCube). Generates PNG images and JSON metadata. Requires separate BTI conversion tool for repacking.
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
- [hactool](https://github.com/SciresM/hactool) - Tool to view information about, decrypt, and extract Nintendo Switch file formats including NCA, XCI, PFS0, HFS0, RomFS, ExeFS, save data, and more.
- [WiiUTools](https://github.com/NWPlayer123/WiiUTools) - Collection of Python utilities for working with Wii U file formats including IPK packages, RPX executables, SARC archives, and texture editing (TexHaxU/TexHaxU2).
- [Syroot.NintenTools.Bfres](https://gitlab.com/Syroot/NintenTools) - Library for reading/writing Nintendo BFRES model format (Wii U).
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

### BioWare

#### Dragon Age: Origins

- [Dragon Age Origins 3dsmax Import Export script](https://www.moddb.com/games/dragon-age-origins/downloads/dragon-age-origins-3dsmax-import-export-script) - 3DS Max script (v5.38) for importing and exporting models from Dragon Age: Origins.

#### Knights of the Old Republic

- [Kotor Tool 1](https://www.moddb.com/games/star-wars-knights-of-the-old-republic/downloads/kotor-tool-1) - Tool for working with Star Wars: Knights of the Old Republic file formats.

### Obsidian Entertainment

#### Neverwinter Nights 2

- [NWN2MDK](https://github.com/Arbos/nwn2mdk) - Neverwinter Nights 2 Modding & Development Kit. Includes a Blender add-on for meshes/animations and command-line converters.

### Panic

- [playdate-reverse-engineering](https://github.com/cranksters/playdate-reverse-engineering) - Reverse engineering notes and tools for Playdate handheld console.
- [noclip.website (A Short Hike)](https://github.com/magcius/noclip.website/tree/main/src/AShortHike) - In-browser A Short Hike viewer.

### Petroglyph Games

- [alo/ala max importer exporter (Star Wars: Empire at War)](https://www.moddb.com/groups/starwars-empire-at-war-fan-mod-group/downloads/aloala-max-importer-exporter) - 3DS Max importer/exporter for ALO/ALA formats used in Star Wars: Empire at War.
- [Blender-ALAMAO-Plugin for 4.2LTS (Star Wars: Empire at War: Forces of Corruption)](https://www.moddb.com/games/star-wars-empire-at-war-forces-of-corruption/downloads/blender-alamao-plugin-for-42lts) - Blender plugin for ALAMAO format in Star Wars: Empire at War: Forces of Corruption.
- [Grey Goo Official Asset Adding Tools](https://www.moddb.com/games/grey-goo/downloads/grey-goo-asset-adding-tools) - Official asset adding tools for Grey Goo.
- [3DS Max 7 and 8 Plugin for Map Editor (Star Wars: Empire At War)](https://www.moddb.com/games/star-wars-empire-at-war/downloads/3ds-max-7-and-8-plugin-for-map-editor) - 3DS Max plugin for map editor in Star Wars: Empire At War.
- [Star Wars Empire At War FOC DDS Tool](https://www.moddb.com/games/star-wars-empire-at-war-forces-of-corruption/downloads/star-wars-empire-at-war-foc-dds-tool) - DDS texture tool for Star Wars: Empire at War: Forces of Corruption.
- [Star Wars Empire At War FOC DDS Viewer & Thumbplug _tga1.10](https://www.moddb.com/games/star-wars-empire-at-war-forces-of-corruption/downloads/star-wars-empire-at-war-foc-dds-viewer-thumbplug-tga110) - DDS viewer and thumbnail plugin for Star Wars: Empire at War: Forces of Corruption (v1.10).
- [Star Wars Empire At War FOC Alamo Object Importer 1.2](https://www.moddb.com/games/star-wars-empire-at-war-forces-of-corruption/downloads/alamo-object-importer-12) - Alamo object importer for Star Wars: Empire at War: Forces of Corruption (v1.2).
- [Star Wars Empire At War FOC Alamo Viewer 1.2](https://www.moddb.com/games/star-wars-empire-at-war-forces-of-corruption/downloads/alamo-viewer-12) - Alamo format viewer for Star Wars: Empire at War: Forces of Corruption (v1.2).

### PlatinumGames

- [platinumgames_stuff](https://github.com/Timo654/platinumgames_stuff) - Collection of Python scripts for PlatinumGames titles including Bayonetta 3 and Metal Gear Rising: Revengeance.

#### Bayonetta

- [bayonetta_patch](https://github.com/Kerilk/bayonetta_patch) - Patching system for modifying Bayonetta executable.
- [noesis_bayonetta_pc](https://github.com/Kerilk/noesis_bayonetta_pc) - Noesis plugin for PlatinumGames models/animations.
  - Games: Bayonetta series (1-3, Origins), Nier Automata, Metal Gear Rising Revengeance, MadWorld, The Legend of Korra, TMNT Mutants in Manhattan, Transformers Devastation, Starfox Zero, Astral Chain, The Wonderful 101, Vanquish, Anarchy Reigns, Babylon's Fall.
- [bayonetta_tools](https://github.com/Kerilk/bayonetta_tools) - Ruby toolkit for extracting/converting PlatinumGames assets (models, textures, animations). Supports Bayonetta 1-3, NieR: Automata, Astral Chain.

#### Nier: Automata / Replicant

- [kaine](https://github.com/neptuwunium/kaine) - C# library for working with Nier Replicant 1.22 file formats.
- [replicant_templates](https://github.com/WoefulWolf/replicant_templates) - 010 Editor binary templates for NieR Replicant ver.1.22474487139 file formats including ARC archives, PACK containers, BXON files, and various model/material/texture formats.
- [replicant_toolkit](https://github.com/WoefulWolf/replicant_toolkit) - Toolkit for working with NieR Replicant file formats.
- [Blender2NieR](https://github.com/WoefulWolf/NieR2Blender2NieR) - Blender addon for exporting WMB/WTP/WTA/DAT/DTT formats to NieR games.
- [NieR2Blender](https://github.com/WoefulWolf/NieR2Blender_2_8) - Blender addon for importing NieR Automata and Replicant models.
- [Replicant2Blender](https://github.com/WoefulWolf/Replicant2Blender) - Blender addon for importing NieR Replicant ver.1.22 mesh packs and textures into Blender (alpha).

### Primal Software

#### The I of the Dragon

- [Archive files plugin for Noesis (The I of the Dragon)](https://www.moddb.com/games/the-i-of-the-dragon/downloads/archive-files-plugin-for-noesis-v001) - Noesis plugin for importing archive files from The I of the Dragon.

### Polytron

- [noclip.website (Fez)](https://github.com/magcius/noclip.website/tree/main/src/Fez) - In-browser Fez viewer.

### Mithis Entertainment

#### Nexus: The Jupiter Incident

- [Nexus Mesh Importer](https://www.moddb.com/games/nexus-the-jupiter-incident/downloads/nexus-mesh-importer) - Mesh importer for Nexus: The Jupiter Incident.
- [Nexus Texture Converter](https://www.moddb.com/games/nexus-the-jupiter-incident/downloads/nexus-texture-converter) - Texture converter for Nexus: The Jupiter Incident.

### Punchline

- [Murugo/Misc-Game-Research (Rule of Rose)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Rule%20of%20Rose) - Reverse engineering notes for Rule of Rose (PS2).

### People Can Fly

#### Painkiller

- [Painkiller 3ds Max Plugins (Upd270522)](https://www.moddb.com/games/painkiller/downloads/painkiller-3ds-max-plugins) - 3DS Max plugins for Painkiller (updated 270522).
- [HavokXML2HKE converter for Ragdoll physics 3ds Max (Painkiller)](https://www.moddb.com/games/painkiller/downloads/havokxml2hke-converter-for-ragdoll-physics) - Havok XML to HKE converter for ragdoll physics in 3DS Max (updated 260117).
- [PainFull Extractor v1.3.2 (Painkiller)](https://www.moddb.com/games/painkiller/downloads/painfull-extractor-v132) - Archive extractor for Painkiller (v1.3.2).
- [Painkiller converters mpk/dat to ASE and ASE to mpk/dat](https://www.moddb.com/games/painkiller/downloads/painkiller-converters-mpk-to-ase-and-ase-to-mpk) - Converters for Painkiller MPK/DAT and ASE model formats.

### Polyphony Digital

- [PDTools](https://github.com/Nenkai/PDTools) - Utilities for extracting and modifying Gran Turismo game files.

### RAD Game Tools

- [Knit](https://github.com/neptuwunium/Knit) - Managed C# library for reading Granny 2 3D model files used in many games.

### Rebel Act

- [3D tools for Severance v2.5](https://www.moddb.com/games/severance-blade-of-darkness/downloads/3d-tools-for-severance-v25) - 3D tools for Severance: Blade of Darkness (v2.5).
- [3D Tools & Scripts v1.2.1](https://www.moddb.com/games/severance-blade-of-darkness/downloads/3d-tools-scripts-v121) - 3D tools and scripts for Severance: Blade of Darkness (v1.2.1).
- [Blade of Darkness Mod Tools & Tutorials](https://www.moddb.com/games/severance-blade-of-darkness/downloads/blade-of-darkness-mod-tools-tutorials) - Mod tools and tutorials for Severance: Blade of Darkness.
- [Blade Tools English. Severance - SDK](https://www.moddb.com/games/severance-blade-of-darkness/downloads/blade-tools-english-severance-sdk) - English SDK tools for Severance: Blade of Darkness.
- [Blade Tools Spanish. Blade SDK](https://www.moddb.com/games/severance-blade-of-darkness/downloads/blade-tools-spanish-blade-sdk) - Spanish SDK tools for Severance: Blade of Darkness.

### Rebellion Developments

- [AvP Editing Tools](https://www.moddb.com/games/aliens-vs-predator/downloads/avp-editing-tools) - Editing tools for Aliens versus Predator (Classic).
- [AVP Gold Tools and Source Code (Aliens versus Predator - Classic)](https://www.moddb.com/games/aliens-vs-predator/downloads/avp-gold-tools-and-source-code) - Gold edition tools and source code for Aliens versus Predator (Classic).

#### Aliens vs. Predator 2

- [AVP2 official tools](https://www.moddb.com/games/aliens-vs-predator-2/downloads/avp2-official-tools) - Official modding tools for Aliens vs. Predator 2.

#### Aliens vs. Predator (2010)

- [Asura Engine Extractor (Aliens vs. Predator 2010)](https://www.moddb.com/games/avp2010/downloads/asura-engine-extractor) - Archive extractor for Asura Engine used in Aliens vs. Predator (2010).

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

### Runic Games

#### Torchlight

- [Nimet - Ogre3D Mesh Viewer (Torchlight)](https://www.moddb.com/games/torchlight/downloads/nimet-ogre3d-mesh-viewer) - Ogre3D mesh viewer for Torchlight models.
- [Cliffside tile set build 1.0.00 (Torchlight)](https://www.moddb.com/games/torchlight/downloads/cliffside-tile-set-build-1000) - Tile set for Torchlight level creation (build 1.0.00).

#### Torchlight II

- [Modified PAK Extractor Tool](https://www.moddb.com/games/torchlight-ii/downloads/modified-pak-extractor-tool-by-jarcho) - Tool for extracting PAK archive files from Torchlight II.
- [GUTS Tools and Assets](https://www.moddb.com/games/torchlight-ii/downloads/guts-tools-and-assets) - GUTS (Torchlight II editor) tools and assets.

### 1C Company / Best Way

#### Men of War

- [Men of War 3DS Max Exporter Tools](https://www.moddb.com/games/men-of-war/downloads/men-of-war-3ds-max-exporter-tools) - 3DS Max exporter for Men of War model formats.

### Ironclad Games / Stardock

#### Sins of a Solar Empire

- [Sins 3D Max Import export](https://www.moddb.com/games/sins-of-a-solar-empire-rebellion/downloads/sins-3d-max-impotrt-export) - 3DS Max import/export plugin for Sins of a Solar Empire model formats.
- [sins TXT Tools with export (Sins of a Solar Empire: Rebellion)](https://www.moddb.com/games/sins-of-a-solar-empire-rebellion/downloads/sins-txt-tools-with-export) - TXT file tools with export functionality for Sins of a Solar Empire: Rebellion.
- [Forge Tools (Sins of a Solar Empire)](https://www.moddb.com/games/sins-of-a-solar-empire/downloads/forge-tools) - Forge tools for Sins of a Solar Empire.
- [Map Conversion (Sins of a Solar Empire)](https://www.moddb.com/games/sins-of-a-solar-empire/downloads/map-conversion) - Map conversion tool for Sins of a Solar Empire.

### Radical Entertainment

- [scarface-p3d](https://github.com/aap/scarface-p3d) - P3D format tools for "Scarface: The World is Yours".

### Reflections Interactive

- [driver-tools](https://github.com/Fireboyd78/driver-tools) - Modding tools for DRIV3R, Driver: Parallel Lines, and Driver: San Francisco.
- [REDRIVER2](https://github.com/OpenDriver2/REDRIVER2) - Driver 2 Playstation game reverse engineering effort.
- [Driver model tools](https://www.moddb.com/games/driver-you-are-the-wheelman/downloads/driver-model-tools) - Model tools for Driver: You Are the Wheelman.

### Riot Games

- [yordle](https://github.com/neptuwunium/yordle) - File format research project for League of Legends.
- [MindCorpViewer](https://github.com/autergame/MindCorpViewer?tab=readme-ov-file) - Model viewer for League of Legends SKN/SKL/DDS files [archived].
- [MindCorpViewer-Rust](https://github.com/autergame/MindCorpViewer-Rust) - Modern Rust rewrite of League of Legends model viewer with improved performance.

### Santa Monica Studio

- [god_of_war_browser](https://github.com/mogaika/god_of_war_browser) - WebGL-based in-browser viewer for God of War I/II (PS2/PS3/Vita) models and textures.
- [God of War 2018 PS4 Tools](https://forum.xentax.com/viewtopic.php?f=16&t=22897) - XeNTaX forum discussion and extraction tools for God of War (2018) on PlayStation 4. *(Link archived/dead)*

### Sega

- [PSO2 Tools](https://github.com/dummycount/blender_pso2_tools) - Blender add-on for Phantasy Star Online 2 assets (`.aqp`, `.aqn`, ICE archives). Features model search, archive browsing, and automatic texture assignment.

#### Creative Assembly

##### Alien: Isolation

- [Alien Isolation Animation Exporter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-animation-exporter) - Tool for exporting animations from Alien: Isolation.
- [Alien Isolation Model Exporter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-model-exporter) - Tool for exporting models from Alien: Isolation.
- [Alien Isolation Texture Exporter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/texture-extractor) - Texture extraction tool for Alien: Isolation.
- [Alien Isolation Audio Converter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-audio-converter) - Audio conversion tool for Alien: Isolation.
- [Alien Isolation BML Converter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-bml-converter) - BML format converter for Alien: Isolation.
- [Alien Isolation UI Mod Tool](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-ui-mod-tool) - UI modification tool for Alien: Isolation.

##### Total War Series

- [Texture 2 DDS Converter (Medieval II: Total War)](https://www.moddb.com/games/medieval-2-total-war/downloads/texture-2-dds-converter) - Texture converter for Medieval II: Total War DDS format.
- [Vercengetorix's CAS Import/Export (Medieval II: Total War)](https://www.moddb.com/games/medieval-2-total-war/downloads/vercengetorix-s-cas-import-export) - CAS (model) format import/export tool for Medieval II: Total War.
- [CAS Exporter (Medieval II: Total War)](https://www.moddb.com/games/medieval-2-total-war/downloads/cas-exporter) - CAS model exporter for Medieval II: Total War.
- [Community Modding Framework (Total War: Warhammer II)](https://www.moddb.com/games/total-war-warhammer-ii/downloads/community-modding-framework-1104) - Modding framework for Total War: Warhammer II (v1.10.4).
- [Symphony Sound Packer (Empire: Total War)](https://www.moddb.com/mods/foothold-in-india/downloads/symphony-sound-packer) - Sound packing tool for Empire: Total War modders.
- [Aqua-Toolset](https://github.com/Shadowth117/Aqua-Toolset) - Toolkit primarily for Phantasy Star Online 2 file formats.
- [NaomiMod/games-ExtractTools](https://github.com/NaomiMod/games-ExtractTools) - QuickBMS scripts to extract NaomiLib models from Dreamcast/Naomi arcade games. Supports Dead or Alive 2, Initial D3, Mortal Kombat 4, Super Monkey Ball, Virtua Tennis, Castlevania Resurrection, Rent-A-Hero, and more.
- [NaomiLib Blender Addon](https://github.com/NaomiMod/blender-NaomiLib) - Blender addon for importing NaomiLib 3D models from SEGA Dreamcast and Naomi arcade games (Crazy Taxi, Dead or Alive 2, Marvel vs. Capcom 2, Shenmue 2, Virtua Tennis, and more).
- [PCSX2 Patches](https://github.com/PCSX2/pcsx2_patches) - Game patches for PCSX2 emulator including widescreen and interlacing fixes.
- [noclip.website (Jet Set Radio)](https://github.com/magcius/noclip.website/tree/main/src/JetSetRadio) - In-browser Jet Set Radio viewer.

### Sonic Team

#### Sonic Adventure

- [SCHG:Sonic_Adventure](https://info.sonicretro.org/SCHG:Sonic_Adventure) - Sonic Community Hacking Guide documentation for Sonic Adventure.
- [sadtools](https://github.com/FraGag/sadtools) - Command-line tools for Sonic Adventure file formats.
- [sa_tools](https://github.com/X-Hax/sa_tools) - Modding toolkit for Sonic Adventure series. Supports Sonic Adventure DX (SADX) and Sonic Adventure 2 PC (SA2PC).
- [SonicAdventureBlenderIO](https://github.com/X-Hax/SonicAdventureBlenderIO) - Blender 4.0+ add-on for exporting Sonic Adventure 1 & 2 3D formats (`.nj`, `.gj`, `.njm`, `.nja`).

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

- [mkpsxiso](https://github.com/Lameguy64/mkpsxiso) - Tool to build and extract PlayStation 1 CD images from XML. Modern cross-platform replacement for BUILDCD from PsyQ SDK. Supports mixed-mode CD-XA with audio/video streams.
- [LibOrbisPkg](https://github.com/OpenOrbis/LibOrbisPkg) - Library, GUI, and CLI tools for creating, inspecting, and modifying PlayStation 4 PKG, SFO, PFS files. Open-source alternative to Sony SDK tools.
- [LibreFios](https://github.com/neptuwunium/LibreFios) - C# library for working with PlayStation PSARC archive format.

### Square Enix

#### Hitman

- [HiTMAN Archive Manager](https://www.moddb.com/games/hitman-world-of-assassination/downloads/hitman-archive-manager) - Archive manager for HiTMAN game files.

- [OpenKH](https://github.com/OpenKH/OpenKh) - Comprehensive reverse-engineering toolkit for Kingdom Hearts series. Handles MDLX/PMO models, PAM/ANB animations, TXA textures, map data, battle configs, and message files. Includes 50+ specialized editors and converters. Supports KH1, KH2, Birth by Sleep, Re:Coded, and Dream Drop Distance.
- [BBSPluginNoesis](https://github.com/Truthkey/BBSPluginNoesis) - Updated Noesis plugin for Kingdom Hearts Birth by Sleep working with modern versions of Visual Studio.
- [WOFFington](https://github.com/neptuwunium/WOFFington) - File format research and tools for World of Final Fantasy.
- [heretic](https://github.com/adamrt/heretic) - Modding toolkit for Final Fantasy Tactics.
- [KH-ReCOM-Tools](https://github.com/Murugo/KH-ReCOM-Tools) - Set of experimental tools for Kingdom Hearts Re:Chain of Memories (PS2).
- [Murugo/Misc-Game-Research (Kingdom Hearts II)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Kingdom%20Hearts%20II%20Final%20Mix) - Reverse engineering notes for Kingdom Hearts II Final Mix (PS2).
- [Murugo/Misc-Game-Research (Musashi: Samurai Legend)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Musashi%20Samurai%20Legend) - Reverse engineering notes for Musashi: Samurai Legend (PS2).
- [kh1](https://github.com/ethteck/kh1) - WIP Decompilation of Kingdom Hearts (PS2, JP).
- [noclip.website (Final Fantasy X)](https://github.com/magcius/noclip.website/tree/main/src/FinalFantasyX) - In-browser Final Fantasy X viewer.
- [Final Fantasy X HD translation tools](https://www.moddb.com/games/final-fantasy-x/downloads/final-fantasy-x-hd-translation-tools) - Translation tools for Final Fantasy X HD.
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

### Supercell

- [gltf-Supercell-IO](https://github.com/Daniil-SV/gltf-Supercell-IO) - Custom Supercell glTF 2.0 importer/exporter for Blender 5.0+ supporting Android/iOS games.

### SuperTuxKart

- [STK Blender Addons](https://github.com/supertuxkart/stk-blender) - Exporter/importer suite for SuperTuxKart `SPM` meshes and `Antarctica` engine assets.

### Telltale Games

- [Telltale-Texture-Tool](https://github.com/Telltale-Modding-Group/Telltale-Texture-Tool) - GUI application for converting `.d3dtx` files to PNG, DDS, TGA, and vice versa.
- [Telltale-Script-Editor](https://github.com/Telltale-Modding-Group/Telltale-Script-Editor) - Unofficial script editor for Telltale Tool games.
- [D3DMESH-Converter](https://github.com/Telltale-Modding-Group/D3DMESH-Converter) - Tool for converting `.d3dmesh` models to standard formats and back.
- [ttarch-docs](https://github.com/Telltale-Modding-Group/ttarch-docs) - Documentation and guide for reading Telltale Archive files programmatically.
- [IMAP-Editor](https://github.com/Telltale-Modding-Group/IMAP-Editor) - Editor for `.imap` files used in Telltale games.
- [Unity_WBOX_Editor](https://github.com/Telltale-Modding-Group/Unity_WBOX_Editor) - Unity-based tool for importing and generating `.wbox` navigation mesh files.
- [TelltaleGames_D3DMesh_Importer](https://github.com/WeaselOnaStick/TelltaleGames_D3DMesh_Importer) - Blender add-on for importing `D3DMesh` models from Telltale titles.

### GSC Game World

#### S.T.A.L.K.E.R.

- [Geometry Decompiler plugin for 3dsmax](https://www.moddb.com/games/stalker/downloads/geometry-decompiler-plugin-for-3dsmax) - 3DS Max plugin for decompiling geometry files from S.T.A.L.K.E.R. Shadow of Chernobyl.
- [STALKER game archives unpacker](https://www.moddb.com/mods/old-good-stalker-evolution/downloads/stalker-game-archives-unpacker) - Tool for unpacking game archive files from S.T.A.L.K.E.R. series.
- [STALKER Extractor](https://www.moddb.com/games/stalker/downloads/stalker-extractor) - Archive extraction tool for S.T.A.L.K.E.R. Shadow of Chernobyl.
- [S.T.A.L.K.E.R Mod Tool](https://www.moddb.com/games/stalker/downloads/stalker-mod-tool) - Modding tool for S.T.A.L.K.E.R. Shadow of Chernobyl.
- [Unpack Pack xr files Stalker (S.T.A.L.K.E.R.: Call of Pripyat)](https://www.moddb.com/games/stalker-call-of-pripyat/downloads/unpack-pack-xr-files-stalker) - Tool for unpacking and packing XR archive files in S.T.A.L.K.E.R.: Call of Pripyat.
- [X-ray game asset tools pack FINAL](https://www.moddb.com/games/stalker/downloads/x-ray-game-asset-tools-pack-final) - Comprehensive asset tools pack for S.T.A.L.K.E.R. Shadow of Chernobyl X-ray engine formats.
- [Clear Sky: Game Database Unpacker](https://www.moddb.com/games/stalker/downloads/clear-sky-game-database-unpacker) - Database unpacker for S.T.A.L.K.E.R.: Clear Sky.
- [STALKER utilities pack](https://www.moddb.com/games/stalker/downloads/stalker-utilities-pack) - Collection of utilities for working with S.T.A.L.K.E.R. game files.
- [Updated Milkshape plugin](https://www.moddb.com/games/stalker/downloads/updated-milkshape-plugin) - Milkshape 3D plugin for S.T.A.L.K.E.R. Shadow of Chernobyl model formats.
- [Database converter (S.T.A.L.K.E.R.: Call of Pripyat)](https://www.moddb.com/mods/call-of-chernobyl/downloads/cop-coc-db-converter) - Database converter for S.T.A.L.K.E.R.: Call of Pripyat modding (v1.4+).
- [Extractor de archivos para S.T.A.L.K.E.R.: Shadow of Chernobyl](https://www.moddb.com/games/stalker/downloads/extractor-de-archivos-para-stalker-shadow-of-chernobyl) - Archive extractor for S.T.A.L.K.E.R.: Shadow of Chernobyl.
- [General X Ray SDK CS-CoP Tools (S.T.A.L.K.E.R.: Call of Pripyat)](https://www.moddb.com/games/stalker-call-of-pripyat/downloads/general-x-ray-sdk-tools) - X-Ray SDK tools for S.T.A.L.K.E.R.: Call of Pripyat.

### Terminal Reality

#### BloodRayne

- [br2proj](https://github.com/PavelSharp/br2proj) - BloodRayne 2 Blender add-on for importing `.tex` textures, `.smb` models, and `.bfm`/`.skb` skeletal meshes.

### THQ / Rainbow Studios

#### Cars

- [carsraceorama](https://github.com/leeao/carsraceorama) - Noesis plugin for Cars Mater-National and Cars Race-O-Rama. Model importer/exporter supporting multiple platform formats: XNG (Xbox 360/PC), P3G (PS3), GCG (Wii/GameCube), DXG (PC/Xbox), PSG (PS2), SLT (text).

#### MX vs ATV

- [3ds Export script (MX vs ATV Reflex)](https://www.moddb.com/games/mx-vs-atv-reflex/downloads/3ds-export-script) - 3DS export script for MX vs ATV Reflex.

### 3D Realms

#### Duke Nukem 3D

- [Landscaping Tools (Duke Nukem 3D)](https://www.moddb.com/games/duke-nukem-3d/downloads/landscaping-tools) - Landscaping tools for Duke Nukem 3D level editing.
- [Duke Nukem 3D source code](https://www.moddb.com/games/duke-nukem-3d/downloads/duke-nukem-3d-source-code) - Source code for Duke Nukem 3D.

#### Duke Nukem: Manhattan Project

- [Duke Nukem Manhattan Project Mesh & Bones Editing Tool](https://www.moddb.com/games/duke-nukem-manhattan-project/downloads/duke-nukem-manhattan-project-mesh-bones-editing-tool) - Tool for editing mesh and bone data from Duke Nukem: Manhattan Project.

#### Duke Nukem Forever (2001)

- [Blender to CPJ Plugin for DNF2001](https://www.moddb.com/mods/dnf2001-restoration-project/downloads/blender-to-cpj-plugin-for-dnf2001) - Blender plugin for converting models to CPJ format for Duke Nukem Forever (2001).
- [Updated Blender to CPJ Plugin (Duke Nukem Forever 2001)](https://www.moddb.com/mods/dnf2001-restoration-project/downloads/updated-blender-to-cpj-plugin) - Updated Blender plugin for converting models to CPJ format for Duke Nukem Forever (2001).

#### The Outforce

- [Outforce meshes extractor](https://www.moddb.com/games/the-outforce/downloads/outforce-meshes-extractor) - Tool for extracting mesh files from The Outforce.
- [The Outforce Box extractor tool](https://www.moddb.com/games/the-outforce/downloads/the-outforce-box-extractor-tool) - Archive extractor for The Outforce BOX format files.

### Techland

- [Call of Juarez: Bound In Blood - Map Pak Tool](https://www.moddb.com/mods/cojbib-map-pak-tool/downloads/call-of-juarez-bound-in-blood-map-pak-tool) - Tool for working with map PAK files from Call of Juarez: Bound In Blood.

### Thekla Inc

- [noclip.website (The Witness)](https://github.com/magcius/noclip.website/tree/main/src/TheWitness) - In-browser The Witness viewer.
- [Braid Editor Universe Tools](https://www.moddb.com/games/braid/downloads/braid-editor-universe-tools) - Editor tools for Braid.

### Slitherine / Proxy Studios

- [Blender Gladius Addon v1.1 (Warhammer 40,000: Gladius - Relics of War)](https://www.moddb.com/mods/blender-gladius-addon/downloads/blender-gladius-addon-v11) - Blender addon for Warhammer 40,000: Gladius - Relics of War.

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
- [Hawx Model Tool 1.04 (Tom Clancy's H.A.W.X.)](https://www.moddb.com/games/tom-clancys-hawx/downloads/hawx-model-tool-104) - Model tool for Tom Clancy's H.A.W.X. (v1.04).
- [Complete UMP40 Source Code and Assets (Tom Clancy's Rainbow Six 3: Raven Shield)](https://www.moddb.com/mods/raven-shield-software-development-kit/downloads/complete-ump40-source-code-and-assets) - Complete source code and assets for UMP40 weapon in Rainbow Six 3: Raven Shield.
- [Damage Triggers - mapping tool (Tom Clancy's Rainbow Six 3: Raven Shield)](https://www.moddb.com/games/tom-clancys-rainbow-six-3-raven-shield/downloads/damage-triggers-mapping-tool) - Mapping tool for damage triggers in Rainbow Six 3: Raven Shield.
- [Flashlights for enemies - mapping tool (Tom Clancy's Rainbow Six 3: Raven Shield)](https://www.moddb.com/games/tom-clancys-rainbow-six-3-raven-shield/downloads/flashlights-for-enemies-mapping-tool) - Mapping tool for adding flashlights to enemies in Rainbow Six 3: Raven Shield.
- [.forge extractor/replacer by Turfster (Assassin's Creed)](https://www.moddb.com/mods/aci-texmod-clothes-mod/downloads/forge-extractorreplacer-by-turfster) - Tool for extracting and replacing files in .forge archives used in Assassin's Creed.

#### Anno 1800

- [Anno 1800 Mod Loader](https://github.com/magicalcookie/anno1800-mod-loader) - Mod loader for Anno 1800 that supports loading of unpacked RDA files, XML auto merging and DLL based mods.
- [Modding Tools for Anno](https://marketplace.visualstudio.com/items?itemName=JakobHarder.anno-modding-tools) - Visual Studio Code extension with utilities to build Anno 1800 mods.

### Bethesda

*The Elder Scrolls, Fallout series, and Starfield.*

- [xEdit](https://tes5edit.github.io) - Advanced graphical module editor and conflict detector for Bethesda games.
- [F2 TOOLS PAK BY LEONARDO (Fallout 2)](https://www.moddb.com/games/fallout-2/downloads/f2-tools-pak-by-leonardo) - Collection of tools for working with Fallout 2 file formats.
- [Fallout2 FRM converter v 2.0](https://www.moddb.com/games/fallout-2/downloads/fallout2-frm-converter-v-20) - Converter for Fallout 2 FRM (frame) format files (v2.0).
- [Wrye Bash](https://wrye-bash.github.io) - Swiss army knife for modding Bethesda games with features including mod installation, conflict manager, load order manager and automatic merging.
- [Synthesis](https://github.com/Mutagen-Modding/Synthesis) - Framework and GUI to empower people to create mods via code instead of by hand, mainly used to create patches.
- [Spriggit](https://github.com/Mutagen-Modding/Spriggit) - Tool to facilitate converting Bethesda plugin files to a text based format that can be stored in Git.
- [ck-cmd](https://github.com/aerisarn/ck-cmd) - Command-line helper for executing some Creation Kit/Engine commands.
- [hkxc](https://www.nexusmods.com/skyrimspecialedition/mods/126214) - CLI tool to convert between x86/x64 HKX and XML animation files.
- [HKX Conversion Tool](https://www.nexusmods.com/skyrimspecialedition/mods/128839) - hkxc Windows GUI for converting between HKX and XML animations files.
- [hkxPoser](https://www.nexusmods.com/skyrimspecialedition/mods/11783) - .hkx animation file editor.
- [DDS Texture Converter](https://www.nexusmods.com/skyrimspecialedition/mods/111378) - Application for bulk conversion and resizing of DDS textures.
- [DDS Texture Scanner](https://github.com/niston/TextureScan) - Application scanning for DDS textures with abnormal dimensions.
- [NifTools Blender Addon](https://github.com/niftools/blender_niftools_addon) - Blender addon for NetImmerse/Gamebryo File Formats (.nif, .kf, .egm) used in Elder Scrolls and Fallout games.
- [PyNifly](https://github.com/BadDogSkyrim/PyNifly) - Blender addon to import/export NIF files with support for Skyrim LE, Skyrim SE, Fallout 4, Fallout New Vegas, Fallout 76, and Fallout 3.
- [noclip.website (Morrowind)](https://github.com/magcius/noclip.website/tree/main/src/Morrowind) - In-browser Morrowind viewer.
- [Daggerfall utilities](https://www.moddb.com/games/daggerfall/downloads/daggerfall-utilities) - Utilities for working with Daggerfall game files.
- [ES Plugin Cracker 0.001b (Elder Scrolls IV: Oblivion)](https://www.moddb.com/games/oblivion/downloads/es-plugin-cracker-0-001b) - Plugin cracker for Elder Scrolls IV: Oblivion (v0.001b).

### 2K Games / Firaxis Games

- [Civilization IV Plugins for 3DS Max 6](https://www.moddb.com/games/civilization-iv-original/downloads/civilization-iv-plugins-for-3ds-max-6) - 3DS Max 6 plugins for Civilization IV.
- [Civilization IV Plugins for 3DS Max 7+](https://www.moddb.com/games/civilization-iv-original/downloads/civilization-iv-plugins-for-3ds-max-7) - 3DS Max 7+ plugins for Civilization IV.

### Bohemia Interactive

- [BI Editing Tools 2 (ARMA 2)](https://www.moddb.com/games/arma-2/downloads/bi-editing-tools-2) - Editing tools for ARMA 2.

### Blizzard Entertainment

- [OWLib](https://github.com/overtools/OWLib) - Toolkit for extracting and working with Overwatch game files.
- [noclip.website (World of Warcraft - Vanilla, The Burning Crusade, Wrath of the Lich King)](https://github.com/magcius/noclip.website/tree/main/src/WorldOfWarcraft) - In-browser World of Warcraft (Vanilla) viewer.
- [3DS/Obj MDX Converter](https://www.moddb.com/games/warcraft-iii/downloads/3ds-obj-mdx-converter) - Converter for Warcraft III model format (MDX) to/from 3DS and OBJ formats.
- [Starcraft Modding Tools](https://www.moddb.com/games/starcraft/downloads/starcraft-modding-tools) - Modding tools for StarCraft.
- [WoW Model Viewer 5.0.7 (World of Warcraft)](https://www.moddb.com/games/world-of-warcraft/downloads/wow-model-viewer-5-0-7) - Model viewer for World of Warcraft (v5.0.7).
- [Blizzard DATA unpacker (Warcraft: Orcs & Humans)](https://www.moddb.com/games/warcraft-orcs-humans/downloads/blizzard-data-unpacker) - Archive unpacker for Warcraft: Orcs & Humans DATA format.

### Westwood Studios / EA Los Angeles

- [C&C big extractor](https://www.moddb.com/groups/tiberium-essence-fans/downloads/cc-big-extractor) - Extractor for Command & Conquer BIG archive files.
- [Command & Conquer 3 Asset Extractor](https://www.moddb.com/groups/tiberium-essence-fans/downloads/command-conquer-3-asset-extractor) - Asset extraction tool for Command & Conquer 3.
- [C&C: Renegade Official Modding Tools](https://www.moddb.com/games/cc-renegade/downloads/cc-renegade-official-modding-tools) - Official modding tools for Command & Conquer: Renegade.
- [CnC Renegade Tools](https://www.moddb.com/games/cc-renegade/downloads/cnc-renegade-tools) - Tools for Command & Conquer: Renegade.
- [Final Big (C&C: Generals)](https://www.moddb.com/games/cc-generals/downloads/final-big) - BIG archive tool for Command & Conquer: Generals.
- [Final Big 3 (C&C: Generals)](https://www.moddb.com/games/cc-generals/downloads/final-big-3) - BIG archive tool for Command & Conquer: Generals (v3).
- [Gmax+RenX+Renegade Public Tools (C&C: Generals Zero Hour)](https://www.moddb.com/games/cc-generals-zero-hour/downloads/gmaxrenxrenegade-public-tools) - Public tools for Gmax, RenX, and Renegade formats used in Command & Conquer: Generals Zero Hour.

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
