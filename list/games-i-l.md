### I
#### RocketWerkz (Icarus)

- [IcarusDataMiner](https://github.com/CrystalFerrai/IcarusDataMiner) - Command-line program to extract data from the Unreal Engine assets of the survival game Icarus.
- [IcarusModManager](https://github.com/CrystalFerrai/IcarusModManager) - GUI application for managing game mods for Icarus, supporting data table (JSON) and blueprint mods via an asset-patching feature that avoids needing mods rebuilt on every game update.
- [IcarusSaveConverter](https://github.com/CrystalFerrai/IcarusSaveConverter) - Converts an Icarus prospect save file to and from a text-based format.
- [EditIcarusProspect](https://github.com/CrystalFerrai/EditIcarusProspect) - Command-line utility for editing properties of an Icarus prospect save.
- [IcarusResourceRespawn](https://github.com/CrystalFerrai/IcarusResourceRespawn) - Command-line program for respawning resources in an Icarus game save file.
- [Icarus-Save-Editor](https://github.com/Wahkah/Icarus-Save-Editor) - Flutter/Windows save editor for Icarus that parses its Unreal-style prospect/world saves and station-storage account files to add, repair and re-stat items, edit currencies and XP, manage the drop loadout, and apply player buffs. It backs up files before writing and only writes a world save if the repacked bytes match the parsed data.

#### Ice-Pick Lodge

- [VoidExtractor](https://github.com/valsaven/VoidExtractor) - Universal game archive extractor for Pathologic (2005) and Pathologic Classic HD (2015) `.vfs` archives (VFS v1/v2), preserving original folder hierarchy.
- [pathologic-vfs-unpacker](https://github.com/valsaven/pathologic-vfs-unpacker) - Go command-line unpacker for the `LP1C` VFS archives of the Pathologic series (e.g. Pathologic Classic HD).
- [pathologic-mesh-viewer](https://github.com/koshkokoshka/pathologic-mesh-viewer) - 3D model viewer for Pathologic Classic HD, supporting the game's .mesh format.
- [GorkhonScriptEditor](https://github.com/adc-ax/GorkhonScriptEditor) - Alpha-stage viewer/editor for Pathologic and Pathologic Classic HD's .bin script format, letting modders disassemble compiled scripts.

#### id Software

##### Dangerous Dave

- [dangerous-dave-re](https://github.com/gmegidish/dangerous-dave-re) - Reverse engineering of Dangerous Dave in the Haunted Mansion, a 1991 IBM PC game programmed by future id Software founders (Tom Hall, John Romero, John Carmack, Adrian Carmack) and distributed through Softdisk's Gamer's Edge disk service; documents its compressed level/tile data and EGA bitplane graphics, with decompression, level unpacking, sprite/tileset extraction, and a level editor.

##### Commander Keen

- [omnispeak](https://github.com/sulix/omnispeak) - Open-source re-implementation of the Commander Keen in Goodbye Galaxy (episodes 4-6) engine, reading the original game's data files.
- [TED5](https://github.com/Fleex255/TED5) - id Software's original TED5 level editor used for Commander Keen, restored and running on modern systems.
- [Commander Keen 4 Tandy source port](https://github.com/FrenkelS/keensource456tandy) - Source port of Commander Keen 4 adding Tandy 320x200 16-color graphics mode support, reading the original game's EGA data files.
- [idgrab](https://github.com/sulix/idgrab) - Header generator for id-engine (Commander Keen: Goodbye Galaxy) games, used alongside omnispeak.
- [randkeen](https://github.com/sulix/randkeen) - Commander Keen 1 randomiser that rewrites the level files (level entrances, key items, enemy and item positions, door colours) and generates a CK1PATCH-compatible patch file.
- [Commander Genius](https://github.com/gerstrong/Commander-Genius) - Actively maintained open-source interpreter for Commander Keen (1-6, Dreams) and Cosmo's Cosmic Adventure, reading the original games' data files. Runs on Linux, Windows, macOS, Android, and Switch.
- [Keen Dreams](https://github.com/keendreams/keen) - id Software's official GPL source code release for Commander Keen: Keen Dreams (1991), useful as a reference for the shared id-engine data formats.

##### Catacomb 3-D & Adventure Series

- [CatacombGL](https://github.com/ArnoAnsems/CatacombGL) - OpenGL source port for Catacomb 3-D (1991, id Software) and the Catacomb Adventure series (Softdisk, 1992-1993: The Catacomb Abyss, Armageddon, and Apocalypse), reading the original games' EGA/VGA graphics, level, and sound data.

##### Wolfenstein 3D & Spear of Destiny

- [wolf4sdl](https://github.com/fabiangreffrath/wolf4sdl) - SDL port of Wolfenstein 3D and Spear of Destiny, the canonical open-source base for the Wolf3D modding/tooling ecosystem, reading the original id Software level/graphics/sound formats.
- [WolfViewer](https://github.com/ioan-chera/WolfViewer) - Wolfenstein 3D viewer and editor for Android, displaying map walls and sprites.
- [MacWolfEd](https://github.com/ioan-chera/MacWolfEd) - macOS editor for Wolfenstein 3D and Spear of Destiny, editing levels, graphics, sounds, and music directly from the original game folder.
- [eced](https://github.com/InsanityBringer/eced) - Level editor for blzut3's ECWolf, a Wolfenstein 3D-engine derivative, editing the game's level format.
- [ECWolf](https://github.com/ECWolfEngine/ECWolf) - Cross-platform Wolfenstein 3D and Spear of Destiny source port also supporting Super 3-D Noah's Ark and Blake Stone, reading original VSWAP/GAMEMAPS/AUDIOT data.
- [WolfensteinCGA](https://github.com/jhhoward/WolfensteinCGA) - Wolfenstein 3D port targeting CGA graphics, reading the original game's VSWAP/GAMEMAPS assets.
- [roguestein](https://github.com/jonsth131/roguestein) - Terminal roguelike built on Wolfenstein 3D's original GAMEMAPS.WL6/MAPHEAD.WL6 map data, with its own Rust reader for the format.
- [wolf3d](https://github.com/id-Software/wolf3d) - id Software's official 1995 open-source release of Wolfenstein 3D, including the original VSWAP/GAMEMAPS/AUDIOT-reading engine.
- [WolfstoneExtract](https://github.com/ECWolfEngine/WolfstoneExtract) - Extracts Wolfenstein 3D-compatible game data from an installed copy of Wolfenstein II: The New Colossus or Wolfenstein: Youngblood, converting the modern titles' archives and Wwise BNK/WEM audio into a wolfstone.pk3/elitehans.pk3 usable with ECWolf-based source ports.
- [Wolf3DExtract](https://github.com/HiPhish/Wolf3DExtract) - Command-line tool for extracting graphics, sounds, and level assets from the PC version of Wolfenstein 3D.
- [snes-wolf3d-extractor](https://github.com/adambiser/snes-wolf3d-extractor) - Python extractor for the images, sounds, and maps in the SNES ROMs of Wolfenstein 3D (USA, Europe, Japan, and two betas) and Super 3D Noah's Ark (1994 and 2013 Steam versions).
- [IMF Creator](https://github.com/adambiser/imf-creator) - Python program for creating IMF music as used by several classic id Software and Apogee games such as Wolfenstein 3D and Commander Keen. Work in progress.
- [imf2mid](https://github.com/Wohlstand/imf2mid) - Command-line converter from the IMF (id Software Music Format) OPL2 register-write music format, used by Commander Keen, Wolfenstein 3D, and many Apogee games, to General MIDI. See also [IMF-Freq-Conv](https://github.com/Wohlstand/IMF-Freq-Conv), which converts the chunk delays of IMF files between 280 Hz, 560 Hz, and 700 Hz tempo speeds.
- [Wolf3D-Mac (original release)](https://github.com/Blzut3/Wolf3D-Mac) - id Software's original Macintosh source release for Wolfenstein 3D: First & Second Encounter, including the original VSWAP/GAMEMAPS-reading engine code. *(Archived.)*
- [MacWolfSDL](https://github.com/kaylagator/MacWolfSDL) - Accurate SDL3 source port of Macintosh Wolfenstein 3D, reading the original Mac resource-fork game data (including Third Encounter scenario compatibility).
- [MacWolf for DOS](https://github.com/FrenkelS/Wolf3D-Mac-for-DOS) - Ports the Macintosh version of Wolfenstein 3D (different graphics, sound, music and levels from the DOS version) to run on DOS.
- [Game Engine Black Book: Wolfenstein 3D](https://github.com/fabiensanglard/gebbwolf3) - Source (LaTeX) for Fabien Sanglard's technical book dissecting the Wolfenstein 3D engine, covering its VSWAP/GAMEMAPS/AUDIOT file formats and raycasting renderer internals in detail.

##### Doom Engine (id Tech 1) & Ports

###### Doom Source Ports & Engine Forks

- [Eternity Engine](https://github.com/team-eternity/eternity) - Advanced Doom source port that originated the UDMF map format and introduces its own EDF (Eternity Definition File) format for game data.
- [UZDoom](https://github.com/UZDoom/UZDoom) - Feature-centric Doom source port based on GZDoom, adding an advanced renderer and powerful scripting capabilities, reading original WAD data.
- [DOOM-ASCII](https://github.com/wojciech-graj/doom-ascii) - Text-based Doom source port that renders the game as ASCII art in a terminal, reading original WAD data.
- [doomgeneric](https://github.com/ozkl/doomgeneric) - Minimal, highly portable Doom source port exposing a tiny platform API (init, draw frame, sleep, get key, etc.) while reading original Doom IWAD/PWAD data; the reference base for hundreds of "Doom on X" embedded and novelty ports.
- [PureDOOM](https://github.com/Daivuk/PureDOOM) - Single-header, dependency-free (no stdlib/stdio) Doom source port designed to run on any device, reading original IWAD/PWAD data; the base for DCIDoom listed below.
- [Crispy Doom](https://github.com/fabiangreffrath/crispy-doom) - Actively maintained, faithful vanilla/limit-removing DOOM, DOOM II, Heretic, Hexen and Strife source port with widescreen and QoL enhancements, reading original IWAD/PWAD files.
- [DOOM Retro](https://github.com/bradharding/doomretro) - Actively maintained DOOM, DOOM II, Final DOOM and Ultimate DOOM source port focused on visual polish and accuracy, reading original IWAD/PWAD files.
- [Helion](https://github.com/Helion-Engine/Helion) - Cross-platform DOOM, Heretic and Hexen source port written in C#, reading original WAD files with modern rendering and multiplayer support.
- [DelphiDoom](https://github.com/jval1972/DelphiDoom) - DOOM, Heretic, Hexen and Strife source port written in Object Pascal, supporting original WAD files plus voxel and high-resolution texture extensions.
- [Doomsday Engine](https://github.com/skyjake/Doomsday-Engine) - Portable, enhanced source port of DOOM, Heretic and Hexen with its own DED definition language and PK3-based resource-pack system layered on top of original WAD data.
- [EDGE-classic](https://github.com/edge-classic/EDGE-classic) - Actively maintained, cross-platform OpenGL DOOM source port with powerful modding features built around its own DDF (Dynamic Data Format) definition language, reading original WAD data.
- [Russian Doom](https://github.com/Russian-Doom/russian-doom) - Limit-removing source port of DOOM, Heretic and Hexen with vanilla bug fixes and enhanced rendering resolutions, correctly restoring the graphics/palette data of the Russian-localized WAD releases.
- [dsda-doom](https://github.com/dsda-org/dsda-doom) - Actively maintained successor to PrBoom+ with a focus on speedrunning/demo tooling, supporting Heretic, Hexen, MBF21, Doom-in-Hexen, and UDMF/MAPINFO while reading original WAD data.
- [Mocha Doom](https://github.com/AXDOOMER/mochadoom) - Pure Java Doom source port reading original WAD/IWAD data.
- [rust-doom](https://github.com/cristicbz/rust-doom) - Doom renderer/engine written in Rust, reading and rendering original WAD level/texture data.
- [Rum and Raisin Doom](https://github.com/GooberMan/rum-and-raisin-doom) - Chocolate Doom branch focused on modernizing the renderer (higher resolutions, modern lighting) while reading original IWAD/PWAD data; adds support for Batman Doom and other total conversions.
- [DietBoom](https://github.com/fragglet/DietBoom) - Boom-derived Doom source port stripped down ("Boom without the fluff"), reading original WAD data.
- [gore](https://github.com/AndreRenaud/gore) - Minimal Doom implementation in pure Go, reading original IWAD/PWAD data (a Go port of doomgeneric).
- [Odamex](https://github.com/odamex/odamex) - Online multiplayer Doom source port focused on preserving original gameplay while reading original IWAD/PWAD data.
- [D2K](https://github.com/camgunz/d2k) - Doom source port forked from PrBoom+, adding Quake III-style enhanced client/server network play (no more pause-on-lag, in-progress join) and moving engine behavior/assets into Lua scripting, while reading original WAD data.
- [Thanatos (Theta)](https://github.com/leximayfield/thanatos) - Work-in-progress Doom source port forked from Chocolate Doom, rewriting the gameloop in C++14 to be easy to tinker with and mod, reading original WAD data with a focus on demo-compatible core logic over full mod/lump support.
- [Woof!](https://github.com/fabiangreffrath/woof) - Actively maintained continuation of the Boom/MBF bloodline of Doom source ports, reading original WAD data with widescreen rendering and accuracy/QoL improvements.
- [ZDoom](https://github.com/rheit/zdoom) - Highly moddable Doom source port supporting all Doom-engine games, reading original WAD data; the predecessor to GZDoom.
- [PrBoom+](https://github.com/coelckers/prboom-plus) - Enhanced fork of PrBoom (itself based on Boom) with recording/statistics and rendering improvements, reading original Doom IWAD/PWAD data; ancestor of D2K and dsda-doom. *(Archived; a cleaned-up copy of the original PrBoom+ SVN repository.)*
- [RZDoom](https://github.com/atsb/RZDoom) - Actively maintained continuation of classic ZDoom (as opposed to GZDoom) moving to an SDL3 backend, reading original Doom-engine WAD data.
- [CRL](https://github.com/JNechaevsky/CRL) - Continuation of the Chocorenderlimits Doom source port focused on removing engine rendering limits.
- [International Doom](https://github.com/JNechaevsky/international-doom) - Minimalist Doom source port based on Chocolate Doom, built with community code contributions.
- [Nugget Doom](https://github.com/MrAlaux/Nugget-Doom) - Doom source port forked from Woof! adding further QoL and feature extensions, reading original WAD data. See also [Cherry Doom](https://github.com/xemonix0/Cherry-Doom), a fork of Nugget Doom with additional features.
- [JDETH](https://github.com/atsb/JDETH) - Doom source port/tooling project for Doom engine (id Tech 1) file format handling.
- [managed-doom](https://github.com/sinshu/managed-doom) - Doom source port written in C#, reading original IWAD/PWAD data.
- [EDGE](https://github.com/3dfxdev/EDGE) - Enhanced Doom Engine, an OpenGL DOOM source port with a DDF definition language; predecessor to the actively maintained EDGE-classic listed above.
- [Chocolate Doom](https://github.com/chocolate-doom/chocolate-doom) - Minimalist, historically accurate Doom source port that closely reproduces the original DOS engine's behavior, reading original IWAD/PWAD data; basis for numerous derivative ports (Rum and Raisin Doom, Thanatos, doom-wasm) listed elsewhere in this section.

###### Console, Handheld, DOS & Novelty Ports

- [DoomRPG-RE-3DS](https://github.com/efimandreev0/DoomRPG-RE-3DS) - Nintendo 3DS port of the reverse engineered Doom RPG.
- [WolfensteinRPG-RE-3DS](https://github.com/efimandreev0/WolfensteinRPG-RE-3DS) - Reverse-engineered implementation of Wolfenstein RPG ported to Nintendo 3DS with SDL2, Zlib, and OpenAL dependencies.
- [DoomRPG-huawei](https://github.com/gzalo/DoomRPG-huawei) - Port of the reverse-engineered Doom RPG to Huawei eSpace feature phones.
- [dsdoom](https://github.com/Doom-Utils/dsdoom) - Port of PrBoom to the Nintendo DS, reading original Doom IWAD/PWAD data.
- [P2kDoom](https://github.com/EXL/P2kDoom) - Ports id Tech 1 engine games to vintage Motorola P2K-platform mobile phones, reading original WAD data.
- [Calico Doom](https://github.com/team-eternity/calico-doom) - Reimplementation of the Atari Jaguar port of DOOM for modern PCs, reading the Jaguar DOOM cartridge's original WAD-like data.
- [doom3do](https://github.com/Olde-Skuul/doom3do) - Complete source archive for the official DOOM port on the 3DO, preserving the console version's extra content and its 3DO-specific WAD/asset data handling.
- [FastDoom](https://github.com/viti95/FastDoom) - DOOM port for DOS optimized to run as fast as possible on real 386/486 hardware, reading original IWAD/PWAD data with hardware-specific EGA/CGA/VGA renderers.
- [Doom Vanille](https://github.com/AXDOOMER/doom-vanille) - DOS port of Linux Doom aiming for 100% compatibility with the original DOS executables' bug-for-bug behavior, reading original Doom, Ultimate Doom, and Final Doom IWAD data.
- [PsyDoom](https://github.com/BodbDearg/PsyDoom) - Backport of PlayStation DOOM and Final DOOM to PC, derived directly from reverse-engineered PS1 machine code and gradually converted from emulated MIPS instructions to structured C++ while reading the original PSX disc/WAD data.
- [uefidoom](https://github.com/Cacodemon345/uefidoom) - Port of DOOM to UEFI firmware, running before the OS boots while reading original IWAD data.
- [64doom](https://github.com/jnmartin84/64doom) - Source port of the original DOOM to the Nintendo 64, reading original IWAD/PWAD data on N64 homebrew hardware.
- [flash-doom](https://github.com/Herschel/flash-doom) - Port of Linux DOOM 1.10 to Adobe Flash using the Alchemy static-recompilation toolchain, reading original IWAD data from within the Flash Player sandbox.
- [OptiDoom3DO](https://github.com/Optimus6128/optidoom3do) - Enhanced/optimized port of the original Doom 3DO source code, reading the original 3DO release's data files (requires a commercial 3DO Doom ISO).
- [GBADoom](https://github.com/doomhack/GBADoom) - Port of PrBoom to the Nintendo Game Boy Advance, reading original Doom IWAD/PWAD data on GBA homebrew hardware.
- [DCIDoom](https://github.com/Cacodemon345/DCIDoom) - Port of PureDOOM to Windows NT 3.51/95's 32-bit DCI display API, reading original IWAD data.
- [DoomGeneric NTDrv](https://github.com/Cacodemon345/doomgeneric_ntdrv) - Ports doomgeneric to run as a Windows NT kernel-mode driver, reading the original Doom II IWAD directly from disk.
- [prboom-3ds](https://github.com/devinacker/prboom-3ds) - Nintendo 3DS port of the Doom engine based on PrBoom v2.5.0, reading original Doom IWAD/PWAD data.
- [Doom8088](https://github.com/FrenkelS/Doom8088) - Port of Doom for 16-bit DOS computers (8088/286-class hardware), reading original IWAD/PWAD data.
- [doom-wasm](https://github.com/cloudflare/doom-wasm) - Chocolate Doom compiled to WebAssembly with WebSocket-based multiplayer support, reading original Doom IWAD/PWAD data in the browser.
- [DoomNew](https://github.com/neozeed/doomnew-for-dos) - Enhanced DOS Doom source port derived from Linux Doom, adding DMX sound engine support, internal/external DeHackEd patches, and raised static limits (e.g. visplanes).
- [Buck](https://github.com/drivelling-spinel/krapfen-doom) - Limit-removing Doom source port for x86 DOS, focused on a compact, performant implementation of core Doom features.
- [CRY](https://github.com/JNechaevsky/CRY) - Reimagining of Jaguar Doom for PC built on International Doom, aiming for high emulation accuracy of the Atari Jaguar port.
- [Genesis64KBDoom](https://github.com/akiyan/genesis-DOOM64KB) - Port of FrenkelS's Doom64KB (a Doom port targeting 64KB of RAM) to the Sega Genesis/Mega Drive, built with SGDK and marsdev.
- [Doom64KB](https://github.com/FrenkelS/Doom64KB) - Port of Doom for systems with as little as 64 KB of RAM, reading original IWAD/PWAD data.
- [Doom8088ST](https://github.com/FrenkelS/Doom8088ST) - Port of Doom for Motorola 68000-based computers (Atari ST and similar), reading original IWAD/PWAD data; sibling project to the already-listed Doom8088.
- [ELKSDOOM](https://github.com/FrenkelS/elksdoom) - Port of Doom to ELKS (Embeddable Linux Kernel Subset) for 8086-class hardware, reading original IWAD/PWAD data.
- [BERNEWFIE](https://github.com/drivelling-spinel/bernewfie) - Hexen (1995) source port to DJGPP and liballeg for DOS with high-resolution rendering support, reading original Hexen IWAD data.
- [Tartar](https://github.com/drivelling-spinel/tartar) - Doom (1993) source port to DJGPP and liballeg for DOS based on the Eternity Engine, reading original Doom IWAD/PWAD data.
- [DOOM Ruby](https://github.com/khasinski/doom) - Faithful port of the DOOM (1993) engine to pure Ruby, reading original shareware/registered WAD files with BSP-accurate rendering, HUD, item pickups, and combat.
- [DCDoom](https://github.com/LemonHaze420/DCDoom) - Port of WinDoom to the Sega Dreamcast, reading original IWAD/PWAD data.

###### Level Editors & Map Tools

- [Eureka](https://github.com/ioan-chera/eureka-editor) - Cross-platform map editor for the Doom engine (id Tech 1).
- [SLADE](https://github.com/sirjuddington/SLADE) - The comprehensive Doom-engine (id Tech 1) editor. Edit WAD/PK3/ZIP archives, maps, textures, graphics, sounds, and text lumps, with support for Doom, Heretic, Hexen, Strife, and other id Tech 1 games.
- [UltimateDoomBuilder](https://github.com/UltimateDoomBuilder/UltimateDoomBuilder) - The actively maintained successor to Doom Builder / GZDoom Builder; a comprehensive map editor for Doom-engine (id Tech 1) games, reading and writing WAD map data.
- [yadex](https://github.com/Doom-Utils/yadex) - Doom level (WAD) editor for Unix/X11 systems.
- [DoomEd](https://github.com/fragglet/DoomEd) - id Software's original NeXTSTEP-era Doom level editor (DoomEd), ported to run on modern macOS/Unix systems.
- [Doom Builder PSX](https://github.com/Erick194/DoomBuilderPSX) - Doom Builder / GZDoom Builder fork modified for creating maps for PSX Doom, Psx Doom Master Edition, and PsyDoom, reading/writing the PlayStation Doom map format.
- [DEU (history mirror)](https://github.com/chocolatiers/deu-history) - Archived source for DEU (Doom Editing Utility) 5.2, one of the original WAD level editors from the early Doom modding scene.
- [JZBuilder](https://github.com/jmickle66666666/jzbuilder) - Browser-based Doom map editor written in TypeScript, using its own non-destructive intermediate data representation (with Edge Modifiers) that compiles/exports to Doom's WAD map format.

###### Node Builders (BSP Tools)

- [zennode](https://github.com/Doom-Utils/zennode) - Doom node builder, computing the BSP tree data embedded in WAD level files.
- [ZokumBSP](https://github.com/zokum-no/zokumbsp) - Actively maintained blockmap, reject-table, and BSP node builder for Doom, Heretic, and Hexen WAD levels, based on Doom-Utils' zennode.
- [nodebuilder](https://github.com/7thSamurai/nodebuilder) - Experimental DOOM node builder that preprocesses WAD level data into BSP trees and block maps, with animated visualizations of the build process.
- [BSP (history mirror)](https://github.com/chocolatiers/bsp-history) - Archived source for BSP 5.2, the most widely used Doom node builder of the 1990s editing scene, computing the BSP tree/NODES lump data a WAD level needs before it can be played.
- [DOOM-Vis](https://github.com/proteal/DOOM-Vis) - Windows port of Doom with a live, side-by-side visualization of BSP tree traversal (plane splits and bounding-box culling) read from the WAD's NODES lump.
- [vigilantbsp](https://github.com/VigilantDoomer/vigilantbsp) - Multi-threaded, polyobject-aware NODES/REJECT/BLOCKMAP builder for Doom and other id Tech 1 WAD levels.
- [ElfBSP](https://github.com/elf-alchemist/elfbsp) - Modern BSP tree/node builder for Doom-engine (id Tech 1) games and source ports, based on Andrew Apted's AJBSP.
- [glBSP (history mirror)](https://github.com/elf-alchemist/glbsp-archive) - Preservation mirror of Andrew Apted's glBSP, a GL-friendly node builder for Doom WAD levels; no actively maintained canonical host remains.
- [ZDBSP](https://github.com/rheit/zdbsp) - Stand-alone version of ZDoom's internal node builder for compiling Doom WAD level BSP/GL nodes.
- [JBSP](https://github.com/atsb/JBSP) - BSP-related tooling for the Doom engine (id Tech 1).

###### WAD/Format Libraries, Parsers & Converters

- [wadext](https://github.com/ZDoom/wadext) - Simple WAD extraction command-line tool for Doom engine (id Tech 1) mods. Extracts and converts Doom format patches/flats to PNG and sounds to WAV. Supports Doom, Heretic, Hexen, and Strife palettes.
- [DOOMP](https://github.com/Ret-HZ/DOOMP) - Doom file format parser and extractor.
- [ExtractDoomDisk](https://github.com/gibbed/ExtractDoomDisk) - Extractor for Doom disk image files.
- [wad2gltf](https://github.com/DethRaid/wad2gltf) - Converts Doom WAD map geometry to the glTF runtime format.
- [UDMF-Convert](https://github.com/CO2/UDMF-Convert) - Converts Doom maps to/from the UDMF (Universal Doom Map Format) text-based map format.
- [UDMF-Converter-EE](https://github.com/ioan-chera/UDMF-Converter-EE) - UDMF map format converter specifically for the Eternity Engine.
- [WADMerge](https://github.com/GitExl/WADMerge) - Merges multiple Doom WAD files into one, correctly combining TEXTURE/PNAMES lumps, maps, and namespaced/text lumps.
- [wadc](https://github.com/jmtd/wadc) - Programming language and compiler for constructing Doom WAD map data.
- [deutex](https://github.com/Doom-Utils/deutex) - Long-standing WAD file composer/extractor and PWAD-to-IWAD merge tool for Doom-engine games.
- [xwadtools](https://github.com/Doom-Utils/xwadtools) - Portable collection of WAD tools for id Software and Raven Software games based on the Doom and Hexen engines.
- [wadmake](https://github.com/leximayfield/wadmake) - Command-line utility for creating WAD, PK3 (ZIP), and PK7 (7z) archives for Doom-engine games.
- [HxDoom](https://github.com/kevansevans/HxDoom) - Haxe library for building Doom (id Tech 1) programs across all Haxe targets (including Flash and PHP), reading original WAD/IWAD data; borrows format details from the 3DO Doom source release for behavior that isn't otherwise documented.
- [JDLE](https://github.com/jmickle66666666/JDLE) - JMickle's Doom Lump Editor, a GUI tool for viewing and editing lumps inside Doom WAD files.
- [Omgifol](https://github.com/devinacker/omgifol) - Python library for reading and writing Doom WAD files, originally by Fredrik Johansson and maintained by Devin Acker.
- [GbaWadUtil](https://github.com/doomhack/GbaWadUtil) - Utility for converting a Doom IWAD into a format for GBADoom, writing a new WAD file and/or C source file to reduce memory footprint on GBA hardware.
- [dshrink](https://github.com/derekmd/dshrink) - Command-line tool to remove redundant sidedefs from Doom PWAD levels, rewriting the SIDEDEFS lump to reduce file size.
- [wadtools](https://github.com/7thSamurai/wadtools) - Command-line tools for creating and extracting Doom 1 & 2 WAD files.
- [WadGadget](https://github.com/fragglet/WadGadget) - Curses-based terminal file manager for Doom WAD archives, for browsing, editing and converting WAD lump data.
- [wadptr](https://github.com/fragglet/wadptr) - Doom WAD file compressor that merges identical/duplicate lumps and graphic columns to shrink WAD file size losslessly.
- [idchoppers](https://github.com/eevee/idchoppers) - Rust library and command-line tool for parsing and manipulating Doom-era WAD files and associated data.
- [GDCC](https://github.com/DavidPH/GDCC) - Game Data Compiler Collection: gdcc-ar-wad packs/unpacks Doom WAD archives, gdcc-acc compiles Hexen ACS source to bytecode, plus a C compiler/linker targeting Doom's ACS virtual machine.
- [ACSVM](https://github.com/DavidPH/ACSVM) - ACS virtual machine library and standalone interpreter for the Hexen/ZDoom ACS bytecode format stored in a WAD's BEHAVIOR lump.
- [SVG2UDMF](https://github.com/KUBA18i/SVG2UDMF) - Converts SVG vector images into Doom level geometry in UDMF format.
- [DH-dlc & DH-wad](https://github.com/DavidPH/DH-dlc) - David's Doom Level Compiler, a text-based Doom map authoring tool with variables and embedded scripting, plus David's WAD Builder for compiling to native WAD format.
- [wadcat](https://github.com/JadingTsunami/wadcat) - Command-line tool to inspect the contents of Doom WAD files, printing map-specific lumps (SECTORS, THINGS, LINEDEFS, SIDEDEFS, VERTEXES).
- [giffy](https://github.com/JadingTsunami/giffy) - Converts an animated GIF into vanilla-compatible Doom WAD texture frames for scrolling animated map displays, including a helper script to auto-generate the WAD template with correct linedef offsets.
- [psxwadgen](https://github.com/haleyjd/psxwadgen) - Converts a PlayStation DOOM CD image into a PC-usable WAD archive.
- [acc](https://github.com/ZDoom/acc) - Official ACS (Action Code Script) compiler used by ZDoom and Hexen, compiling script sources to the BEHAVIOR lump bytecode format.
- [wad-js](https://github.com/jmickle66666666/wad-js) - JavaScript library for reading Doom-engine (id Tech 1) WAD files.
- [MAD2WAD](https://github.com/jval1972/MAD2WAD) - Converts MAD data files from Mars, Hero & Tao (a 1997 shareware FPS trilogy) to the Doom WAD format. See also [Mars3D](https://github.com/jval1972/Mars3D), a source port of Mars - The Ultimate Fighter reading the original mars.mad file.
- [wadcode](https://github.com/johndoe31415/wadcode) - WAD compiler/decompiler that disassembles WAD files (Doom, Heretic, and similar id Tech 1 games) into individually editable resources and recompiles them back into a WAD.

###### Modding, Scripting & Content Tools

- [WhackEd4](https://github.com/GitExl/WhackEd4) - Modern replacement for the DOS-based Dehacked tool, loading and editing Doom Dehacked (.deh/.bex) patch files.
- [ListACS](https://github.com/alexey-lysiuk/ListACS) - Disassembler and decompiler for ACS (Action Code Script) bytecode, including ZDoom's ACS extensions.
- [umapinfo](https://github.com/dsda-org/umapinfo) - Specification and reference tooling for UMAPINFO, the community-standard Doom map-metadata lump format.
- [DoomTools](https://github.com/MTrop/DoomTools) - GUI/CLI suite of DOOM utilities: WadTool (WAD management), DoomMake (build automation), DECOHack (DeHackEd patch compiler) and WSwAnTBL.
- [mbf21](https://github.com/dsda-org/mbf21) - Specification and documentation for MBF21, an extended DEHACKED-based patch format for Doom-engine mods.
- [ACE Engine for DOOM 2](https://github.com/kgsws/doom_ace) - Achieves arbitrary native code execution in vanilla DOS DOOM2.EXE purely from a crafted WAD file, exploiting a negative-size ZONE allocation and an out-of-bounds stack read in the engine's WAD-loading code to inject and run a custom "ACE Engine" entirely from WAD lump data.
- [DoomUnity](https://github.com/jmickle66666666/DoomUnity) - Various tools for working with Doom WADs and levels in Unity.
- [htic4doom](https://github.com/fragglet/htic4doom) - Hack that makes Heretic levels loadable and playable with `doom.wad`, via a Dehacked patch remapping Heretic thing types to Doom equivalents plus replacement TEXTURE1/TEXTURE2, flat, ANIMATED and SWITCHES lumps.
- [UMAPINFO Designer](https://github.com/JadingTsunami/umapinfo-designer) - GUI tool for creating UMAPINFO lumps for Doom WAD files, customizing per-map gameplay settings supported by many source ports.
- [UDMF Engine Support Tables](https://github.com/biwa/engine-udmf-support) - Reference tables documenting which UDMF map-format fields are supported by which Doom source ports/engines.
- [SBARDEF HUD Mod for Woof!](https://github.com/NightFright2k19/doom_sbardef) - Editor/mod for creating custom status bar and fullscreen HUD layouts using Doom's SBARDEF lump format.
- [doom_lua](https://github.com/ribbiks/doom_lua) - Collection of Lua scripts for Doom Builder X / the Lua fork of Ultimate Doom Builder, automating map-editing tasks (e.g. linedef beveling) directly on WAD map data.
- [eternityportalhelper](https://github.com/biwa/eternityportalhelper) - GZDoom Builder/Eureka helper script for building portal setups in the Eternity Engine (Doom source port).
- [soundpropagationmode](https://github.com/biwa/soundpropagationmode) - Documentation/reference tool for Doom source port sound propagation mode behavior (map format-adjacent, Doom/UDMF engines).
- [VULD](https://github.com/JadingTsunami/vuld) - Launcher/build tool for vanilla Doom mods that merges WAD and DeHackEd (.deh) patches (via DEUTEX/DEUSF and DEHACKED.EXE) into a runnable mod without modifying the base game files; includes DEHPICK for finding and applying DeHackEd patches.
- [DD_VOXEL](https://github.com/jval1972/DD_VOXEL) - Voxel model editor for DelphiDoom's voxel extension format, used by the DelphiDoom source port above.

###### Level Generators, Utilities & Documentation

- [Oblige](https://github.com/Doom-Utils/Oblige) - Random level generator that produces playable WAD files for Doom-engine games.
- [OBSIDIAN](https://github.com/obsidian-level-maker/Obsidian) - Actively maintained community continuation of Oblige (combined with the ObAddon project), producing playable WAD files for Doom-engine games.
- [lmpc](https://github.com/Doom-Utils/lmpc) - Little Movie Processing Centre, a tool for processing and editing Doom .lmp demo files.
- [DIYDoom](https://github.com/amroibrahim/DIYDoom) - Step-by-step guide to rebuilding the DOOM engine from scratch in C++/SDL, with detailed notes documenting the WAD file format, BSP rendering, and other engine internals.
- [DMXOPL](https://github.com/sneakernets/DMXOPL) - YMF262 (OPL3)-enhanced FM instrument patch set replacing DOOM's DMX GENMIDI lump, used by Chocolate Doom, Crispy Doom, and other source ports for improved FM synth music playback.
- [dmvis](https://github.com/devinacker/dmvis) - Doom map visualizer that reads WAD level geometry and renders it as animated GIFs.
- [TheUnofficialDoomSpecs](https://github.com/nukeop/TheUnofficialDoomSpecs) - Markdown conversion of Matthew S. Fell's classic Unofficial DOOM Specs, documenting the WAD file format, level data structures, and other Doom engine internals.
- [midisnd](https://github.com/fragglet/midisnd) - Generates a WAD file containing MIDI-based Doom sound effects, a feature discovered in Vanilla Doom.
- [rutti-tutti-find-a-frutti](https://github.com/sponge/rutti-tutti-find-a-frutti) - Scans vanilla DOOM IWAD/PWAD level data for common visual/texture-alignment errors.
- [wallpaint](https://github.com/jmickle66666666/wallpaint) - Extracts wall texture patches from a Doom map's linedefs into an editable PNG (correcting for offsets/pegging), then rebuilds them back into the WAD as palettized textures.
- [dmsvg](https://github.com/devinacker/dmsvg) - Renders top-down SVG maps of Doom engine levels, drawing scaled floor textures and approximate sector lighting directly from WAD level data.
- [miniwad](https://github.com/fragglet/miniwad) - Minimalist Doom IWAD demonstrating how small a playable WAD can be, exploiting wadptr's lump-merging (palette-reduced, repeated textures and reused sound effects) to stay under a quarter-megabyte while remaining usable with any WAD from the idgames archive.
- [Squashware Doom](https://github.com/fragglet/squashware) - Rework of the Shareware Doom IWAD for embedded/low-memory devices, shrinking it under 1.7MB (with silent and 1-level variants down to ~700KB) via a restricted texture set, shorter sounds/music and fewer animation frames; includes the DOOF (Doom On One Floppy) subproject.
- [LmpStats](https://github.com/Xymph/LmpStats) - Library for collecting statistics (demo version, map slot, skill, length, gameplay flags, players) from Doom-engine .lmp demo files.
- [liquorice](https://github.com/jmtd/liquorice) - Haskell embedded domain-specific language (eDSL) for algorithmically constructing Doom maps by scripting a virtual "turtle" that defines walls, floors, rooms and monsters, exporting to the Doom map format.
- [Doom Text Generator](https://github.com/eevee/doom-text-generator) - Renders custom text images using Doom-ecosystem console/menu fonts, reading FON1/FON2 and other Doom font formats directly from WAD/PK3 files.
- [imagetool](https://github.com/rheit/imagetool) - ZDoom font/image tool for converting to/from FON1/FON2 and other ZDoom-ecosystem font/image formats.
- [vanilla-utilities](https://github.com/fragglet/vanilla-utilities) - Collection of MS-DOS utilities for the original vanilla Doom engine, by longtime Doom community developer fragglet (Chocolate Doom).
- [WAD Vault](https://github.com/leximayfield/WADVault) - Metadata catalog/database of official and user-created WAD files for Doom, Heretic, Hexen and Strife, publishing logiqx-format DAT files for collection organization.
- [doom-utils](https://github.com/RyanMallon/doom-utils) - Small collection of Doom tools: wad_strip.py (removes unused textures/patches/flats from a WAD), demo_extend.py (extends .lmp demo files), and info_to_decohack.py (converts DEHACKED-style INFO data to MTrop DoomTools' DECOHack patch format), plus reference Dehacked patches for Doom II, Heretic, and Hexen.
- [linguortal-gen](https://github.com/jmickle66666666/linguortal-gen) - Creates a linked "linguortal" connection between two Doom WAD map files at specified linedefs, built on the already-listed Omgifol WAD library.
- [DoomSoundFixer](https://github.com/Edward850/DoomSoundFixer) - Utility for fixing broken/corrupted sound lumps in older Doom WAD files.
- [texSorter](https://github.com/JadingTsunami/texSorter) - GUI tool for sorting and renaming Doom TEXTURE lumps in a WAD by category and dominant color, including a remapper.py script to update existing maps to the new texture names.
- [Game Engine Black Book: Doom](https://github.com/fabiensanglard/gebbdoom) - Source (LaTeX) for Fabien Sanglard's in-depth technical book dissecting the DOOM engine, including the WAD file format, level/BSP data structures, and renderer internals.

###### Doom 64 & Hexen 64 Tools

- [D64TOOL](https://github.com/Erick194/D64TOOL) - Converts Doom64 EX map format to native Doom 64 N64 format, and encodes/decodes Doom64 WAD lumps.
- [HexenN64Tool](https://github.com/Erick194/HexenN64Tool) - Extracts and decompresses Hexen 64's HEXEN64.WAD, HEXEN64.PTR, HEXEN64.WBK and HEXEN64.DAT ROM data; also encodes/decodes the format.
- [DLight](https://github.com/svkaiser/dlight) - Lightmap-building utility for Doom64EX WAD maps pre-compiled with GLBSP GL nodes.
  - See also [dlightgui](https://github.com/svkaiser/dlightgui), a frontend tool for the DLight and GLVIS utilities.
- [wadutil64](https://github.com/thekovic/wadutil64) - CLI tool for Doom 64 (N64) WADs: decompresses vanilla-compressed WAD data and pads it to satisfy libultra's DMA alignment requirements.
- [Doom Builder 64](https://github.com/thekovic/DoomBuilder64) - Fork of Doom Builder 2 adding map-editing support for Doom 64 on N64 and PC (EX/Steam/GOG), reading and writing the Doom 64 map format.
  - See also [svkaiser/DoomBuilder64](https://github.com/svkaiser/DoomBuilder64), a custom Doom Builder 2 branch for Doom64 EX support.
- [Doom Builder 64 Enhanced](https://github.com/Styd051/Doom-Builder-64-Enhanced) - Fork of Doom Builder 64 updated to the latest Doom Builder 2 codebase, with added features for Doom 64 mappers.
- [BSP64 Enhanced](https://github.com/Immorpher/BSP64Enhanced) - Doom 64 node builder with blockmap optimization, sidedef compression, and reject-table editing; extends Diema's DMA-BSP64 with ZokumBSP-derived features.
- [BLAM](https://github.com/Immorpher/blam) - Basic Line Action Macro compiler for Doom 64, a fork of Kaiser's original tool that compiles macro scripts referenced by Doom 64 WAD levels.
- [Doom 64 Compendium](https://github.com/Immorpher/doom64) - Documentation project covering the Doom 64 engine, its various source ports/forks, and how to modify its WAD-based level and asset data.
- [Doom64EX](https://github.com/svkaiser/Doom64EX) - Reverse-engineered Doom 64 recreation with added modding features; reads the Doom 64 data as doom64.wad, which its -wadgen option generates from a Doom 64 ROM (source includes WAD, ROM-WAD and ZIP-WAD readers).
- [Doom64EX-Plus](https://github.com/atsb/Doom64EX-Plus) - Improved, modernized continuation of Doom64EX (archived, considered feature-complete by its author).
- [Doom64EX-Classic](https://github.com/atsb/Doom64EX-Classic) - Active successor to Doom64EX-Plus (by the same author), continuing development of the Doom 64 source port after the original was archived as feature-complete.
- [Doom 64 XE](https://github.com/Immorpher/doom64xe) - Expanded Edition Doom 64 N64 source port combining DOOM64-RE, DOOM64 CE, Doom 64 Merciless Edition, and Doom 64 Ultra; builds from the original WAD/WMD/WSD/WDD resource files extracted from a Doom 64 ROM, with an included BPS patch to pull in Nightdive's 2020 rerelease assets.
- [MIDI-64nicator](https://github.com/Immorpher/MIDI-64nicator) - Formats standard MIDI files to satisfy Doom 64's proprietary event quirks (note-off handling, loop-point event, tempo/info events, channel re-organization) for use with Doom 64 EX, Doom 64 Remaster, Retribution, and DZDoom.
- [doom64-dc](https://github.com/jnmartin84/doom64-dc) - Doom 64 port for Sega Dreamcast / KallistiOS.

###### Decompilations, Source Releases & Historical Archives

- [DOOM64-RE (decomp)](https://github.com/Erick194/DOOM64-RE) - Matching decompilation of Doom 64.
- [PSXDOOM-RE (decomp)](https://github.com/Erick194/PSXDOOM-RE) - Matching decompilation of Doom (PlayStation).
- [DOOM](https://github.com/id-Software/DOOM) - id Software's official 1997 GPL source code release for the original DOOM (1993) and DOOM II (1994), including the WAD-reading and rendering engine.
- [PSXFINALDOOM-RE](https://github.com/Erick194/PSXFINALDOOM-RE) - Matching decompilation of the PlayStation version of Final Doom, building on the same author's PSXDOOM-RE.
- [RomeroDoomDump](https://github.com/chocolatiers/RomeroDoomDump) - Archive of original Doom development files released by John Romero, including cut MIDI tracks, unreleased artwork/sprites, and other pre-release assets, with provenance notes for each.
- [Hexen ACS Reconstructed](https://github.com/fragglet/hexen-acs-reconstructed) - Project reconstructing readable Hexen ACS (Action Code Script) source from DEACC-decompiled output, compiling back byte-for-byte to the original BEHAVIOR lumps in the Hexen IWAD.
- [WadSmoosh (archive)](https://github.com/elf-alchemist/wadsmoosh-archive) - Preservation mirror of WadSmoosh, which merges Ultimate Doom, Doom 2, Master Levels, No Rest for the Living and other IWADs into a single combined IWAD; original author has stopped maintaining it.
- [Hexen Development Files](https://github.com/svkaiser/hexen-development-files) - Original Raven Software development archive for Hexen: ACS script sources, a modified DoomED level editor, DWD level source files, and other period development tools, recovered by Grayman53.
- [WolfensteinRPG-RE](https://github.com/Erick194/WolfensteinRPG-RE) - Reverse engineering of Wolfenstein RPG, the J2ME mobile spin-off; upstream of the WolfensteinRPG-RE-3DS port above.
- [DoomRPG-RE](https://github.com/Erick194/DoomRPG-RE) - Reverse engineering of Doom RPG, the J2ME mobile spin-off; upstream of the DoomRPG-RE-3DS and DoomRPG-huawei ports above.
- [DoomIIRPG-RE](https://github.com/Erick194/DoomIIRPG-RE) - Reverse engineering of Doom II RPG, the J2ME mobile spin-off sequel to Doom RPG.

##### Quake & Wolfenstein Engines (id Tech 2/3)

###### Official Source Releases & Historical Archives

- [Quake Rerelease QuakeC Source Code](https://github.com/id-Software/quake-rerelease-qc) - Official id Software release of the QuakeC source for the 2021 Quake re-release, covering all five codebases: base campaign, Scourge of Armagon, Dissolution of Eternity, Dimension of the Machine (shared with Dimension of the Past), and Capture the Flag. Useful reference for understanding the updated engine's data and localization changes versus the original QuakeC.
- [Quake](https://github.com/id-Software/Quake) - id Software's official GPL source release for Quake, QuakeWorld and their GL variants, including the original PAK/BSP/MDL-reading engine.
- [Quake 2 Tools](https://github.com/id-Software/Quake-2-Tools) - id Software's official GPL source release of the Quake 2 asset-compiling tools (qdata, qbsp, qvis, qrad), used to build the game's original BSP maps and MDL/SP2 models.
- [Quake III: Arena](https://github.com/id-Software/Quake-III-Arena) - id Software's official 2005 GPL source code release for Quake III Arena, including the id Tech 3 BSP-reading and rendering engine.
- [Return to Castle Wolfenstein (SP)](https://github.com/id-Software/RTCW-SP) - id Software's official GPL source release for Return to Castle Wolfenstein's single-player campaign, including the id Tech 3 (Quake III-derived) BSP/MD3-reading engine.
- [Wolfenstein: Enemy Territory](https://github.com/id-Software/Enemy-Territory) - id Software's official GPL source release for Wolfenstein: Enemy Territory, an id Tech 3-derived engine reading the game's original BSP/MD3/PK3 assets.
- [GtkRadiant](https://github.com/id-Software/GtkRadiant) - id Software's official GPL source release for GtkRadiant, the canonical level editor for Quake, Quake III and Doom 3-era (idTech 4) games; forked to create DarkRadiant (see Modern DOOM section).
- [Quake II Rerelease Game Source](https://github.com/id-Software/quake2-rerelease-dll) - Official id Software release of the game code for the 2023 Quake II rerelease alongside the original game code kept as reference; a Quake II companion to the already-listed Quake Rerelease QuakeC Source Code, useful for understanding the updated engine's data changes.
- [Quake Map Source](https://github.com/fzwoch/quake_map_source) - Archive of the original Quake `.map` source files for the retail episodes as released by John Romero in October 2006, with compiled BSPs and free texture-WAD replacements standing in for the non-redistributable originals.

###### Quake and Wolfenstein Source Ports & Engine Forks

- [vkQuake](https://github.com/Novum/vkQuake) - Vulkan-based Quake source port supporting original PAK/BSP/MDL/SPR assets, higher resolution textures and modern rendering features.
- [Chocolate Quake](https://github.com/Henrique194/chocolate-quake) - Minimalist Quake source port focused on faithfully restoring the v1.09/DOS-era look, feel, and bugs, reading original PAK/BSP/MDL data.
- [SharpQuake](https://github.com/Memorix101/SharpQuake) - GLQuake reimplementation in C# using OpenTK and .NET, reading original PAK/BSP/MDL assets.
- [QuakEMBD](https://github.com/FantomJAC/quakembd) - WinQuake port to ARM Cortex-M embedded devices (e.g. STM32H747I-DISCO), reading original Quake PAK files from an SD card.
- [ctrQuake](https://github.com/masterfeizz/ctrQuake) - Unofficial port of Quake to the Nintendo 3DS, reading the original shareware or full-game PAK files.
- [iortcw](https://github.com/iortcw/iortcw) - Actively maintained community continuation of Return to Castle Wolfenstein (both single-player and multiplayer), merging ioquake3 engine fixes into the RTCW codebase while reading original BSP/MD3/PK3 assets.
- [QuakeSpasm](https://github.com/sezero/quakespasm) - Modern, cross-platform Quake source port based on FitzQuake, reading original PAK/BSP/MDL game data. See also [Ironwail](https://github.com/andrei-drexler/ironwail), a high-performance fork with a modernized renderer.
- [QuakePSX](https://github.com/fgsfdsfgs/quakepsx) - Experimental port of Quake to the PlayStation, with a build-time asset "cooker" that converts the original PC Quake data (from a legitimately owned copy) into PSX-native resource formats.
- [yquake2](https://github.com/yquake2/yquake2) - The Yamagi Quake II client, an actively maintained Quake II source port.
  - [pakextract](https://github.com/yquake2/pakextract) - Small tool to list or extract Quake, Quake II, Daikatana, and Sin pak files.
- [qrustyquake](https://github.com/cyanbun96/qrustyquake) - Rust reimplementation/port of the original Quake engine (WinQuake-derived), reading original Quake PAK/BSP asset data.
- [QuakespasmNX](https://github.com/fgsfdsfgs/QuakespasmNX) - Nintendo Switch port of QuakeSpasm, reading original Quake PAK/BSP/MDL data with OGG/MP3 music support.
- [Chocolate QuakeWorld](https://github.com/Henrique194/chocolate-quakeworld) - Minimalist QuakeWorld source port focused on faithfully preserving the classic '90s multiplayer experience, reading original PAK/BSP/MDL data; companion project to Chocolate Quake.
- [fteqw](https://github.com/fte-team/fteqw) - Actively maintained, heavily-extended Quake engine fork (FTEQW) supporting a wide range of QuakeC-based mods and games, reading original PAK/BSP/MDL data.
- [ps2quake](https://github.com/dirsors/ps2quake) - Source port of Quake for the PlayStation 2, reading original PAK/BSP/MDL game data.
- [DarkPlaces](https://github.com/DarkPlacesEngine/DarkPlaces) - Actively maintained Quake engine fork by LadyHavoc with an advanced renderer, reading original PAK/BSP/MDL data.
- [QuakeForge](https://github.com/quakeforge/quakeforge) - Long-running, portable Quake engine fork supporting Quake and QuakeWorld, reading original PAK/BSP/MDL data.
- [ezQuake](https://github.com/QW-Group/ezquake-source) - Actively maintained QuakeWorld client focused on competitive multiplayer, reading original PAK/BSP/MDL data.
- [quake-rb](https://github.com/khasinski/quake) - Port of the Quake (1996) engine to Ruby with OpenGL/SDL2 rendering, reading original PAK/BSP/MDL assets (shareware or registered `pak0.pak`/`pak1.pak`).
- [three-quake](https://github.com/mrdoob/three-quake) - Browser port of Quake to Three.js, reading the original `pak0.pak` (shareware Episode 1 included; supports full-game PAKs from a registered copy).
- [WebQuake](https://github.com/Triang3l/WebQuake) - HTML5/WebGL port of Quake, reading the original `id1` (and mission pack `hipnotic`/`rogue`) PAK/BSP/MDL data.
- [JoeQuake](https://github.com/j0zzz/JoeQuake) - Quake engine fork targeted at speedrunning, reading original PAK/BSP/MDL data.
- [Super8](https://github.com/qbism/super8) - Quake engine fork (based on Makaqu) focused on authentic 8-bit color rendering for contemporary Quake maps, reading original PAK/BSP/MDL data; adds per-liquid transparency, higher resolutions, and pixel-doubling over its base. Archived.
- [Q2RTX](https://github.com/NVIDIA/Q2RTX) - NVIDIA's discontinued Quake II engine fork adding real-time RTX path-traced global illumination, reading original PAK/BSP/MDL data; built on Q2PRO via Christoph Schied's [Q2VKPT](https://github.com/cschied/q2vkpt) prototype.

###### Level Editors, Map Compilers & BSP Tools

- [TrenchBroom](https://github.com/TrenchBroom/TrenchBroom) - Level editor for Quake and Quake-engine based games, supporting BSP map format creation and editing.
- [QuakePrism](https://github.com/lancebord/QuakePrism) - Engine editor/IDE for the Quake engine that streamlines mod and game development, working with PAK/WAD archives and Quake model formats.
- [bspc](https://github.com/bnoordhuis/bspc) - Standalone build of id Software's Quake III: Arena BSP-to-AAS compiler, generating the bot navigation (AAS) data from a compiled BSP map.
- [Quake--QBSP-and-VIS](https://github.com/fabiensanglard/Quake--QBSP-and-VIS) - Annotated/modified source for Quake's original bsp.exe and vis.exe map compilers, instrumented to trace and explain the BSP tree and Potentially Visible Set (PVS) building process.
- [vis.py](https://github.com/pekkavaa/vis.py) - Computes a potentially visible set (PVS) for Quake maps, converting a BSP's portal file (PRT) into a leaf-to-leaf visibility matrix written back into the map's BSP file.
- [ericw-tools](https://github.com/ericwa/ericw-tools) - Actively maintained Quake/Hexen 2 map compiling tools (qbsp, vis, light), a modernized branch of the original id Software compilers with bug fixes and new features.
- [NetRadiant-Custom](https://github.com/Garux/netradiant-custom) - Actively maintained, cross-platform level editor for id Tech based games, a modernized continuation of the GtkRadiant/NetRadiant lineage.
- [q3mapx](https://github.com/themuffinator/q3mapx) - Performance-focused continuation of NetRadiant-custom's q3map2 compiler with a CLI and Qt workbench, adding BSP-to-`.map` decompilation (`-convert -format map`) with recovery reports, BSP inspection, and stored-lighting and visibility evidence commands.
- [q2tools-220](https://github.com/qbism/q2tools-220) - Quake 2 map compiler tools (qbsp/qvis/qrad) with v220 map format support, automatic phong shading, and other enhancements/fixes; base project for the Anachronox-specific anoxtools fork (see Ion Storm section).
- [blarghrad](https://github.com/zzsort/blarghrad) - Decompiled source of ArghRad, a modified id Software radiosity/lightmap compiler for Quake-engine BSP maps.
- [optixlight](https://github.com/matthewearl/optixlight) - Adds path-traced bounced lighting into Quake 2 BSP files already lit by a direct-light compiler (e.g. ericw-tools), using Nvidia's Optix API for GPU ray tracing.
- [BSP-Entity-Edit](https://github.com/SomaZ/BSP-Entity-Edit) - Editor for id Tech 3 BSP entity strings: renders opened BSP files with vertex colors, lets you pick entities in the viewport, and saves the edited entities back into the BSP or to a standalone `.ent` file.
- [pyidtech3lib](https://github.com/SomaZ/pyidtech3lib) - Python library for loading id Tech 3 BSP files, with a virtual file system over the game's base directories and readers for several BSP variants (IBSP, RBSP, FBSP, EF2BSP, FAKK).

###### Blender/DCC Plugins & Model/Map Importers

- [blender_io_mesh_bsp](https://github.com/andyp123/blender_io_mesh_bsp) - Blender addon for importing Quake BSP (Binary Space Partition) map files.
- [rtcw-wet-blender-model-tools](https://github.com/mino-git/rtcw-wet-blender-model-tools) - Blender model tools for Return to Castle Wolfenstein: Enemy Territory.
- [Quake MAP File Importer for Blender](https://github.com/andyp123/blender_io_mesh_qmap) - Blender add-on for importing Quake MAP level editor files; enables using brush-based level geometry in Blender for collision meshes and other purposes.
- [io_export_qmap](https://github.com/c-d-a/io_export_qmap) - Blender add-on that exports geometry to the Quake `.map` brush format.
- [Blender_BSP_Importer](https://github.com/SomaZ/Blender_BSP_Importer) - Blender importer for id Tech 3 BSP maps (Quake III and derivatives); imports entities and converts Quake 3 shaders to Eevee materials.
- [io_import_wad2](https://github.com/c-d-a/io_import_wad2) - Blender add-on that imports Quake WAD2 texture archives.
- [Chisel.Import.Quake1](https://github.com/Quixotic7/Chisel.Import.Quake1) - Quake 1 BSP map importer for the Unity Chisel level-editing toolkit.
- [RCSGQuake1MapImporter](https://github.com/Quixotic7/RCSGQuake1MapImporter) - Add-on to RealtimeCSG that imports Quake 1 `.map` files exported from TrenchBroom, supporting both Valve 220 and Quake Standard map formats.
- [Quake and Hexen II MDL Importer/Exporter for Blender](https://github.com/victorfeitosa/quake-hexen2-mdl-export-import) - Blender 2.8+ add-on for importing and exporting id Software's Quake and Raven Software's Hexen II MDL model format.
- [godot_bsp_importer](https://github.com/jitspoe/godot_bsp_importer) - Godot addon for importing BSP files from the Quake family of engines; full support for Quake 1 BSP/BSP2, with in-progress Quake 2, Quake 3 and Half-Life (GoldSrc) basic level geometry.
- [blender-md3](https://github.com/neumond/blender-md3) - Blender import/export addon for the Quake III Arena MD3 model format.
- [UE4 Quake .map Importer](https://github.com/GoomiiV2/UE4-Quake-Map-Importer) - Unreal Engine 4 plugin to import Quake-style .map files (Quake 1, Half-Life 1, and Quake 3) and convert them into UE4 level geometry.
- [UE4_QuakeImport](https://github.com/Perpixel/UE4_QuakeImport) - Unreal Editor plugin for importing Quake 1 BSP level, MDL model, and LMP 2D graphics files.

###### Format Converters, Viewers & QuakeC Tools

- [PakFu](https://github.com/themuffinator/PakFu) - Cross-platform Qt GUI and CLI archive manager, asset viewer, and converter for idTech-era games (Quake through Quake 4, Doom/Heretic/Hexen, RTCW/Enemy Territory, Jedi Knight, SiN, Kingpin, Heretic II, Doom 3 BFG and others); opens, extracts, and rebuilds PAK, PK3/PK4, WAD2/WAD3, Doom WAD, SiN and Doom 3 BFG `.resources` archives, previews and converts images, IDWAV audio, CIN/ROQ cinematics, and model formats, and decompiles BSP maps to `.map`.
- [LunarViewer](https://github.com/TheEnbyWitch/LunarViewer) - Model viewer for Quake 1 and Hexen 2 (MDL format).
- [noclip.website (Quake)](https://github.com/magcius/noclip.website/tree/main/src/Quake) - In-browser Quake level viewer, parsing id Tech 2 BSP maps and WAD texture lumps (all four episodes plus the deathmatch arenas).
- [any2wad](https://github.com/c-d-a/any2wad) - Converts images to a Quake-compatible .wad file.
- [q1fbfix](https://github.com/c-d-a/q1fbfix) - Fullbright color patches and tools for Quake.
- [md3view](https://github.com/QuinnEbert/md3view) - Cross-platform Quake 3 player model (.md3) viewer with native model rendering.
- [Arbatel](https://github.com/ItEndsWithTens/Arbatel) - A Quake .map viewer with support for func_instance entities.
- [Quinstance](https://github.com/ItEndsWithTens/Quinstance) - Wrapper around VMFInstanceInserter enabling the use of func_instances in Quake maps.
- [mdl2obj](https://github.com/fzwoch/mdl2obj) - Converts Quake 1 MDL model files to Wavefront OBJ model data.
- [DIYQuake](https://github.com/amroibrahim/DIYQuake) - Companion to DIYDoom: step-by-step notes rebuilding the Quake engine with SDL, documenting PAK file structure, the color palette, and Alias model (MDL) skins.
- [paktools](https://github.com/7thSamurai/paktools) - Command-line tools for creating and extracting Quake 1 & 2 PAK archive files.
- [bsp2obj](https://github.com/fzwoch/bsp2obj) - Converts Quake BSP maps to Wavefront OBJ models.
- [mdl2json](https://github.com/fzwoch/mdl2json) - Converts Quake 1 MDL model files to three.js-compatible JSON model data, a sibling tool to the same author's [mdl2obj](https://github.com/fzwoch/mdl2obj) (already listed above).
- [quake-cli-tools](https://github.com/joshuaskelly/quake-cli-tools) - Command-line tools for creating Quake content, including WAD, PAK, BSP, and MDL format converters and inspectors.
- [quake2c](https://github.com/Paril/quake2c) - Quake II game DLL that runs game logic through a QuakeC virtual machine instead of native code.
- [QCVM](https://github.com/erysdren/QCVM) - Bite-sized, embeddable QuakeC virtual machine implementation in C.
- [qpakman](https://github.com/bunder/qpakman) - Command-line tool for managing PAK and WAD archive files from Quake, Quake II, and Hexen II.
- [ProQCC](https://github.com/lbsmith/ProQCC) - QuakeC compiler and decompiler.
- [QMDL-JSON-Tool](https://github.com/KUBA18i/QMDL-JSON-Tool) - Converts Quake-family model formats to and from JSON.
- [Q2SpriteJSONTool](https://github.com/KUBA18i/Q2SpriteJSONTool) - Converts Quake II SP2 sprites to and from JSON.
- [q3bsp2povray](https://github.com/matthewearl/q3bsp2povray) - Converts Quake III BSP map files into POV-Ray scene (SDL) files.
- [PatchMeshToBrushes](https://github.com/themuffinator/PatchMeshToBrushes) - Command-line tool that converts curved `patchDef` meshes in Quake III-era `.map` files into grouped convex `brushDef` brushes (`func_group`, detail flagged, `common/caulk` support faces), with a dry-run preview and an option to keep the original patches.
- [pyquake](https://github.com/matthewearl/pyquake) - Python library and tools for Quake 1 formats and protocols.
  - Modules: `pak` (PAK filesystem), `proto` (network/demo protocol), `blenddemo`/`blendmdl`/`blendbsp` (Blender import of demos, MDL models, and BSP maps).
  - Tools: `demo_viewer` (OpenGL demo playback), `demo_parser` (human-readable demo dump), `pyq_pak_extract` (PAK viewer/extractor). Same author's [dem-transpose](https://github.com/matthewearl/dem-transpose) is a small prototype that transforms `.dem` demo files into a more compressible byte layout, [demsuperimpose](https://github.com/matthewearl/demsuperimpose) overlays the view entity from several other demos as "ghosts" into a base demo, and [showros](https://github.com/matthewearl/showros) patches a demo to replace the invisible "Ring of Shadows" entity model with the player model for viewing. [unusedtex](https://github.com/matthewearl/unusedtex) blacks out texture regions unused by a BSP map's faces to improve compression ratio.
- [RTCW-BSP-Map-Viewer](https://github.com/Helioform/RTCW-BSP-Map-Viewer) - Loads and renders Return to Castle Wolfenstein's original BSP maps.
- [QEBSPEditor](https://github.com/jpiolho/QEBSPEditor) - Browser-based (WebAssembly) tool for editing Quake BSPs for Quake Enhanced and other versions: edit entities, view, replace, and export textures (as WAD or zip), use custom palettes, and adjust global light; supports BSP versions 29, BSP2, and 2PSB.
- [reQuest](https://github.com/malespiaut/request) - Maintenance continuation of Quest, a 3D map editor for Quake-engine games; supports Quake, Quake 2, Quake 3, Hexen 2, Heretic 2, Half-Life, and Sin.
- [Rust Quake](https://github.com/Thinkofname/rust-quake) - Quake level renderer in Rust, reading the original `PAK0.PAK`.
- [Q2-Gladiator-Bot](https://github.com/themuffinator/Quake2-Gladiator-Bot) - Open, buildable reconstruction of the Gladiator Bot botlib for Quake II, recovered from the retail `gladiator.dll` binary so the original bot mod keeps running on modern toolchains.
- [bsp2bmp](https://github.com/QW-Group/bsp2bmp) - Generates a wireframe picture from a Quake BSP map file.
- [Tyr-Utils](https://github.com/sezero/tyrutils) - Git mirror of Kevin Shanahan's command-line utilities for building Quake levels and working with Quake file formats: `qbsp`, `light` and `vis` compile maps, plus `bspinfo` (BSP statistics) and `bsputil` (BSP data manipulation).
- [VisPatch](https://github.com/sezero/vispatch) - Prepares and applies patch files that add water-vis data to Quake maps for transparent water in GLQuake; a revised version of Andy Bay's 1.2a source.
- [MVDparser](https://github.com/QW-Group/mvdparser) - Parses QuakeWorld/MVDSV Multi-View Demo (MVD) files and outputs statistics and information about the recorded match in a customizable format.
- [QWDTOOLS](https://github.com/QW-Group/qwdtools) - Converter for QuakeWorld's `.qwd` single-view demo format.

##### Modern DOOM (id Tech 4 / 6 / 7)

###### DOOM 3 & id Tech 4 Source Ports, Editors & Tools

- [DarkRadiant](https://github.com/codereader/DarkRadiant) - Level editor for The Dark Mod and other idTech 4 / Doom 3-based games, forked from GtkRadiant with extensive improvements for Doom 3, Quake 4, and stealth-game mapping workflows.
- [BFG-Resource-File-Manager](https://github.com/BoBoBaSs84/BFG-Resource-File-Manager) - Tool for extracting, previewing, editing, and creating .resources game archive files in DOOM 3 BFG Edition.
- [dhewm3](https://github.com/dhewm/dhewm3) - Cross-platform Doom 3 GPL source port using SDL, reading and implementing the original game's idTech 4 file formats (models, maps, resource archives).
- [DOOM 3](https://github.com/id-Software/DOOM-3) - id Software's official GPL source code release for DOOM 3, covering the idTech 4 engine's file-reading and rendering code.
- [RBDOOM-3-BFG](https://github.com/RobertBeckebans/RBDOOM-3-BFG) - Actively maintained DOOM 3 BFG Edition source port with a modern DX12/Vulkan renderer and engine features, reading the original BFG Edition's .resources archives and idTech 4 file formats.
- [doom3.gpl (TTimo mirror)](https://github.com/TTimo/doom3.gpl) - Widely-referenced mirror of id Software's DOOM 3 GPL source release, maintained by former id Software programmer TTimo; predates and is more heavily starred than id Software's own official repo.
- [hellforge](https://github.com/klaussilveira/hellforge) - Level editor for HellCore, RBDOOM-3-BFG and dhewm3 idTech 4 engines.
- [NextBroom](https://codeberg.org/NextBroomTeam/NextBroom) - Cross-platform level editor for id Tech-engine based games, forked from TrenchBroom and extended beyond Quake to idTech4-era titles.
- [BFGFontTool](https://github.com/Zbyl/BFGFontTool) - Tool for manipulating Doom 3 and Doom 3 BFG Edition font files.
- [DOOM 3 BFG Edition](https://github.com/id-Software/DOOM-3-BFG) - id Software's official GPL source code release for DOOM 3: BFG Edition, covering the idTech 4 engine's updated file-reading and rendering code.
- [blender-bfg](https://github.com/klaussilveira/blender-bfg) - Blender addon supporting the RBDOOM-3-BFG GLTF mapping workflow.
- [etqw-extractor](https://github.com/klaussilveira/etqw-extractor) - CLI tool to extract and restore original TGA textures from Enemy Territory: Quake Wars DDS cache files.

###### id Tech 4 Documentation & Community Resources

- [iddevnet](https://github.com/dhewm/iddevnet) - Mirror of id Software's iddevnet.com developer documentation, covering id Tech 4 (Doom 3, Quake 4) modding and engine APIs. Also browsable at [iddevnet.dhewm3.org](https://iddevnet.dhewm3.org).
- [awesome-idtech4](https://github.com/FriskTheFallenHuman/awesome-idtech4) - Curated list of source ports, tools, and plugins for idTech4 games (Doom 3, Quake 4, Prey 2006).
- [idtecharchives](https://friskthefallenhuman.github.io/idtecharchives/) - Documentation and research on id Tech 4 engine internals, covering Doom 3, Quake 4 (including Raven Software's engine changes), and Prey (2006).
- [modWiki](https://github.com/OpenTechEngine/modWiki) - Git mirror of modwiki.dhewm3.org, a community wiki documenting idTech 4 (Doom 3) modding, scripting, and file formats.

###### DOOM (2016), Eternal & id Tech 6/7 Tools

- [valen](https://github.com/jandk/valen) - Multi-game resource extractor with GUI. Supports DOOM Eternal, Dark Ages, Great Circle, and other id Software games. Features file browser, bulk export, texture/model/material/skeleton/animation extraction, and preview capabilities.
  - Formats: DDS, PNG, GLTF (export).
- [EternalResourceExtractor](https://github.com/brunoanc/EternalResourceExtractor) - Extracts files from DOOM Eternal `.resources` and `.wad7` archive files.
- [AutoHeckinTextureConverter](https://github.com/brunoanc/AutoHeckinTextureConverter) - Converts DOOM Eternal `.btex` texture files to standard image formats.
- [IdTech.EntitiesFileParser](https://github.com/dcealopez/IdTech.EntitiesFileParser) - C# library for parsing and writing `.entities` files from id Tech 6 (DOOM 2016) and id Tech 7 (DOOM Eternal).
- [idSaveDecompressor](https://github.com/brongo/idSaveDecompressor) - Tool for decompressing DOOM Eternal saved games (game_duration.dat); enables parsing and editing save data with hex editors. See also [DOOMSaveManager](https://github.com/GoobyCorp/DOOMSaveManager), a GUI tool for importing/exporting DOOM Eternal saves.
- [DOOMExtract](https://github.com/emoose/DOOMExtract) - Command-line tool for extracting and repacking DOOM (2016) resource files.
- [tinycast](https://github.com/jandk/tinycast) - Library for reading id Software's .cast animation/scene container format, used in DOOM Eternal and other id Tech 7 games.
- [SAMUEL](https://github.com/brongo/SAMUEL) - Cross-platform GUI asset extractor for DOOM Eternal.
- [Snapmap+](https://github.com/doom-snapmap/snapmap-plus) - Clean-room reimplementation of SnapHak, a closed-source companion tool for DOOM (2016)'s in-game SnapMap level editor, extending the original's rawmap/decl file handling with new console commands and a WebView2-based editor window.
- [snapmap-midi](https://github.com/doom-snapmap/snapmap-midi) - Compiles a MIDI file into a playable music map for DOOM (2016)'s SnapMap editor.

##### id Tech Legacy Tools & Downloads (ModDB)

- [Doom 3 model import tutorial files](https://www.moddb.com/games/doom-iii/downloads/doom-3-model-import-tutorial-files) - Sample files for use with the Doom 3 model import tutorial on ModDB.
- [Doom 3 Compatibility Tool Mod](https://www.moddb.com/games/doom-iii/downloads/doom-3-compatibility-tool-mod) - Compatibility tool for Doom 3. Tool by Dafama.
- [Doom 3 - Quake 3 Map Converter](https://www.moddb.com/games/doom-iii/downloads/doom-3-quake-3-map-converter) - Use this tool to convert your favorite Quake 3 maps to Doom 3's (Quake 4 also) new format. The tool can also convert textures to the new format.
- [Doom 3: ROE (XBOX) .gfc extract](https://www.moddb.com/games/doom-iii/downloads/doom-3-roe-xbox-gfc-extract) - QuickBMS script for extracting .gfc files from Doom 3: Resurrection of Evil's Xbox port.
- [Doom maps Converter 1.4](https://www.moddb.com/games/doom-iii/downloads/doom-maps-converter-14) - Converter of old Doom maps to maps for Doom 3, made from QuakeDM sources.
- [DOOM Audio Tools](https://www.moddb.com/games/doom-4/downloads/doom-audio-tools) - Dragon UnPACKer, Wwise ADPCM Converter, Batch script for handling multiple files. Guide below.
- [Export Font To Doom 3 v1.02](https://www.moddb.com/games/doom-iii/downloads/export-font-to-doom-3-v102) - A command-line application that exports standard fonts into Doom 3's font format. Created by Grant Davis. Includes source code.
- [.GOB & global.d3tfull unpacker (Doom III)](https://www.moddb.com/games/doom-iii/downloads/gob-globald3tfull-unpacker)
- [IdTech4 File Unpacker 1.5 (Doom III)](https://www.moddb.com/games/doom-iii/downloads/idtech4-file-unpacker-15) - Automatic file extraction tool for IdTech4 engine (Trinity) games. Supports: Doom 3, Doom 3: Resurrection of Evil, Quake 4, Prey, Enemy Territory: Quake Wars, and Wolfenstein (v1.5).
- [Lightwave to MD5 converter (Doom III)](https://www.moddb.com/games/doom-iii/downloads/lightwave-to-md5-converter)
- [Daikatana to Quake 2 model converter](https://www.moddb.com/games/daikatana/downloads/daikatana-to-quake-2-model-converter) - Includes source code.
- [Quake 1 Model Viewer v0.50 alpha](https://www.moddb.com/games/quake/downloads/quake-1-model-viewer-v050-alpha) - Model viewer utility for Quake 1 modders by Unkle Mike. Based on original MD2V code by Mete Ciragan with features similar to Half-Life Model Viewer. Updated November 1, 2018 (v0.50 alpha).
- [Skyboxer - Map-to-Skybox Tool for Quake (1.0)](https://www.moddb.com/games/quake/downloads/skyboxer-a-map-to-skybox-tool-for-quake-10) - Simple mod/tool for creating skyboxes from Quake maps (v1.0).
- [Adjusted MD5 blender exporter (Quake III Arena)](https://www.moddb.com/mods/project-rdx/downloads/adjusted-md5-blender-exporter) - Modified MD5 exporter for Blender that allows exporting animations without certain channels. Some bones move while others remain static, which is crucial for combining animations.
- [Q3-Games Model Tool v1.6.0 (Quake III Arena)](https://www.moddb.com/games/quake-iii-arena/downloads/q3-games-model-tool-v160) - Model tool for Q3-Engine based games (formerly ET Model Tool). Tool for playermodel-makers, mappers, and modders (v1.6.0).
- [RtCW – SDK Editing Tools v1.1 (Return to Castle Wolfenstein)](https://www.moddb.com/mods/rtcw-classic-cooperative-campaign/downloads/rtcw-sdk-editing-tools-v11) - Editing tools for creating and editing Return to Castle Wolfenstein levels for solo and multiplayer modes. Includes WolfRadiant editor (updated version of QERadiant/GTK Radiant). Not the full SDK (v1.1).
- [RTCW .bsp to .map Converter (Return to Castle Wolfenstein)](https://www.moddb.com/games/return-to-castle-wolfenstein/downloads/rtcw-bsp-to-map-converter) - RtCW .BSP to .MAP Converter - A very handy map-making tool for Return to Castle Wolfenstein mappers, either new or experienced. The "comdlg32.ocx" file is also included in the download, with instructions on how to install it. Usage Information # Run DeBSP.EXE and [Browse] for the BSP file you wis...
- [Wolfenstein SPK & MPK Extractor v0.2](https://www.moddb.com/games/wolfenstein/downloads/wolfenstein-spk-mpk-extractor-v02) - The Wolfenstein SPK/MPK Extractor made by Bellox902 is a powerful tool to extract .spk/.mpk gamefiles from the Wolfenstein Game. These files contain all kinds of stuff like the music (.mp3), bink videos (.bik) or textures (.dds). The latest 0.2 version can also pack mp3 files into spk/mpk!
- [Blender Terrain scripts (Quake III Arena)](https://www.moddb.com/mods/project-rdx/downloads/blender-terrain-scripts) - Blender scripts to turn an elevation grid into a terrain in .map format to be used in Radiant.
- [Blocks II v0.2 Editing Package (Doom II)](https://www.moddb.com/mods/blocks-of-doom-ii/downloads/blocks-ii-v02-editing-package) - Editing package with all tools needed to create levels for Blocks of Doom II (v0.2).
- [Blender MD3 Import-Export Tool](https://www.moddb.com/games/quake-iii-arena/downloads/blender-md3-import-export-tool) - MD3 import/export script for Blender with shader path configuration, material name mapping, animation frame export, and UV image preview.
##### Rise of the Triad

- [taradino](https://github.com/fabiangreffrath/taradino) - Source port of Rise of the Triad that duplicates the original 1994 game's functionality using its original registered/shareware data files.
- [drott](https://github.com/darkhaven3/drott) - Rise of the Triad source port (based on rottexpr/icculus's ROTT port) reading the original game's WAD/RTL data, adding expanded texture and sky-definition limits for user maps.
- [rott (2002 official source)](https://github.com/videogamepreservation/rott) - Preserved copy of the official 2002 Rise of the Triad source code release.
- [USDC](https://github.com/Blzut3/USDC) - Compiler for the Universal Strife Dialog Format (USDF), targeting vanilla Strife's proprietary binary dialog-script format (id Tech 1).

#### Idea Factory

- [Pac_Utils](https://github.com/usagirei/Pac_Utils) - C++ unpack, pack and patch utilities (with the libPac library) for Idea Factory `DW_PACK` `.pac` archives, including their compressed entries; the patch tool replaces only files already present in an archive.
- [hkki](https://github.com/xyzz/hkki) - Format notes on the uncompressed STCM2L script bytecode used by Hakuoki, with C++ source for parsing and handling these script files.

##### Date A Live

- [DALTools](https://github.com/thesupersonic16/DALTools) - Collection of tools for modifying files from the Date A Live visual novels, mainly Rio Reincarnation and Ren Dystopia.
  - Tools: PCKTool (unpacks/repacks `.pck` archives, including PS3 big-endian variants), TEXTool (extracts/rebuilds `.tex` texture sheets and frames), STSCTool (disassembles/reassembles Rio Reincarnation's `.bin` scripts), FontEditor, ScriptDatabaseEditor (`database.bin` editor), ScriptDialogueEditor (integrated GUI for script text editing/translation with live preview), TableEditor (Ren Dystopia table files).
- [DALLLBDump](https://github.com/Escartem/DALLLBDump) - Dump of textures, audio, video, and code from Date A Live: Love Limit Break, the mobile gacha game.

##### Edel Blume

- [blumeutil](https://github.com/robbie01/blumeutil) - Edel Blume (PS2) translation toolkit: analyzes and patches the ISO's `script.uni` container and STCM2 dialogue scripts (IDs 100-199) into a database with machine-translation assist and a web editor, plus a standalone STCM2 disassembler and an `art` tool for extracting art from the game's UNI2 containers (back.uni, chara.uni, etc.uni, memory.uni, system.uni).
  - See also the author's [stcm2-asm](https://github.com/robbie01/stcm2-asm), a byte-accurate STCM2/STCM2L disassembler/assembler covering Edel Blume and four other Otomate/Idea Factory visual novels (listed under Script Collections & Multi-Game Tools).

##### Hidamari Sketch: Dokodemo Sugoroku x 365

- [miyako](https://github.com/minirop/miyako) - Tool to convert graphics from Hidamari Sketch: Dokodemo Sugoroku x 365 (Nintendo DS).
- [yuno](https://github.com/minirop/yuno) - Tool to extract and translate strings from Hidamari Sketch: Dokodemo Sugoroku x 365 (Nintendo DS).

#### Illusion

*Koikatsu, Koikatsu Sunshine, Honey Select, AI Girl, PlayHome.*

- [KK-Blender-Porter-Pack](https://archive.org/details/kkbp-importer-8.0.2) - Exporter/importer pack for Koikatsu characters in Blender with near-perfect mesh and texture replication, facial shapekeys, Rigify armature, and FBX export.
  - Games: Koikatsu, Koikatsu Sunshine.
  - See also [gitgoon mirror](https://gitgoon.dev/kkbp-dev/KKBP_Importer).
- [KKBP_Exporter](https://gitgoon.dev/kkbp-dev/KKBP_Exporter) - In-game BepInEx plugin that exports Koikatsu character cards as PMX models with textures and skeletal data for use with KKBP Importer or MMD tools.
- [KoikatsuModdingTools](https://gitgoon.dev/IllusionMods/KoikatsuModdingTools) - Unity Editor toolkit for creating Koikatsu mods including clothing, accessories, hair, maps, and custom shaders. Supports asset bundle building, FBX import with bone optimization, and uTinyRipper integration.
- [ZipStudio](https://gitgoon.dev/IllusionMods/ZipStudio) - Utility for converting Koikatsu hard-mods to sideloader format with automatic list conversion to CSV and manifest editing.
- [kk-save-edit](https://github.com/hozuki/kk-save-edit) - Browser-based save file editor for Koikatsu.
- [KoikatuGameSaveEditor](https://github.com/hozuki/KoikatuGameSaveEditor) - Save game editor for Koikatsu.
- [koikatsu-card-texture-tool](https://github.com/EeEeX4/koikatsu-card-texture-tool) - GUI and command-line tool that recompresses and downsizes the textures embedded in Koikatsu coordinate and character cards (`.png`), with per-part settings, lossless recompression options and presets.
- [archival_illusion_viewer](https://github.com/coreynguyen/archival_illusion_viewer) - Archival re-upload of a legacy Illusion Viewer tool for browsing assets across multiple Illusion titles.
- [mxs_illusion_aga_pc](https://github.com/coreynguyen/mxs_illusion_aga_pc) - 3ds Max MaxScript for importing `.x` 3D model files from Illusion's AGA (PC).
- [KKManager](https://github.com/IllusionMods/KKManager) - Mod, plugin, and character card manager for games by Illusion that use BepInEx. Browses installed zipmods/plugins/cards, auto-detects and installs mod updates, and supports drag-and-drop card/scene loading.
- [IllusionModdingAPI](https://github.com/IllusionMods/IllusionModdingAPI) - Base modding API for games made by Illusion (PHAPI, KKAPI, ECAPI, AIAPI, HS2API, KKSAPI); abstracts the games' character card and save/load data handling, used as the foundation for most other plugins in this ecosystem.
- [TranslationTools](https://github.com/IllusionMods/TranslationTools) - Toolkit for translating Illusion games.
  - Features: TextDump extracts untranslated strings from game assets to text files; TextResourceRedirector overrides individual localized assets at runtime; TranslationSync reformats and merges translation files between versions.

#### Imageepoch

##### Black Rock Shooter (PSP)

- [BRS-Tools](https://github.com/priverop/BRS-Tools) - Unpacks non-compressed BIN/GZ archives and extracts/inserts text for Black★Rock Shooter (PSP).

##### Luminous Arc

- [LA-Tools](https://github.com/priverop/LA-Tools) - Unpacks and repacks Luminous Arc's (Nintendo DS) `.iear` archive format; the same repo also includes a separate text extractor/inserter for the DS game My Healthy Cooking Coach.

#### IdolFX (IMP)

- [IdolFX-IMP-Formats](https://github.com/Nielk1/IdolFX-IMP-Formats) - Research and format documentation for IMP (2001), a fighting game originally distributed on 50 separate single-character discs.
  - Formats: ANB (model data), AMB (movement data), DAT (object/attack parameters), documented via 010 Editor/ImHex `.hexpat` templates.

#### Impressions Games

- [Citybuilding tools](https://github.com/bvschaik/citybuilding-tools) - Utilities for the game files shared across the Impressions/BreakAway Games citybuilding series made between 1998 and 2002.
  - Tools: EngConverter (converts .eng language files to/from XML for easy editing), SGReader (extracts .sg2/.sg3/.555 graphics archives to PNG).
- [CBMappers](https://github.com/bvschaik/citybuilding-mappers) - Collection of programs (Caesar3Mapper, PharaohMapper, ZeusMapper, EmperorMapper) to extract PNG images from the game files of Caesar 3, Pharaoh, Zeus, and Emperor.

##### Caesar II

- [Caesar II Reconstruction](https://github.com/second-impressions/caesar2-reconstruction) - Byte-exact reconstruction of Caesar II (1995, Impressions Games), the predecessor to Caesar III. See also the same project's [Caesar II Port](https://github.com/second-impressions/caesar2-port), a portable continuation of the reconstruction.

##### Caesar III

- [Julius](https://github.com/bvschaik/julius) - Open-source re-implementation of Caesar III; requires the original game's data files (purchasable from GOG/Steam) to run and produces saves 100% compatible with the original game.
  - Features: Cross-platform (Windows, Linux, macOS, PS Vita, Switch, Android, browser), widescreen/windowed mode, high-quality MP3 music support.
  - See also [Augustus](https://github.com/Keriew/augustus), an actively developed fork prioritizing new gameplay features (roadblocks, market orders, global labor pools, expanded warehouse storage, higher limits, zoom) over Julius's vanilla-compatible focus; Augustus saves are not compatible back with Julius or the original game.
- [Caesar3Unpacker](https://github.com/bvschaik/caesar3unpacker) - macOS utility to unpack the Caesar III GOG/CD-ROM installer files, extracting what's needed to run Julius.
- [c3-pkware-example](https://github.com/bvschaik/c3-pkware-example) - Example program demonstrating PKWare decompression of the Caesar III .sav save format, printing an ASCII-art map of the decoded terrain.

##### Pharaoh

- [Ozymandias](https://github.com/Banderi/Ozymandias_Julius) - Fork of the Julius/Augustus Caesar III engine adapted to run Pharaoh (1999) and its Cleopatra expansion instead, reading the original game's data files and loading original save games.
  - See also the same author's from-scratch [Ozymandias (Godot rewrite)](https://github.com/Banderi/Ozymandias), an early-stage reimplementation targeting Pharaoh/Zeus in the Godot engine instead of forking Julius/Augustus; also requires the original game files.

#### Mind Shear Software (In Pursuit of Greed)

- [xGreed](https://github.com/jval1972/xGreed) - Source port of In Pursuit of Greed (1996, Mind Shear Software, published by Softdisk), reading the original DOS game's data files.

#### Incoming

- [incoming-reader](https://github.com/sapphire-bt/incoming-reader) - JavaScript (browser and Node.js/TypeScript) plugin for reading and writing the `.IAN` 3D model format of Incoming (1998), with a Python script for batch OBJ export and OBJ-to-IAN conversion.

#### Incredible Technologies

- [PowerUpBaseball](https://github.com/DickBlackshack/PowerUpBaseball) - Recovered source code and original art/sound data for Power Up Baseball, an unreleased Incredible Technologies arcade title, recovered from Chris Oberth's personal archives.
##### Carnival King

- [CarnivalKingExtraction](https://github.com/Retiu/CarnivalKingExtraction) - Tools for extracting audio from the Incredible Technologies Carnival King arcade game's CHD ROM.

#### iNiS

- [Murugo/Misc-Game-Research (Gitaroo Man)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Gitaroo%20Man) - Reverse engineering notes for Gitaroo Man (PS2).
- [blender3d_xeios](https://github.com/boringhexi/blender3d_xeios) - Blender importer for Xeios engine games including Gitaroo Man (PS2) and まげる つける はしーる.

#### Inkle

- [sorcery-xtractobb](https://github.com/flamewing/sorcery-xtractobb) - Extracts Inkle's "Sorcery!" Android OBB archives.
- [inkcpp](https://github.com/JBenda/inkcpp) - C++ runtime for Inkle's "Ink" narrative scripting language, including a JSON-to-binary compiler for the compiled story format used across Inkle's games.

#### Inland Productions

##### WCW Nitro

- [nitro (decomp)](https://github.com/martinbean/nitro) - Matching decompilation of WCW Nitro (PS1), including an RLE decoder for WGAME.BIN/WMENU.BIN.

##### WCW/nWo Thunder

- [thunder (decomp)](https://github.com/martinbean/thunder) - Matching decompilation of WCW/nWo Thunder (PS1).

#### Innerloop Studios

- [IGI2ModTool](https://github.com/REDxEYE/IGI2ModTool) - Modding tools for I.G.I.-2: Covert Strike file formats.
- [igipy](https://github.com/artiom-rotari/igipy) - Python CLI tool for converting proprietary Project I.G.I and Project I.G.I 2: Covert Strike file formats into standard formats (BMP, FBX, TGA); a direct successor and refactor of NEWME0/Project-IGI, published on PyPI.
- [project-igi-toolkit](https://github.com/heaven-hm/project-igi-toolkit) - All-in-one modding toolkit for Project I.G.I., editing map, AI, graph, level, and mission data.
  - See also [project-igi-editor](https://github.com/heaven-hm/project-igi-editor), a professional 3D level editor; [project-igi-converter (igi1conv)](https://github.com/heaven-hm/project-igi-converter), a standalone command-line converter/inspector for the game's 2D/3D/binary asset formats; [project-igi-qvm-editor](https://github.com/heaven-hm/project-igi-qvm-editor) (archived), a tool for Project I.G.I. 1 & 2 QVM game files; and [project-igi-research-data](https://github.com/heaven-hm/project-igi-research), reverse-engineering research notes on the game's internals.
- [IGI2_MTP_Converter](https://github.com/FeritCoderTR/IGI2_MTP_Converter) - Compiles the DAT file format and decodes the MTP file format used by I.G.I.-2: Covert Strike.
- [cpp_igi2_mefview](https://github.com/coreynguyen/cpp_igi2_mefview) - 3D viewer for I.G.I.-2: Covert Strike's MEF model file format.
- [Project-IGI-Terrain](https://github.com/hjcminus/Project-IGI-Terrain) - OpenGL reimplementation of Project I.G.I.'s terrain rendering system, based on analysis of the decompiled igi.exe.

#### Innocent Grey

- [IG_tools](https://github.com/lennylxx/IG_tools) - Tools to process and extract game files from Innocent Grey visual novels (Kara no Shoujo, Cartagra, Caucasus), built for use alongside Noesis.
- [igapack](https://github.com/RikuKH3/igapack) - Unpacker/packer for the `.iga` archive files used by Innocent Grey games.

#### Intelligent Systems

- [fe11-us (decomp)](https://github.com/Eebit/fe11-us) - Matching decompilation of Fire Emblem: Shadow Dragon (NDS, USA).
  - See also [fe11us-arm9](https://github.com/MokhaLeee/fe11us-arm9), a companion decompilation of the arm9.bin overlay for the same release.
- [fireemblem8u (decomp)](https://github.com/FireEmblemUniverse/fireemblem8u) - Decompilation/disassembly of Fire Emblem: The Sacred Stones (GBA).
- [fireemblem6j (decomp)](https://github.com/FireEmblemUniverse/fireemblem6j) - Decompilation of Fire Emblem: The Binding Blade (GBA).
- [fe7_us (decomp)](https://github.com/StanHash/fe7_us) - Disassembly/partial decompilation of Fire Emblem (GBA, USA) — the Western localization known as Fire Emblem: The Blazing Blade.
- [FireEmblem7J (decomp)](https://github.com/MokhaLeee/FireEmblem7J) - Decompilation of Fire Emblem: Rekka no Ken, the Japanese release of The Blazing Blade (GBA).
- [mgfembp (decomp)](https://github.com/StanHash/mgfembp) - Decompilation of the Mysterious GBA Fire Emblem MultiBoot Payload.
- [fe1 (disasm)](https://github.com/StanHash/fe1) - Disassembly of Fire Emblem: Ankoku Ryu to Hikari no Tsurugi ("Shadow Dragon and the Blade of Light", Famicom).
- [gbfe2-stuff](https://github.com/StanHash/gbfe2-stuff) - Reverse-engineering notes, ROM map, map data tables, dump scripts and a partial disassembly of "gbfe2", Waixing's bootleg Fire Emblem Gaiden remake/port for the Game Boy Color (also known as "Sheng Huo Hui Zhang").
- [fe2 (disasm)](https://github.com/minirop/fe2) - Disassembly of Fire Emblem Gaiden (NES/Famicom).
  - See also [fe2-tiled](https://github.com/minirop/fe2-tiled), which converts Tiled (.tmx) maps into the game's binary map format.
- [fe3 (disasm)](https://github.com/minirop/fe3) - Disassembly of Fire Emblem: Mystery of the Emblem (SNES).
  - See also [fe3-png](https://github.com/minirop/fe3-png) (extracts the game's compressed graphics), [fe3-text](https://github.com/minirop/fe3-text) (converts/decompiles its dialogue and string lists), [sable-text-converter](https://github.com/RobertTheSable/sable-text-converter), an extensible text converter developed for the same game (itself fed by [ttf2bpp](https://github.com/RobertTheSable/ttf2bpp), a SNES 2BPP font converter), [fe3-tileset-dumper](https://github.com/RobertTheSable/fe3-tileset-dumper), which dumps and decompresses the game's tilesets via Lunar Compress, [fe3-menu-font-editor](https://github.com/RobertTheSable/fe3-menu-font-editor), a Qt-based menu tileset/font builder sharing its codebase with the Thracia 776 tile editor below, [fe3spcinitdumper](https://github.com/RobertTheSable/fe3spcinitdumper), which separates out the game's SPC sound-driver code for disassembly with tools like [spcdas](https://github.com/gocha/spcdas), and [reverseFE3](https://github.com/RobertTheSable/reverseFE3), which generates a reverse-recruitment ROM patch.
- [nightmare-modules](https://github.com/RobertTheSable/nightmare-modules) - Nightmare Module editor definitions for Fire Emblem: Mystery of the Emblem and Fire Emblem: Thracia 776 (SNES), distinct from the GBA-focused Fire-Emblem-Nightmare-Modules collection above.
- [fe5-tile-edit](https://github.com/RobertTheSable/fe5-tile-edit) - Tileset and world-map editor for Fire Emblem: Thracia 776 (SNES).
  - See also [ThraciaMapConverter-QT](https://github.com/RobertTheSable/ThraciaMapConverter-QT) (archived), which converts Tiled maps into the game's map format, and [thracia-unit-order](https://github.com/RobertTheSable/thracia-unit-order), an Asar patch reordering the preparation-screen unit list.
- [fe4-inheritance](https://github.com/RobertTheSable/fe4-inheritance) - Asar patch removing fixed character pairings in Fire Emblem: Genealogy of the Holy War (SNES).
- [snesfe-2rn](https://github.com/RobertTheSable/snesfe-2rn) - Asar patches adding the GBA-style 2RN hit-rate calculation formula across the SNES Fire Emblem games (Mystery of the Emblem, Genealogy of the Holy War, Thracia 776).
- [Kid-Icarus-JSON-Parser](https://github.com/onepiecefreak3/Kid-Icarus-JSON-Parser) - JSON parser for Kid Icarus file formats.
- [FEAT](https://github.com/SciresM/FEAT) - Fire Emblem Archive Tool for automatically extracting data from 3DS Fire Emblem archives.
- [FEIF_ARC](https://github.com/GovanifY/FEIF_ARC) - Fire Emblem If ARC re/unpacker.
- [Event-Assembler](https://github.com/TimoVesalainen/Event-Assembler) - Nintenlord's event code assembler for Fire Emblem GBA games, compiling human-readable event scripts into the games' proprietary event bytecode. See also [ColorzCore](https://github.com/FireEmblemUniverse/ColorzCore), a from-scratch rewrite of the assembler's Core.exe, and [EAFormattingSuite](https://github.com/FireEmblemUniverse/EAFormattingSuite), a suite for formatting data into an Event Assembler-insertable format, and [StanHash/EventAssembler](https://github.com/StanHash/EventAssembler), a Linux/WSL build script for an Event Assembler distribution (ColorzCore, lyn, the EA Formatting Suite, a compress tool) for use in buildfiles.
- [FEBuilderGBA](https://github.com/FEBuilderGBA/FEBuilderGBA) - All-in-one Fire Emblem GBA ROM editor covering maps, events, portraits, palettes, class/character data, and dozens of other game data tables, with a built-in patch installer. Originally created by [laqieer](https://github.com/laqieer/FEBuilderGBA).
- [FE_GBA_Function_Library](https://github.com/laqieer/FE_GBA_Function_Library) - Function signature library identifying known library/engine functions embedded in Fire Emblem GBA ROMs, easing disassembly and hacking.
- [fe-maps](https://github.com/laqieer/fe-maps) - Web-published GBA Fire Emblem data maps (RAM/ROM structures, struct/enum definitions) used across the FE modding toolchain.
  - Underlying data: [fe-info](https://github.com/laqieer/fe-info), forked from [biosp4rk/mf-zm-info](https://github.com/biosp4rk/mf-zm-info) (originally for Metroid Fusion/Zero Mission) and repurposed for Fire Emblem.
- [GBA_Graphics_Editor](https://github.com/laqieer/GBA_Graphics_Editor) - Editor for palettes, graphics, and tile-set-arrangement (TSA) data in GBA games, continuing NintenLord's original hacking utilities.
- [Fire-Emblem-Nightmare-Modules](https://github.com/laqieer/Fire-Emblem-Nightmare-Modules) - Collection of Nightmare Module editor definitions for the Fire Emblem series.
  - See also [nightmare](https://github.com/laqieer/nightmare), an online modularized ROM editor and successor to the original Nightmare/Nightmare 2 module system.
- [eventiel_fe8](https://github.com/boviex/eventiel_fe8) - Web-based event script editor for Fire Emblem 8, ported from Cedar Nyx's Eventiel for FE7 with data sourced from Nightmare Modules.
- [FE-ROM-Hack-Database](https://github.com/laqieer/FE-ROM-Hack-Database) - CRC-32 checksum database of Fire Emblem ROM hacks, for identifying hacks in ROM managers.
- [FE17-DOC](https://github.com/laqieer/FE17-DOC) - Documentation of extracted text and data from Fire Emblem Engage (Switch).
- [Astra](https://github.com/thane98/Astra) - WIP editor for Fire Emblem: Engage game data, covering core data like character, class, and item stats.
  - [astra-msbt](https://github.com/thane98/astra-msbt) - CLI for extracting and importing FE: Engage MSBT text, built on [astra-formats](https://github.com/thane98/astra-formats), a Rust library with modules for bundles, MSBT, and texture atlases.
- [Cobalt](https://github.com/Raytwo/Cobalt) - Import tool for Fire Emblem: Engage game data.
- [Fire-Emblem-Fates-Dual-Dub](https://github.com/Raytwo/Fire-Emblem-Fates-Dual-Dub) - Assembly patches adding a dual-dub option (Japanese/English voice mixing) to Fire Emblem Fates.
- [fe-decomp-portal](https://github.com/laqieer/fe-decomp-portal) - Portal site indexing active Fire Emblem GBA decompilation and modding projects.
- [FE-Clib-Decomp](https://github.com/laqieer/FE-Clib-Decomp) - Generates linker scripts and lyn/Event Assembler symbol references from the FE6/FE8U/FE8J decompilation ELFs, for use by downstream ROM hacking projects.
- [Exalt](https://github.com/thane98/Exalt) - Script editor for 3DS-era Fire Emblem games.
  - [exalt-rs](https://github.com/thane98/exalt-rs) - Rust port of Exalt with separate assembler, compiler, decompiler, and disassembler crates.
- [Universal-FE-Randomizer](https://github.com/lushen124/Universal-FE-Randomizer) - Randomizer supporting Fire Emblem 4, 6, 7, 8, and the Tellius/Elibian Nights ROM hacks.
- [fire-editor-awakening](https://github.com/Danius88/fire-editor-awakening) - Save editor for Fire Emblem Awakening (3DS).
- [FESOV-SaveEditor](https://github.com/vince11/FESOV-SaveEditor) - Minimal character save editor for Fire Emblem Echoes: Shadows of Valentia (3DS).
- [FEHDataExtractor](https://github.com/Lorenzooone/FEHDataExtractor) - Generic multipurpose extractor for Fire Emblem Heroes (mobile) data.

- [FE-CHAX](https://github.com/StanHash/FE-CHAX) - Collection of ASM/C code patches ("wizardry") and an EA/lyn/C build setup for hacking Fire Emblem 8 (US).
  - See also [Simple_C_HAX](https://github.com/boviex/Simple_C_HAX), a simplified, beginner-friendly fork/introduction to the same FE8U C build setup.
- [fe8u-cskillsys-kernel](https://github.com/MokhaLeee/fe8u-cskillsys-kernel) - Modernized C-based skill system kernel for the FE8U SkillSystem, built on FE-CHAX.
- [FE-PyTools](https://github.com/StanHash/FE-PyTools) - Collection of Python 3 tools for make/Event Assembler Fire Emblem GBA buildfiles, most outputting EA events: `c2ea` (CSV + NMM definitions to events), `tmx2ea`/`tmx1ea` (Tiled `.tmx` maps to map installers), `text-process` (text to `.fetxt` installers) and `portrait-process`.
  - See also [tmx2ea](https://github.com/StanHash/tmx2ea), a standalone fork of the Tiled-to-Event-Assembler map converter that generates per-map and master installers and exposes chapter-data properties as Tiled layer properties.
- [paragon](https://github.com/thane98/paragon) - Toolkit for editing various 3DS/Switch-era Fire Emblem games.
- [Lumina](https://github.com/thane98/lumina) - GUI file converter for Fire Emblem: Path of Radiance / Radiant Dawn (FE9/FE10) Tellius files, packing and unpacking `.cmp` archives and `.m` files, converting `.bin` files to a text format, and LZ10 compression/decompression.
  - [fe9cmp](https://github.com/thane98/fe9cmp) - Command-line tool that LZ10-decompresses and unpacks FE9/FE10 `.cmp` archives.
  - [fe10msg](https://github.com/thane98/fe10msg) - Extracts FE10 `.m` text files to YAML and imports the edited YAML back.
  - [fe-sheet-list](https://github.com/thane98/fe-sheet-list) - Dumps sheet lists and struct metadata from FE9-FE15 `.bin` files.
  - [mila](https://github.com/thane98/mila) - Rust library for common FE13-FE15 formats, including `.bin` archive serialization and LZ compression.
- [Ignis](https://github.com/thane98/ignis) - Randomizer for Fire Emblem Fates (FE14) that works from an extracted RomFS, randomizing stats, chest and village items, and join order.

##### Panel de Pon

- [PDPTools](https://github.com/April93/PDPTools) - Decrypts and extracts files from Panel de Pon in the Nintendo Puzzle Collection (GameCube); the author notes it should also work on the shared-codebase Pokémon Puzzle League (N64).

##### Fire Emblem: Three Houses

- [Throne-of-Knowledge](https://github.com/three-houses-research-team/Throne-of-Knowledge) - Central repository for Fire Emblem: Three Houses reversing and documentation.
- [010-binary-templates (FE3H)](https://github.com/three-houses-research-team/010-binary-templates) - 010 Editor templates for Fire Emblem: Three Houses file formats (G1T, G1M, etc.).
  - See also [Reichard-III's fork](https://github.com/Reichard-III/FE3H-010-Binary-Templates-Fork) with faster parsing, more accurate enum sizing, and new format discoveries.
- [th-hack-tools](https://github.com/HeartHeroDE/th-hack-tools) - Toolkit for hacking and editing data in Fire Emblem: Three Houses.
- [G1Tool](https://github.com/three-houses-research-team/G1Tool) - GUI for creating and editing Koei Tecmo G1T texture files.
- [THAT](https://github.com/three-houses-research-team/THAT) - Three Houses Archive Tool: compresses/decompresses game files, unpacks and packs `.bin` and `.bin.gz` archives, and patches the `INFO0`/`INFO2` files to register modded files.
- [bsic](https://github.com/three-houses-research-team/bsic) - Battle map editor (Java GUI with tile, BAI and BSI editors) plus a command-line converter between binary BSI scripts and a readable DSL.
- [koeipy](https://github.com/3096/koeipy) - Python library for Koei Tecmo Engine file formats, specifically targeting Fire Emblem: Three Houses.
- [Progenitor](https://github.com/three-houses-research-team/Progenitor) - All-in-one data editor for Fire Emblem: Three Houses.
- [fe3h-editor](https://github.com/imouto1994/fe3h-editor) - Save editor for Fire Emblem: Three Houses.

##### Paper Mario 64

*See also [Fast3d/F3dex (N64)](middleware.md#fast3df3dex-n64) for graphics format tools used in this game.*

- [papermario (decomp)](https://github.com/pmret/papermario) - Matching decompilation of Paper Mario (Nintendo 64).
- [leaflitter (decomp)](https://github.com/darxoon/leaflitter) - Work-in-progress decompilation of Paper Mario: Sticker Star.
- [noclip.website (PM64)](https://github.com/magcius/noclip.website/tree/main/src/PaperMario64) - In-browser Paper Mario 64 map viewer.
- [star-rod](https://github.com/z64a/star-rod) - Modding tool for Paper Mario 64 including map editor and script tools.
- [Hack64 Paper Mario](https://hack64.net/wiki/doku.php?id=paper_mario) - Documentation for Paper Mario 64 file formats and data structures.
- [Mamar](https://github.com/bates64/mamar) - Paper Mario (N64) music editor; parses and extracts BGM and SBN audio file formats.
- [Merlon](https://github.com/bates64/merlon) - Mod manager for the Paper Mario (N64) decompilation that packages and applies mods built on the decomp source.
- [papermario-dx](https://github.com/bates64/papermario-dx) - Enhanced fork of the Paper Mario (N64) decompilation providing an improved engine base for romhacks.
- [midi2bgm](https://github.com/KernelEquinox/midi2bgm) - MIDI to BGM converter for Paper Mario (N64).
- [Kalmar](https://github.com/imaandrew/kalmar) - Compiler for Paper Mario 64's reverse-engineered scripting language, a companion tool to star-rod.

##### Paper Mario: TTYD / Super Paper Mario

*See also [JSYSTEM](middleware.md#jsystem-gamecubewii) for additional format tools used in these games.*

- [ttyd (decomp)](https://github.com/doldecomp/ttyd) - Matching decompilation of Paper Mario: The Thousand-Year Door.
- [spm-decomp (decomp)](https://github.com/seekyct/spm-decomp) - Matching decompilation of Super Paper Mario.
- [SpmViewer](https://github.com/follycake/SpmViewer) - Tool for viewing Super Paper Mario model files.
- [ttyd-utils](https://github.com/jdaster64/ttyd-utils) - Utilities for modding Paper Mario: TTYD.
- [noclip.website (TTYD)](https://github.com/magcius/noclip.website/tree/main/src/PaperMarioTTYD) - In-browser TTYD map viewer.
- [noclip.website (Super Paper Mario)](https://github.com/magcius/noclip.website/tree/main/src/PaperMarioTTYD) - In-browser Super Paper Mario (Wii) map viewer, sharing the TTYD loader.
- [MeltyTool (TTYD)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/PaperMarioTheThousandYearDoor) - Model viewer/exporter.
- [PistonMiner/ttyd-tools](https://github.com/PistonMiner/ttyd-tools) - Development tools including Blender exporter, disassembler, and REL linker.
- [PaperMarioModelViewer](https://github.com/uyjulian/PaperMarioModelViewer) - Model viewer for Paper Mario games.
- [lzarc](https://github.com/jam1garner/lzarc) - Rust library and CLI for extracting and packing LZARC compressed archives used in Paper Mario Color Splash.
- [CollisionSceneBinary](https://github.com/KillzXGaming/CollisionSceneBinary) - A library and tool for handling csb and ctb collision files found in paper mario games.
- [spm-docs](https://github.com/SeekyCt/spm-docs) - Documentation of various parts of Super Paper Mario's internal formats and data structures.
- [PaperMario2 (decomp)](https://github.com/NWPlayer123/PaperMario2) - Decompilation of Paper Mario: The Thousand Year Door.
- [Shufflizer](https://github.com/jdaster64/shufflizer) - Randomizer mod for Paper Mario: The Thousand-Year Door that shuffles field item pickups, shop stock, and Pit of 100 Trials encounters, patched onto a retail ISO via a GCI/Gecko REL loader built on PistonMiner's REL framework.
- [TTYD Infinite Pit](https://github.com/jdaster64/ttyd-infinite-pit) - Roguelike mod of Paper Mario: TTYD's Pit of 100 Trials with seeded random enemy encounters, item drops, and chest rewards, built on PistonMiner's REL framework and patched onto a retail ISO via GCI loader.
- [Tower of Trials](https://github.com/jdaster64/ttyd-tot) - Rogue-like mod of Paper Mario: TTYD reworking Hooktail Castle into a seeded roguelike tower with unlockable characters, moves, and badges; ships as a standalone ISO patcher built on PistonMiner's REL framework.
- [evt-disassembler](https://github.com/SeekyCt/evt-disassembler) - Disassembler for the binary `evt` script format found in Super Paper Mario RAM dumps.
- [GhidraEvt](https://github.com/SeekyCt/GhidraEvt) - Ghidra extension integrating disassembly of the `evt` script format used by Paper Mario: The Thousand-Year Door and Super Paper Mario directly into the disassembly view.
- [evt-assembler](https://github.com/SeekyCt/evt-assembler) - Assembler for Super Paper Mario's text-format `evt` scripts, with minor edits also supporting TTYD.
- [Flipside-Mod-Manager](https://github.com/L5050/Flipside-Mod-Manager) - Command-line mod manager for Super Paper Mario; installs/uninstalls mods, patches the ROM to support loading REL mods, and backs up files replaced by mods.
- [SPME](https://github.com/InconspicuousCactus/SPME) - Command-line editor for Super Paper Mario level data: extracts/repacks U8 archives and TPL textures, and converts `map.bin` level geometry to/from FBX and GLB for editing in 3D tools.
- [Flint](https://github.com/Luma48/Flint) - Editor for Super Paper Mario's in-game text/dialogue, with live in-editor preview of how edited text will render before patching via Riivolution.
- [Paper-Mario-Tools](https://github.com/KillzXGaming/Paper-Mario-Tools) - Tools for Paper Mario games, including a LightConverter utility for converting light-probe binaries from Zstd-compressed assets, as used in the Paper Mario: The Thousand-Year Door Switch remake.
- [Unsimplifier](https://github.com/Darxoon/Unsimplifier) - Browser-based data editor for the Paper Mario: The Thousand Year Door remake. Opens files from the game's romfs and edits object properties.
- [samptool](https://github.com/ShrineFox/samptool) - Repacker for Paper Mario: The Thousand Year Door (GameCube) MusyX `.samp` sound archives, originally created by tge-was-taken in 2016. GUI and command-line.

##### Paper Mario: The Origami King

- [noclip.website (Paper Mario: The Origami King)](https://github.com/magcius/noclip.website/tree/main/src/PaperMarioTheOrigamiKing) - In-browser Paper Mario: The Origami King (Switch) map viewer. Reads the game's Zstd-compressed ELF data files for level/model definitions and object placement (mobj/sobj/aobj/npc/item instances) alongside BFRES models.
- [Emblem-Magic](https://github.com/LexouDuck/Emblem-Magic) - All-purpose ROM hacking tool for the GBA Fire Emblem games.
- [PaperMarioTOK](https://github.com/turtle-insect/PaperMarioTOK) - Save data editor for Paper Mario: The Origami King (Switch).

#### Mattel Electronics (Intellivision)

- [AstroSmash](https://github.com/EXL/AstroSmash) - Port of Mattel's AstroSmash from its Java ME (J2ME) MIDlet release to Android, using a Java decompiler to recover and restore the original game's logic before porting.

#### Interaction Studios

- [Chicken-Extractor](https://github.com/ravenDS/Chicken-Extractor) - Unpacker/repacker for Chicken Invaders game archives.

#### Interactive Studios

##### Glover

- [noclip.website (Glover)](https://github.com/magcius/noclip.website/tree/main/src/Glover) - In-browser Glover level viewer.
- [libgarib](https://github.com/naclomi/libgarib) - Glover reverse engineering tools and information library.
- [glover-decomp](https://github.com/djsaunde/glover-decomp-1) - In-progress N64 decompilation of Glover, driven by an AI-assisted decompilation agent.
##### HardWar

- [HardWar-SaveEdit](https://github.com/JulianOzelRose/HardWar-SaveEdit) - Web-based save game editor for the cyberpunk PC game HardWar, written in plain JavaScript and HTML.

#### Interplay / Black Isle Studios

##### Fallout (Interplay)

- [Fallout Community Edition](https://github.com/alexbatalov/fallout1-ce) - Full re-implementation of Fallout with original gameplay, engine bugfixes, and quality-of-life improvements for modern systems.
- [falltergeist](https://github.com/falltergeist/falltergeist) - Alternative game engine implementation that parses and runs original Fallout 2 data files (master.dat, critter.dat).
- [fallout1-re](https://github.com/alexbatalov/fallout1-re) - Reverse-engineered, fully working reconstruction of the original Fallout source code.
- [fallout2-re](https://github.com/alexbatalov/fallout2-re) - Reverse-engineered, fully working reconstruction of the original Fallout 2 source code.
- [fot-save-edit](https://github.com/mykola2312/fot-save-edit) - Rust CLI that decodes and encodes Fallout Tactics save files (implements the binary save format), for editing character stats and entity properties.

##### Fallout 2

- [Fallout 2 Community Edition](https://github.com/fallout2-ce/fallout2-ce) - Full re-implementation of Fallout 2 engine built from reverse-engineering the original binary; parses DAT archives, FRM sprites, and MAP/PRO data files; supports original mods.
- [Fallout 2 Community Edition (BoBoBaSs84 fork)](https://github.com/BoBoBaSs84/fallout2-ce) - Community decompilation/re-implementation variant.
- [vault13](https://github.com/pingw33n/vault13) - Work-in-progress Rust reimplementation of the Fallout 2 engine, reading the original game's data files (e.g. `vault13 /path/to/fallout2 artemple`).
- [Fallout-2-Item-Data-Extractor-for-Wikis](https://github.com/An-on-im/Fallout-2-Item-Data-Extractor-for-Wikis) - Extracts Fallout 2 item data for use in wiki documentation.
- [Fallout-2-Simple-DAT-Archive-Extractor](https://github.com/An-on-im/Fallout-2-Simple-DAT-Archive-Extractor) - Simple extractor for unpacking all files from Fallout 2's DAT archives.
- [frm_recolour_python](https://github.com/Dr-Felix116/frm_recolour_python) - Python script to automatically recolor sprites in Fallout/Fallout 2 FRM sprite files by batch-replacing colors.
- [HexWaste](https://github.com/eko1495/HexWaste) - C#/.NET + MonoGame (DesktopGL) re-implementation of a slice of the Fallout 2 engine, loading and running the original data files.
- [fallout2-save-editor](https://github.com/efossvold/fallout2-save-editor) - Save game editor for Fallout 2.
- [fallout-2-editor](https://github.com/freesalu/fallout-2-editor) - Python command-line save game editor for Fallout 2 (written against the GOG version on macOS); edits stats, skills and perks directly in the save file.
- [DarkFO](https://github.com/darkf/darkfo) - Browser-based (TypeScript/Python) reimplementation of the Fallout 2 engine, reading the original game's data files, with accompanying file format documentation.

##### Dragon Wars

- [opendw](https://github.com/devinsmith/opendw) - Game engine reimplementation for Interplay's Dragon Wars (1989/1990), loading the original game data.

##### Icewind Dale II

- [iwd2-re](https://github.com/alexbatalov/iwd2-re) - Reverse-engineered, buildable source code for Icewind Dale II, Black Isle Studios' Infinity Engine RPG.

##### Baldur's Gate

- [py-eekeeper](https://github.com/grm/py-eekeeper) - Save game editor for Baldur's Gate: Enhanced Edition and other Infinity Engine games; a Python/PySide6 rewrite of eekeeper-qt, itself based on Shadow Keeper.
- [wand_of_saves](https://github.com/hugo-bluecorn/wand_of_saves) - Flutter desktop saved-game editor for Baldur's Gate: Enhanced Edition (a successor to EE Keeper) that edits characters in savegames and `.chr` files, using pure-Dart Infinity Engine format codecs (`infinity_formats`).

##### Atomic Bomberman

- [open-atomic-bomberman-97](https://github.com/Egerion/open-atomic-bomberman-97) - Clean-room C++20 rewrite of Interplay's Atomic Bomberman (1997) that loads and renders the original game's assets, reverse-engineered from the 1997 binary, with a deterministic lockstep simulation core and added online multiplayer.
- [Fallout-2-Image-Extractor-FRM-to-PNG-or-GIF](https://github.com/An-on-im/Fallout-2-Image-Extractor-FRM-to-PNG-or-GIF) - Converts Fallout 2's original FRM sprite format to PNG or GIF.
- [Deep-Dive-into-SW-Rebellion-PC-Game-Internals](https://github.com/TheArchitect2018/Deep-Dive-into-SW-Rebellion-PC-Game-Internals) - Reverse-engineering notes on Star Wars: Rebellion's internal game data structures.

##### The Lord of the Rings

- [lotr-snes-disassembly](https://github.com/patrickmollohan/lotr-snes-disassembly) - In-progress full disassembly of J.R.R. Tolkien's The Lord of the Rings: Volume 1 (SNES, Interplay, 1994) using DiztinGUIsh.

##### Boogerman

- [boogerman-rom-tools](https://github.com/vitalya834/boogerman-rom-tools) - Reverse engineering of the Boogerman: A Pick and Flick Adventure (Sega Mega Drive) cartridge: resource unpacking and map/collision format documentation, plus an experimental Godot remake and native recompilation.

##### Wasteland

- [wastelib](https://github.com/kayahr/wastelib) - TypeScript/JavaScript library for reading Wasteland's (1988) original game assets.
  - Formats: title/portrait/ending animations, sprites, tilesets, maps, savegames, shop item lists, the color font, and the `paragraphs.bin` text file from the "Wasteland 1 - The Original Classic" re-release.
- [wlandsuite](https://github.com/kayahr/wlandsuite) - Java suite for reading and writing Wasteland's original data files.
- [darkwasteland](https://github.com/darkf/darkwasteland) - Browser-based JavaScript reimplementation of the Wasteland 1 engine, built on wastelib/wlandsuite to read the original DOS game files.

#### IO Interactive

- [io_scene_glacier](https://github.com/TheDodylectableX/io_scene_glacier) - Work-in-progress Blender 3.x/4.x+ add-on for importing and exporting models, skeletons, and textures from IO Interactive Glacier 1 and Glacier 2 engine games.
  - Glacier 1 (Hitman 2: Silent Assassin, Freedom Fighters, Hitman: Contracts, Hitman: Blood Money, Mini Ninjas): imports .GMS, .PRM, .TEX.
  - Glacier 2 (Hitman: Absolution, Hitman: World of Assassination, 007 First Light): imports .PRIM, .TEXT/.TEXD, .BORG, .CLOS; export is work in progress.

##### 007 First Light

- [007-firstlight-toolkit](https://github.com/7akeem0/007-firstlight-toolkit) - Toolkit for the RPKG v2 archive format used by IO Interactive's Glacier engine in 007 First Light (2025).
##### Freedom Fighters

- [frfi-decomp](https://github.com/andresj-sanchez/frfi-decomp) - Work-in-progress matching decompilation of Freedom Fighters (2003, GameCube).
- [Freedom](https://github.com/minexew/Freedom) - Reverse-engineering documentation and tools for Freedom Fighters (2003) and other Glacier-engine titles, covering the BUF/GMS/LOC/PRM/TEX/ZGF map and resource formats; includes a texture dumper and a PRM model exporter that reconstructs scene geometry as OBJ for import into Blender.

##### Kane & Lynch

- [KaneLynchLoc](https://github.com/x1nixmzeng/KaneLynchLoc) - Command-line C# tool converting Kane & Lynch locale (.loc) language databases to and from XML language exports, with a console export option.

#### Ion Storm

##### Anachronox

- [Anachronox Modding Tools](https://www.moddb.com/games/anachronox/downloads/anachronox-modding-tools) - Mapping and modding tools for Anachronox, includes documentation.
- [chronon](https://github.com/hogsy/chronon) - Open-source reimplementation of Anachronox (Ion Storm, 2001) built on the Quake 2 engine, reading original game data files.
- [anoxtools](https://github.com/hogsy/anoxtools) - Fork of qbism's q2tools-220 map compiler with added support for Anachronox.

##### Daikatana

- [daikatana-restoration-project](https://github.com/atsb/daikatana-restoration-project) - Restoration/modernization project for Daikatana (Ion Storm, id Tech 2), reading the original game's data files.
- [FuseMDX2DKM](https://github.com/KUBA18i/FuseMDX2DKM) - Fuses Kingpin: Life of Crime .mdx models into a single Daikatana .dkm model.
- [MD22DKM](https://github.com/KUBA18i/MD22DKM) - Converts Quake II .md2 models into Daikatana's .dkm format.

#### Iron Gate AB

- [VSideLoader](https://github.com/BlueAmulet/VSideLoader) - Texture dumper and replacer for Valheim.
- [ValheimExportHelper](https://github.com/heinermann/ValheimExportHelper) - AssetRipper plugin that streamlines exporting Valheim's assets into a Unity project.
- [valheim-character-editor-python](https://github.com/blakebjorn/valheim-character-editor-python) - Python-based character save editor for Valheim.
- [MakeFwl](https://github.com/CrystalFerrai/MakeFwl) - Standalone CLI program to create Valheim world metadata (.fwl) files with specific seeds, for dedicated server operators who want specific world seeds without generating a full world first.

#### Drew Pictures (Iron Helix)

- [PACoPlayer](https://github.com/GregDomzalski/PACoPlayer) - Software preservation project to read and play back video/animation files created with the PICS Animation Compiler (PACo, by the Company of Science and Art), used for Iron Helix (1993)'s pre-rendered CD-ROM graphics.

#### Iron Lore Entertainment

##### Titan Quest

- [tq-mapdecompiler](https://github.com/epinter/tq-mapdecompiler) - Decompiles Titan Quest map files (.map + .wrl) back into editable form; an updated/fixed version of the original MapDecompiler by p0a.

#### Ironclad Games / Stardock

##### Sins of a Solar Empire

- [Sins 3D Max Import export](https://www.moddb.com/games/sins-of-a-solar-empire-rebellion/downloads/sins-3d-max-impotrt-export) - 3DS Max importer for Sins of a Solar Empire: Rebellion TXT mesh format. Exporter in progress. Trial alpha version.
- [sins TXT Tools with export (Sins of a Solar Empire: Rebellion)](https://www.moddb.com/games/sins-of-a-solar-empire-rebellion/downloads/sins-txt-tools-with-export) - This version with export to TXT! Alpha version...adds sins standart material with default settings
- [Forge Tools (Sins of a Solar Empire)](https://www.moddb.com/games/sins-of-a-solar-empire/downloads/forge-tools) - Official development tools for creating custom maps and modifications for Sins of a Solar Empire. Includes Galaxy Forge and Particle Forge tools used by the development team.
- [Map Conversion (Sins of a Solar Empire)](https://www.moddb.com/games/sins-of-a-solar-empire/downloads/map-conversion) - Convert maps between Sins versions with this user-created tool. Created by Ross Placing. Requires .Net 2.0; Updated for Sins 1.15/Entrenchment 1.01.

#### Itadaki Street

- [itadaki-street-2](https://github.com/Xkeeper0/itadaki-street-2) - Reverse-engineering utilities for Itadaki Street 2 (SNES), in PHP, including a data decompressor for ROM offsets and tools to dump and view the game's text, maps and graphics.

### J
#### J.League Pro Soccer Club o Tsukurou! 04

- [sakatsuku04](https://github.com/caol64/sakatsuku04) - Game and save editor for J.League Pro Soccer Club o Tsukurou! 04 (PS2); edits memory card save files (players, teams and other in-game data) or, alternatively, game data live through PCSX2.

#### Jagex

*Old School RuneScape / RuneScape.*

- [CacheModelTools](https://github.com/Bloodspawns/CacheModelTools) - Tools for extracting and viewing OSRS cache models.
- [OSRS-Environment-Exporter](https://github.com/ConnorDY/OSRS-Environment-Exporter) - Environment and map exporter for Old School RuneScape.
- [modelviewer](https://github.com/waleedyaseen/modelviewer) - Model viewer for RuneScape cache files.
- [clue-chunk-map](https://github.com/ConnorDY/clue-chunk-map) - Game data mapping tool for Old School RuneScape clue steps and chunk locations.
- [RuneBlend](https://github.com/tamateea/RuneBlend) - Blender add-on for importing RuneScape 3D assets.
- [rscachefinder](https://github.com/edward4096/rscachefinder) - Tool to locate RuneScape cache files, developed to support the rs-archive preservation project.

##### RuneScape Classic

- [Core-Framework](https://github.com/Open-RSC/Core-Framework) - OpenRSC game server framework, a black-box reverse-engineered reimplementation of RuneScape Classic (RSC)'s server-side game logic and network protocol.
- [rsc-remastered](https://github.com/Danjb1/rsc-remastered) - Alternate remake of the original RuneScape Classic.
- [rsc-c](https://github.com/2003scape/rsc-c) - RuneScape Classic client ported to C99, refactored from the leaked mudclient204 Java source; supports the 204 and 177 protocols.
- [rsc-landscape](https://github.com/2003scape/rsc-landscape) - (De)serializes RuneScape Classic's original `land`/`maps` archive files into tile objects, dumping them as PNGs and re-encoding edits back to the original format.
- [rsc-sounds](https://github.com/2003scape/rsc-sounds) - Extracts RuneScape Classic's cache-stored sounds (Sun's `.au` format) to WAV and re-encodes them back to the original format.
- [rsc-models](https://github.com/2003scape/rsc-models) - (De)serializes RuneScape Classic's 3D model archives to/from Wavefront `.obj`/`.mtl`.
- [rsc-sprites](https://github.com/2003scape/rsc-sprites) - (De)serializes RuneScape Classic's entity, UI, and texture sprite images.
- [rsc-archiver](https://github.com/2003scape/rsc-archiver) - Compresses/decompresses RuneScape Classic's `.jag`/`.mem` cache archive files.
- [rsc-config](https://github.com/2003scape/rsc-config) - (De)serializes RuneScape Classic's config/definition archive files.
- [RSC-OpenGL-Map-Viewer](https://github.com/sean-niemann/RSC-OpenGL-Map-Viewer) - Interactive OpenGL landscape and model viewer for RuneScape Classic.
- [RSC-Single-Player](https://github.com/sean-niemann/RSC-Single-Player) - Standalone single-player RuneScape Classic client and sandbox that loads the original game's landscape/data files directly, without a server or database backend.
- [RSC-Landscape-Generator](https://github.com/sean-niemann/RSC-Landscape-Generator) - Command-line tool that renders RuneScape Classic landscape files to images, covering the RSCD, Jag (maps28+), and legacy Jag (maps27 and earlier) archive format revisions.
- [rsc_lwjgl](https://github.com/rscgl/rsc_lwjgl) - RuneScape Classic client rewritten to run on LWJGL.
- [rsc-client](https://github.com/2003scape/rsc-client) - JavaScript/browser port of the leaked mudclient204 Java client, designed to run against rsc-server.
- [rsc-server](https://github.com/2003scape/rsc-server) - Private server/MMORPG emulator for RuneScape Classic, compatible with rsc-client and the java-based mudclient204; uses the JSON data formats from rsc-data.
- [rsc-world-map](https://github.com/2003scape/rsc-world-map) - Standalone JS interactive world map viewer for RuneScape Classic, rendering the landscape/dungeon data extracted by rsc-landscape.

#### Jellyvision

- [ydkjx (Jack Player)](https://github.com/james-wallace-ghub/ydkjx) - Swing-based reader for the SRF resource files used by the You Don't Know Jack (YDKJ) game engine, currently supporting text and audio resources.

#### Ultimate Play the Game (JETPAC)

- [jetpac-disassembly](https://github.com/mrcook/jetpac-disassembly) - Fully annotated disassembly of JETPAC (1983), Ultimate Play the Game's classic 16K ZX Spectrum cartridge ROM.

#### Juice Games (Juiced)

- [JCED.DAT.Tool](https://github.com/Ekey/JCED.DAT.Tool) - Tool for extracting DAT archives from Juiced.
- [JCED2.JFS.Tool](https://github.com/Ekey/JCED2.JFS.Tool) - Tool for extracting JFS archives from Juiced 2: Hot Import Nights.
- [d8wTool](https://github.com/coreynguyen/Juiced_D8W_Tool) - C++/wxWidgets desktop tool for viewing, exporting, importing, and converting `.d8w`/`.d8t` texture banks used in Juiced.

#### Julegame

##### League of Angels

- [LoAHF.PAK.Tool](https://github.com/Ekey/LoAHF.PAK.Tool) - PAK (JPAK) archive extractor for League of Angels series, supporting League of Angels – Heaven's Fury, League of Angels: Chaos, Eternal Epoch, and other Julegame titles.

#### LEGO Media (Junkbot)

- [junkbot-code](https://github.com/JakeSteam/junkbot-code) - Extracted source code and assets from LEGO's Junkbot (2002), a browser-based Adobe Director/Shockwave puzzle game, preserving Lingo scripts, level data, and cast-ripped sprites/sounds/animations.
- [janitorial-android](https://github.com/1j01/janitorial-android) - HTML5 remake of Junkbot and Junkbot Undercover with a fancy level editor, loading the original level format and reusing sprites/sounds ripped from the original Shockwave games.

#### Jupiter

*Mario's Picross (Game Boy).*

- [MarioPicrossRipper](https://github.com/AkagitsuneYuki/MarioPicrossRipper) - Asset extraction tool for Mario's Picross.
- [MeltyTool (Picross)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/MariosPicross/MariosPicross) - Format viewer and exporter for Mario's Picross.
- [cgrr-mariospicross](https://github.com/sopoforic/cgrr-mariospicross) - Graphics extraction tool for Mario's Picross.
- [MarioPicrossLoader3000](https://github.com/T0biasCZe/MarioPicrossLoader3000) - Asset loader and viewer for Mario's Picross.
- [Picross Level Data](https://www.zophar.net/fileuploads/3/21546xutra/picrossleveldata.txt) - Technical documentation for Mario's Picross level data format.

### K
#### Tate Interactive (Kao the Kangaroo)

- [KAO_PAK](https://github.com/Flower35/KAO_PAK) - Extracts files from "Kao the Kangaroo 1" PAK archives.
- [KAO2_PAK](https://github.com/Flower35/KAO2_PAK) - Extracts files from "Kao the Kangaroo: Round 2" PAK archives.
- [ZookieWizard](https://github.com/Flower35/ZookieWizard) - Advanced editor for "Kao the Kangaroo: Round 2", supporting custom 3D mesh import into AR files, PAK archive file replacement, texture extraction/reimport, and level creation.
- [Challengers2Kao3](https://github.com/Flower35/Challengers2Kao3) - Helps port "Kao Challengers" (PSP) levels to the "Kao: Mystery of Volcano" (PC) engine.

#### Kawaiinium

- [kawaiiniumTool](https://github.com/shiikwi/kawaiiniumTool) - Unpacks Kawaiinium visual novel `.pcarc`/`.arc` archives, converts `.ext` images to PNG, and exports `.mul` scripts to text.

#### Keen Software House

- [blender_mwm_importer](https://github.com/aaronsaderholm/blender_mwm_importer) - Blender importer for Space Engineers .mwm model files.
- [SEToolbox](https://github.com/midspace/SEToolbox) - Toolbox for Space Engineers that imports images and 3D models into the game and edits save game content. The README notes it has been non-functional since the 2019 Economy update.

#### Kemco

- [Catrap---game-boy-decompilation](https://github.com/nefelibatacfg/Catrap---game-boy-decompilation) - Byte-exact disassembly and reverse-engineering kit for Catrap (Kemco, 1990, Game Boy).

#### Ember Lab (Kena: Bridge of Spirits)

- [Kena-Bridge-of-Spirits_MeshTool](https://github.com/kboykboy2/Kena-Bridge-of-Spirits_MeshTool) - Patches cooked UE4.25 mesh `.uasset`/`.uexp` pairs so custom meshes can be modded into Kena: Bridge of Spirits without crashing.

#### Lo-Fi Games (Kenshi)

- [kenshi-mkii-editor](https://github.com/butteredstardust/kenshi-mkii-editor) - Web-based save game editor for the RPG Kenshi.
- [Kenshi-Save-Editor](https://github.com/wansolanso/Kenshi-Save-Editor) - Python desktop save editor for Kenshi with a binary record parser; edits character stats, limb status, inventories, faction relations and raw record fields, resolving names from `gamedata.base` and mods.

#### KeroQ

- [nijuuei-va](https://github.com/Vast-eel/nijuuei-va) - Dreamcast content patches and rudimentary asset extraction tools for KeroQ visual novels.

#### KID

*Never7, Ever17: The Out of Infinity, Remember11, 12Riven - the Infinity series of visual novels.*

- [kidfile](https://github.com/malucard/kidfile) - Library (Kidfile) and explorer app (Kidfile Explorer) for decoding file formats used across KID's Infinity series. Supports OGDT, TIM2, GIM, PVR, BIP, and other image/archive/compression formats across PS2, PSP, Dreamcast, and PC ports.
- [Infinity-PSP-TL](https://github.com/bibarub/Infinity-PSP-TL) - Fan translation/porting toolchain for the Infinity series (Never7, Ever17, Remember11) on PSP: unpacks and repacks game resources, decodes text and the FONT00.FOP font format, and rebuilds the patched ISO/EBOOT.PBP; includes original engine research into the PSP ports and BIP image format. Actively maintained continuation of dreambottle's original Remember11-only [R11-psp-english](https://github.com/dreambottle/R11-psp-english).
- [Rivened](https://github.com/malucard/Rivened) - Cross-platform script editor for 12Riven (Infinity series), building on format research from the original [12Riven Script Editor](https://github.com/Exormeter/12Riven_ScriptEditor) by Essometer and [chroipahtz's version](https://github.com/chroipahtz/12Riven_ScriptEditor).
- [e17p](https://github.com/uyjulian/e17p) - (Archived) Python reverse-engineering of the storage formats of the Infinity series visual novels, focused on Ever17 with preliminary Remember11 work, toward a free engine for them.

#### Kid Chameleon

- [kid-chameleon-disasm](https://github.com/sonicretro/kid-chameleon-disasm) - Split disassembly of Kid Chameleon (Sega Genesis/Mega Drive) for the AS assembler: `split.py` separates ROM data (theme art, mappings, collision, palettes, level layouts, GEMS sound assets) into individual files, with documentation of the ROM and data formats.

#### Tripwire Interactive (Killing Floor)

- [KFTempArchiveExtractor](https://github.com/Mateos81/KFTempArchiveExtractor) - Manually extracts Killing Floor's Steam Workshop TempArchiveXX files when the game's own downloader fails, based on the documented internal format of the TempArchive files.
- [killingfloor2musictool](https://github.com/overlandandseas/killingfloor2musictool) - GUI tool for Killing Floor 2 that converts custom WAV audio to Wwise WEM format and swaps it into the game's existing soundtrack banks.
- [killingfloor-map-viewer](https://github.com/TheBestPlan/killingfloor-map-viewer) - Desktop (Electron) and browser viewer for Killing Floor `.rom` maps (Unreal Engine 2.5) that reads the game's `.utx`/`.usx` packages and draws the BSP, static meshes, terrain and skybox with textures; format notes in `docs/RESEARCH.md`.
  - See also [killingfloor-map-importer](https://github.com/TheBestPlan/killingfloor-map-importer), which converts Counter-Strike 1.6/Half-Life (GoldSrc BSP v30), Quake III Arena/Team Arena (IBSP v46), Lineage 2 (Interlude) and Tactical Ops maps into Killing Floor `.rom` levels.

#### Giant Network (King of Kings 3)

- [KOK3.LPQ.Tool](https://github.com/Ekey/KOK3.LPQ.Tool) - Tool for extracting LPQ archives from King of Kings 3.

#### Glowmade (King of Meat)

- [KM.ARCHIVE.Tool](https://github.com/Ekey/KM.ARCHIVE.Tool) - Tool for extracting archives from King of Meat (Technical Test build).

#### King of Route 66

- [bpy_king_of_route_66](https://github.com/coreynguyen/bpy_king_of_route_66) - Blender addon that imports `.mdl` models from both the PS2 and arcade versions of King of Route 66.

#### Kingdom Come: Deliverance

- [Warbox](https://github.com/vawser/Warbox) - Modding tool for Kingdom Come: Deliverance II with a table editor for the game's configuration tables and a text editor for localization, saving full or patch-only files and packaging them into PAK files.

#### Blueside (Kingdom Under Fire II)

- [KUF2.PKG.Tool](https://github.com/Ekey/KUF2.PKG.Tool) - Tool for extracting PKG archives from Kingdom Under Fire II.
- [KUF2_2014_vap](https://github.com/alanm20/KUF2_2014_vap) - Noesis plugin for viewing Kingdom Under Fire II (2014) hero character VAP models with texture binding.

#### Xatrix Entertainment (Kingpin)

- [blender_kingpin_models](https://github.com/hypov8/blender_kingpin_models) - Blender import/export addon for Quake II and Kingpin: Life of Crime .md2/.mdx models.
- [Kingpin Model Viewer](https://github.com/hypov8/Kingpin_Model_Viewer) - Standalone viewer for Kingpin: Life of Crime's MD2 and MDX model formats.
- [kingpin_skin_changer](https://github.com/hypov8/kingpin_skin_changer) - AutoIt tool for swapping skins on Kingpin/Quake II MD2, MDX, and MD3 models.
- [kingpin_noesis](https://github.com/hypov8/kingpin_noesis) - Noesis plugin for importing and exporting Kingpin: Life of Crime's MD2/MDX models.
- [KMKingpin](https://github.com/hypov8/KMKingpin) - Kingpin-converted fork of Knightmare's KMQuake2 engine (KMKingpin II).

#### Beam Software (KKnD)

- [OpenKrush](https://github.com/IceReaper/OpenKrush) - KKnD and KKnD2: Krossfire mod for the OpenRA engine, with file-format readers (Blit/Mapd/Mobd sprites, Lvl packages, Son/Soun audio, Vbc video) for the original games' assets.

#### Joymania Entertainment (Knights and Merchants)

- [kam_remake](https://github.com/reyandme/kam_remake) - "KaM Remake", a from-scratch RTS engine rewrite of Knights and Merchants: The Shattered Kingdom, still relying on the original game's resource files (installer checks for an owned copy). Actively-developed continuation of [Kromster80's original repo](https://github.com/Kromster80/kam_remake) (378 stars, now archived), per the latter's own README.
- [KAM-graphics-edit](https://github.com/IJzerbaard/KAM-graphics-edit) - Editor for modifying Knights and Merchants: The Peasants Rebellion's building/construction sprite data and animation data (sprite set, count, offset), with live preview of changes.

#### Knowledge Adventure

##### Dr. Brain: Action Reaction

- [DrBrainActionReaction_PackageDecomp](https://github.com/SirHenricus/DrBrainActionReaction_PackageDecomp) - Decompiled assets from the package files of Dr. Brain: Action Reaction (1999), an Unreal Engine 1 game developed and published by Knowledge Adventure.

#### Nifflas (Knytt Underground)

- [kug-mapper](https://github.com/rr-/kug-mapper) - Map generator for Knytt Underground, reading and rendering the game's terrain, backgrounds, objects, tiles, and warp data directly from the original game files.

#### Kobo Deluxe

- [cgrr-kobodeluxe](https://github.com/sopoforic/cgrr-kobodeluxe) - Python module (part of Classic Game Resource Reader) that reads and writes Kobo Deluxe score and profile files.

#### Gust (Koei Tecmo)

- [slpm86183 (decomp)](https://github.com/Erizur/slpm86183) - Matching decompilation of Pop'N Music CS1 (PS1).
- [gust_stuff](https://github.com/eArmada8/gust_stuff) - Modding toolkit for G1M model files used in Gust games (Atelier series).
- [gust_tools](https://github.com/VitaSmith/gust_tools) - Utilities for archive management and data extraction for Gust PC games (Atelier, Blue Reflection, Nights of Azure).
- [atelier_pak_decrypt](https://github.com/shizukachan/atelier_pak_decrypt) - Small utility to decrypt GUST .pak archives.
- [zig-gtx2dds](https://github.com/shimamura-sakura/zig-gtx2dds) - Zig converter between Gust GTX (`.gtx`) and DDS textures; supports only DXT1 (UBC1) and DXT5 (UBC3).
- [Project-G1M](https://github.com/Joschuka/Project-G1M) - Noesis plugin for importing G1M 3D model format used in Gust and Bandai Namco games.
- [Cethleann](https://github.com/neptuwunium/Cethleann) - KTGL (Soft Engine) data exploration and research tool for Koei Tecmo games.
- [atelier-tools](https://github.com/holly-hacker/atelier-tools) - Library and CLI for decoding modern Atelier PC titles' .pak archives and .g1t textures (Sophie, Firis, Lydie & Suelle, Ryza 1-3, Sophie 2), aiming to be easier to use as a library than gust_tools; powers the author's atelier-wiki format documentation.
- [AtelierManager](https://github.com/marcussacana/AtelierManager) - Tool to translate Atelier EBM script files.
- [atelier-resleriana-2-patterns](https://github.com/CatClawed/atelier-resleriana-2-patterns) - ImHex patterns for Atelier Resleriana 2 (Red/White) data files; continuation of [holly-hacker's initial RE](https://github.com/holly-hacker/atelier-resleriana-2-patterns), which points to this fork as the maintained follow-up.
- [pssg-g1t-extractor](https://github.com/CatClawed/pssg-g1t-extractor) - Extracts G1T texture files from PSSG container files; tested against Atelier Rorona DX.
- [AtelierDatamining](https://github.com/CatClawed/AtelierDatamining) - Datamining scripts and CheatEngine tables for extracting and mapping data from recent Atelier games (Yumia and earlier), building on gust_tools' PAK extraction.
- [resleriana-db](https://github.com/theBowja/resleriana-db) - Provides scripted access to game resources and a web API for building third-party tools for Atelier Resleriana.
- [AtelierIris1-Randomizer](https://github.com/punk7890/AtelierIris1-Randomizer) - Randomizer for Atelier Iris: Eternal Mana (PS2), currently covering music and enemies; applies as an xdelta patch to a redump ISO, with accompanying ARMIPS-compiled code injected into the executable.
- [psarc-nx](https://github.com/Sage-of-Mirrors/psarc-nx) - Packer/unpacker for the variant of Sony's PSARC archive format used by Gust in its Nintendo Switch games.

#### Koei Tecmo

- [fdata_dump](https://github.com/DeathChaos25/fdata_dump) - Extractor for Koei Tecmo's FData archive format.
  - Games: Fate/Samurai Remnant, Fairy Tail 2, Dynasty Warriors: Origin, Rise of the Ronin, Atelier Yumia, Fatal Frame II: Crimson Butterfly Remake, Fire Emblem Warriors: Three Hopes, Nioh 3.
- [kvs-tools](https://github.com/Hairo/kvs-tools) - Tools for extracting and archiving Koei Tecmo's .ktsl2stbin archive format.

##### Fatal Frame

- [himuro (decomp)](https://github.com/mikompilation/himuro) - Matching decompilation of Fatal Frame (PS2).
##### Nioh

- [RDBExplorer](https://github.com/MrIkso/RDBExplorer) - GUI archive browser, extractor, and injector for Nioh 3's .fdata/archive_xx.bin/.rdx files, with locale CSV pack/unpack tools.

##### Hyrule Warriors

- [HWL-SaveEditor](https://github.com/nedron92/HWL-SaveEditor) - Save editor for Hyrule Warriors Legends (Nintendo 3DS).

#### Konami

- [kbinxmlcs](https://github.com/FSH-B/kbinxmlcs) - Decoder/encoder for Konami's binary XML (KBinXML) format, used across many Konami arcade and console games.
- [kbinxml](https://github.com/mon/kbinxml) - Python decoder/encoder for Konami's binary XML (KBinXML) format.
- [kbinxml-rs](https://github.com/mbilker/kbinxml-rs) - Rust library and CLI for Konami's binary XML (KBinXML) format, with a derive macro for mapping nodes onto structs.
- [aeptools](https://github.com/aoki-marika/aeptools) - Converts Konami's proprietary AEP format between x86/x64 binary and human-readable JSON for inspection and modification. See the [wiki](https://github.com/aoki-marika/aeptools/wiki) for format documentation.
- [s3ptools](https://github.com/aoki-marika/s3ptools) - Tools for working with Konami's proprietary S3P file format.
- [txrcconv](https://github.com/piratesephiroth/txrcconv) - Exports the text of Konami `.txrc` files to editable plain text (one string per line) and converts it back, as long as the string count is unchanged; used by games such as Suikoden Tierkreis, Love Plus and Castlevania: Harmony of Despair.
- [kcej_ipk_dec](https://github.com/Nisto/kcej_ipk_dec) - Decodes and extracts IPK files from PS2 games developed by Konami Computer Entertainment Japan; known supported games include Metal Gear Solid 2, Metal Gear Solid 3 and Zone of the Enders: The 2nd Runner.

##### Teenage Mutant Ninja Turtles

- [tmnt2](https://github.com/xntrz/tmnt2) - Reimplementation of the PC version of Teenage Mutant Ninja Turtles 2: Battle Nexus (2004), built from a leaked PS2 prototype's PDB symbols; loads the original game's data files.
- [eintourname](https://github.com/romhack/eintourname) - RLE tool for decoding/encoding the tile maps in NES Teenage Mutant Ninja Turtles: Tournament Fighters.
- [t3gbLz](https://github.com/romhack/t3gbLz) - LZSS compression tool for Teenage Mutant Ninja Turtles III: Radical Rescue (Game Boy).

##### Ganbare Goemon

- [sfc-goemon-3-disassembly](https://github.com/gocha/sfc-goemon-3-disassembly) - Disassembly of Ganbare Goemon 3 (Super Famicom, 1994).

##### Vandal Hearts

- [VandalHearts-PcPort](https://github.com/HalmyLyseas/VandalHearts-PcPort) - Native PC port of Vandal Hearts (PlayStation), built on a byte-exact matching decompilation; runs on Windows and Linux (bring your own disc).

##### Shaman King

- [gba-shaman-king-toolkit](https://github.com/RetributionByRevenue/gba-shaman-king-toolkit) - Reverse-engineering notes, tools, and extracted maps for Shaman King: Master of Spirits (Game Boy Advance, Konami/KCEJ, 2003).

##### BEMANI

*Konami's arcade rhythm-game brand: beatmania IIDX, DDR, pop'n music, jubeat, GITADORA, Sound Voltex, and others.*

- [bemaniutils](https://github.com/DragonMinded/bemaniutils) - Collection of utilities implementing a hobby BEMANI game services network for historic arcade titles, including binary/save data and network protocol tooling.
- [bemanitools](https://github.com/djhackersdev/bemanitools) - Runs recent Konami arcade games on PC by emulating their arcade hardware (I/O boards, security dongles) and e-amusement network services from the original game data.
- [konami_archive_tools](https://github.com/Subject38/konami_archive_tools) - Library and tools for parsing and extracting Konami arcade update archives.
- [VoxCharger](https://github.com/SirusDoma/VoxCharger) - Music asset manager for Sound Voltex, with a built-in KSH-to-VOX/2DX converter/encoder and Music DB metadata editor.
  - Formats: VOX (chart), 2DX (audio), KSH import.
- [klz77](https://github.com/SirusDoma/klz77) - Go library implementing Konami's LZ77 variant ("Konmai LZ77") compression, used to compress various BEMANI resource files and network messages.
- [BemaniPatcher](https://github.com/mon/BemaniPatcher) - Web-based tool for applying community-submitted hex-edit binary patches to BEMANI arcade game binaries.
- [mempatcher](https://github.com/aixxe/mempatcher) - Drop-in replacement for bemanitools' mempatch-hook with extra features: auto-loading `.mph` patch files, file-based and host-executable offsets, and load-order guarantees so patches apply before the game's entrypoint runs.
- [scharfrichter](https://github.com/SaxxonPike/scharfrichter) - Class library and CLI toolset for converting Konami arcade rhythm-game media: djmain and Twinkle (beatmania IIDX) hard drive images, bemanipc files, DDR SSQ charts, and Xbox/XAudio-based XWB/XSB audio banks used in later DDR games; also includes an experimental beatmania IIDX IFS extractor.
  - See also [RhythmCodex](https://github.com/SaxxonPike/RhythmCodex), the author's successor project, a C# rhythm game data tool.
- [afptools](https://github.com/camprevail/afptools) - Tools and an ImHex pattern for working with Konami's AFP graphics/animation format, used across BEMANI arcade titles. See also [AfpViewerEx](https://github.com/aixxe/AfpViewerEx), a hook for dumping rendered frames as transparent PNGs from the beatmania IIDX AFP viewer at runtime.
- [SD9Tool](https://github.com/TheFooestBar/SD9Tool) - Extracts and imports audio (with loop-point and volume parameters) in Konami's SD9 format and SSP containers, used by Dance Dance Revolution and other BEMANI titles.
- [ddr_arc_extract](https://github.com/mon/ddr_arc_extract) - Extracts files from DDRA (Dance Dance Revolution Arcade) archives.
- [ifstools](https://github.com/mon/ifstools) - Extractor/repacker for Konami's IFS container files, used across many BEMANI arcade titles.
- [ifs_layeredfs](https://github.com/mon/ifs_layeredfs) - LayeredFS-style live file-replacement engine for libavs-based Konami arcade games, letting modified files (including IFS contents) override the originals without repacking.
- [2dxTools](https://github.com/mon/2dxTools) - Small tools for working with 2dx audio container files.
- [2dxPlay](https://github.com/camprevail/2dxPlay) - Command-line player for Konami's 2dx audio container files.
- [sdpdump](https://github.com/camprevail/sdpdump) - Extracts audio from Konami's SDP audio container files.
- [gitadora-textool](https://github.com/littlecxm/gitadora-textool) - Converter for GITADORA's TEX image archive format.
- [gitadora-customs](https://github.com/fisyher/gitadora-customs) - Custom song/package manager for GITADORA.
- [iidxOnEar](https://github.com/Nyanm/iidxOnEar) - Batch-converts the songs in a beatmania IIDX `contents/` folder (including omnimix songs; loose song folders from IIDX 30 onward, `.ifs`-packed songs in earlier versions) into organised Opus music files with song metadata and album art, building on the author's [IIDX on Knitting](https://github.com/Nyanm/iidxOnKnitting) for the BMS-style keysound mixdown.
- [unigst](https://github.com/OffbeatDX/unigst) - Rust command-line generator of full-length soundtrack files (FLAC, MP3, or Opus, via ffmpeg) from the game contents of Sound Voltex, beatmania IIDX, and pop'n music, with per-version and per-song-ID filtering; the pop'n music mode reads the music database from `popn.dll`.
- [Destroy](https://github.com/Walter-o/Destroy) - Decryption library for Konami's e-amusement arcade network traffic.
- [SDVX-Song-Extract](https://github.com/Walter-o/SDVX-Song-Extract) - Python script that extracts music from Sound Voltex's `.s3v` audio files (renamed ASF containers) in an installed game folder, copying them as ASF or converting to MP3/WAV via ffmpeg, with title, artist and genre tags read from `music_db.xml`.
- [card-connect-extract](https://github.com/proeren2002/card-connect-extract) - Asset extractor for Konami's CARD CONNECT arcade game.
- [Malody2Jubeat](https://github.com/VALLIS-NERIA/Malody2Jubeat) - Converts Malody chart files to jubeat's .eve chart format.
- [extdrm](https://github.com/Ambloplites/extdrm) - Decrypts and verifies extdrm-encrypted filesystems used by modern AVS2-based Konami arcade titles and their Konasute (Konami Network) client counterparts.
  - Games: DANCERUSH STARDOM, beatmania IIDX (30 RESIDENT–current, INFINITAS 2020/2024), SOUND VOLTEX (VIVID WAVE–current, EXCEED GEAR), DanceDanceRevolution GRAND PRIX, GITADORA, NOSTALGIA, pop'n music Lively, DANCE aROUND, Polaris Chord, Bombergirl.
- [eapki](https://github.com/Ambloplites/eapki) - EAPKI/drmfs toolkit for AVS2-based Konami arcade games: dumps and file-checks encrypted drmfs filesystems, decrypts PKCS#7-wrapped files (kdm.dll) and obfuscated boot-time files (kbt.dll, avs2-core.dll), and can proxy e-amusement authentication.
- [packagetool](https://github.com/Ambloplites/packagetool) - Extracts Konami arcade archive formats: BAR (both variants), MAR, and QAR. See also [unarchive](https://github.com/proeren2002/unarchive), a minimal x86 assembly CLI extractor for the same BAR/QAR/MAR formats plus D2.
- [eaclient](https://github.com/Ambloplites/eaclient) - Client and protocol documentation for Konami's e-amusement (XRPC) network services, for sending arbitrary requests to arcade backend services.
- [vibea3](https://github.com/GEEKiDoS/vibea3) - Typed Rust implementation of the e-Amusement HTTP RPC transport: decodes XML or KBinXML directly into structs, dispatches `{class}.{method}` handlers, and reimplements the request packet format, custom LZ77 compression, and RC4 transport wrapper. Includes a module for pop'n music High Cheers (M39).
- [bio2-tools](https://github.com/Feiryn/bio2-tools) - Tools, libraries, and documentation for the BI2A/BI2X "BIO2" arcade cabinet I/O board (Renesas RX621 MCU).
  - Features: Firmware dumping/decryption from `libaio_iob.dll`, encryption/decryption of the `biovideo` firmware file, MOT file generation for official Renesas flashing tools, board identification.
- [avsproperty](https://github.com/Ambloplites/avsproperty) - Library and CLI for converting Konami AVS2 property files.
- [2dxrender](https://github.com/Kuroshirowak/2dxrender) - Renders beatmania IIDX `.1` chart files into audio, mixing in BGM and keysounds from 2dx/s3p audio archives; supports beatmania IIDX 25 CANNON BALLERS.
- [avslz](https://github.com/Ambloplites/avslz) - Library and CLI for Konami AVS2's LZ-based data compression format.
- [gobbletools](https://github.com/987123879113/gobbletools) - Archived grab-bag of tools for older Konami/BEMANI arcade systems.
  - Systems: System 573 (Dance Maniax video/animation renderer, GuitarFreaks/DrumMania tools, MP3 .DAT decryption, JAMMA I/O), Twinkle (beatmania IIDX video conversion, MGP key generation), Viper (ParaParaParadise 2nd Mix HDD dumper), Python1 (pop'n music HDD dumper), Python2 (DanceDanceRevolution, GuitarFreaks/DrumMania, Toy's March).
  - Also includes: DDR character model converter (AC/PS1, outputs glb/gltf/obj/StepMania), DDR animation and chart tools, a TM2C texture converter, and beMouse tools.
- [ddr-tools](https://github.com/root670/ddr-tools) - Tools for extracting and modifying files from Dance Dance Revolution CS games: TCB image extractor and TCB-to-PNG converter/injector, plus a `filedata.bin` extract/create tool driven by the game ELF file table.
- [iidx-ps2tools](https://github.com/SaxxonPike/iidx-ps2tools) - Work-in-progress tools for PS2 beatmania IIDX games (3rd style onward) that extract data directly from the archives: overlay animations (saved as GIF), movies, and charts convertible to JSON or other IIDX chart formats.
  - [iidx-datatools](https://github.com/SaxxonPike/iidx-datatools) - Python scripts for IIDX data: building `texturelist.xml` from an image folder and operations on `music_data.bin`.
- [sys573tools](https://github.com/SaxxonPike/sys573tools) - Konami System 573 miscellany, including py573a (Python recreation of 573a.jar for encrypting/decrypting digital audio data) and a hardware digital-audio decryption patch tool based on Drummania 5th Mix.
- [rhythm-game-formats](https://github.com/SaxxonPike/rhythm-game-formats) - Documentation of file formats used by Bemani games.
- [eamold](https://github.com/987123879113/eamold) - Research server reimplementing the old XML-based (pre-binary XML) System 573 e-Amusement network protocol for GuitarFreaks/DrumMania (7th-11th Mix era), including ee'mall content update data handling.

##### Tokimeki Memorial

- [Tokimeki-Memorial-2-Substories-Tool](https://github.com/gopicolo/Tokimeki-Memorial-2-Substories-Tool) - Tool for extracting, editing, and reinserting text in Tokimeki Memorial 2 Substories.
- [TM3_Tools](https://github.com/ShrNme/TM3_Tools) - Work-in-progress toolset for a fan translation of Tokimeki Memorial 3: Yakusoku no Ano Basho de (PS2).
- [OFS3-TOOL](https://github.com/Liquid-S/OFS3-TOOL) - Unpacks and repacks OFS3 archives (which recursively nest further OFS3 containers and gzip-compressed files) for Tokimeki Memorial Girl's Side 3rd Story (PSP).

##### Yu-Gi-Oh

- [TFCardEditGUI](https://github.com/xan1242/TFCardEditGUI) - GUI frontend for TFCardEdit to edit the card database format found in Yu-Gi-Oh! Tag Force games, Yu-Gi-Oh! Online, and other Yu-Gi-Oh! titles developed by Other Ocean Interactive. Currently supports Tag Force 1.
- [TFCardEdit](https://github.com/xan1242/TFCardEdit) - Command-line tool for manipulating the card database in Yu-Gi-Oh! Tag Force games; tested with Tag Force 1.
- [YGOFM-BGEx](https://github.com/xan1242/YGOFM-BGEx) - Extracts the campaign-mode background images of Yu-Gi-Oh! Forbidden Memories from `WA_MRG.MRG` as DDS (SLUS-01411 only).
- [UnityLangDataUtil](https://github.com/xan1242/UnityLangDataUtil) - Extracts all strings from Unity `LangData` assets (found in games such as Yu-Gi-Oh! Cross Duel) into a readable text file; rebuilding is not supported yet.
- [md_spine_tools](https://github.com/UNOWEN-OwO/md_spine_tools) - Blender add-on that imports Yu-Gi-Oh! Master Duel's Spine 2D character/Live2D animation files into a 3D Blender model.
- [YGO_VN_Toolkit](https://github.com/hiroshil/YGO_VN_Toolkit) - Localization toolkit for the "Power of Chaos" engine PC games (Yugi the Destiny/Joey the Passion): editor and rebuilder for the language-dependent BIN text assets plus an EXE patcher to inject a new language.
- [YGO_SystemDat_Editor](https://github.com/hiroshil/YGO_SystemDat_Editor) - Decoder/editor/encoder for the `system.dat` config format used by "Power of Chaos" engine Yu-Gi-Oh! PC games.
- [YuGiOh-PoC-ModTools](https://github.com/derplayer/YuGiOh-PoC-ModTools) - Launcher and modding toolkit covering the "Power of Chaos" engine across all its PC/Online variants (Yugi the Destiny, Kaiba the Revenge, Joey the Passion, and the Online SHONEN JUMP/Phase 1/Phase 2/Duel Evolution builds).
  - Formats: `.dat` archives (decompression/decryption), `.YGA` graphics (Yu-Gi-Oh Graphic Acronym), LZSS-compressed text/bin files.
  - Features: Resolution/position editing for graphic elements and effects, modernization fixes for the game launcher.
- [yugioh-dor-deckedit](https://github.com/RenolY2/yugioh-dor-deckedit) - Python tool for editing the deck data in Yu-Gi-Oh! Duelist of Roses (PS2).
- [Yu-Gi-OhEarlyDaysCollection](https://github.com/turtle-insect/Yu-Gi-OhEarlyDaysCollection) - Save data editor for Yu-Gi-Oh! Early Days Collection (Switch).

##### Contra

- [nes-contra-us](https://github.com/vermiceli/nes-contra-us) - Annotated disassembly of the Contra (US) NES ROM that reassembles byte-for-byte from source with cc65.
  - Includes: control-flow diagrams and enemy AI documentation, graphics/audio/ROM-mapping guides, extracted sprite libraries, and FCEUX/Mesen debugging symbols.
  - Also builds the PAL Probotector variant. See also [nes-super-c](https://github.com/vermiceli/nes-super-c) by the same author, an equivalent disassembly of the sequel Super C (US) / Probotector (EU).

##### Boktai

- [boktai2](https://github.com/akatsuki105/boktai2) - Work-in-progress disassembly of Boktai 2: Solar Boy Django (GBA, Japan v1.1).

##### Metal Gear Solid

###### Archive & Data Extraction Tools

- [Rex](https://github.com/Jayveer/Rex) - A tool to extract the Stage Dir and Dar files from the game Metal Gear Solid on PS1
- [DAR Archive Editor (Metal Gear Solid 2: Sons of Liberty)](https://www.moddb.com/games/metal-gear-solid-2-sons-of-liberty/downloads/dar-archive-editor)
- [GzsTool](https://github.com/Atvaark/GzsTool) - Archive tool for MGSV supporting QAR, GZS, and FPK files.
- [MGTools](https://github.com/GrzybDev/MGTools) - Tools for extracting and importing data from Metal Gear PC ports.
  - Games: Metal Gear, Metal Gear 2: Solid Snake
  - Features: Data extraction, conversion, import, export
- [MGS4Datless](https://github.com/Zoft123/MGS4Datless) - Tool to unpack and restructure Metal Gear Solid 4's stage.dat archive files.
- [tools-mgs](https://github.com/Joy-Division/tools-mgs) - Collection of tools for working with Metal Gear Solid game file formats.
- [Arsenal](https://github.com/Jayveer/Arsenal) - Extracts Face and Stage archive files from the PS2 version of Metal Gear Solid 2, with a filename dictionary to resolve hashes.
- [Chrysalis](https://github.com/Jayveer/Chrysalis) - Extracts SLOT.DAT and STAGEDAT.PDT archive files from Metal Gear Solid: Peace Walker (PSP and PS3 versions), including DAR/QAR sub-archives.
- [Shagohod](https://github.com/Jayveer/Shagohod) - Extracts Slot and Stage archive files from Metal Gear Solid 3, including the Subsistence version, with a filename dictionary to resolve hashes.
- [Solideye](https://github.com/Jayveer/Solideye) - Extracts and repacks Slot, Stage, DAR, and QAR archive files from Metal Gear Solid 4, with decryption/encryption support for MGS4 Database disc, Metal Gear Online 2, and MGS4 Demo Package stage files.
- [MGSDATool](https://github.com/gdkchan/MGSDATool) - Metal Gear Solid 3/4 translation toolkit.

###### Models, Textures, Animation & Stage Tools

- [MGS-KMD-Noesis](https://github.com/Jayveer/MGS-KMD-Noesis) - Noesis Plugin for Metal Gear Solid PS1 Model (KMD) and Animation (OAR) files
- [MGS-MDL-Noesis](https://github.com/Jayveer/MGS-MDL-Noesis) - Noesis plugin for importing Metal Gear Solid 3 MDL models and MTAR animations.
- [MGS-Master-Collection-Noesis](https://github.com/Jayveer/MGS-Master-Collection-Noesis) - Noesis plugin to load textured models and animations from the Master Collection versions of MGS2 and MGS3.
- [MGS4-MDN](https://github.com/cipherxof/MGS4-MDN) - Blender addon to import/export models from Metal Gear Solid 4's proprietary MDN model format.
- [MTAR-GEAR](https://github.com/316austin316/MTAR-GEAR) - Tool for modifying and swapping animations in Metal Gear Solid games on PC.
- [MGS-MDN-Noesis](https://github.com/Jayveer/MGS-MDN-Noesis) - Noesis plugin for viewing textured 3D models and animations from Metal Gear Solid 4: Guns of the Patriots (MDN format).
- [MGS-MDP-Noesis](https://github.com/Jayveer/MGS-MDP-Noesis) - Noesis plugin for viewing textured 3D models and animations from Metal Gear Solid: Peace Walker.
- [MGS-KMS-EVM-Noesis](https://github.com/Jayveer/MGS-KMS-EVM-Noesis) - Noesis plugin for viewing textured 3D models and animations from Metal Gear Solid 2: Sons of Liberty (KMS/EVM formats, PS2 GS swizzling).
- [CTXR-Converter](https://github.com/316austin316/CTXR-Converter) - Converts CTXR texture files used in the Metal Gear Solid 3 HD/Metal Gear Solid 2 HD (Master Collection) releases to PNG/TGA/DDS and back.
- [Haven (HavenStudio)](https://github.com/cipherxof/Haven) - Stage editor for all games running on the Metal Gear Solid 4 (Fox Engine predecessor) MGS4 engine.
- [CtxrTool](https://github.com/Jayveer/CtxrTool) - Converts CTXR textures from Metal Gear Solid: Master Collection to DDS, BMP, or TGA, with work-in-progress support for converting back to CTXR.
- [FMDL](https://github.com/Jayveer/FMDL) - 3ds Max script for working with Metal Gear Solid V's proprietary Foxmodel (FMDL) format.
- [kmy2obj](https://github.com/gdkchan/kmy2obj) - Metal Gear Solid: The Twin Snakes model exporter.
- [MilkGear](https://github.com/LeonamMiiller/MilkGear) - Metal Gear Solid 3 / Collection HD (PS3) `.ctxr` texture editor.

###### Save, Audio & Video Tools

- [MGSV_SaveTranslator](https://github.com/mi5hmash/MGSV_SaveTranslator) - Tool for decrypting and encrypting Metal Gear Solid v save files.
- [MGS3-Audio-Converter](https://github.com/316austin316/MGS3-Audio-Converter) - Converts Metal Gear Solid 3's proprietary audio formats to standard WAV files and back.
- [MG-REXXS](https://github.com/316austin316/MG-REXXS) - GUI tool for encrypting and decrypting .xxs video files from the Metal Gear Solid Master Collection.

###### Scripting & Bytecode Tools

- [Gcx](https://github.com/Jayveer/Gcx) - Decompiles GCX bytecode files from Metal Gear Solid games to original Game Command Language scripts.
  - Games: Metal Gear Solid 3, Metal Gear Solid 4+
  - Features: GCX bytecode decompilation
- [gcx_decompiler](https://github.com/oct0xor/gcx_decompiler) - Decompiler for GCX/GCL bytecode scripts used in Metal Gear Solid games, tested on MGS2 (PC) and MGS3 (PS2).
- [LiquidGear](https://github.com/LeonamMiiller/LiquidGear) - Metal Gear Solid 3 / Collection HD `.sdt` text editor.
- [mgsgbLz](https://github.com/romhack/mgsgbLz) - Text tool for Metal Gear Solid: Ghost Babel (Game Boy Color), handling the game's MTE and LZ text compression.

###### Documentation, Decompilation & Disassembly

- [libgcl](https://github.com/Jayveer/libgcl) - Attempt at reversing the libgcl library used in Metal Gear Solid 4. Expected to be compiled on Big Endian architecture as per the original.
- [mgs_reversing (decomp)](https://github.com/FoxdieTeam/mgs_reversing) - Matching decompilation of Metal Gear Solid (PSX).
- [MGSV QAR Dictionary Project](https://github.com/emoose/MGSV-QAR-Dictionary-Project) - Community project documenting QAR archive format and file naming for MGSV Ground Zeroes and The Phantom Pain.
- [TPP.FileFormats](https://github.com/Atvaark/TPP.FileFormats) - Fox Engine file format documentation for Metal Gear Solid V: The Phantom Pain.
- [MetalGear](https://github.com/GuillianSeed/MetalGear) - Fully annotated disassembly of the original Metal Gear (MSX2, Konami, 1987).
- [mgs3](https://github.com/GirianSeed/mgs3) - Matching decompilation of Metal Gear Solid 3: Snake Eater (PS2, 2004).

###### Online / Server Tools

- [mgo2server](https://github.com/comradesean/mgo2server) - Metal Gear Online 2 server emulator for the retail MGS4 disc (BLUS30109), reimplementing the game's network protocol layer.

##### Silent Hill

- [silent-hill-decomp (decomp)](https://github.com/shdecompilations/silent-hill-decomp) - Matching decompilation of Silent Hill (PS1, US 1.1).
- [sh2SaveTools](https://github.com/TheMachineAmbassador/sh2SaveTools) - Save file tools for Silent Hill 2.
- [SH2Unpack](https://github.com/SamusAranX/SH2Unpack) - Unpacker for Silent Hill 2 archive files.
- [SilentHillOrigins_PS2_AudioExtractor](https://github.com/iluny1/SilentHillOrigins_PS2_AudioExtractor) - Audio extractor for Silent Hill Origins (PS2).
- [sh3redux](https://github.com/Palm-Studios/sh3redux) - Silent Hill 3 archive extraction and modification tools.
- [Sparagas/Silent-Hill](https://github.com/Sparagas/Silent-Hill) - Reverse engineering research and documentation for Silent Hill file formats.
- [Murugo/Misc-Game-Research (Silent Hill 2)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Silent%20Hill%202%2B3) - Reverse engineering notes for Silent Hill 2 & 3 (PS2).
- [Silent Hill Museum](https://silenthillmuseum.org/) - Website dedicated to Silent Hill series with file format documentation.
- [dreamingmoths/silent-hill-museum](https://github.com/dreamingmoths/silent-hill-museum) - Repository for Silent Hill Museum website with technical documentation.
- [Silent-Hill-2-Enhancements](https://github.com/elishacloud/Silent-Hill-2-Enhancements) - Project to enhance Silent Hill 2 (PC) graphics and audio, includes scripts to build or modify SH2 audio files (SFX, BGM, Dialog).
- [memory-of-alessa](https://github.com/dreamingmoths/memory-of-alessa) - Matching decompilation project of Silent Hill 3 (PS2), reverse-engineering the binary and asset handling.
- [SilentEngine](https://github.com/Sezzary/SilentEngine) - In-progress cross-platform engine port of Silent Hill based on decompilation, parsing original game data with support for translation and modding.
- [SilentHillMapExaminer](https://github.com/ItEndsWithTens/SilentHillMapExaminer) - BizHawk external tool utility to help reverse engineer the map format used in the original Silent Hill (PS1).
- [SilentHillDatabase](https://github.com/Polymega/SilentHillDatabase) - File format documentation and glossary for Silent Hill 1-3.
- [RenderEclipse-Tools](https://github.com/IWILLCRAFT-M0d/RenderEclipse-Tools) - Toolset and documentation for reverse-engineering Climax Studios' RenderWare-based Silent Hill games (Origins, Shattered Memories, Homecoming).
- [Silent-Hill-3-Modding](https://github.com/316austin316/Silent-Hill-3-Modding) - Hub for Silent Hill 3 reverse-engineering and file format documentation.
- [sh3-evil-effect](https://github.com/SNMetamorph/sh3-evil-effect) - Reverse-engineered reimplementation of the "Another World Evil" procedural texturing visual effect from Silent Hill 3.
- [SHresearch](https://github.com/SILENTpavel/SHresearch) - Research project documenting Silent Hill demo builds, with file specifications and format details.
- [Climax_Silent-Hill_Engine](https://github.com/BlackLineInteractive/Climax_Game_Engine_Toolkit) - Toolkit for reverse-engineering Climax Studios' RenderWare-based Silent Hill engine, covering Silent Hill Origins (PS2/PSP) and related titles.
- [Silent-Hill-Shattered-Memories-Localization-Tool](https://github.com/LittleBitUA/Silent-Hill-Shattered-Memories-Localization-Tool) - Toolkit for localizing Silent Hill: Shattered Memories across three platforms from a single shared translation source, handling the game's archive/text formats.
- [sh2tex](https://github.com/iOrange/sh2tex) - Silent Hill 2 Textures Explorer, a tool born from reverse-engineering Silent Hill 2's proprietary texture resource formats.
- [SilentHillOriginsPS2](https://github.com/leeao/SilentHillOriginsPS2) - Noesis plugin for Silent Hill Origins (PS2) DFF models (with Delta Morph support), TXD textures, and ANM animations.
- [DownpourRecomp](https://github.com/LittleBitUA/DownpourRecomp) - Silent Hill: Downpour native Windows PC port via static recompilation of the Xbox 360 binary.
- [SH3_chr](https://github.com/alanm20/SH3_chr) - Noesis plugin/loader for Silent Hill 3 character CHR/MDL models, exporting to Blender/glTF/OBJ.
- [SH4_map_bin_PC](https://github.com/alanm20/SH4_map_bin_PC) - Noesis plugin for viewing Silent Hill 4 (PC) map BIN files.
- [SH2_map](https://github.com/alanm20/SH2_map) - Noesis plugin for viewing Silent Hill 2 (PC) map files.
- [sh4bin](https://github.com/HunterStanton/sh4bin) - Unpacks and repacks Silent Hill 4's .bin archive files.
- [sh4pac](https://github.com/HunterStanton/sh4pac) - Unpacks and repacks Silent Hill 4's .PAC sound archives.
- [sh4texturetool](https://github.com/HunterStanton/sh4texturetool) - Extracts and replaces textures stored in Silent Hill 4's .bin texture chunks.
- [sh4sh4](https://github.com/HunterStanton/sh4sh4) - Packs and unpacks the .sh4 archives used by the PC and Xbox versions of Silent Hill 4: The Room.
- [sh4modeltool](https://github.com/HunterStanton/sh4modeltool) - Experimental tool for converting Silent Hill 4 models.
- [sh4texteditor](https://github.com/HunterStanton/sh4texteditor) - Editor for text stored in Silent Hill 4's message_*.bin files.
- [MFA-Tool-for-Silent-Hill-3-PS2](https://github.com/RayneDuarte/MFA-Tool-for-Silent-Hill-3-PS2-) - Unpacks and repacks MFA archives from the Silent Hill 3 (PS2) ISO, built from aluigi auriemma's original BMS extraction script.
  - See also [Silent-Hill-3-MFA-Tool](https://github.com/OAleex/Silent-Hill-3-MFA-Tool), an independent MFA archive unpacker/repacker for the same game.


##### Castlevania

- [Castlevania](https://github.com/Sparagas/Castlevania) - Castlevania reverse engineering file formats documentation and tools.
- [cv64 (decomp)](https://github.com/k64ret/cv64) - Matching decompilation of Castlevania (N64).
- [CV64Recomp](https://github.com/RevoSucks/CV64Recomp) - Static recompilation of Castlevania (N64) into a native executable, built on the cv64 decompilation above, with a companion [CV64Syms](https://github.com/RevoSucks/CV64Syms) repo of reverse-engineered function/data symbol maps.
- [cvaos (decomp)](https://github.com/testyourmine/cvaos) - Matching decompilation of Castlevania: Aria of Sorrow.
- [sotn-decomp (decomp)](https://github.com/xeeynamo/sotn-decomp) - Matching decompilation of Castlevania: Symphony of the Night (PSX, PSP, Saturn).
- [ooe (decomp)](https://github.com/LagoLunatic/ooe) - Matching decompilation of Castlevania: Order of Ecclesia (Nintendo DS).
- [graveyardduck](https://github.com/fo-fo/graveyardduck) - Compressor/decompressor for the run-length encoding used in Dracula II: Noroi no Fuuin (Famicom Disk System), the Japanese original of Castlevania II: Simon's Quest, and other 8-bit Konami games.
- [cotmsav](https://github.com/haleyjd/cotmsav) - Save RAM viewer for Castlevania: Circle of the Moon.
- [k64-rom-decompressors](https://github.com/k64ret/k64-rom-decompressors) - Decompresses and recompresses Konami N64 ROMs that use Nisitenma-Ichigo table filesystems, including Castlevania (N64).
- [SotN-Editor](https://github.com/KernelEquinox/SotN-Editor) - Mod tool for Castlevania: Symphony of the Night.
- [SNEER](https://github.com/KernelEquinox/SNEER) - Symphony of the Night Editor and Entity Recompiler.
- [DSVEdit](https://github.com/LagoLunatic/DSVEdit) - Multi-purpose editor for ROM hacking the Nintendo DS and GBA Castlevania games (Dawn of Sorrow, Portrait of Ruin, Order of Ecclesia, Aria of Sorrow, Circle of the Moon, Harmony of Dissonance).
- [dsvrandom](https://github.com/LagoLunatic/dsvrandom) - Randomizer for the Nintendo DS Castlevania games, built on DSVEdit. See also [DSVania_C_Hacking](https://github.com/LagoLunatic/DSVania_C_Hacking), notes on DSVania romhacking with C.
- [sotnrando](https://github.com/sotnrando/sotnrando) - Randomizer for Castlevania: Symphony of the Night (sotn.io), covering PS1, Sega Saturn, PSP, and XBLA versions. See also [SotnRandoTools](https://github.com/TalicZealot/SotnRandoTools), a companion collection of tools enhancing the randomizer experience, and [Sotn-Rando-Write-Diff-Generator](https://github.com/sotnrando/Sotn-Rando-Write-Diff-Generator), which diffs two game image `.bin` files into the randomizer's preset write format (JSON, CSV, or randomizer writes), accounting for CD-ROM sector layout.
- [NocturneRecomp](https://github.com/birabittoh/NocturneRecomp) - Static recompilation of Castlevania: Symphony of the Night (Xbox Live Arcade) for Windows and Linux, built on the ReXGlue SDK.
- [MariaGfxImport](https://github.com/MottZilla/MariaGfxImport) - Builds the PS1 version's "Maria" graphics chip data for Symphony of the Night by extracting assets from the PSP Dracula X Chronicles ISO image, using sotn-decomp.
- [SotN_StageEditor](https://github.com/MottZilla/SotN_StageEditor) - Editor for the tilemap layers of Symphony of the Night's stages, written in C with the Allegro 4.2 runtime.
- [saturn-sound-player](https://github.com/sozud/saturn-sound-player) - Offline player for Sega's Saturn sound library, playing Symphony of the Night's in-game sequenced sound effects (Japanese retail `0.BIN`) and Scorcher's `.MUS` songs from the user's own game files, with Ymir emulating the 68k and SCSP in low-level mode or a C++ reimplementation of Sega's sound driver in high-level mode.
- [CurseLament-Tool](https://github.com/OAleex/CurseLament-Tool) - Tool for managing Castlevania game files for PlayStation 2.

##### Elebits

- [noclip.website (Elebits)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Elebits (Wii) level viewer, built on noclip's NW4R/BRRES loader.

##### Enthusia Professional Racing

- [EnthusiaVolumeFS](https://github.com/Nenkai/EnthusiaVolumeFS) - Extract files from Enthusia Professional Racing volumes (PS2). Supports SLPM_68519 (Subaru Demo), SLPM_65948 (Japan), SLUS_20967 (US), and SLES_53125 (Europe).

##### Love Plus

- [NLPUnpacker](https://github.com/gdkchan/NLPUnpacker) - Unpacker for New Love Plus's (Nintendo 3DS) img.bin archive.

##### Zone of the Enders

- [tools-zoe (Vivid Transparency)](https://github.com/Joy-Division/tools-zoe) - Tools for working with files from Zone of the Enders (PS2).
  - Formats: ZOE.DAT/PAK archives, SDX sound archives (EFX/MDX sequences, WVX wave archives → VAG), PSS video/audio streams (M2V/VAG/subtitle demuxing), TEX textures.
  - Tools: `dat-extract`, `pak-extract`, `sdx-extract`, `efx-splitter`, `mdx-parser`/`mdx-splitter`, `pss-demux`, `subtitle-convert`, `tex-to_image`, `wvx-extract`.
  - See also the same author's [ArmsDepot](https://github.com/Joy-Division/tools-mgs) *(archived)* for unpacking Zone of the Enders 2's STAGE.DAT archives.
- [CyArchiveTool](https://github.com/Surihix/CyArchiveTool) - Tool to extract and repack the .pack archive files from the PC version of the game Zone of Enders 2 MARS.
  - See also [CyArchivePathGenerator](https://github.com/Surihix/CyArchivePathGenerator), a companion tool that generates file paths for files stored in those .pack archives from a text file of candidate paths.
- [Zoe2PacTool](https://github.com/Surihix/Zoe2PacTool) - Unpacks (all files, a single file, or just the filenames) and repacks the .pac archives in the atlas folder of Zone of the Enders 2, with separate modes for the Hexadrive HD Collection version and the PC/PS4 versions.
##### Yu-Gi-Oh! GX: Duel Academy

- [yugiohgx-da](https://github.com/coolstuffinc/yugiohgx-da) - Reverse-engineering toolkit for Yu-Gi-Oh! GX: Duel Academy (GBA) with a CLI for extracting/patching card artwork, duelist sprites, and location thumbnails, plus extracting and patching string tables.

##### Yu-Gi-Oh! Tag Force

- [CIPTool](https://github.com/xan1242/CIPTool) - Unpacks and repacks CIP/CPM card art package files from the Yu-Gi-Oh! Tag Force series (PSP).
- [ehppack](https://github.com/xan1242/ehppack) - Unpacks and repacks EHP archive files from the Yu-Gi-Oh! Tag Force series (PSP).
- [tagforcestring](https://github.com/xan1242/tagforcestring) - General-purpose string data utility for the Yu-Gi-Oh! Tag Force series (PSP), designed to aid translation.
- [TFSndEdit](https://github.com/xan1242/TFSndEdit) - Extracts and repacks the `SNDDAT` sound banks of Yu-Gi-Oh! Tag Force (PSP), tested with Tag Force 1 and 6; needs the SHDS sound header from the executable (EBOOT.BIN).
  - [TagForceMusicEx](https://github.com/xan1242/TagForceMusicEx) - Earlier, simpler extractor for the AT3 music files (no repacking).
- [EHPScanner](https://github.com/xan1242/EHPScanner) - Scans for and extracts EhFolder (EHP) archives embedded in files, mainly Tag Force EBOOT files, with autodetection and filename assignment.

##### Pop'n Music

- [pop'n rhythmin (source reconstruction)](https://github.com/Tatsh/expert-rotary-phone) - Reconstructed source code for pop'n rhythmin (jp.konami.popnmusic), the mobile spin-off of Konami's Pop'n Music series, recovered from the original iOS binary's embedded debug/assert strings and RTTI; requires the original game's IPA to build.
- [SH-Save-Editor](https://github.com/nuttycream/SH-Save-Editor) - Save file editor for a Silent Hill title.
##### REFLEC BEAT

- [expert-xylophone](https://github.com/Tatsh/expert-xylophone) - Reconstructed source of REFLEC BEAT plus (`jp.konami.rbplus`), Konami's iOS rhythm game, recovered from the shipped binary; requires your own IPA with the game assets to build.

##### jubeat

- [jubeat plus (source reconstruction)](https://github.com/Tatsh/expert-satphone) - Reconstructed source code for jubeat plus, Konami's iOS jubeat spin-off, recovered from the shipped binary; requires your own IPA with the game assets to build. By the same author as the pop'n rhythmin and REFLEC BEAT plus reconstructions above.

##### Green Beret

- [ZXSpectrumGreenBeret](https://github.com/Paulie68000/ZXSpectrumGreenBeret) - Fully documented, reverse engineered source code for the ZX Spectrum version of Green Beret.

#### Konjak

##### Iconoclasts

- [Iconoclast-Translation-Tool](https://github.com/Liquid-S/Iconoclast-Translation-Tool) - Extracts and repacks Iconoclasts' `dia` script file to/from gettext `.po` for translation, for the PC and PS Vita versions.

#### Sacnoth (Koudelka)

- [Koudelka-Noesis-Plugin](https://github.com/korobetski/Koudelka-Noesis-Plugin) - Noesis plugin for Koudelka models and animations.

#### PUBG (Krafton)

- [pubg-maps](https://github.com/cgcostume/pubg-maps) - Extracts and converts PUBG's (Erangel, Erangel Classic, Miramar, Sanhok, Vikendi, Karakin, Camp Jackal) and Fortnite's (Apollo, Papaya, Athena) Unreal Engine terrain tile textures (.tga/.ubulk, exported via UE Viewer) into lossless 16-bit height and 8-bit normal PNGs.
- [ifs-unpacker](https://github.com/halloweeks/ifs-unpacker) - Extractor for the `.ifs`/`.nifs` archive format used to package PUBG Mobile's game data.
- [pubg-unpacker](https://github.com/halloweeks/pubg-unpacker) - C extractor for PUBG Mobile's `.pak` files, targeting versions prior to the 1.1.0 update.
- [PR-Pak-Tool](https://github.com/0xPrince/PR-Pak-Tool) - Cross-platform tool to unpack `.pak` files across multiple PUBG variants (PUBG Mobile, PUBG Mobile Lite, Game For Peace); repacking is planned but not yet implemented.
- [PUBGLiteExplorerWV](https://github.com/zeroKilo/PUBGLiteExplorerWV) - Tool for browsing and exporting content from PUBG Lite pak files.

#### LEGOLAND (Krisalis Software)

- [legoland](https://github.com/marijnvdwerf/legoland) - Matching decompilation of LEGOLAND (2000), the LEGO theme-park management game, in the style of the LEGO Island decompilation. Uses [reccmp](https://github.com/isledecomp/reccmp) to verify recompiled functions byte-for-byte against the original binary via the [wibo](https://github.com/decompals/wibo) PE loader.

#### Kuju London

- [PF2-BMP-Editor](https://github.com/htimsnhoj543678/PF2-BMP-Editor) - .pf2 file editor for Battalion Wars 2 (BWii).
- [Battalion-Wars-SFX-Editor](https://github.com/JasperZebra/Battalion-Wars-SFX-Editor) - Sound effects editor for Battalion Wars.
- [MeltyTool (BattalionWars)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/BattalionWars) - Battalion Wars format viewer/exporter.
- [battalion-level-editor](https://github.com/RenolY2/battalion-level-editor) - Level editor for Battalion Wars.
- [battalion-tools](https://github.com/RenolY2/battalion-tools) - Collection of tools for working with Battalion Wars files.
- [bw-model-viewer](https://github.com/RenolY2/bw-model-viewer) - Model viewer for Battalion Wars.
- [bwterrain-blender](https://github.com/RenolY2/bwterrain-blender) - Blender addon for Battalion Wars terrain.
- [bw-restool](https://github.com/RenolY2/bw-restool) - Resource tool for Battalion Wars files.
- [bw-texture-conv](https://github.com/RenolY2/bw-texture-conv) - Texture converter for Battalion Wars.
- [bw-restool-GUI](https://github.com/JasperZebra/bw-restool-GUI) - Battalion Wars Unified Tool combining restool and texture converter. Handles RES archive extraction and texture file conversion with automatic game version detection for both BW1 and BW2.
- [BW2_Custom_Unit_Maker](https://github.com/JasperZebra/BW2_Custom_Unit_Maker) - GUI tool for creating custom unit variants in Battalion Wars 2 (Wii).
- [bw_lua_docs](https://github.com/RenolY2/bw_lua_docs) - Documentation of Battalion Wars/Battalion Wars 2 Lua functions.

#### Kuro Games

##### Wuthering Waves

- [WWMI-Tools](https://github.com/SpectrumQT/WWMI-Tools) - Blender addon for importing and modifying 3D models, animations, and textures from Wuthering Waves game files.
- [WuwaTools](https://github.com/Hiro420/WuwaTools) - Collection of Wuthering Waves reverse-engineering scripts.
  - Tools: protodumperv2 (Protobuf message dumper), fbsdumper (FlatBuffers schema dumper), WWParser (BinData/TextMap parser for the game's ConfigDB).

### L
#### Team Bondi (L.A. Noire)

- [LANoireNX](https://github.com/masagrator/LANoireNX) - Python scripts for repacking modified files back into L.A. Noire's Nintendo Switch port archives (BIG/WAD/DDS formats).

#### Invictus Games (L.A. Street Racing)

- [lasr-editors](https://github.com/Niko666233/lasr-toolkit) - Windows GUI vehicle-data and save editors for the original L.A. Street Racing (2006); the vehicle editor patches numeric literals in the per-part class bytecode inside `classes.zip` packages. README states the code was AI-generated and some parts are unverified.

#### Lab Zero Games

##### Indivisible

- [indivisible](https://github.com/minirop/indivisible) - Tool to extract `.pkg` files from Indivisible.

#### ZOOM Inc. (Lagoon)

- [lagoon_x68k_trans](https://github.com/nleseul/lagoon_x68k_trans) - English translation patch for Lagoon, the Japan-exclusive Sharp X68000 action RPG; as far as the author knows, the only attempt to translate the original X68000 version rather than the altered SFC/SNES port.

#### Climax Entertainment (Landstalker)

- [landstalker_editor](https://github.com/lordmir/landstalker_editor) - Tool for extracting, viewing, editing, and re-inserting the various data found in Landstalker (Sega Genesis) ROMs and its disassembly.
- [landstalker_disasm](https://github.com/lordmir/landstalker_disasm) - Landstalker (Sega Genesis) ROM disassembly.
- [landstalker_tools](https://github.com/lordmir/landstalker_tools) - Collection of tools for editing the compressed/encoded assets found in Landstalker and other Sega Genesis games.
- [landstalker_engine](https://github.com/lordmir/landstalker_engine) - Reimplementation of the DDS520 engine used by Landstalker, running on modern hardware (SDL3) while loading the original game's assets.

#### Larian Studios

- [dos2de_collada_exporter](https://github.com/Norbyte/dos2de_collada_exporter) - Blender addon for importing/exporting Collada and glTF models from Baldur's Gate 3 and Divinity: Original Sin 2.
- [Norbyte's Baldur's Gate 3 Script Extender](https://github.com/Norbyte/bg3se) - Baldur's Gate 3 Script Extender.
- [Native Mod Loader](https://www.nexusmods.com/baldursgate3/mods/944) - Native DLL plugin loader for Baldur's Gate 3.
- [BG3-DialogsBinary-Node-Editor](https://github.com/kitmods/BG3-DialogsBinary-Node-Editor) - Node-based editor for Baldur's Gate 3 dialog binary files.

##### Divinity: Original Sin 2

- [DoS-2-Savegame-Editor](https://github.com/NovFR/DoS-2-Savegame-Editor) - Save game editor for Divinity: Original Sin 2.
- [LSLib](https://github.com/Norbyte/lslib) - Tools for manipulating Divinity Original Sin and Baldur's Gate 3 files including archive extraction.
- [Norbyte's Divinity Script Extender](https://github.com/Norbyte/ositools) - Divinity: Original Sin 2 script extender toolkit adding features to the scripting language of the game.

##### Divine Divinity / Beyond Divinity

- [DivEdit](https://github.com/Raan/DivEdit) - Level and asset editor for Divine Divinity and Beyond Divinity (Larian Studios), parsing proprietary packed archive formats (CPackedb, CPackedi) with LZO compression; supports editing terrain, textures, and game objects.
- [Beyond-Divinity-Translation-Tool](https://github.com/dortkoldantaciz/Beyond-Divinity-Translation-Tool) - Translation tool for Beyond Divinity (extract/repack .cmp, .gsm).
- [OsirisRE](https://github.com/usernameak/OsirisRE) - Reverse-engineering project for Larian's Osiris VM, the scripting engine behind Divine Divinity's story files.
  - Contents: DLL wrapper/import library for OsirisDLL.dll, a compiler wrapper for building `story.000` script files from `.div` sources, and an ASI-loader mod that fixes INIT-goal recompilation breaking vanilla scripts.
- [DivineDivinity_StoryEditor](https://github.com/Raan/DivineDivinity_StoryEditor) - GUI story/script editor for Divine Divinity, built on OsirisRE above.
- [bg3-dialog-reader](https://github.com/angaityel/bg3-dialog-reader) - Tool to view, extract, convert, and listen to dialog files from Baldur's Gate 3.
- [bg3-dds-convert](https://github.com/Geminitrix/bg3-dds-convert) - Batch texture converter for Baldur's Gate 3 modding, converting PNG/JPG/BMP/TGA/TIF/HDR images into game-accurate .DDS files using the same texconv settings BG3 itself uses per icon type, verified by inspecting the game's shipped assets.
- [BG3SE (Savegame Library)](https://github.com/Wahkah/BG3SE) - Baldur's Gate 3 savegame library and editor parsing LSPK/LSF/LSMF from scratch to decode abilities, classes, feats, XP, and items. Not related to Norbyte's Script Extender of the same abbreviation; character edits currently produce saves the game won't load (read-only in practice).
- [dos2de-save-game-editor-macos](https://github.com/XEonAX/dos2de-save-game-editor-macos) - macOS-compatible save game editor for Divinity: Original Sin 2 - Definitive Edition.

#### MiCROViSiON (Legend of Galactic Heroes)

- [LoGHTools](https://github.com/derplayer/LoGHTools) - Modding tools for Legend of Galactic Heroes (2008, PC).

#### Contrail (Legend of Legaia)

- [LegaiaText](https://github.com/gdkchan/LegaiaText) - Text editor for Legend of Legaia.

#### Obb Studio (Legend of Mortal)

- [lom_modkit](https://github.com/mohui666/lom_modkit) - Visual story-modding toolkit for Legend of Mortal (活侠传); a graphical editor (no Lua required) for character dialogue, scene staging, branching plots, and music/sound cues, using the game's own characters/scenes/systems, exporting standalone `.lommod` mod packages loaded by an in-game plugin.
- [lom_save_analyzer](https://github.com/mohui666/lom_save_analyzer) - Read-only, browser-based save analyzer for Legend of Mortal (活侠传); implements a custom MS-NRBF parser for `.dat` save slots and cross-references the game's own data tables and story text for global collection tracking.
- [mortal-save-editor](https://github.com/wildwing821/mortal-save-editor) - Python CLI save editor for Legend of Mortal (活俠傳) that patches values directly in the binary `Save_XXX.dat` (length-prefixed key + little-endian int32 pattern), covering money, martial points, sect stats and character attributes.

#### LEGO Desktop Toy

- [ldtsmash](https://github.com/JrMasterModelBuilder/ldtsmash) - Library and CLI for listing, extracting, and rebuilding LEGO Desktop Toy's `smash.ndx`/`smash.wad` archive pair.
- [ldtshp2bmp](https://github.com/JrMasterModelBuilder/ldtshp2bmp) - Converts LEGO Desktop Toy's `.SHP` pixel/`.PAL` palette image pairs to indexed BMP files.

#### LEGO Digital Designer

- [LIF-Extractor](https://github.com/JrMasterModelBuilder/LIF-Extractor) - Extracts LEGO Digital Designer's LIF archive files.

#### TT Games (LEGO Island)

- [isle (decomp)](https://github.com/isledecomp/isle) - Matching decompilation of LEGO Island (1997).
- [Lego-City-Undercover-Decompilation (decomp)](https://github.com/Nintendocustom/Lego-City-Undercover-Decompilation) - Matching decompilation of Lego City Undercover.
- [BionicleHeroesTools](https://github.com/REDxEYE/BionicleHeroesTools) - Blender plugin for importing Bionicle Heroes files. Supports NUP and HGP model formats and PAK archive extraction. Requires Blender 3.1 to 3.5.
- [LegoTools](https://github.com/REDxEYE/LegoTools) - Tools for working with LEGO game file formats.
- [FUSExplorer](https://github.com/efimandreev0/FUSExplorer) - Tool for editing LEGO games by unpacking and repacking .loc and .fib archive and localization file formats.
- [NuXtractor](https://github.com/IsaMorphic/NuXtractor) - Extracts textures and models from Lego Star Wars: The Video Game (PC/Xbox) map files. Deprecated by its author in favor of the unreleased StudSmelter successor.
- [nu-blender](https://github.com/IsaMorphic/nu-blender) - Modern Blender addon for importing scene files from the PC and Xbox versions of LEGO Star Wars: The Video Game (.nup and .nux formats).
- [DATOneArchiver](https://github.com/IsaMorphic/DATOneArchiver) - Clean-room RE tool for extracting, modifying, and building TT Games DAT archive files.
- [MightyStruct](https://github.com/IsaMorphic/MightyStruct) - .NET reimagining of KaitaiStruct for binary format declaration, used internally by NuXtractor for LEGO games asset extraction.
- [QuesoStruct](https://github.com/IsaMorphic/QuesoStruct) - C# source-generation library for writing binary serialization code (read/write) for TT Games and related binary file formats.
- [CFS.SnabNet](https://github.com/IsaMorphic/CFS.SnabNet) - .NET implementation of the SNAB stream format, used in TT Games modding tools.
- [SNAB](https://github.com/AlubJ/SNAB) - Struct n' Array Binary (SNAB) format spec for serializing and deserializing struct and array data, underlying CFS.SnabNet.
- [SNAB.py](https://github.com/AlubJ/SNAB.py) - Python implementation of the SNAB binary serialization format.
- [BactaTank-Classic](https://github.com/AlubJ/BactaTank-Classic) - Character creator and viewer for LEGO Star Wars: The Complete Saga, LEGO Indiana Jones: The Original Adventures, and LEGO Batman: The Videogame, previewing models directly from game files.
- [SIEdit](https://github.com/isledecomp/SIEdit) - Fully graphical viewer and editor for the SI streaming asset pack format used by LEGO Island, supporting textures, sounds, animations, path information, FMVs, and game logic/metadata.
- [isle-portable](https://github.com/isledecomp/isle-portable) - Portable version of LEGO Island (1997), built on the isle decompilation, reading and running with the original game's SI asset files.
- [racers (decomp)](https://github.com/isledecomp/racers) - Matching decompilation of LEGO Racers (1999), modeled after the LEGO Island decompilation.
- [racers-portable](https://github.com/isledecomp/racers-portable) - Portable reimplementation of LEGO Racers (1999) built on the matching decompilation, loading and parsing the original game's assets.
- [lego-tt-nxg-formats](https://github.com/JaanDev/lego-tt-nxg-formats) - Data format descriptions for Traveller's Tales' LEGO games of the NXG (next-generation) engine era.
- [TTGames-Extraction-Tools](https://github.com/AlubJ/TTGames-Extraction-Tools) - Collection of TT Games extraction tools originally created by 'sluicer' on Rock Raiders United, decompiled and preserved for researching TT Games' LEGO titles.
- [BacTSH](https://github.com/AlubJ/BacTSH) - DX11 texture sheet tool for TT Games' titles released after LEGO Batman 3: Beyond Gotham, for creating and editing texture pages.
- [LEGO-Modding-Tool](https://github.com/AlubJ/LEGO-Modding-Tool) - Modding tool for LEGO Star Wars: The Complete Saga supporting mesh and texture import into the game's files.
- [BrickBench](https://github.com/BrickBench/BrickBench) - Map editor for TT Games' LEGO titles. See also [OpenGGEngine's fork](https://github.com/OpenGGEngine/BrickBench) with additional features.
- [Diorama](https://github.com/connorh315/Diorama) - Tool for viewing and editing the 3D geometry used in Traveller's Tales' LEGO videogames.
- [BrickVault](https://github.com/connorh315/BrickVault) - Cross-platform archive extractor for TT Games' LEGO titles, from the original LEGO Star Wars through the LEGO Harry Potter Collection and LEGO Star Wars: The Skywalker Saga, handling LZHAM- and Oodle-compressed archives.
- [DATManager](https://github.com/connorh315/DATManager) - C# program for extracting files from newer Traveller's Tales (LEGO Dimensions and later) .DAT archives.
- [DATPacker](https://github.com/connorh315/DATPacker) - Builds and manages LEGO Dimensions .DAT archives.
- [Hologram](https://github.com/connorh315/Hologram) - LEGO Dimensions level viewer and exporter, with a full level editor planned.
- [GCMAudioConverter](https://github.com/linterniGamer/GCMAudioConverter) - Converts stereo WAV files to the GCM music format used by Wii-era LEGO games.
- [CBXDecoder](https://github.com/connorh315/CBXDecoder) - Converts TT Games CBX (ChatterBoX) audio files into WAV files.
- [anomaly](https://github.com/connorh315/anomaly) - Open-source mod loader for LEGO Dimensions on PS4, handling the game's archive/asset formats to load mods.
- [SEEditor](https://github.com/connorh315/SEEditor) - SoundEvent editor for LEGO Dimensions sound_event files.
- [LEGOIslandRebuilder](https://github.com/isledecomp/LEGOIslandRebuilder) - Launcher and mod/patch tool for the 1997 video game LEGO Island, from the isledecomp organization behind the isle decompilation.
- [saga (decomp)](https://github.com/opensagadev/saga) - Matching decompilation of LEGO Star Wars: The Complete Saga, from the ttdecomp organization (sibling project to isle and racers).
- [TravellersTalesPSXCollisionViewer](https://github.com/juanmv94/TravellersTalesPSXCollisionViewer) - Collision and GFX model viewer for Traveller's Tales' shared PSX-era 3D engine, reading data from PSX emulator savestates.
  - Games: Rascal, A Bug's Life, Toy Story 2, Toy Story Racer, Muppet Race Mania, The Weakest Link, Buzz Lightyear of Star Command.
- [LIME](https://github.com/mathom/LIME) - Python script that extracts wave audio files from LEGO Island `.SI` package files (eg. `JUKEBOX.SI`).

##### Toy Story 2

- [Toy-Story-2-Modding](https://github.com/mouksx/Toy-Story-2-Modding) - Tools and decompiled assets for Toy Story 2 (1999), documenting the NGN file format (character models, animations, level geometry/textures, area portals, shape links).
- [ToyTwoToolbox](https://github.com/EpicMinecartz/ToyTwoToolbox) - Editor for Toy Story 2, loading and saving .SAV save files and .NGN level/model files.
- [Toy2LevelDump](https://github.com/EpicMinecartz/Toy2LevelDump) - Extracts level format data from Toy Story 2.
- [ToyStory2Fix](https://github.com/RibShark/ToyStory2Fix) - Compatibility fixes and enhancements for the PC version of Toy Story 2, including widescreen support and increased render distance.

##### Toy Story Racer

- [TSR-PS1-Tools](https://github.com/mateusfavarin/TSR-PS1-Tools) - Tools for extracting Toy Story Racer (PS1) in-game files.

##### Sonic R

- [sonic-r](https://github.com/jnmartin84/sonic-r) - Decompilation/reimplementation of Sonic R (1997) for modern platforms, currently able to generate a Sega Dreamcast CDI of a beta build.
- [sonicr-mod-loader](https://github.com/sonicretro/sonicr-mod-loader) - Mod loader for the 2004 PC version of Sonic R.
- [RAW2BMP](https://github.com/sonicretro/RAW2BMP) - Console converter between Sonic R's headerless 24-bit `.raw`/`.ply` texture files (dimensions inferred from file size) and BMP; also includes a MapConverter that builds a map image from a `.ply` file.
- [Sonic-R-Utilities](https://github.com/InvisibleUp/Sonic-R-Utilities) - Archived. Python utilities for Sonic R files: convert tracks and character models to/from Wavefront OBJ, a Blender track importer, a model part reorder script and a modified character model viewer.
- [NTT-Model-Dumper](https://github.com/KillzXGaming/NTT-Model-Dumper) - Tool to dump .model files used by Lego Star Wars: The Skywalker Saga.
- [tt-save-editor](https://github.com/fisherjoey/tt-save-editor) - Browser-based save editor for LEGO Batman: Legacy of the Dark Knight. Decrypts the RC4-encrypted, fixed 32-byte-key save file and parses its Unreal Engine 5 GVAS fields by name to fix the "created on an updated version" error, unlock collectibles and characters, and edit mission progress. Runs entirely client-side.
- [Tt-Games-quickbms-scripts](https://github.com/linterniGamer/Tt-Games-quickbms-scripts) - QuickBMS scripts for extracting and modding archives from games made by TT Games.
- [LegoRacers2Explorer](https://github.com/adarec1994/LegoRacers2Explorer) - Browser and exporter for LEGO Racers 2's game files.

#### LEGO Loco

- [LEGO-LOCO-Decompression-Tool](https://github.com/shinyquagsire23/LEGO-LOCO-Decompression-Tool) - Decompresses LEGO Loco's proprietary bitmap/image compression format (ported from the original ASM) to BMP/raw output, for modding and resource extraction.
- [LocoDecomp](https://github.com/shinyquagsire23/LocoDecomp) - AI-assisted decompilation of LEGO Loco's engine binary (`Loco.exe`), documenting the game's `resource.RFD` archive and TileKind resource-ID system along the way.

#### LEGO Racers

- [Lego-Racers-Mod](https://github.com/Laupetin/Lego-Racers-Mod) - Modding tools and experiments for LEGO Racers (1999), working with the game's original files.

#### Attention to Detail (LEGO Racers 2)

- [UNGTC](https://github.com/JrMasterModelBuilder/UNGTC) - Extracts and rebuilds Attention to Detail's ATD GTC archives (GAMEDATA.GTC/FILELIST.INF/COMPRESS.INF) used by LEGO Racers 2, handling both known format versions and its LZ-style compression.
- [atdstrings](https://github.com/JrMasterModelBuilder/atdstrings) - Converts LEGO Racers 2's ATD binary string-table format (DBCS-aware key/value pairs with a charset table) to and from human-editable text via `txt2bin`/`bin2txt`.

#### Data Design Interactive (LEGO Rock Raiders)

- [legorockraiders-analysis](https://github.com/trigger-segfault/legorockraiders-analysis) - Reverse engineering and decompilation of LEGO Rock Raiders (1999), covering the underlying Gods98 engine shared with Data Design Interactive's earlier titles. Includes a Ghidra archive, decompiled source dumps, and a VS Code syntax-highlighting plugin for the game's scripting/config formats.
- [manic-miners-level-indexer](https://github.com/Wal33D/manic-miners-level-indexer) - Level format indexer for Manic Miners, the community-built continuation of LEGO Rock Raiders' Gods98-derived level format.
- [vscode-manic-miners](https://github.com/Wal33D/vscode-manic-miners) - Visual Studio Code extension for Manic Miners `.dat` level files, with syntax highlighting for the `info`, `tiles`, `height`, `resources`, `objectives`, entity and `script` sections, `info` field completion and hover docs, and a live visual map preview with tile-replacement quick actions.
- [manic-map-tools](https://github.com/Wal33D/manic-map-tools) - TypeScript toolset for parsing Manic Miners `.dat` level files, to clean map files, render PNG images and thumbnails, check tile integrity, and compute map statistics such as size, elevation, and ore and crystal counts.
  - [manic-miner-map-renderer](https://github.com/Wal33D/manic-miner-map-renderer) - Related package that reads Manic Miners `.dat` map files and renders full-size PNGs and thumbnails of the tile layout.
- [lrr-tech-docs](https://github.com/darkf/lrr-tech-docs) - Technical documentation wiki (reStructuredText) covering LEGO Rock Raiders' engine internals and file formats (textures, models), for modding and preservation purposes. Archived/inactive.

#### LEGO Universe

- [lu-assets](https://github.com/LU-Rebuilt/lu-assets) - C++20 library with cross-platform parsers for LEGO Universe client asset formats, including DDS, FSB, Havok, and TGA.
- [lu-rebuilt](https://github.com/LU-Rebuilt/lu-rebuilt) - Cross-platform remake of the LEGO Universe client, reading the original game's assets.
- [cdclient-manager](https://github.com/LU-Rebuilt/cdclient-manager) - Manager for LEGO Universe's CDClient SQLite database, with a table editor, schema patching, loot/vendor editors, and an integrated skill editor.
- [zone-tools](https://github.com/LU-Rebuilt/zone-tools) - LUZ/LVL zone file editor and CLI converters for LEGO Universe.
- [model-tools](https://github.com/LU-Rebuilt/model-tools) - Viewers for LEGO Universe's NIF, HKX, and LXFML 3D model formats.
- [pk-tools](https://github.com/LU-Rebuilt/pk-tools) - Extractor and viewer for LEGO Universe's PK archive format.
- [audio-tools](https://github.com/LU-Rebuilt/audio-tools) - FMOD audio extraction and conversion tools for LEGO Universe.
- [fdb-tools](https://github.com/LU-Rebuilt/fdb-tools) - Converter and viewer for LEGO Universe's FDB database format.
- [navmesh-tools](https://github.com/LU-Rebuilt/navmesh-tools) - Navigation mesh editor for LEGO Universe zones.
- [terrain-viewer](https://github.com/LU-Rebuilt/terrain-viewer) - Viewer for LEGO Universe zone terrain heightmaps.
- [skill-editor](https://github.com/LU-Rebuilt/skill-editor) - Behavior tree editor for LEGO Universe skills.
- [psb-editor](https://github.com/LU-Rebuilt/psb-editor) - Editor for LEGO Universe's ForkParticle PSB particle-effect format.
- [blender-lu-physics](https://github.com/LU-Rebuilt/blender-lu-physics) - Blender add-on for authoring LEGO Universe Havok collision geometry.

#### Level-5

- [Metanoia](https://github.com/Ploaj/Metanoia) - Model viewer and research tool for Level-5 games.
- [MeltyTool (Level5)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/Level5) - Level-5 format viewer/exporter for games like Dark Cloud and Professor Layton.
- [blender-ymd-io](https://github.com/hinadevi/blender-ymd-io) - Blender addon for decompiling .ez files and converting .ymd files to Blender.
  - Formats: .ez, .ymd (Level-5 YMD model format).
- [CfgBinEditor](https://github.com/Tiniifan/CfgBinEditor) - Level 5 Bin Editor
- [Fougere](https://github.com/Tiniifan/Fougere) - Level-5 games tool.
- [level5_material](https://github.com/Tiniifan/level5_material) - Convert .mtr to .json and back
- [Level5Outline](https://github.com/Tiniifan/Level5Outline) - Converter for Level-5 outline files. Converts .sil (XCSL) format to JSON and back for easier editing.
- [Level5ResourceEditor](https://github.com/Tiniifan/Level5ResourceEditor) - Level-5 Resource Editor (RES.bin)
- [Nyanko](https://github.com/Tiniifan/Nyanko) - Level 5 Text Editor
- [Pingouin](https://github.com/Tiniifan/Pingouin) - Level 5 Archive File Manager
- [studio_eleven](https://github.com/Tiniifan/studio_collection) - Blender addon for Level-5 3DS file formats.
  - Formats: XPRM (3D mesh), XPCK (archives), XMTN (bone animation), XIMA (UV animation), XMTM (material animation), XCMA (camera).
  - Games: Inazuma Eleven GO series, Yo-Kai Watch series, Professor Layton vs. Phoenix Wright.
- [StudioElevenLib](https://github.com/Tiniifan/StudioElevenLib) - Additional C# library for files supported by the Studio Eleven Blender Addon
- [studio_collection](https://github.com/Tiniifan/studio_collection) - Collection of Blender addons for Level-5 3DS 3D files, bundling Studio Eleven with Studio Optimizer (reduces face counts and splits models using more than 24 bones before export) and Studio X (imports Unity models, textures, animations and cameras from Inazuma Eleven Cross for export via Studio Eleven).
- [XtractQuery](https://github.com/onepiecefreak3/XtractQuery) - Command-line tool to decompile and recompile script files (.xq, .xs) from Level-5 3DS games and (.cq, .lb, .gds) from Level-5 NDS games.

##### Mobile Suit Gundam AGE

- [Gundam-AGE-PSP](https://github.com/kjjkjjzyayufqza/Gundam-AGE-PSP) - Asset research tools and age_viewer (Windows) for the Level-5-developed Mobile Suit Gundam AGE PSP game. Extracts XPCK/IMGP/XMPR formats with mesh/texture preview and glTF/OBJ export.

##### Dark Cloud

- [dcdecomp (decomp)](https://github.com/TheMoonPeople/Chronicle) - Matching decompilation of Dark Cloud (PS2).
- [OpenCloud](https://github.com/Gundorada-Workshop/OpenCloud) - Open-source reimplementation of the Dark Cloud games, starting with Dark Cloud 2, reading the original game's data files.
- [DCExtractor](https://github.com/muddle12/DCExtractor) - Unpacker/converter for PS2-era Level-5 games, targeting Dark Cloud 1 & 2.
  - Formats: DAT/HD2/HD3 root archives; MDS/WGT/MOT/BBP models; IMG/TM2 textures; PAK/CHR/EFP/IPK/MPK/PCP/SKY/SND package archives.
  - Features: Converts models to Wavefront OBJ or Studiomdl SMD (with skeleton/weights) and images to PNG; extraction only, no repacking.
- [DarkCloud (LightCloud/WhiteCloud)](https://github.com/Xeeynamo/DarkCloud) - WhiteCloud unpacks and LightCloud repacks Dark Cloud 1 & 2 .DAT archives described by their .HD2/.HD3 index files.
- [paktools (Level-5 PS2)](https://github.com/HarmfulBreeze/paktools) - Cross-platform (Windows/Linux) command-line tool for managing Level-5 PS2 package files (.chr, .pac, .pak, .snd) used in Dark Cloud and other Level-5 PS2 titles.
- [DarkCloud-Toolkit](https://github.com/Gundorada-Workshop/DarkCloud-Toolkit) - Modding compendium for Dark Cloud, bundling known community tools (7-Zip, dcmds, Deswizzle, etc.) alongside file format documentation and manual editing techniques.
- [Blender-Tools-For-Dark-Cloud](https://github.com/Gundorada-Workshop/Blender-Tools-For-Dark-Cloud) - Blender plugin for importing and exporting Dark Cloud 1 .chr character files.
- [Dark-Cloud-2-Data-Editor](https://github.com/64BitMaster/Dark-Cloud-2-Data-Editor) - GUI editor for Dark Cloud 2 gameplay config files (comdat.cfg, comdatmes1.cfg, robodat.cfg, wepdat.cfg), covering weapons and ridepod parts.

##### Inazuma Eleven

- [Inazuma-Eleven-Toolbox](https://github.com/SwareJonge/Inazuma-Eleven-Toolbox) - Toolbox for Inazuma Eleven game files.
- [EnumaLimunada](https://github.com/Tiniifan/EnumaLimunada) - Converter for Inazuma Eleven GO models. Converts IEGO CS/Galaxy model formats to IEGO format.
- [GetNPCPos](https://github.com/Tiniifan/GetNPCPos) - Converting minimap coordinates to real NPC positions in Level-5 games
- [IEGOFormationEditor](https://github.com/Tiniifan/IEGOFormationEditor) - Formation editor for Inazuma Eleven GO series. Edit formations and strategies for Inazuma Eleven GO, Chrono Stone, and Galaxy.
- [InazumaElevenGoMapenv](https://github.com/Tiniifan/InazumaElevenGoMapenv) - Compiler and decompiler for mapenv files used in Inazuma Eleven GO games.
- [InazumaElevenGoScript](https://github.com/Tiniifan/InazumaElevenGoScript) - Documentation and research on Squirrel scripts used in Inazuma Eleven GO games. Covers script format, event system, and reverse engineering notes.
- [InazumaElevenMapEventEditor](https://github.com/Tiniifan/InazumaElevenMapEventEditor) - Map event editor for Inazuma Eleven GO games.
- [InazumaElevenSaveEditor](https://github.com/Tiniifan/InazumaElevenSaveEditor) - Save editor for Inazuma Eleven GO series. Supports Inazuma Eleven GO, Chrono Stone, and Galaxy.
- [InazumaDSEditor](https://github.com/NielsHotweels/InazumaDSEditor) - ROM editor for Inazuma Eleven 1 and 2 (NDS). Edit player data from unitbase.dat, unitbase.STR, and unitstat.dat directly in ROM.
- [inz_cond](https://github.com/Tiniifan/inz_cond) - Condition compiler and decompiler for Level-5 3DS games. Converts Base64-encoded condition data to human-readable C/Squirrel code and back. Supports Inazuma Eleven GO condition system.
- [Lynx](https://github.com/Tiniifan/Lynx) - Comprehensive game editor for Inazuma Eleven GO Light and Shadow. Includes charabase editor, charaparam editor, shop editor, skill editor, script editor, map viewer, and save editor.
- [mini_map_converter](https://github.com/Tiniifan/mini_map_converter) - Mini map converter for Inazuma Eleven GO series. Converts mini map formats between IEGO and CS/Galaxy versions.
- [MyTagsIE](https://github.com/Tiniifan/MyTagsIE) - Enhanced tag definitions for CfgBinEditor. Provides labeled field names for editing .cfg.bin files from Inazuma Eleven GO games.
- [Ocelot](https://github.com/Tiniifan/Ocelot) - Map event editor for Inazuma Eleven GO Light & Shadow. Edit map information, events, NPCs, and heal points with visual interface.
- [projectz](https://github.com/Tiniifan/projectz) - Modding template and toolkit for Inazuma Eleven GO Light/Shadow. Provides template for modifying code.bin, enhancement patches, and game documentation. Includes Squirrel scripting engine integration.
- [Strikers2013Editor](https://github.com/obluda3/Strikers2013Editor) - Modding tool and save editor for Inazuma Eleven GO Strikers 2013. Edit moves and player information.
- [UltimateGalaxyRandomizer](https://github.com/Tiniifan/UltimateGalaxyRandomizer) - Randomizer for Inazuma Eleven GO Galaxy. Randomizes player elements, positions, move power, and other game elements.
- [ie3ogres (decomp)](https://github.com/CacaBueno64/ie3ogres) - Matching decompilation of Inazuma Eleven 3 - Sekai e no Chousen: The Ogre!! (NDS).

##### Yo-Kai Watch

- [Albatross](https://github.com/Tiniifan/Albatross) - Game editor for Yo-Kai Watch series. Modifies game data files (yokai tribe, attacks, soultimates) for Yo-Kai Watch, Yo-Kai Watch 2 (BF/FS/PS), Yo-kai Watch 3, and Yo-Kai Watch Blasters.
- [YKWrandomizer](https://github.com/Tiniifan/YKWrandomizer) - Randomizer for Yo-Kai Watch, Yo-Kai Watch 2 (Psychic Specters) and partially Yo-kai Watch 3 (EU/US). Reads and rewrites Level-5 game data via bundled XPCK/ARC0 archive and CfgBin support to randomize yo-kai tribes, stats, attacks and evolutions.
- [yw-cond](https://github.com/n123git/yw-cond) - Web-based UI and toolkit for parsing, decompiling, analyzing and generating Yo-kai Watch Conds (CExpressions). Supports Yo-kai Watch franchise condition system with more complex features than Inazuma Eleven GO.
- [madhatter](https://github.com/bullbin/madhatter) - Low-level library for data formats used by early Nintendo DS Professor Layton games (Curious Village through Unwound Future), handling asset/archive unpacking, LZ77/RLE/Huffman compression, scripts, animations, backgrounds, and save files.
- [InazumaElevenSaveEditor](https://github.com/Tiniifan/InazumaElevenSaveEditor) - Save file editor for the Inazuma Eleven series.

##### Ni no Kuni

- [NinoImager](https://github.com/pleonex/ninoimager) - Batch image importer/exporter for Ni no Kuni: Shikkoku no Madoushi (NDS). Supports NPCK pack files (N2D/N3D) and NitroImage formats: NCLR/NCGR/NSCR backgrounds, NCLR/NCGR/NCER sprites, and BTX0/BMD0 textures.
- [NiNoKuni](https://github.com/turtle-insect/NiNoKuni) - Save data editor for Ni no Kuni (Switch).

##### Professor Layton

- [widebrim](https://github.com/bullbin/widebrim) - Playable high-level reimplementation of the engine for Professor Layton and the Diabolical Box / Pandora's Box (LAYTON2, NDS), loading the original game's data.
- [widebrim_editor](https://github.com/bullbin/widebrim_editor) - High-level editor for LAYTON2 game files, built for the widebrim engine.
- [widebrim_hd](https://github.com/bullbin/widebrim_hd) - Work-in-progress high-level reimplementation of the LAYTON2 HD remaster's engine.
- [tools_motdm](https://github.com/bullbin/tools_motdm) - Tools for understanding files from Professor Layton and the Mansion of the Deathly Mirror.
- [madhatter](https://github.com/bullbin/madhatter) - Low-level library for asset, archive, scripting, animation, background, database, savefile, room, and puzzle formats across the NDS Professor Layton trilogy (Curious Village, Diabolical Box, Unwound Future), with the most complete support for Diabolical Box; supersedes the archived tools_layton3.
- [LayTea](https://github.com/pleonex/LayTea) - Modding tools and .NET library for Professor Layton - London Life (NDS), covering DARC/DENC/ARCHIVE containers, DENC-LZSS and LZX compression, MSG text (with PO import/export), ACL/ACG/ACB palettes/pixels, and ASC/NCCL/NCCG/NCSC screen maps.

#### Deck Nine (Life is Strange: Before the Storm)

- [LSBExtractImport](https://github.com/kh0shn4w/LSBExtractImport) - Console tool for extracting `.lsb` subtitle files from Life is Strange: Before the Storm to `.txt` for editing, and importing them back.

#### Innoxia (Lilith's Throne)

- [LTSaveEd](https://github.com/Exiua/LTSaveEd) - Browser-based save editor (Blazor WebAssembly) for Lilith's Throne, editing player/NPC names, stats, attributes, and body configuration in save files.

#### Artem Skakunov (Little Bombers Returns)

- [ArtemSkakunovResourceExtractor](https://github.com/Retiu/ArtemSkakunovResourceExtractor) - Extraction tool for "Artem Skakunov's resource file", a custom archive format used by Little Bombers Returns (Alawar Entertainment, 2004), reverse-engineered from scratch (no prior documentation existed) from the game's `resource.dat`; covers both zlib-compressed text/data entries and image/sprite entries. Now integrated into [GameExtractor](https://github.com/wattostudios/GameExtractor).

#### Little Witch Nobeta

- [LittleDecryptedNobeta](https://github.com/entrophite/LittleDecryptedNobeta) - JavaScript save and achievement progress viewer/editor that decrypts and re-encrypts Little Witch Nobeta save data.

#### Sean Young (Littlewood)

- [LittleTownViewer](https://github.com/luisdcb97/LittleTownViewer) - Save editor for Littlewood.

#### Looking Glass Studios

##### System Shock

- [hacked](https://github.com/inkyblackness/hacked) - HackEd, the main graphical resource/level editor of the InkyBlackness project, editing System Shock 1's proprietary archive and level data.
- [shockmac](https://github.com/NightDive-Studio/shockmac) - Official GPL source code release of System Shock (PowerMac version) by Night Dive Studios, including the original engine and its file format implementations.
- [Shockolate](https://github.com/Interrupt/systemshock) - Minimalist, cross-platform System Shock source port built on Night Dive's official PowerPC source release, implementing the original engine's file format handling.
- [chunkie](https://github.com/inkyblackness/chunkie) - InkyBlackness project CLI tool providing import/export access to System Shock 1's proprietary resource files, complementing the project's HackEd GUI editor.
- [ss-specs](https://github.com/inkyblackness/ss-specs) - Unofficial System Shock 1 Specifications, documenting the game's proprietary resource/archive and level data formats; continuation of the earlier System Shock Hack Project (TSSHP) research.

##### System Shock 2

- [shock2quest](https://github.com/tommy-xr/shock2quest) - Engine recreation of the Dark Engine targeting Meta Quest VR, reading original System Shock 2 game data files. *See also [Dark Engine](engines.md#dark-engine) for general Dark Engine format tools.*

##### Thief

- [KCTools](https://github.com/JarrodDoyle/KCTools) - Tools for working with Thief fan missions under the NewDark 1.27 engine.
  - Features: Multithreaded lightmapper (KCLight) as a drop-in replacement for DromEd's single-threaded lighter — dramatically faster (up to 185× speedup) with better shadow accuracy; model exporter converting NewDark .BIN models to .GLB (GLTF binary) with sub-object hierarchy and bundled textures.

##### Ultima Underworld

- [UnderworldExporter](https://github.com/hankmorgan/UnderworldExporter) - Unity-based reimplementation and asset exporter for Ultima Underworld I & II; loads original game levels, geometry, textures, objects, and save files. Development has since migrated to [UnderworldGodot](https://github.com/hankmorgan/UnderworldGodot).
- [UWReverseEngineering](https://github.com/hankmorgan/UWReverseEngineering) - Reverse engineering research for Ultima Underworld I & II; includes IDA Pro 5 databases (UW.idb / UW2.idb) with annotated disassembly and a detailed game mechanics guide.
- See [UltimaHacks](https://github.com/JohnGlassmyer/UltimaHacks) under Origin Systems → Ultima VII below; its assembly patches and UltimaPatcher executable-patching tool also add mouse-look and other engine changes to Ultima Underworld I & II.
- [UnderworldAdventures](https://github.com/vividos/UnderworldAdventures) - Project to recreate Ultima Underworld 1: The Stygian Abyss for modern operating systems, reading and rendering original game files.
- [Ultima-Underworld-Save-Editor](https://github.com/ShaneHarro/Ultima-Underworld-Save-Editor-C-C-Sharp-) - Work-in-progress C# save game editor for Ultima Underworld.
- [UUUSaveEditor](https://github.com/gr4nada/UUUSaveEditor) - Python save editor for Kweepa's Unity port of Ultima Underworld that decompresses the `.json.gz` save slots, edits character stats and skills, and repacks them.

#### Looney Tunes: Carrot Crazy

- [carrotpatch](https://github.com/huderlem/carrotpatch) - Map editor (work in progress) for the Looney Tunes: Carrot Crazy disassembly project.

#### Mike Singleton (Lords of Midnight)

- [lords-of-midnight-disassembly](https://github.com/mrcook/lords-of-midnight-disassembly) - Unofficial disassembly of both the ZX Spectrum and PC DOS versions of The Lords of Midnight (1984), reconstructing readable source code from the original binaries.

#### Deck13 Interactive (Lords of the Fallen)

- [LOTF.PKG.Tool](https://github.com/Ekey/LOTF.PKG.Tool) - Tool for extracting PKG archives from Lords of the Fallen (2014).

#### Lords of Xulima

- [LoX_Editor](https://github.com/mgslack/LoX_Editor) - C# save game editor for Lords of Xulima; edits the XML save (repacking it and setting the password as needed) with a dialog for saved characters.

#### Lost Saga

- [mxs_lost_saga_online_pc](https://github.com/coreynguyen/mxs_lost_saga_online_pc) - MaxScript for importing `.msh` 3D models from Lost Saga Online.

#### Magnetic Fields (Lotus Esprit Turbo Challenge)

- [lotus-ste](https://github.com/jonathanopalise/lotus-ste) - Reverse-engineered enhancements to the Atari ST version of Lotus Esprit Turbo Challenge (1990), adding STE-specific Blitter-rendered graphics and digital sound support.

#### KLab (Love Live! School Idol Festival ALL STARS)

- [reversing-sifas](https://github.com/Francesco149/reversing-sifas) - Reverse-engineering diary for the mobile rhythm game Love Live! School Idol Festival ALL STARS; documents the game's encrypted `masterdata.db` SQLite database (custom `klb_vfs` VFS, key derivation) and the client-server login/asset-sync protocol (RSA-encrypted requests, `asset_state` asset-pack tracking), with Python snippets for decrypting and querying the master database directly.
- [klbvfs](https://github.com/Francesco149/klbvfs) (archived) - Python proof-of-concept that decrypts and queries the game's encrypted SQLite databases (`masterdata.db_*`) using the master key from a dump of the Android app data.

#### Love Once

- [LoveOnceExt](https://github.com/Manicsteiner/LoveOnceExt) - Extraction tool for the PS3 game Love Once: Mermaids' Tears (BLJM60322), unpacking `data.bin`/`list.bin` into CG/background and character DDS textures plus BGM/SE/voice BNK audio.

#### Crazy Diamond (LoveBeat)

- [LoveBeat_Tools](https://github.com/AzielCF/LoveBeat_Tools) - Suite of tools for extracting, analyzing, exporting, and visualizing assets from the LoveBeat rhythm game engine (and its LoveRitmo regional release), decrypting the game's containers to SLK, OBJ, OGG, DDS, XML, GLB, and JSON.

#### Lowiro

##### Arcaea

- [ArcCreate](https://github.com/Arcthesia/ArcCreate) - Community-made rhythm game editor and player for Arcaea, built with Unity; reads and writes the game's `.aff` chart file format.
- [Arcade-plus](https://github.com/yojohanshinwataikei/Arcade-plus) - Continuation of the original Arcade editor (taken down via DMCA takedown) for previewing and editing Arcaea's `.aff` chart files.
- [vscode-arcaea-file-format](https://github.com/yojohanshinwataikei/vscode-arcaea-file-format) - VS Code extension for reading and editing Arcaea `.aff` chart files, with syntax highlighting, snippets, parsing, and semantic diagnostics for known metadata and events.
- [Arcaea-server](https://github.com/Lost-MSth/Arcaea-server) - Local server reimplementing Arcaea's Flask-based client-server API for offline/private play.
- [Arcaea-Bundler](https://github.com/Lost-MSth/Arcaea-Bundler) - Bundles and debundles Arcaea's content bundle files.

#### Asmik Ace Entertainment (LSD: Dream Emulator)

- [lsddecomp (decomp)](https://github.com/FirecatFG/lsddecomp) - Matching decompilation of LSD: Dream Emulator (PS1).

#### Johan Kotlinski (LSDj)

- [lsdj-decompiled](https://github.com/gmoben/lsdj-decompiled) - pret-style, byte-exact disassembly of LSDj (Little Sound Dj) 9.4.0 for the Game Boy, with full symbol coverage (~8,800 named symbols) and annotated RAM/SRAM maps.
- [LSDPatcher](https://github.com/jkotlinski/lsdpatch) - Tool by LSDj's creator for modifying songs, samples, fonts, and palettes on LSDj Game Boy ROM images and save files.
- [pylsdj](https://github.com/alexras/pylsdj) - Python library for reading, writing, and editing LSDj's Game Boy save data (songs and instruments).
- [lsmc](https://github.com/alexras/lsmc) - Little Sound MC, a wxPython GUI multitool for LSDj .sav files built on pylsdj.
- [lsdj-rs](https://github.com/stijnfrishert/lsdj-rs) - Rust library and CLI for manipulating LSDj save files/SRAM, including the .lsdsng song format and LSDj's compression algorithm.
- [lsdpack](https://github.com/jkotlinski/lsdpack) - Standalone LSDj song recorder/player, converting LSDj songs for .gbs conversion or embedding in stand-alone Game Boy ROMs.
- [libLSDJ](https://github.com/stijnfrishert/libLSDJ) - Cross-platform C library for the LSDj Game Boy save format (.sav) and song format (.lsdsng), including LSDj's compression algorithm. Ships with the lsdsng-export, lsdsng-import, lsdj-mono, and lsdj-wavetable-import command-line tools; used by TommityTom's RetroPlug for save file management.

#### LucasArts

- [rogue_squadron64 (decomp)](https://github.com/Tmcg2/rogue_squadron64) - Matching decompilation of Star Wars: Rogue Squadron (N64).
- [SW_RACER_RE (decomp)](https://github.com/tim-tim707/SW_RACER_RE) - Matching decompilation of Star Wars Episode 1: Racer.
- [openswe1r](https://github.com/OpenSWE1R/openswe1r) - Open-source reimplementation of Star Wars Episode 1: Racer that patches the original game binary at runtime with open-source code (x86 CPU emulation and a Windows API compatibility layer), requiring the original game data.
- [scummtools](https://github.com/UnBeatWaterGH/scummtools) - Tools for SCUMM (Script Creation Utility For Maniac Mansion).
- [Monkey-Island-Explorer](https://github.com/bgbennyboy/Monkey-Island-Explorer) - Explorer/viewer/dumper for Monkey Island 1 and 2 Special Edition: browses and dumps game files, plays and dumps audio, views images (saves as PNG or DDS) and shows text and csv files.
- [Grim Fandango model viewer](https://www.moddb.com/games/grim-fandango/downloads/grim-fandango-model-viewer)
- [Easy Saber Editing Script 2.0 (Star Wars: Jedi Academy)](https://www.moddb.com/games/star-wars-jedi-academy/downloads/easy-saber-editing-script-2-0) - Script for skipping the saber menu and receiving a default saber in Star Wars: Jedi Academy (v2.0).
- [JK editing manuals (Star Wars Jedi Knight: Dark Forces II)](https://www.moddb.com/games/star-wars-jedi-knight-dark-forces-ii/downloads/jk-editing-manuals) - Offline archive of notable JED level editor tutorials for Star Wars Jedi Knight: Dark Forces II.
- [jkversions](https://github.com/The-MAZZTer/jkversions) - Uses the official Jedi Knight: Dark Forces II 1.0.1 patch to generate three versions of the JK.EXE binary suitable for using mods or bypassing Steam DRM.
- [Urgon](https://github.com/smlu/Urgon) - Mod tools and asset extraction utilities for Indiana Jones and the Infernal Machine.
  - Tools: gobext (GOB archive extractor), cndtool (CND/NDY level file manipulation, OBJ export), matool (MAT texture editor).
  - Formats: GOB, CND, NDY, MAT, KEY, 3DO.
- [Indy3DModInstaller](https://github.com/thekovic/Indy3DModInstaller) - Graphical mod installer for Indiana Jones and the Infernal Machine that unpacks the game files (optionally converting `.CND` levels to `.NDY`), installs and uninstalls mods, and can install OpenJones3D.
- [OpenJones3D](https://github.com/smlu/OpenJones3D) - Function-by-function C reconstruction of the Jones3D engine (a Sith engine derivative) behind Indiana Jones and the Infernal Machine, reverse-engineered from the original Indy3D.exe and loading the original game assets.
- [SED](https://github.com/smlu/SED) - Delphi port of the JED level editor for Sith engine games (Jedi Knight: Dark Forces II, Mysteries of the Sith, Indiana Jones and the Infernal Machine), with a rewritten 3D preview and many fixes.
- [OpenSith](https://github.com/r1sc/OpenSith) - Engine reimplementation of Jedi Knight Dark Forces II in Unity, parsing and rendering .JKL levels, .3DO models, and .GOB archive containers.
- [The Force Engine](https://github.com/TheForceEngine/TheForceEngine) - Modern reverse-engineered replacement for the Jedi Engine supporting Dark Forces and Outlaws with modern tools including a level editor.
- [gorc](https://github.com/jdmclark/gorc) - Early-development engine recreation of Jedi Knight: Dark Forces II that parses the original game's GOB archives, JKL levels, and 3DO models.
- [habitat](https://github.com/Museum-of-Art-and-Digital-Entertainment/habitat) - Preservation archive of the original 1986 *Habitat* (Commodore 64 MMORPG) source, restored by The Museum of Art and Digital Entertainment from Lucasfilm Games' technology-transfer tapes.
  - Contents: Commodore 64 6502 assembly source and art (`macross`), PL/I server source for Stratus VOS, server database tools (`ghu`/`muddle`), and design/beta documentation.
- [OpenJKDF2](https://github.com/shinyquagsire23/OpenJKDF2) - Reimplementation of the Jedi Knight: Dark Forces II engine (Sith engine) built from reverse-engineered original binaries, reading the original game's assets.
- [JkGfxMod](https://github.com/jdmclark/jkgfxmod) - Graphics enhancement and compatibility mod for Star Wars Jedi Knight: Dark Forces II, patching the original engine's rendering to run on modern systems.
- [Necrofy](https://github.com/Piranhaplant/Necrofy) - Level editor for Zombies Ate My Neighbors (SNES).
- [YOGEME](https://github.com/MikeG621/YOGEME) - All-in-one mission editor for the X-wing series (X-Wing, TIE Fighter, X-Wing vs. TIE Fighter, X-Wing Alliance), reading and writing the games' original mission file formats.
- [swe1r-re](https://github.com/OpenSWE1R/swe1r-re) - Reverse engineering research and documentation for Star Wars Episode 1: Racer, companion to the same organization's openswe1r reimplementation.
- [Star-Wars-Starfighter-C3PO-Converter](https://github.com/GlitcherOG/Star-Wars-Starfighter-C3PO-Converter) - Decompiles the C3PO file format used by Star Wars: Starfighter to JSON and back.
- [jediknight2blender](https://github.com/Ecki81/jediknight2blender) - Blender addon to import Jedi Knight: Dark Forces II / Mysteries of the Sith level files (.jkl).
- [blender-sith](https://github.com/smlu/blender-sith) - Blender addon for games built on LucasArts' Sith engine (Jedi Knight: Dark Forces II, Mysteries of the Sith, Outlaws).
- [jkview](https://github.com/stephanreiter/jkview) - 3D preview tool for Star Wars Jedi Knight: Dark Forces II and Mysteries of the Sith level and model formats.
- [gimp-ijim](https://github.com/smlu/gimp-ijim) - GIMP 3 plugin for importing/exporting Indiana Jones and the Infernal Machine texture files (.mat), complementing Urgon's matool above.
- [swe1r-assets](https://github.com/akopetsch/swe1r-assets) - C#/.NET library, published as a NuGet package, for reading and writing Star Wars Episode I: Racer's proprietary asset formats (models, textures, and data blocks). See also [swe1r-assets-unity](https://github.com/akopetsch/swe1r-assets-unity), a Unity package built on it for bit-perfect importing, modifying, and re-exporting the game's assets from inside the Unity Editor.
- [Obi-Wan Importer](https://github.com/janglesworthy/ObiWanImporter) - Autodesk Maya plug-in that imports levels, environments, props, characters, rigs, textures, and character animations from an extracted Xbox copy of Star Wars: Obi-Wan.
- [ROTS Maya Importer](https://github.com/janglesworthy/ROTSMayaImporter) - Autodesk Maya 2024.2/2027.2 plug-in that imports complete editor levels, characters, props, textures, materials, skeletons, skin weights, and animations from the Xbox version of Star Wars: Episode III - Revenge of the Sith.
- [Maniac.Mansion.Disassembly](https://github.com/segrax/Maniac.Mansion.Disassembly) - Commented disassembly of Maniac Mansion's SCUMM game scripts, with spreadsheets detailing room objects, variables, and their usage.
- [mm-explained](https://github.com/pditincho/mm-explained) - Fully-commented, reconstructed disassembly of the Commodore 64 version of Maniac Mansion, covering the main engine code and the game's special disk loaders. See also [law-of-the-west-explained](https://github.com/pditincho/law-of-the-west-explained), the same author's partial disassembly of Access Software's Law of the West (C64), documenting its branching dialogue system, scoring, and Rapidlok disk-loader protection.
- [Jones3D-The-Infernal-Engine Documentation](https://github.com/Jones3D-The-Infernal-Engine/Documentation) - Unofficial documentation of Indiana Jones and the Infernal Machine's file structures and modding, companion to Urgon's extraction tools above.
- [Blender-scripts (Jones3D-The-Infernal-Engine)](https://github.com/Jones3D-The-Infernal-Engine/Blender-scripts) - Blender scripts for Indiana Jones and the Infernal Machine, exporting objects to NDY/JKL level format and re-importing MAT texture files; requires the blender-sith addon above.
- [ImFlagger](https://github.com/Jones3D-The-Infernal-Engine/ImFlagger) - Editor for viewing and modifying the 32-bit flags used by Indiana Jones and the Infernal Machine's game scripts.
- [swep1r_decomp](https://github.com/DeonPoncini/swep1r_decomp) - Ghidra-derived decompilation reference for the Star Wars Episode 1: Racer Steam executable, feeding type information back into the SW_RACER_RE decompiler effort above.
- [Sw_Racer](https://github.com/Olganix/Sw_Racer) - C tools for understanding Star Wars Episode I: Racer's file formats, extracting models to Collada for use in 3D software.
- [swe1r-tools](https://github.com/OpenSWE1R/swe1r-tools) - Python scripts for Star Wars Episode I: Racer covering spline, sprite, and texture block extraction (to OBJ/PNG), SCR-to-WAV audio conversion, executable string extraction for translation, and save data parsing.
- [SWE1R-Mods](https://github.com/louriccia/SWE1R-Mods) - Collection of texture packs, track modifications, and unpack/repack scripts for Star Wars Episode I: Racer's asset blocks, building on OpenSWE1R's swe1r-tools.
- [blender-swe1r](https://github.com/louriccia/blender-swe1r) - Blender add-on for importing, modifying, and exporting Star Wars Episode I: Racer's proprietary asset (.bin) files.
- [Star-Wars-Racer-Revenge-Extraction-Tools](https://github.com/louriccia/Star-Wars-Racer-Revenge-Extraction-Tools) - Tools for extracting assets from Star Wars Racer Revenge (PS2), from the same author as the Episode I: Racer tools above.
- [DesktopAdventuresToolkit](https://github.com/IceReaper/DesktopAdventuresToolkit) - Unpacker/repacker for Desktop Adventure Games engine archives (Indiana Jones and Yoda Stories), also usable as a Java library. Unpacks zones to Tiled-compatible .tmx files, sounds to .wav/.mid, images to .png, and characters/weapons/puzzles to .xml; can repack either game's archive from an unpacked folder, including converting between the two games' formats.
- [DesktopAdventures](https://github.com/shinyquagsire23/DesktopAdventures) - Reimplementation of the Desktop Adventures engine (Indiana Jones and his Desktop Adventures, Star Wars: Yoda Stories), parsing the original .DAT game data (VERS, STUP, SNDS, TILE, ZONE, CHAR, and other sections) to run on Linux, 3DS, and Wii U; complements DesktopAdventuresToolkit above.
- [Yodecomp](https://github.com/shinyquagsire23/Yodecomp) - AI-assisted decompilation of Star Wars: Yoda Stories' engine binary (`Yodesk.exe`) into buildable C++ source, including its original asset-loading code.
- [dftools](https://github.com/njankowski/dftools) - Python tools for Star Wars: Dark Forces and Outlaws assets, covering GOB/LFD/LAB archives and BM/CMP/FME/FNT/PAL/WAX/GMD formats.
- [DarkForces](https://github.com/The-MAZZTer/DarkForces) - .NET file format library (MZZT.DarkForces) for reading and generating Dark Forces PC file formats, with Unity scripts and a showcase app of asset tools. Works with the DOS and Steam remaster versions, but not the remaster's enhanced formats.
##### Star Wars: Galactic Battlegrounds

- [Star-Wars-Galactic-Battlegrounds-Save-Game-Editor](https://github.com/Prekzursil/Star-Wars-Galactic-Battlegrounds-Save-Game-Editor) - Resource editor for Star Wars: Galactic Battlegrounds save games.

#### Lumines Remastered

- [lumines-remastered-decrypt](https://github.com/unknown321/lumines-remastered-decrypt) - Go tool that decrypts LUMINES REMASTERED (Steam, Unity) `.bytes` asset bundles, e.g. `skin001sound.bytes` exported with AssetRipper, so the contents can be extracted.

#### Working Designs (Lunar)

- [lunar2-psx-decomp (decomp)](https://github.com/Zackmon/lunar2-psx-decomp) - Matching decompilation of Lunar 2: Eternal Blue Complete (PS1).

#### Epoch Co. (Lupin Sansei - Pandora no Isan)

- [Lupin Sansei - Pandora no Isan (disassembly)](https://github.com/PavelSha/Lupin-Sansei---Pandora-no-Isan) - Annotated disassembly of the Famicom game Lupin Sansei: Pandora no Isan (1987).
