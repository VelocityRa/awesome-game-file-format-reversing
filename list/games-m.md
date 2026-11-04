### M
#### Charybdis (Machines: Wired for War)

- [machines](https://github.com/markol/machines) - GL port of Machines: Wired for War (1999), released as free software with permission from rights holder Night Dive Studios; loads and reads the original game's data files.

#### Macrospace

##### Fatal Force: Earth Assault

- [mff-extract](https://github.com/xNyaDev/mff-extract) - Command-line utility for extracting PAK archives from Fatal Force: Earth Assault.
  - Formats: .pak archives (J2ME game resources).
  - Features: List archive contents, extract specific or all files, verbose output support.

#### Madagascar

- [madagascar-game-asset-tools](https://github.com/MaxStache/madagascar-game-asset-tools) - Python toolset for modding Madagascar (2005), loading the game's RenderWare-based asset formats.
  - Formats: `.stream`, `.dff`, `.txd`, `.bsp`, `.txl`, `.rws`, `.lpa`.
- [madagascar-2-tools](https://github.com/MaxStache/madagascar-2-tools) - Reverse-engineered reader for Madagascar 2 (PC) `.bld` level files, an igArchive version 2 container distinct from the versions handled by igRewrite8; also includes a tool that recovers the engine's reflection metadata from the game's DLLs.

#### MAGES.

- [mpk_tool](https://github.com/LinkOFF7/mpk_tool) - CLI tool for extracting and modifying MAGES MPK archives.
- [impacto](https://github.com/CommitteeOfZero/impacto) - Open-source reimplementation of the "MAGES." visual novel engine used across 5pb./Chiyomaru Studio's Science Adventure series (Steins;Gate, Chaos;Child, Robotics;Notes, Occultic;Nine, and others), reading the engine's proprietary script and asset formats. Actively maintained.
- [TUNER](https://github.com/CommitteeOfZero/TUNER) - Conversion framework that transplants the Kaleido ADV Workshop (MAGES. engine) PS4 release of Occultic;Nine onto PC, unpacking, converting, and repacking its script, asset, audio, and video archives.
- [DoNut](https://github.com/CommitteeOfZero/DoNut) - Kaleidoscope ADV Workshop (MAGES. engine) tool for creating archives containing patch assets.
- [LanguageBarrier64](https://github.com/CommitteeOfZero/LanguageBarrier64) - Core runtime component for Committee of Zero's MAGES. engine game patches, hooking engine functions to redirect filesystem/asset access and enable rendering changes.
- [compendium](https://github.com/CommitteeOfZero/compendium) - Unofficial specification and reverse-engineering guide for the MAGES. visual novel engine, documenting the SC3 scripting VM used across the Science Adventure series.
- [sc3ntist](https://github.com/CommitteeOfZero/sc3ntist) - Interactive disassembler/debugger for MAGES. engine SC3 scripts (work-in-progress). Also includes SCXParser, for batch-disassembling all .scx script files in a directory.
- [MAGES-Tools](https://github.com/Aclios/MAGES-Tools) - Tools for modifying MPK and other file formats used by the MAGES. (ex 5pb.) engine.
- [MagesTools (wetor)](https://github.com/wetor/MagesTools) - Go rewrite of a general-purpose MAGES. engine toolset, importing/exporting MES (msb) and SC3 (scx) script files with configurable charset/TBL character tables.
- [ChaosChildPCTools](https://github.com/ningshanwutuobang/ChaosChildPCTools) - Python scripts for Chaos;Child PC version files: `.mpk` archive extraction, `.lay`/`.mvl` layer-to-PNG conversion, and `.gxt` texture-to-PNG conversion.
- [mvl_preview](https://github.com/Manicsteiner/mvl_preview) - GUI viewer for MAGES. engine `.mvl` character tachie/sprite files from console releases (2016 onward), also reading Kaleido ADV Workshop's decompiled `.psb.m` character JSON exports; a console-focused counterpart to ChaosChildPCTools' PC-version `.mvl` handling above.
- [RNE_image_converter](https://github.com/Manicsteiner/RNE_image_converter) - Image conversion tool for several MAGES./5pb. PS3 and PS Vita releases from 2012-2014, including Robotics;Notes, Chaos;Head Love Chu Chu, Memories Off 6/7, and multiple Steins;Gate PS3 editions; adapted and extended from wetor's original script.

#### Magicraft

- [Game-Save-Editor-Magicraft](https://github.com/KatahdinOutpost/Game-Save-Editor-Magicraft) - Browser-based save editor for Magicraft that decodes the XOR-encrypted `WorldData` save files to JSON for editing and re-encrypts them on save.

#### LKA (Martha Is Dead)

- [MarthaIsDead-TextTool](https://github.com/rm-NoobInCoding/MarthaIsDead-TextTool) - Extracts and imports text from `.uexp` files for Martha Is Dead.

#### CR-Space (Martial Heroes)

- [Diamond](https://github.com/tge-was-taken/Diamond) - Reverse engineering and enhancement project for Martial Heroes. Provides tooling, parsers, and client-side improvements including binary parsers, VFS archive tools, and 010 Editor templates.

#### Martian Gothic: Unification

- [mgu-speech-exporter](https://github.com/kapdap/mgu-speech-exporter) - Exports speech audio and text files from Martian Gothic: Unification (PC), based on file format notes from the Xentax forum.

#### Massive Development

##### Archimedean Dynasty

- [SF-Converter](https://github.com/LMCrashy/SF-Converter) - Batch converter for Archimedean Dynasty (Schleichfahrt) resources; converts R16/IMB/PCX/IMG images to PNG, PCM audio to WAV, MOD models to glTF 2.0, and MVI movies to MP4.
- [vertigo](https://github.com/pnordhus/vertigo) - Engine recreation of Archimedean Dynasty (Schleichfahrt) that loads and renders original game data files.

#### Massive Entertainment

##### AquaNox

- [aquanox-tools](https://github.com/Swyter/aquanox-tools) - Reverse engineering tools for the first AquaNox's file formats. Includes 010 Editor binary template (`.bt`) to decrypt and open `.pak` files and their filenames/sizes, and extractor script (`.1sc`). Documents internal formats: `.dds`, `.tga` textures, `.sco` Lua bytecode, `.des` configuration files, `.fog` volumetric fog tables, and `.msb` mesh files.
- [AquaNox 1-2 modding tools](https://www.moddb.com/games/aquanox/downloads/aquanox-1-2-modding-tools) - Modding tools for AquaNox 1-2 including: save editor, file unpacker (for PAK files containing models, scripts, materials, etc.), model converter (MSB to X format), and modding guides. Tools and guides by GodGell and ProjectAqua.

##### World in Conflict

- [massgate](https://github.com/ubisoft/massgate) - Official open-sourced online backend server for World in Conflict, enabling self-hosting of matchmaking, stats, and account services. Archived.
- [Broadcast Tool v6 (World in Conflict)](https://www.moddb.com/games/world-in-conflict/downloads/broadcast-tool-v6) - Allows DX10 users to broadcast a game T.V.-like. Good for LAN or other multi-player matches for spectators. Just a way for someone to watch a match without having to crowd around the two players' screens.
- [Broadcast Tool v7 (World in Conflict)](https://www.moddb.com/games/world-in-conflict/downloads/broadcast-tool-v7) - Allows DX10 users to broadcast a game T.V.-like. Good for LAN or other multi-player matches for spectators. Just a way for someone to watch a match without having to crowd around the two players' screens.
- [Broadcast Tool v8 (World in Conflict)](https://www.moddb.com/games/world-in-conflict/downloads/broadcast-tool-v8) - Allows DX10 users to broadcast a game T.V.-like. Good for LAN or other multi-player matches for spectators. Just a way for someone to watch a match without having to crowd around the two players' screens.

#### Master of Dimensions

- [master-of-dimension-rewrite](https://github.com/gmegidish/master-of-dimension-rewrite) - Reverse-engineered decoders for Master of Dimensions' palette, picture, video, script, and icon formats, aimed at a ScummVM port.

#### Mastertronic

- [feud](https://github.com/hitchhikr/feud) - Complete disassembly of the Amiga version of Feud, almost fully decoded and re-assemblable into a working game.

#### Maxis

##### 3D Pinball for Windows

- [SpaceCadetPinball](https://github.com/k4zmu2a/SpaceCadetPinball) - Decompilation of 3D Pinball for Windows – Space Cadet with support for original game data files from Windows and Full Tilt versions.
- [DatPartoutExplorer](https://github.com/belaw/DatPartoutExplorer) - Parses and displays the contents of the PARTOUT(4.0)RESOURCE file format used by Maxis/Cinematronics in Full Tilt Pinball.

##### SimCity

- [snescityeditor](https://github.com/usrshare/snescityeditor) - Map creator/editor for the NES and Super NES versions of SimCity, modifying the games' SRAM save files.
- [SimCity (SNES) Static Recomp](https://github.com/Junior-Jones/SimCity-SNES-Static-Recomp) - Static recompilation of the SNES port of SimCity into a native Windows executable; no ROM included.

##### SimCity 2000

- [SC2k-docs](https://github.com/OpenCity2k/SC2k-docs) - Unofficial documentation of the implementation of SimCity 2000, covering its .sc2/.scn city file format and other game data.
- [OpenSC2K](https://github.com/OpenSC2K/OpenSC2K) - Open-source WebGL/Phaser 3 remake of SimCity 2000 that parses the original game's data files (LARGE.DAT, PAL_MSTR.BMP from the Windows 95 Special Edition) directly for graphics and city loading.
- [sc2kfix](https://github.com/sc2kfix/sc2kfix) - Bugfix and modding plugin (DLL) for SimCity 2000 Special Edition (1996) that reverse-engineers and reimplements parts of the game's rendering, palette-cycling animation, and sound engine to fix crashes and bugs, restore cut content, and add new features, while remaining compatible with original .sc2/.scn city files.

##### SimCity 3000

- [sc3k_unradio](https://github.com/victormayor/sc3k_unradio) - Removes permanent radiation from SimCity 3000 city save files.

##### SimCity BuildIt

- [simcitybuildit](https://github.com/clanner/simcitybuildit) - Documentation of SimCity BuildIt (mobile, Marmalade engine) internals, including its asset/data formats.

##### The Sims 1

- [Simitone](https://github.com/riperiperi/Simitone) - Re-implementation of The Sims 1 based on FreeSO, parsing original Sims game data files (IFF/FAR proprietary formats).

##### The Sims Bustin' Out

- [Breakin-In](https://github.com/riperiperi/Breakin-In) - Lobby server emulator for The Sims Bustin' Out (PS2)'s Online Weekend mode.

##### The Sims 2

- [OpenTS2](https://github.com/LazyDuchess/OpenTS2) - Open-source re-implementation of The Sims 2 in Unity, reading the original game's proprietary data files.
- [sims2_mac_decomp (decomp)](https://github.com/ChrisNonyminus/sims2_mac_decomp) - Work-in-progress matching decompilation of the Mac port of The Sims 2.
- [DBPF.js](https://github.com/anonhostpi/DBPF.js) - TypeScript/JavaScript library for reading DBPF (Database Packed File) archives, the container format shared across Maxis titles including The Sims and SimCity. Supports DBPF v1.0-v2.x with v3 support in progress; currently on hold but documented for others to continue.
- [clod](https://github.com/zenzoa/clod) - Command-line multi-tool for The Sims 2 that extracts original outfit and hair templates (from Skins.package and globalcatbin.bundle.package) and original object packages as .package files for making default replacements.
- [sims-package2glb](https://github.com/infinition/sims-package2glb) - Windows desktop/CLI tool that reads The Sims 2, 3 and 4 `.package` mods and exports their meshes, UVs, normals and textures as glTF `.glb` (with recolour selection and a built-in 3D preview); can also dump the raw resources and textures as `.dds`/`.png`.
- [S2GBADecomp](https://github.com/tssoret/S2GBADecomp) - Work-in-progress disassembly and decompilation of The Sims 2 (Game Boy Advance).

##### The Sims 4

- [FastDec-TS4](https://github.com/KitsuneDev/FastDec-TS4) - Fast Python decompiler for The Sims 4's compiled .pyc script files, used to decompile the game's own scripts and TS4Script mods back to readable Python source.
- [Sims-4-Modding-Docs](https://github.com/zmilla93/Sims-4-Modding-Docs) - Archive of official Maxis/EA Sims 4 modding documentation (the original Custom Content Guide, forum discussions, and binary templates for .package resource formats), preserved from now-defunct forum pages via the Internet Archive.
- [Sims4Tools](https://github.com/s4ptacle/Sims4Tools) - The Sims 4 modding library and tool suite (S4PE package editor and related tools) for reading/writing DBPF .package resource files; actively maintained continuation of the now-deprecated [Kuree/Sims4Tools](https://github.com/Kuree/Sims4Tools).

##### The Sims Online

- [Project Dollhouse](https://github.com/Afr0Games/Project-Dollhouse) - Reconstruction of The Sims Online from the ground up in C#, requiring the original TSO client assets to run alongside its Docker-based server implementation.
- [FreeSO](https://github.com/riperiperi/FreeSO) - Open-source re-implementation of The Sims Online, reading the original game's client assets.
  - [TSO-Version-Patcher](https://github.com/riperiperi/TSO-Version-Patcher) - .NET Core filesystem patcher (based on bsdiff) for patching a The Sims Online client back to an earlier version (e.g. v1.1239.1.0 to N&I) needed to run against FreeSO.

##### MySims

- [MySims-Str-Tool](https://github.com/OAleex/MySims-Str-Tool) - Tool for extracting and inserting text from `.str` files in MySims (PC and Wii).

##### Spore

- [SporeModder-FX](https://github.com/Spore-Community/SporeModder-FX) - Modding tool for Spore, with a syntax-highlighting text editor for the game's text-based resource formats, a Spore UI editor, an image/texture viewer, and a model viewer for Spore's proprietary model format.
- [SporeModder-Blender-Addons](https://github.com/Spore-Community/SporeModder-Blender-Addons) - Blender add-ons for Spore: RW4 importer/exporter for game models (with textures, materials, and animations), an animation exporter for creature animations, and a GMDL importer for Spore creations.
- [SporeTools](https://github.com/Spore-Community/SporeTools) - Browser-based TypeScript tools for Spore: an asset tool that decodes the data embedded in Spore creation PNGs and queries Spore.com for an asset ID, and a hash tool for the FNV hashes used in package files.
- [PNG-Decoder-NetCore](https://github.com/Spore-Community/PNG-Decoder-NetCore) - .NET Core console app that reads a Spore creation PNG and outputs the embedded Pollen metadata and Spore model XML; adventure data must be processed separately with the Java decoder below.
  - [Adventure-Decoder](https://github.com/Spore-Community/Adventure-Decoder) - Java app that extracts data from Spore: Galactic Adventures adventures, taking the output of the PNG decoder as input; includes DBPF and property-file classes.
  - [PNG-Decoder-Python](https://github.com/Spore-Community/PNG-Decoder-Python) - Older Python 2 Spore PNG decoder by ymgve and rick that writes the creation's metadata header and model XML; does not handle adventures.
- [Spore_EP1Stegano-Python](https://github.com/Spore-Community/Spore_EP1Stegano-Python) - Python encoder/decoder for the steganography used by Spore: Galactic Adventures to store additional data in PNG files alongside thumbnails.
- [starmap](https://github.com/TheOnlyZac/starmap) - Interactive 3D viewer of the Spore galaxy built from the game's `stars.db` star-record data (`cStarRecord`, 42,010 generated stars), with a work-in-progress 010 Editor binary template for the `cStarRecord` resource.

#### Day 1 Studios / FASA Interactive (MechAssault)

- [MGF Explorer](https://github.com/LarvalExtract/MGF-Explorer) - C++/Qt GUI tool for opening and viewing assets contained in Meyer/Glass Interactive archive files used by MechAssault and MechAssault 2: Lone Wolf; supports BMP, DXT-compressed textures, FBX models, animation, and audio. Inspired by Adjutant, the Halo map viewer.
- [MATif](https://github.com/LarvalExtract/MATif) - CLI tool to convert common image formats into MechAssault's proprietary TIF texture format for both games (DXT5 for MechAssault 1, ARGB8888 for MechAssault 2); pairs with a companion MGF-Packer tool to repack textures into the game.
- [MGF-Editor](https://github.com/LarvalExtract/MGF-Editor) - Fork of Sony's Authoring Tools Framework LevelEditor adapted into an experimental level editor for MechAssault 1 and 2.

#### Media.Vision

- [MVGLTools](https://github.com/SydMontague/MVGLTools) - Modding tools for Media.Vision's MVGL game engine, supporting packing, unpacking, decrypting and encrypting file formats used in Digimon Story: Cyber Sleuth, Digimon Story: Time Stranger, and The Hundred Line -Last Defense Academy-.
- [Valkyria4MxeReader](https://github.com/akorov/Valkyria4MxeReader) - Python script for working with the MXE format found in Valkyria Chronicles 4.
- [Ginnungagap](https://github.com/Pherakki/Ginnungagap) - Program for editing MXE files in Valkyria Chronicles 4.
- [wa1tools](https://github.com/cebix/wa1tools) - Suite of command-line translation and hacking tools for the PlayStation 1 version of Wild Arms (1996), focused on dumping and editing in-game text and map script code.
- [Wild-Arms-2-Retranslation](https://github.com/TheSparda/Wild-Arms-2-Retranslation) - Translation toolkit and browser-based editor for a Wild Arms 2 (PS1) retranslation: extracts and aligns the US and JP script boxes from disc images, with notes on the JP kanji encoding, and exports in-place, PPF3 or xdelta patches.
- [Blender-Tools-for-DSCS](https://github.com/Pherakki/Blender-Tools-for-DSCS) - WIP Blender addon for importing and exporting Digimon Story: Cyber Sleuth (PC) model files, with experimental support for the PS4 version and Digimon Story: Cyber Sleuth Complete Edition's Megido 72 crossover assets.
- [DSCSRenderer](https://github.com/Pherakki/DSCSRenderer) - C++ library for loading and rendering Digimon Story: Cyber Sleuth models in an OpenGL context.
- [DSCSModelDataEditor](https://github.com/Pherakki/DSCSModelDataEditor) - Software to edit and visualize the data and shaders of Digimon Story: Cyber Sleuth models.
- [SimpleDSCSModManager](https://github.com/Pherakki/SimpleDSCSModManager) - Mod manager for the PC release of Digimon Story: Cyber Sleuth Complete Edition, bundling GUI tools built on MVGLTools above for extracting/repacking game archives and on NutCracker for decompiling the game's Squirrel scripts.
- [CSGeom](https://github.com/xdanieldzd/CSGeom) - Experimental model viewer and exporter for `.geom` model files from Digimon Story: Cyber Sleuth, using separately converted `.pvr` texture files.
- [pyValkLib](https://github.com/Pherakki/pyValkLib) - Python library for reading and writing files in the Valkyria Chronicles game series.
- [MXEEditor](https://github.com/Pherakki/MXEEditor) - Program for unpacking and re-packing Valkyria Chronicles MXE files to and from CSV, built on pyValkLib above; complements Ginnungagap above, which targets Valkyria Chronicles 4 specifically.

#### Megapede

- [cgrr-megapede](https://github.com/sopoforic/cgrr-megapede) - Python module (part of Classic Game Resource Reader) that reads Megapede `MEGAPEDE.SCO` score files and, experimentally, the `MEGAPEDE.RES` resource file.

#### MercurySteam

##### Metroid Dread

- [MercuryEngine.Data](https://github.com/ArcanoxDragon/MercuryEngine.Data) - .NET library for parsing and working with data formats used in MercurySteam's game engine (Metroid Dread, Metroid: Samus Returns).
- [MD.PKG.Tool](https://github.com/Ekey/MD.PKG.Tool) - Tool for extracting PKG archives from Metroid Dread.
- [mercury-engine-data-structures](https://github.com/randovania/mercury-engine-data-structures) - Construct-based type definitions for MercurySteam's Mercury Engine file formats.
- [open-dread-rando](https://github.com/randovania/open-dread-rando) - Randomizer patcher for Metroid Dread, directly modifying the game's original assets for Randovania.
- [open-samus-returns-rando](https://github.com/randovania/open-samus-returns-rando) - Randomizer patcher for Metroid: Samus Returns, directly modifying the game's original assets for Randovania.
- [dread-editor](https://github.com/randovania/dread-editor) - Visualizer for Metroid Dread's BRFLD level/actor-layout files.

##### Scrapland

- [ScrapHacks](https://github.com/ReScrap/ScrapHacks) - Reverse-engineering notes and tools for Scrapland: `scrapper.py` extracts and repacks `*.packed` archives, a work-in-progress parser for the game's chunked model/animation/map format, a save-to-JSON converter, and Frida and radare2 scripts plus Python documentation for the in-game scripting system.

#### Archetype Interactive (Meridian 59)

- [GZDoomBuilder (Meridian 59 port)](https://github.com/OpenMeridian105/GZDoomBuilder_M59) - Port of the GZDoomBuilder map editor for editing Meridian 59 MMORPG rooms in the game's native .roo (v15) format, in 2D and 3D.

#### Metal Arms

- [DJs_MA_TOOLs](https://github.com/dj0wns/DJs_MA_TOOLs) - Extraction/conversion tools for Metal Arms: Glitch in the System's .MST format.
- [io_scene_metal_arms](https://github.com/hypermegacrash/io_scene_metal_arms) - Blender addon for importing/exporting Metal Arms models, compiling with PASM.

#### Metropolis Software

##### Gorky 17

- [Gorky 17 *.dat and *.kdt extractor tool](https://www.moddb.com/games/gorky-17/downloads/gorky-17-dat-and-kdt-extractor-tool) - Extractor tool for *.dat and*/.kdtr files. You can now extract the contents of these data containers. I'm started to working on the gui version of the program that will supports more filetypes and will include a scripter, updated extractor - builder, you will be able to pl...

#### Microids

##### Still Life 2

- [pff_life](https://github.com/mbikovitsky/pff_life) - Python scripts for Still Life 2 file formats: extracts frames and audio from PFF video files (optionally converting to MP4 via FFmpeg), and packs directories into the game's DAT asset archives.

##### Syberia

- [SyberiaDatamine](https://github.com/Hiro420/SyberiaDatamine) - Viewer/extractor for Syberia and Syberia II game files, inspired by AssetStudio; supports videos, audio, meshes, textures, 3D objects, and behaviors.

#### MicroProse

##### Civilization

- [Civilization (SNES) Static Recomp](https://github.com/Junior-Jones/Civilization-SNES-Static-Recomp) - Static recompilation of the SNES port of Sid Meier's Civilization into a native Windows executable; no ROM included.

##### X-COM (UFO Defense / Terror from the Deep)

- [OpenXcom](https://github.com/OpenXcom/OpenXcom) - Open-source engine recreation of the original X-COM (UFO: Enemy Unknown / Terror from the Deep), reading the original game's proprietary data files (GEODATA, UFOGRAPH, map blocks, and more).
- [openxcom-save-editor](https://github.com/aaronjacobs-chelt/openxcom-save-editor) - Python save game editor for OpenXCom Extended aimed at the X-Com Files mod; edits funds, research progress, soldier stats, base facilities, production queues and inventory.
- [xcom2edi](https://github.com/bovine/xcom2edi) - MS-DOS saved-game editor (C++) for X-COM: Terror from the Deep; edits soldiers (names, armour), tactical battle state and other saved game data, and can carry soldiers over from the first X-COM.

##### XCOM Apocalypse

- [OpenApoc](https://github.com/OpenApoc/OpenApoc) - Open-source re-implementation of XCOM: Apocalypse engine written in C++/SDL2; requires and parses original game files for assets and data structures.

##### F-15 Strike Eagle II

- [f15se2-re (decomp)](https://github.com/neuviemeporte/f15se2-re) - Reconstructed source code for MicroProse's F-15 Strike Eagle 2 (MS-DOS), based on disassembly of the original executable.
- [f15se2-ex](https://github.com/neuviemeporte/f15se2-ex) - Port of the reconstructed F-15 Strike Eagle 2 to modern architectures, with bugfixes and enhancements, built on f15se2-re.

##### Sid Meier's Covert Action

- [CovertActionTools](https://github.com/RedMike/CovertActionTools) - Tools for inspecting and modifying game files for Sid Meier's Covert Action.
- [PanAnimationPlayer](https://github.com/RedMike/PanAnimationPlayer) - Browser-based viewer for the .PAN animation files used by Sid Meier's Covert Action (1990).

##### Darklands

- [Darklands](https://github.com/vvendigo/Darklands) - File reading utilities and preserved file format documentation for Darklands (MicroProse, 1992).
- [darklandscompanion](https://github.com/illusium77/darklandscompanion) - Save game editor for Darklands (MicroProse, 1992), reading and modifying the original save file structures.

##### MPS Show

- [mps-show](https://github.com/canadianavenger/mps-show) - Reverse-engineering and extraction tools for the MicroProse MPS Show slideshow data format used with some of their DOS game demos.
##### Master of Magic

- [openmom](https://github.com/Jakz/openmom) - Cross-platform open-source port of Master of Magic (1994, MicroProse/SimTex), reading the original game's LBX archive files for graphics, sound, and data.

##### Master of Orion II

- [reorion2](https://github.com/turican0/reorion2) - Work-in-progress native Windows port of Master of Orion II (MicroProse/SimTex, 1996), turning a decompilation of the original DOS binary into readable C++/SDL3 behind a small BIOS/DOS/VGA port layer. Requires the original game's LBX archives and is checked frame by frame against the original running under DOSBox-X.

##### RollerCoaster Tycoon

- [OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) - Open-source re-implementation of RollerCoaster Tycoon 2, loading the original game's data files (including add-ins RCT1 and Time Twister) and extending the engine with new features.
- [RCT_tools](https://github.com/KolijnWolfaardt/RCT_tools) - Scripts for working with RollerCoaster Tycoon 2's files, including sprite exporting; requires the original game.
- [libsawyer](https://github.com/OpenRCT2/libsawyer) - C++ library and CLI utilities (`fsaw`, `gxc`) shared by OpenRCT2 and OpenLoco: inspects, compresses, and decompresses Sawyer-encoded RollerCoaster Tycoon 2/Locomotion save files, and builds/extracts the two engines' graphics data files.
- [G1Extract](https://github.com/Gericom/G1Extract) - Extractor for the `g1.dat` graphics data file from RollerCoaster Tycoon 2.
- [OpenRCT2 Title Sequence Editor](https://github.com/OpenRCT2/title-sequence-editor) - Plugin for creating, editing, and previewing custom `.parkseq` title sequence files played on OpenRCT2's title screen; split out from the base game into an optional plugin.

##### Star Trek: The Next Generation - Klingon Honor Guard

- [KlingonHonorGuard_UCSource](https://github.com/SirHenricus/KlingonHonorGuard_UCSource) - Decompiled UnrealScript source code for Star Trek: The Next Generation - Klingon Honor Guard (1998), an Unreal Engine 1 game.

#### Microsoft Studios / Bungie / Turn 10

- [XbxDeTool](https://github.com/Nenkai/XbxDeTool) - Xbox file format tool.
- [Halo Asset Blender Development Toolset](https://github.com/General-101/Halo-Asset-Blender-Development-Toolset) - Blender addon for creating and exporting assets for multiple Halo titles (Halo CE, 2, 3, ODST, Reach, 4, 5, Infinite).
- [Foundry](https://github.com/ILoveAGoodCrisp/Foundry) - Blender extension for Halo Reach, 4, and 2A Multiplayer asset pipeline.
- [Halo-CR4B-Tool](https://github.com/PlasteredCrab/Halo-CR4B-Tool) - One-click game-accuracy tool for Halo 3/ODST/Reach assets in Blender that also exports assets from every Halo game.


##### SkiFree

- [skifree_decomp](https://github.com/yuv422/skifree_decomp) - Decompilation project for SkiFree.

##### Hover!

- [Merlin](https://github.com/philip-searle/Merlin) - Reverse engineering research and tools for Hover!, the Windows 95-era pack-in game from Microsoft.

##### Halo

###### Engine, Tag Formats & Documentation

- [halo (decomp)](https://github.com/punpckhdq/halo) - Work-in-progress matching decompilation of Halo: Combat Evolved (build 2342, `cachebeta.exe`).
- [KSoft](https://github.com/KornnerStudios/KSoft) - Toolkit for working with Halo engine file formats.
- [ekur](https://github.com/TheHaloArchive/ekur) - Blam! engine (Halo) format library and research tools.
- [HaloWarsDocs](https://github.com/HaloMods/HaloWarsDocs) - Documentation and 010 Editor templates for modding Halo Wars 1 and 2.
- [Osoyoos Launcher](https://github.com/num0005/Osoyoos-Launcher) - Halo Editing Kit (HEK) launcher and toolset manager supporting various HEK versions and community modifications for editing level files, tags, textures, models, and scenarios.
- [Assembly](https://github.com/XboxChaos/Assembly) - Multi-generation Blam engine research and modding tool for browsing/editing map and cache file formats.
- [c20 (The Reclaimers Library)](https://github.com/Sigmmma/c20) - Living knowledge base/wiki for the Halo CE modding community, documenting Halo engine tag and file formats.
- [vkblam](https://github.com/Wunkolo/vkblam) - Re-implementation of the Halo 1 Blam engine's graphics library in Vulkan.
- [blf](https://github.com/Blam-Network/blf) - Rust workspace of crates for reading and writing Blam! engine (Halo) files.
- [blam-tags](https://github.com/camden-smallwood/blam-tags) - Cross-platform Rust library for parsing and manipulating Halo tag files.
  - Related: [definitions](https://github.com/camden-smallwood/definitions), JSON tag definitions for Halo MCC titles.
- [Blam-Creation-Suite](https://github.com/ChimpsAtSea/Blam-Creation-Suite) - Collection of modular C++ frameworks (Mandrill tag/resource editor, Blofeld tag layout framework) for creating custom Blam engine content across Halo Combat Evolved through Halo Infinite.
- [Reach (decomp)](https://github.com/ChimpsAtSea/Reach) - Work-in-progress matching decompilation of Halo: Reach (Xbox 360 build `tag_debug_untracked_jul_11_2011`), companion project to the halo (decomp) Combat Evolved effort above.
- [HaloKSY](https://github.com/Sigmmma/HaloKSY) - Kaitai Struct definitions for Halo tag file formats.
- [halo-guerilla-sounds](https://github.com/xyx0826/halo-guerilla-sounds) - Analysis notes and prototype tools for decoding sound and music tags from the Guerilla authoring tool (Halo: Combat Evolved and Halo 2 mod tools), which differ in structure from shipping-game tags.
  - ImHex patterns for HCE and Halo 2 sound tags, plus a Zig decoder for HCE sound tags and a Python tool with a native ADPCM decoder for Halo 2 sound tags.

###### Asset Extraction & Viewing Tools

- [Reclaimer](https://github.com/Gravemind2401/Reclaimer) - Halo asset extraction and analysis tool supporting Halo 1, 2, 3, 4, Reach, and Online.
  - See also [ReclaimerFiles](https://github.com/Surasia/ReclaimerFiles), per-tag XML definition files for Halo 5 and Halo Infinite meant for use with Reclaimer.
- [IndexV2](https://github.com/Wildenhaus/IndexV2) - Tool for Halo: Combat Evolved Anniversary and Halo 2 Anniversary that extracts textures, models, and more.
- [h5_dumper](https://github.com/Surasia/h5_dumper) - Simple tag dumper for Halo 5 and Halo 5 Forge written in Rust. Recursively goes through each .module file in directory and writes tags to specified path.
- [FiveTool](https://github.com/ElDewrito/FiveTool) - Unofficial Halo 5 modding toolkit; its ModuleExtractor unpacks the `.module` files used by the Windows Store version of the game (the README notes there is no way to rebuild modules after editing).
- [libpyinfinite](https://github.com/Surasia/libpyinfinite) - Typed Python library for parsing Halo Infinite binary files, with module and tag readers (Oodle decompression through the game's oo2core DLL) usable separately or together.
- [infinite-rs](https://github.com/TheHaloArchive/infinite-rs) - Rust deserialization library for Halo Infinite, loading the game's .module archives and reading tags from them, with a derive macro for defining tag structures.
- [libInfinite](https://github.com/Coreforge/libInfinite) - C++ library for working with Halo Infinite files, based on MontagueM's HIMU, with module and tag readers, bitmap batch extraction and material JSON export; tag headers can be generated from IRTV/HIRT XML definitions.
  - [infiniteExplorer](https://github.com/Coreforge/infiniteExplorer) - GUI frontend for libInfinite with bitmap, BSP and 3D model viewers, texture export, and optional mounting of module contents through FUSE3 or WinFsp.
  - [blender-halo-infinite](https://github.com/Coreforge/blender-halo-infinite) - Blender add-on based on HIME that imports Halo Infinite `.render_model` files with their chunk files and textures.
- [infinitebnk](https://github.com/xyx0826/infinitebnk) - Extracts Wwise SoundBanks from Halo Infinite modules, built on [libInfinite](https://github.com/Coreforge/libInfinite) and optionally mapping tag IDs to paths using a tagnames.txt list.
- [inf_vectorart](https://github.com/TheHaloArchive/inf_vectorart) - Rust command-line tool that extracts vector art tags from a Halo Infinite deploy folder and writes them as SVG, built on infinite-rs above.
- [Olympus](https://github.com/Surasia/Olympus) - Blender add-on for importing Halo Infinite render models, material styles (coatings) and bitmaps from the game's modules; a fork of Coreforge's Blender Halo Infinite importer.
- [XTraction - Halo 3/ODST texture extractor](https://www.moddb.com/games/halo-3/downloads/xtraction-halo-3-odst-texture-extractor-tool) - Versatile texture extractor for Halo 3 and ODST. Extracts textures from MAP files as TIFF images, enabling editing and replacement of Halo 3 era textures. Originally created for WMClan members.
- [Stream Ripping Tools - Halo 3/4/ODST/CEA/HR Game Asset Extractors Converters Kit](https://www.moddb.com/games/halo-2/downloads/stream-ripping-tools-game-asset-extractors-converters-kit) - Large collection of tools for extracting, modding, and converting game assets from up to 2100 games. Includes Halo 3/2/4/ODST/Reach tools. Contains help instructions, documentation, and links to sources.
- [Halo2 Gravemind Tool Extractor v1.6B](https://www.moddb.com/games/halo-2/downloads/halo2-gravemind-tool-extractor) - Extractor tool for Halo 2 assets including models, sounds, textures, and maps (v1.6B).
- [Bonobo [Version 1.0.0.3] Halo2/3/ODST/Reach Animation Extractor](https://www.moddb.com/games/halo-2/downloads/bonobo-version-1003) - Animation extractor for Halo 2, 3, ODST, and Reach (v1.0.0.3).
- [Composer Halo 4 Audio Extractor](https://www.moddb.com/games/halo-4/downloads/composer-halo-4-audio-extractor) - Tool used with QuickBMS to extract and convert Halo 4's .XMA audio files to WAV format. Includes all necessary tools and documentation.
- [noclip.website (Halo: Combat Evolved)](https://github.com/magcius/noclip.website/tree/main/src/Halo1) - In-browser Halo: Combat Evolved viewer.
- [Halo CE Batch Bitmap Extractor](https://www.moddb.com/downloads/halo-ce-batch-bitmap-extractor)
- [H2PC_TagExtraction](https://github.com/Project-Cartographer/H2PC_TagExtraction) - Tool for extracting assets and tags from Halo 2 PC cache files using BlamLib.
- [halo2-color-plate-extractor](https://github.com/SnowyMouse/halo2-color-plate-extractor) - Extracts Halo 2 tag color plate data (used for team-color bitmap masking).
- [PckTool](https://github.com/coconutbird/PckTool) - .NET library and CLI tool for manipulating Wwise PCK/BNK audio packages, used by Halo Wars: Definitive Edition.
- [phxtool](https://github.com/coconutbird/phxtool) - Rust CLI toolkit for Halo Wars: Definitive Edition modding, covering ERA, XMB, UGX, Wwise, ECF, BDT, and Scaleform formats; a modern successor to KornnerStudios' PhxTool.
- [HaloWwise](https://github.com/Nibre/HaloWwise) - Unpacks Wwise `.pck` audio packages from Halo 4/Halo 5 into their `.wem`/`.bnk` contents, preserving pack folder structure and Bank info for tracing sounds back to their Blam tag.
  - Built on [pcktool-rs](https://github.com/coconutbird/pcktool-rs) (zero-copy Rust library/CLI for parsing and writing Wwise PCK/BNK audio packages).
  - Related: [ensemble-assets](https://github.com/coconutbird/ensemble-assets) (Ensemble game asset resolution and typed database schemas), [hwm](https://github.com/coconutbird/hwm) (command-line manager for Halo Wars installations and mods), [sevenzip-era](https://github.com/coconutbird/sevenzip-era) (7-Zip plugin for reading/writing Ensemble ERA archive files).
- [Composer (XboxChaos)](https://github.com/XboxChaos/composer) - Extracts audio from Halo 4's `soundbank.pck` and `soundstream.pck`, with bundled helper utilities to convert the extracted files to common formats.
- [aera](https://github.com/paleauraaaa/aera) - Standalone renderer for Halo 1 maps, reading original Xbox build (`cachebeta.exe`) map files with in-progress support for Gearbox PC and MCC map formats.
- [Composer (Sigmmma)](https://github.com/Sigmmma/composer) - Standalone music player that reads and plays Halo 1's `sound`/`sound_looping` tag files directly, reproducing the game's dynamic music system outside the game.

###### Map Editing, Modding & DCC Tools

- [3ds Max GBX Importer (Halo CE)](https://www.moddb.com/downloads/3ds-max-gbx-importer-halo-ce) - 3DS Max plugin for importing Halo: Combat Evolved GBX model formats.
- [Halo 2 Xbox Modding Tools](https://www.moddb.com/games/halo-2/downloads/halo-2-xbox-modding-tools) - Collection of 5 tools for modding Xbox Halo 2 maps.
- [Halo-Spartan-Translation-Toolkit](https://github.com/dortkoldantaciz/Halo-Spartan-Translation-Toolkit) - Translation toolkit for Halo: Spartan Assault and Spartan Strike, extracting text from game archives and converting .GFxPackage font files.
- [invader](https://github.com/SnowyMouse/invader) - Toolkit for creating maps and assets for Halo: Combat Evolved.
  - Formats: Bitmap tags, sound tags, model files (.JMS), cache files (.map)
  - Features: Map and scenario creation, asset editing
  - Related tools by the same author: [riat](https://github.com/SnowyMouse/riat) (Rust compiler for Halo: CE scripts), [ceaflate](https://github.com/SnowyMouse/ceaflate) (compresses and decompresses MCC: CEA PC map files), [proximity-mine](https://github.com/SnowyMouse/proximity-mine) (C tool that "implodes" Halo PC maps, rewriting scenario, bitmap, and sound data offsets), [gorilla](https://github.com/SnowyMouse/gorilla) (dumps tag definitions from the HEK's guerilla.exe to JSON), [last-resort](https://github.com/SnowyMouse/last-resort) (converts Gearbox tags for the Xbox version of Halo, including HUD meter channel order and Xbox ADPCM sound), [mcc-cshd-map-patcher](https://github.com/SnowyMouse/mcc-cshd-map-patcher) (patches or unpatches MCC CEA maps for client-side hit detection), and [xbadpcm](https://github.com/SnowyMouse/xbadpcm) (Rust Xbox ADPCM encoder/decoder).
- [Baboon](https://github.com/Zoephie/Baboon) - Native Rust GUI, built on blam-tags, for editing Halo MCC editing-kit tag files (Halo 3, ODST, Reach, Halo 4, H2A). Provides byte-exact tag reading/editing, asset extraction (bitmaps, geometry, animation), and a Guerilla-style editing surface.
- [Reclaimer.Architect](https://github.com/Gravemind2401/Reclaimer.Architect) - Visual editor for Halo scenario/map files, directly parsing and editing game format structures.
- [OpenH2](https://github.com/ronbrogan/OpenH2) - Open-source engine and tools for Halo 2 with reverse-engineered map file format and tag deserialization. See also [OpenBlam](https://github.com/ronbrogan/OpenBlam), the same author's base libraries factored out for building Halo engine tech, and [h2-speedmod](https://github.com/ronbrogan/h2-speedmod), a companion set of Halo 2 map script patches (applied directly to map files via OpenH2's MccBulkPatcher tool) that skip repetitive/non-interactive sections for speedrunning.
- [H2Codez](https://github.com/Project-Cartographer/H2Codez) - Mod for Halo 2 Editing Kit restoring and adding functionality, enabling asset format handling and tag editing.
- [HaloOnlineTagTool](https://github.com/ElDewrito/HaloOnlineTagTool) - Low-level Halo Online `tags.dat` editor and research project.
- [AusarDocs](https://github.com/ElDewrito/AusarDocs) - Documentation of the Ausar/Halo Online engine's tag and cache file formats, compiled from ElDewrito's reverse-engineering work.
- [Halo Online Variant Editor](https://github.com/ThiconZ/Halo-Online-Variant-Editor) - Editor for Halo Online game variant and map variant files, exposing the full variant file structure including settings not present in the in-game interface. Includes an 010 Editor binary template documenting the variant format.
- [Liberty](https://github.com/XboxChaos/Liberty) - Free campaign save editor for Halo 4, Halo: Reach, Halo: Combat Evolved Anniversary, Halo 3 and Halo 3: ODST.
  - [halosigner](https://github.com/XboxChaos/halosigner) - Rehashes Halo content files after hex editing: campaign saves from Halo Anniversary, Halo 3, Halo 3: ODST, Halo: Reach and Halo 4, plus Halo: Reach GPDs.
- [nitrogen](https://github.com/XboxChaos/nitrogen) - .NET interface to Halo 4 map and game variants (variant BLF files), including a WumboScript Viewer that outputs Megalo scripts in a human-readable format.
- [HaloMD](https://github.com/foonull/HaloMD) - Community continuation project for Halo: Combat Evolved on Mac, built on packet-sniffing research into the original network protocol.
  - Features: master server replacement reimplementing the original protocol, versioned mod distribution via delta binary patches, run-time game extensions.
- [ManagedDonkey](https://github.com/twist84/ManagedDonkey) - Ongoing project to reimplement/mod Halo Online (`ms23 1.106708` build), reading the original client simulation and broadcast (systemlink) logic while documenting the process.
- [Rampancy](https://github.com/GoomiiV2/Rampancy) - Halo level creation toolset bridging modern level editors like TrenchBroom into the Halo Editing Kit (HEK) workflow.
  - See also [Rampancy.LightBridge](https://github.com/GoomiiV2/Rampancy.LightBridge), the bridge component connecting TrenchBroom's level geometry output to Halo's map compiling pipeline.
- [Prometheus-Alpha](https://github.com/grimdoomer/Prometheus-Alpha) - Modding tool for the original Xbox version of Halo 2, allowing map modification/creation, spawn placement, and object property editing.
- [InfiniteTool](https://github.com/ronbrogan/InfiniteTool) - Speedrunning companion tool for Halo Infinite Campaign (PC), reading and writing the game's own progression save data for gamesave import/export, alongside keybind remapping.
- [Mozzarilla](https://github.com/Sigmmma/mozzarilla) - Visual tag editor/IDE for Halo CE content, intended as a full-featured replacement for the HEK's Guerilla.
  - Built on [Reclaimer (Sigmmma)](https://github.com/Sigmmma/reclaimer) (Python library for creating/modifying Halo tag content), [Binilla](https://github.com/Sigmmma/binilla) (its generic visual editor for structures defined with the [Supyr Struct](https://github.com/Sigmmma/supyr_struct) binary serialization library), and [Arbytmap](https://github.com/Sigmmma/arbytmap) (bitmap conversion library handling raw and DXT1-5/DXN texture formats, swizzling, and mipmap generation).
  - Related: [Refinery](https://github.com/Sigmmma/refinery) (extractor for compiled Halo 1 Xbox/PC/CE/Demo/Yelo maps), [Librarian](https://github.com/Sigmmma/Librarian) (Halo CE tag <-> YAML converter for version-controlling mod projects), [Blendkrieg](https://github.com/Sigmmma/Blendkrieg) (Halo model importer/exporter for Blender), [Ghostbuster](https://github.com/Sigmmma/ghostbuster) (detects and fixes phantom BSP collision artifacts in `scenario_structure_bsp` tags), and [MEK](https://github.com/Sigmmma/mek) (installer bundling this whole toolchain).
- [Halo 3 Map Variant Editor](https://github.com/twist84/map_variant_yaml_test) - Browser-based editor for Halo 3 Forge map variants that opens `.map`, `.mvar`, `.bin` or `.blf` files as YAML via a Rust/WebAssembly codec, resolves object and quota indices to tag names, and exports a new map-variant binary.
- [Alteration](https://github.com/Xenomega/Alteration) - Halo 3 modding tool (created in 2008) used by the modding community to research the game's file formats and modify or extract its assets, with map package support. Also includes HaloDevelopmentExtender, a library for talking to Xbox 360 development units over the debug socket (TCP 730).
- [ScaleformTools](https://github.com/Sopitive/ScaleformTools) - Desktop editor for Halo MCC Scaleform UI assets: inspects and edits GFX/SWF layouts, decompiles and recompiles AS3 (AVM2) scripts, and edits UFG `.perm.bin`/`.temp.bin` texture packs with PNG/DDS import and export.

##### Destiny

- [alkahest](https://github.com/cohaereo/alkahest) - Multi-tool for viewing Destiny 2 assets, with a focus on an accurate recreation of the renderer. Supports Tiger engine formats.
- [tiger-pkg](https://github.com/v4nguard/tiger-pkg) - Destiny 1/2 package library and tools (unpacker, verification). Supports Destiny 1 (Internal Alpha, The Taken King, Rise of Iron), Destiny 2 (Beta through Edge of Fate), and Marathon. Handles PKG files across PS3, PS4, X360, XONE, and Windows platforms.
- [tiger](https://github.com/Blam-Network/tiger) - TypeScript libraries for Destiny's Tiger engine: reading `.pkg` packages and decoding tags with per-build definitions, a VM and decompiler for compiled activity scripts, package block decompression, and an RSAT bitstream encoder/decoder.
- [quicktag](https://github.com/v4nguard/quicktag) - Destiny 1/2 package file data structure explorer. Scans and analyzes Tiger engine structure files (8080 files) to discover structures, patterns, strings, and more. Features tag viewer, localized/raw strings browser, and asset preview for textures and Wwise audio streams.
- [Charm](https://github.com/cohaereo/Charm) - Destiny 2 reverse engineering tool for extracting assets from game files. Supports multiple Tiger engine versions and Destiny 2 game versions (Shadowkeep through Lightfall). Focuses on providing access to information in game files for artists and content preservation.
- [d2-map-importer-addon](https://github.com/DeltaDesigns/tiger-importer-blender-addon) - Blender 4.0+ addon for importing Destiny 2 rips from Charm. Assembles maps (statics, dynamics, lights, terrain), auto-assigns gear shaders and textures to player gear, compatible with DARE/DCG skeletons and IK Player Skeleton.
- [Destiny-Collada-Generator](https://github.com/DeltaDesigns/Destiny-Collada-Generator) - Tool to generate Collada files of items from Destiny 2 via web/mobile API. Exports geometry, mesh weights, UV coordinates, normals, tangents, vertex colors, and dye slots. Generates textures in PNG format and shader parameter lists.
- [SBox-Destiny-2-Map-Importer](https://github.com/DeltaDesigns/SBox-Destiny-2-Map-Importer) - Tool for importing ripped Destiny 2 maps from Charm into S&Box Hammer. Imports maps with materials, shaders, and models into S&Box scenes.
- [MIDA](https://github.com/DeltaDesigns/MIDA) - Fork of Charm designed for Marathon. Tool for extracting assets from Marathon game files, focused on artists and content preservation. Supports Marathon Closed Alpha. Note: Most features currently non-functional, development status uncertain.
- [destinydocs](https://github.com/cohaereo/destinydocs) - Documentation for Destiny 1/2 internals.
- [DestinyDocs](https://github.com/MontagueM/DestinyDocs) - Documentation on Destiny game files, particularly for recent versions of Destiny 2. Includes Charm wiki, engine overview, and tag format explanations.
- [D2StaticDocs](https://github.com/nblockbuster/D2StaticDocs) - Documentation on the Destiny 2 Beyond Light static model format. Covers main model files, subfiles, material tables, and loadzone structures.
- [destinypkgtool](https://github.com/v4nguard/destinypkgtool) - Rust library and tools for working with Destiny 1 pkg files (unpacker, verification).
- [DestinyUnpackerCPP](https://github.com/nblockbuster/DestinyUnpackerCPP) - C++ unpacker for Destiny 1 (PS4/PS3/X360) and Destiny 2 PC packages. Supports WEM conversion, TXTP generation, hex ID naming, and music-only extraction. See also [MontagueM/DestinyUnpackerCPP](https://github.com/MontagueM/DestinyUnpackerCPP) for the original version.
- [DestinyPKGTool](https://github.com/cra0kalo/DestinyPKGTool) - Package extractor for Destiny (Xbox 360/PS3) packages.
- [destiny-unpacker-rs](https://github.com/nblockbuster/destiny-unpacker-rs) - Rust implementation of Destiny unpacker (archived).
- [D2StaticExtractor](https://github.com/nblockbuster/D2StaticExtractor) - Static model extraction tool that converts Destiny 2 static models into FBX files. Supports Beyond Light and later versions. Note: Superseded by Charm, but still useful for specific use cases (archived).
- [D2TextureRipper](https://github.com/nblockbuster/D2TextureRipper) - Batch texture and image ripper for Destiny 2. Supports versions 1.0.0.1 through 4.0.0.1 (The Witch Queen). Extracts textures from package files with batch processing support.
- [MontevenDynamicExtractor](https://github.com/nblockbuster/MontevenDynamicExtractor) - Fork of MDE for extracting Destiny 2 dynamic models to FBX. Supports textures, skeletons, weighted models, and batch extraction. See also [MontagueM/MontevenDynamicExtractor](https://github.com/MontagueM/MontevenDynamicExtractor) for the original version.
- [Destiny-API-Ripper-Extension](https://github.com/nblockbuster/Destiny-API-Ripper-Extension) - Extension and GUI for Destiny Collada Generator and Monteven Dynamic Extractor. Provides automated workflow for extracting Destiny 2 assets via API.
- [Destiny-Collada-Generator](https://github.com/nblockbuster/Destiny-Collada-Generator) - Fork of tool to generate Collada files of items from Destiny 2 via web/mobile API. Exports geometry, mesh weights, UV coordinates, normals, tangents, vertex colors, and dye slots. See also [DeltaDesigns/Destiny-Collada-Generator](https://github.com/DeltaDesigns/Destiny-Collada-Generator) for the maintained version.
- [DestinyOSTListGen](https://github.com/nblockbuster/DestinyOSTListGen) - Tool to generate a list (OSTs.db) of all GinsorIDs of music from Destiny. Uses WwiseParser to parse soundbanks. Supports comparison with previous lists and SFX filtering.
- [DestinyWwiseParserScript](https://github.com/nblockbuster/DestinyWwiseParserScript) - Python script to create and parse JSON files created by WwiseParser, specialized for Destiny and Destiny 2. Supports automatic WAV export and version switching (D1/pre-BL).
- [bungie-lua-decompiler](https://github.com/nblockbuster/bungie-lua-decompiler) - Tool to decompile Bungie's Lua scripts found in the Destiny 1 Alpha with format 14.

##### Marathon (1994)

- [alephone](https://github.com/Aleph-One-Marathon/alephone) - Open source continuation of Bungie's Marathon, Marathon 2: Durandal, and Marathon Infinity game engines; loads and plays the original commercial scenario/map, Shapes, and Sounds data files.
- [m2-infinity-source-code](https://github.com/Aleph-One-Marathon/m2-infinity-source-code) - Original Bungie-released source code for Marathon 2: Durandal and Marathon Infinity, the authoritative reference for the original engine's native map/shapes/sounds format handling.

##### Myth

- [Myth2ools](https://github.com/opcow/Myth2ools) - Console tools for extracting, editing, and rebuilding Myth II: Soulblighter map assets.
  - Tools: extract_map (dumps mesh tags, terrain layers as indexed BMPs, screens, strings, and PNG reference layers, with optional OpenRaster `.ora` layered export), a matching build tool that reassembles edited layers back into the original tag format, and an imgui-based graphical shell wrapping the console tools.
  - Workflow: supports round-tripping terrain/flag edits through Blender via a `displacement.obj` mesh for precise 3D editing, plus placing units, monsters, and sounds.

##### Phantom Dust

- [Esper-RE](https://github.com/Torphedo/Esper-RE) - Tools and a C library for researching and modding Phantom Dust file formats.
  - Tools: Polaris (graphical ALR editor with texture/mesh/animation import-export), Deck Reader (TUI editor for deck/arsenal files), SSB Tool (function export table dumper).
  - Formats: ALR (textures, meshes, animations, skeletons), Deck/Arsenal, SSB scripts, stage layout (.dat), music (.stx), sound effects (.bin), quest data (.qdt), NPC bundles (.ak/.mk).

##### Gears of War

- [Gears of War Map Cooker Tool for Newbies](https://www.moddb.com/mods/gears-multiplayer-enhancement-mod/downloads/gears-of-war-map-cooker-tool-for-newbies) - .NET application for simplifying map cooking for H.I.V.E Mode and Multiplayer Enhancement Mod.

##### Forza

- [ForzaTech-extraction-tools](https://github.com/Doliman100/ForzaTech-extraction-tools) - Documentation and tools for ForzaTech .carbin and .modelbin file structures.
- [forzatech-localization-toolkit](https://github.com/7akeem0/forzatech-localization-toolkit) - Reverse engineering documentation and tools for ForzaTech engine's text/localization system (string tables, font formats, UI archives), covering Forza Horizon 4/5/6 and Forza Motorsport.
- [Forza-X360-IO](https://github.com/austinbaccus/Forza-X360-IO) - Blender addon for importing Xbox 360-era Forza racetracks, 3D models, and materials.
  - Games: Forza Motorsport 3/4, Forza Horizon 1/2 (not FM2).
  - Formats: PVS (track model instances/textures), STX.BIN/BIN (CAFF textures), FXOBJ (Effects Lite shaders), RMB.BIN (3D geometry), BIX (textures).
  - Features: Model/instance placement, vertex buffer layout support, DDS texture repacking without re-encoding.

##### Age of Empires

- [Audio Modding Guide (AoE2DE)](https://steamcommunity.com/sharedfiles/filedetails/?id=1915891079) - Comprehensive tutorial for audio modding in Age of Empires II: Definitive Edition.
  - Topics: Scenario triggers, SFX replacement, music, voice-overs, taunts, data file editing with Wwise audio system.
  - Tools: Ravioli Tools, vgmstream, Advanced Genie Editor.
- [halo (decomp)](https://github.com/halo-re/halo) - Matching decompilation of Halo: Combat Evolved (Xbox).
- [OniFoxed](https://github.com/hogsy/OniFoxed) - Bungie's Oni source modified to build with modern Visual Studio, enabling study and modification of the game and its original data formats.
- [openage](https://github.com/SFTtech/openage) - Free/open-source clone of the Age of Empires II engine, reading the original game's .dat/.drs data files to reproduce gameplay, graphics, and sound.
- [aoc-mgx-format](https://github.com/stefan-kolb/aoc-mgx-format) - Reverse-engineered file format specification for Age of Empires II: The Conquerors savegame (.mgx) files.
- [Resource-Manager](https://github.com/eBaeza/Resource-Manager) - Utility for viewing, comparing, creating, and extracting files from Age of Empires III `.BAR` archives.
- [AoE2ScenarioParser](https://github.com/KSneijders/AoE2ScenarioParser) - Python library for reading and editing Age of Empires II: Definitive Edition `.aoe2scenario` files, exposing triggers, conditions, effects, units, maps, players, and messages across all supported game versions.
- [extract-drs](https://github.com/vs49688/extract-drs) - Small C utility to extract Age of Empires 1 `.drs` resource archives [archived].

##### Microsoft Plus! for Windows XP

- [noclip.website (Plus! for XP)](https://github.com/magcius/noclip.website/tree/main/src/PlusForXP) - In-browser recreation of the 3D screensavers shipped with Microsoft Plus! for Windows XP (Mercury Pool, Robot Circus, Sand Pendulum), including a parser for the games' SCX scene format, light baking, keyframe animation, and reimplementations of each screensaver's simulation logic.

##### Microsoft Bob

- [robert.js](https://github.com/Treeki/robert.js) - JavaScript tools for working with Microsoft Bob data files (also used, in an upgraded version, by the Office 97 Assistants), with live demos for actors and rooms.

##### 3D Movie Maker

- [Microsoft-3D-Movie-Maker](https://github.com/microsoft/Microsoft-3D-Movie-Maker) - Official Microsoft-released original 1995 source code for 3D Movie Maker, the upstream basis for the preservation/reverse-engineering projects below.
- [3DMMForever](https://github.com/foone/3DMMForever) - Preservation and modernization project for Microsoft 3D Movie Maker, reading and importing the original program's archive, model, and asset formats.
- [3dmm-source-notes](https://github.com/benstone/3dmm-source-notes) - Research notes on Microsoft 3D Movie Maker's leaked source code, documenting its internal data structures and file formats.
- [3dmmInternals](https://github.com/foone/3dmmInternals) - Reverse engineering notes and tools for Microsoft 3D Movie Maker's internal formats.
- [DecompVM](https://github.com/foone/DecompVM) - x86 emulator in Python for running 3D Movie Maker's native decompression functions directly, to decode its custom-compressed asset data.
- [PyQ](https://github.com/foone/PyQ) - Python remake of 3D Movie Maker's HighQ tool for importing high-quality WAV audio into the game's format.
- [7gen](https://github.com/foone/7gen) - Collection of utilities for generating v3dmm expansion packs for 3D Movie Maker.
- [3dmmDecompress](https://github.com/foone/3dmmDecompress) - Standalone implementation of the decompression algorithms used by 3D Movie Maker's data files.
- [zbmp-sweeper](https://github.com/foone/zbmp-sweeper) - Generates zbuffer-sweeping animations from 3D Movie Maker's ZBMP background format.
- [3DMMEx](https://github.com/benstone/3DMMEx) - Source port of Microsoft 3D Movie Maker built on top of the 3DMMForever preservation project, reading the original program's archive, model, and asset formats with minor modern enhancements.
- [pymaginopolis](https://github.com/benstone/pymaginopolis) - Collection of Python and Ghidra scripts for reverse engineering Microsoft 3D Movie Maker.
- [audioman-decomp](https://github.com/benstone/audioman-decomp) - Decompilation of AudioMan, the sound mixer library used by Microsoft 3D Movie Maker, based on reverse engineering of its debug static library.
- [3dmm-notes](https://github.com/frank-weindel/3dmm-notes) - Reverse engineering notes on Microsoft 3D Movie Maker's internal classes and script interpreters (KidWorld, GOKs, Help Balloons).
- [3dmm-dissolve](https://github.com/benstone/3dmm-dissolve) - Reimplementation of Microsoft 3D Movie Maker's dissolve transition effect, based on the original patent and reverse engineering of the program.
- [3dmm-pencil-2](https://github.com/frank-weindel/3dmm-pencil-2) - 3DMM Pencil++ 2, a C++ utility for examining and editing Microsoft 3D Movie Maker data files, extracting music, sounds, textures, images, video frames, and 3D models.
##### Minesweeper

- [ReversingMinesweeper](https://github.com/repnz/ReversingMinesweeper) - Ongoing project to reconstruct the full source code of Microsoft Minesweeper through binary reverse engineering.
- [H2AMap](https://github.com/Zriecka1727/H2AMap) - Map tool for Halo 2: Anniversary, working with the game's original map data.

#### Midway

##### Area 51

- [area51](https://github.com/ProjectDreamland/area51) - Source code release for Area 51 (2005) by Midway Games / Midway Studios Austin.
- [engine-51](https://github.com/bigianb/engine-51) - Experimental tools for Area 51 (2005) engine.
- [dfs-tool](https://github.com/ProjectDreamland/dfs-tool) - CLI utility for working with Area 51's DFS (Data File System) archive format, based on Inevitable Entertainment's original C++ implementation.
- [json-playsurface-processer](https://github.com/Source2Spy/json-playsurface-processer) - Blender script that rebuilds Area 51 playsurface maps by placing glTF models at the transforms from a playsurface `.json` exported by engine-51's DFS Viewer.
- [Inevitable-MATX-Toolkit](https://github.com/Source2Spy/Inevitable-MATX-Toolkit) - Blender add-on for importing and exporting `.matx` mesh files (File > Import/Export > MATX), including skinned/armature data and a rigid-body visualizer, made for the GeomCompiler and Art2Code tools from the Area 51 source release.
- [audiopkgextractor](https://github.com/ProjectDreamland/audiopkgextractor) - QuickBMS-based extractor for Area 51's audiopkg audio package files.
- [xbmp-converter](https://github.com/ProjectDreamland/xbmp-converter) - Converts Area 51's XBMP texture files to and from standard image formats.
- [000extractor](https://github.com/ProjectDreamland/000extractor) - QuickBMS script for extracting Area 51's 000 archive files.

##### Gauntlet

- [gdl-tools (haekb)](https://github.com/haekb/gdl-tools) - Toolkit for Gauntlet Dark Legacy files.
- [gdl_wad_decoder](https://github.com/haekb/gdl_wad_decoder) - WAD archive decoder for Gauntlet Dark Legacy.
- [gdl_vbnk_decoder](https://github.com/haekb/gdl_vbnk_decoder) - Voice bank decoder for Gauntlet Dark Legacy.
- [gl_rom_decoder](https://github.com/haekb/gl_rom_decoder) - ROM decoder for Gauntlet Legends.
- [io_scene_gdl](https://github.com/haekb/io_scene_gdl) - Blender addon for Gauntlet Dark Legacy scene format.
- [gdl_tools (MosesofEgypt)](https://github.com/MosesofEgypt/gdl_tools) - Alternative toolkit for Gauntlet Dark Legacy.
- [MeltyTool (Gauntlet)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/GauntletDarkLegacy) - Gauntlet Dark Legacy format viewer/exporter.
- [gex](https://github.com/alinsavix/gex) - Gauntlet II arcade ROM tile, stamp, and maze extractor, rendering tiles, stamps, floors, walls, items, monsters, and complete mazes as PNG images. See also the author's [python-gex](https://github.com/alinsavix/python-gex) port.
- [gauntlet-soundrom-ai-reveng](https://github.com/alinsavix/gauntlet-soundrom-ai-reveng) - AI-assisted reverse engineering of the Gauntlet II arcade sound coprocessor ROM.
- [gauntlet-gamerom-ai-reveng](https://github.com/alinsavix/gauntlet-gamerom-ai-reveng) - AI-assisted reverse engineering of the Gauntlet II arcade main 68010 game ROM.

##### Mortal Kombat

- [MortalKombat (leeao)](https://github.com/leeao/MortalKombat) - Noesis plugin for Mortal Kombat: Deadly Alliance, Deception, and Armageddon (PS2), and Mortal Kombat: Unchained (PSP) DFF/MKA models.
- [Ultimate Mortal Kombat 3 iOS Recomp](https://github.com/MaryNCRT/Ultimate-Mortal-Kombat-3-iOS-Decompiled) - Decompilation of Ultimate Mortal Kombat 3 (iOS, EA Mobile 2011) into readable C for a native Windows/Linux port; recovers 4,342 named functions across 135 source files from the retail binary's STABS table, validated by differential testing against a static ARM-to-C recompiler. Requires the player's own copy of the game.
- [Unpacker-and-Repacker-to-MK-Shaolin-Monks-pack-PS2](https://github.com/RayneDuarte/Unpacker-and-Repacker-to-MK-Shaolin-Monks-pack-PS2-) - Unpacks and repacks the archive format used by Mortal Kombat: Shaolin Monks (PS2).
- [SSFExplorer](https://github.com/ermaccer/SSFExplorer) - Tool to view and edit Mortal Kombat PS2-era archive files.
- [rewolf-mortal-kombat](https://github.com/rwfpl/rewolf-mortal-kombat) - Parser for Mortal Kombat's GRA graphics resource files (compressed sprites and palettes). See also the companion [rewolf-mortal-kombat-viewer](https://github.com/rwfpl/rewolf-mortal-kombat-viewer), a viewer for the uncompressed GRA files it produces.

##### NARC

- [narc](https://github.com/Asure/narc) - Rebuildable source and assets for the 1988 Williams/Midway arcade game N.A.R.C., an actively fixed-up fork of [Luigi30/narc](https://github.com/Luigi30/narc) (8 additional commits); documents IMG sprite/mugshot data and RLE-encoded assets and produces MAME-compatible ROM images.

##### NBA Hangtime

- [nba-hangtime-rebuild](https://github.com/Asure/nba-hangtime-rebuild) - Actively-developed rebuild of NBA Hangtime (1996, Midway) source, a heavily extended fork of [historicalsource/nba-hangtime](https://github.com/historicalsource/nba-hangtime) (300+ additional commits) adding DCS audio sample support (.GLO/.TBL), a new playable court, updated rosters, and a pure-Python build pipeline producing MAME-compatible GFX/DCS ROMs.

##### NBA Jam

- [Roaster](https://github.com/fabiensanglard/roaster) - Tool to patch the EPROM images (character graphics/palettes and text) of the NBA Jam Tournament Edition (rev 4.0) arcade board.
- [jamedit](https://github.com/chriskearney/jamedit) - Edits an NBA Jam cartridge dump's rosters, portraits, artwork, and league marks, and produces a patch.

##### NFL Blitz

- [NFL-Blitz-File-Editor](https://github.com/thompjake/NFL-Blitz-File-Editor) - File editor for NFL Blitz game data.
- [NFL-Blitz-Play-Maker](https://github.com/thompjake/NFL-Blitz-Play-Maker) - Playbook editor for NFL Blitz.
- [NFL_Blitz_Roster_Manager](https://github.com/thompjake/NFL_Blitz_Roster_Manager) - Roster management tool for NFL Blitz.
- [NFLBlitzDataEditor.Core](https://github.com/thompjake/NFLBlitzDataEditor.Core) - Core library for editing NFL Blitz data files.
- [afsys](https://github.com/DaveShepperd/afsys) - Filesystem I/O library for reading Atari Games and Midway Games West arcade game disks and images.
- [midway-loadimg](https://github.com/Asure/midway-loadimg) - Replacement for the MS-DOS LOAD2/LOADW tool used to build graphics ROM images for Williams/Midway arcade games.
- [midway-univiewer](https://github.com/Asure/midway-univiewer) - 3D viewer for Midway arcade game universe files (UNI format), written in C99 with SDL2.
- [midway-bddtool](https://github.com/Asure/midway-bddtool) - Viewer/editor for Midway arcade game background and sprite data (BDB/BDD formats).
- [midway-imgtool](https://github.com/Asure/midway-imgtool) - IMGTOOL for creating and editing IMG container files used by various Midway arcade games; runs under DOSBox.
- [elf2ol](https://github.com/DaveShepperd/elf2ol) - Converts m68k-elf ELF object files to llf's .ol format; bundles the author's 1990s elf2zo/rdelf tools that compressed MIPS ELF boot images for Midway Games arcade hardware.
- [macxx](https://github.com/DaveShepperd/macxx) - Macro assembler for 6502, 6800, 6809, 68000/68010, 8080/8085, Z80, PDP11, and the Atari ASAP/Tom&Jerry DSP processors; the author's modernized rebuild of the in-house assembler originally used at Atari Games/Midway to build 1980s arcade coin-op game code.
- [dmp_vlda](https://github.com/DaveShepperd/dmp_vlda) - Dumps the .ob (macxx) and .vlda/.lb (llf) binary object/library file formats produced by the macxx/llf Atari/Midway arcade build toolchain.
- [gca](https://github.com/DaveShepperd/gca) - Resurrected 1990s port of gcc 1.40 targeting the Atari Simplified Architecture Processor (ASAP) used in Atari Games arcade hardware, emitting macxx-compatible assembly for use with the macxx/llf toolchain.
- [llf](https://github.com/DaveShepperd/llf) - Link+Locate+Format linker, companion to macxx, tracing back to the original in-house Atari Games coin-op cross-development toolchain.

##### San Francisco Rush: The Rock

- [rushtherock-build-tooling](https://github.com/cheeseandcereal/rushtherock-build-tooling) - Docker-based reproducible build environment that compiles San Francisco Rush: The Rock (1997, Atari Games) from the historicalsource source dump using a period-correct gcc 2.7.2.3/newlib 1.6.1 MIPS toolchain, producing a MAME/cabinet-compatible ELF.

##### Wizard of Wor

- [wizardofwor](https://github.com/dabadab/wizardofwor) - Reverse-engineered disassembly of the Commodore 64 version of Wizard of Wor (1983), reconstructed into re-assemblable 6502 source code.

#### Millennium Kitchen

##### Attack of the Friday Monsters! A Tokyo Tale

- [AttackFridayMonsters](https://github.com/pleonex/AttackFridayMonsters) - Tools and format documentation for translating the 3DS game Attack of the Friday Monsters! A Tokyo Tale. *(Archived on GitHub; development continues at the author's self-hosted [Forgejo instance](https://code.pleonex.dev/pleonex/AttackFridayMonsters).)*

#### Milon's Secret Castle

- [milondasm](https://github.com/spannerisms/milondasm) - Complete disassembly of Milon's Secret Castle (NES) that assembles to the original version, with music data parsed from the ROM into LilyPond (.ly) files; graphics binaries must be supplied by the user.

#### Mindscape

- [Days-of-Thunder-NES-Unpublished](https://github.com/DickBlackshack/Days-of-Thunder-NES-Unpublished) - Recovered source code for an unpublished Days of Thunder game for the NES developed for Mindscape (distinct from the game the publisher released in 1990), recovered from Chris Oberth's personal archives.
- [eaglenest](https://github.com/hitchhikr/eaglenest) - Complete disassembly of the Amiga version of Into The Eagle's Nest, fully decoded and re-assemblable into a working game.

#### MindStorm Software

- [Dr. Riptide Dissected](https://github.com/movAX13h/DrRiptideDissected) - Reverse-engineered tool for "In Search of Dr. Riptide" (1994, MindStorm Software), loading the game's DAT files to view/play animated sprite lumps, maps (with entities/triggers/tile sets/palette rotation), PCX images, Adlib/CMF music, VOC sound effects and text; supports hex-editing assets back into the DAT and exporting sprites/images as GIF/PNG. Includes an independently reverse-engineered map file format writeup.

#### MiST Land / GFI

- [mgc-file-formats](https://github.com/AlexKimov/mgc-file-formats) - Game resource format documentation and viewing tools for games by GFI/MiST Land.

#### Virtys (Mist Legacy)

- [ML.DAT.Parsed](https://github.com/Ekey/ML.DAT.Parsed) - Parsed database tables extracted from Mist Legacy.

#### Mithis Entertainment

##### Nexus: The Jupiter Incident

- [Nexus Mesh Importer](https://www.moddb.com/games/nexus-the-jupiter-incident/downloads/nexus-mesh-importer) - A plug-in for Milkshape 3d that'll allow you to work on existing Nexus ship mesh & tex files.
- [Nexus Texture Converter](https://www.moddb.com/games/nexus-the-jupiter-incident/downloads/nexus-texture-converter) - converts Nexus' proprietary .tex file format to regular .tga images .NET Framework 3.5 required

#### Dragon Soul (MMORPG)

- [.AUP File Type Decryptor and Viewer](https://github.com/PredatorIWD/.AUP-File-Type-Decryptor-and-Viewer) - Client-side decryptor/viewer for Dragon Soul's custom .aup packed asset format, reverse-engineering its LZSS-variant ring-buffer compression.
  - Features: Batch export with folder structure preservation; previews PNG, JPG, BMP, TGA, DDS, custom game icons, and WAV; GB18030 Chinese text decoding.

#### Mojang Studios

- [NBT (twoolie)](https://github.com/twoolie/NBT) - Python library for parsing and writing Minecraft's NBT file format and its RegionFile container; the original NBT library used by early Minecraft modding tools including pymclevel and MCEdit.
- [Substrate](https://github.com/minecraft-dotnet/Substrate) - .NET SDK for reading and writing Minecraft Java Edition worlds, chunks, and NBT data. See also [NBToolkit](https://github.com/minecraft-dotnet/NBToolkit), a command-line map-processing toolkit built on it.
- [Burger](https://github.com/TkTech/Burger) - "Topping"-based framework that decompiles and analyzes a Minecraft client JAR to automatically extract blocks, items, entities, packets, language strings, and other internal game data, primarily for building protocol/data specifications.
- [NBTSerializer](https://github.com/gigaherz/NBTSerializer) - Minecraft NBT serialization library.
- [PCK-Studio](https://github.com/LCERD/PCK-Studio) - Editor for Minecraft Legacy Console Edition .PCK archive format. See also [Quiver](https://github.com/LCERD/Quiver), its IDE-style successor for editing LCE DLC packs (formerly PCK++), and [LegacyPlusPlus](https://github.com/LCERD/LegacyPlusPlus), a Legacy Console Edition file editor built on the same author's libLCE library.
- [MCLCEArchiver](https://github.com/Pyogenics/MCLCEArchiver) - CLI tool and library for reading Minecraft Legacy Console Edition `.arc` archive files (work-in-progress; archive creation not yet supported).
- [CompareNbt](https://github.com/gigaherz/CompareNbt) - Tool for comparing and analyzing Minecraft NBT binary data format files.
- [MinecraftLCE](https://github.com/GRAnimated/MinecraftLCE) - Decompilation of Minecraft: Legacy Console Edition with asset parsing. See also [Minecraft-Xbox-360-Decompilation](https://github.com/LCERD/Minecraft-Xbox-360-Decompilation), a separate decompilation/rewrite effort targeting the Xbox 360 version.
- [DumpModel](https://github.com/gigaherz/DumpModel) - Forge mod to export Minecraft models (items, blocks, entities) to .OBJ format.
- [YSMParser](https://github.com/OpenYSM/YSMParser) - Decrypts and converts .ysm model files used by the Yes Steve Model mod (all encrypted format versions, including its custom-encrypted C++ rewrite) into Blockbench projects, restoring models, animations, controllers, textures, sounds, and language files.
- [Minecraft-Unstitcher](https://github.com/master801/Minecraft-Unstitcher) - Unstitches pre-1.6.4 stitched Minecraft texture atlases into individual named sprites, easing porting of older mods.
- [MinecraftLocTool](https://github.com/efimandreev0/MinecraftLocTool) - Tool to edit Minecraft .loc game files; parses and modifies localization/config binary data.
- [NBT Studio](https://github.com/tryashtar/nbt-studio) - Up-to-date NBT viewer and editor for Minecraft. Supports Java and Bedrock formats with undo/redo, drag-and-drop, multiselect, and SNBT support.
- [NBTExplorer](https://github.com/jaquadro/NBTExplorer) - Graphical NBT editor for Minecraft data that reads and writes standard NBT files (eg. `level.dat`), schematics, uncompressed NBT, Anvil and region files (`.mca`, `.mcr`) and Cubic Chunks region files.
- [minecraft-ttf](https://github.com/tryashtar/minecraft-ttf) - Rust tool that converts Minecraft: Java Edition font definitions (bitmap and Unifont hex glyph providers read from the game jar) into TrueType fonts, including regular/bold/italic variants; can also build fonts from resource packs and across version history.
- [NBT (Querz)](https://github.com/Querz/NBT) - Java library for reading, writing, and manipulating Minecraft's NBT (Named Binary Tag) format, including support for implementing custom tags.
- [CombinedAudioTool](https://github.com/Cracko298/CombinedAudioTool) - GUI/CLI tool for extracting and manipulating Minecraft New Nintendo 3DS Edition audio archives (CombinedAudio.bin, FSB SoundBank files).
- [NBCraft](https://github.com/nbcraft-org/nbcraft) - Cross-platform decompilation-based Minecraft Pocket Edition re-implementation, parsing original game assets and resources.
- [mcaselector](https://github.com/Querz/mcaselector) - Tool for selecting, exporting, and deleting chunks and regions from Minecraft Java Edition world saves (MCA format). See also [arvitus/mcascripts](https://github.com/arvitus/mcascripts), a collection of custom filter scripts for it.
- [WorldPruner](https://github.com/Querz/WorldPruner) - GUI and command-line app to prune chunks from a Minecraft Java Edition world (Anvil region/MCA format), by the same author as mcaselector above.
- [MCMapViewer](https://github.com/Querz/MCMapViewer) - Tool to view and edit Minecraft maps.
- [Minecraft-Overviewer](https://github.com/overviewer/Minecraft-Overviewer) - Renders high-resolution, zoomable Leaflet maps of a Minecraft world directly from its Anvil region/chunk save data.
- [mcmap](https://github.com/spoutn1k/mcmap) - Pixel-art isometric map visualizer for Minecraft, rendering images directly from world save data.
- [MinedMap](https://github.com/neocturne/MinedMap) - Incremental Minecraft world map renderer/viewer written in Rust, parsing Anvil region/chunk data directly to generate tiled web maps for large multiplayer worlds.
- [Minutor](https://github.com/mrkite/minutor) - Cross-platform Minecraft world map viewer, rendering biome, height, spawn, and other overlays directly from Anvil region/chunk save data.
- [Project Lodestone - Documentation](https://github.com/Team-Lodestone/Documentation) - Comprehensive documentation for Minecraft file formats (NBT, world structure, MCRegion, LCE editions); supports all platforms (Java, Bedrock, 3DS, PS Vita, PS3/PS4, Xbox 360/One, Nintendo Switch).
- [libLodestone](https://github.com/Team-Lodestone/libLodestone) - Project Lodestone's library for reading and writing Minecraft file types and converting worlds between editions, with converters for Java Edition, Legacy Console Edition, New Nintendo 3DS Edition, and classic.minecraft.net worlds.
- [nbt-edit](https://github.com/Team-Lodestone/nbt-edit) - Svelte NBT editor and viewer component for the web.
- [mcSavefileParsers](https://github.com/TCA166/mcSavefileParsers) - C utilities for Minecraft save files: extract chunk NBT from region files (all chunks or a single one), generate Wavefront OBJ/MTL from resource packs, and generate 3D models of a save.
- [hematite](https://github.com/PistonDevelopers/hematite) - Minecraft client/renderer written in Rust with the Piston game engine; loads and renders actual .minecraft world saves.
- [WorldEdit](https://github.com/EngineHub/WorldEdit) - In-game map/world editor and mod for Minecraft; reads and writes world data and schematic (.schem/.schematic) files for large-scale terrain and structure editing.
- [SchematicWebViewer](https://github.com/EngineHub/SchematicWebViewer) - NPM package for importing and viewing modern Minecraft schematic (.schem) files in the browser.
- [muscode](https://github.com/ata4/muscode) - Encoder/decoder for Minecraft's XOR-encrypted .mus background music files, converting them to and from standard Ogg Vorbis.
- [nbtpp](https://github.com/JaanDev/nbtpp) - Modern C++ library for reading and writing Minecraft's NBT (Named Binary Tag) file format.
- [mc-anvil](https://github.com/hpratt/mc-anvil) - TypeScript library for reading Minecraft's Anvil region-file format and NBT data in the browser.
- [libanvil](https://github.com/majestic53/libanvil) - C++ library for reading and writing Minecraft's Anvil region-file format. (Archived.)
- [rpw (Resource Pack Workbench)](https://github.com/mcRPW/rpw) - Standalone application for editing and managing Minecraft resource packs.
- [MCEdit-Unified](https://github.com/Podshot/MCEdit-Unified) - Combined MCEdit and Pymclevel world editor for Minecraft Java Edition; reads and edits chunk/region world save data for large-scale terrain and structure editing.
- [Amulet Editor](https://github.com/Amulet-Team/Amulet-Map-Editor) - Actively maintained Minecraft world editor/converter supporting all versions since Java 1.12 and Bedrock 1.7, the spiritual successor to MCEdit. Reads and writes world/chunk save data through its own library stack: [Amulet-Core](https://github.com/Amulet-Team/Amulet-Core) (Java/Bedrock save format I/O), [PyMCTranslate](https://github.com/Amulet-Team/PyMCTranslate) (cross-version block/entity/biome translation), [Amulet-NBT](https://github.com/Amulet-Team/Amulet-NBT) (binary/stringified NBT library), and [Minecraft-Model-Reader](https://github.com/Amulet-Team/Minecraft-Model-Reader) (block model/resource pack reader).
  - In-development rewrite: [Amulet-Editor](https://github.com/Amulet-Team/Amulet-Editor) reimplements the same editor on a new modular library stack — [Amulet-Level](https://github.com/Amulet-Team/Amulet-Level) (world/structure API), [Amulet-Anvil](https://github.com/Amulet-Team/Amulet-Anvil) (Java Anvil region format), [Amulet-LevelDB](https://github.com/Amulet-Team/Amulet-LevelDB) (Mojang's modified LevelDB for Bedrock worlds), [Amulet-Game](https://github.com/Amulet-Team/Amulet-Game) (per-version data translation), and [Amulet-Resource-Pack](https://github.com/Amulet-Team/Amulet-Resource-Pack) (resource pack parsing) — and documents a new cross-version [Construction schematic format](https://github.com/Amulet-Team/construction-specification) for exchanging world sections between editors.
- [Mineways](https://github.com/erich666/Mineways) - Actively maintained Minecraft world exporter, reading Java and Bedrock world save data directly to produce 3D-printable or renderable models (OBJ, VRML, USD, and other formats), with terrain/schematic export and texture-atlas generation.
- [MiEx](https://github.com/BramStoutProductions/MiEx) - Modern Minecraft (and Hytale) world exporter for high-fidelity rendering, reading world save data and resource packs directly to produce renderable models.
- [minecraftfinder](https://github.com/edward4096/minecraftfinder) - Tool to locate Minecraft installation and world files on disk, adapted from the author's RuneScape cache-finding work for the rs-archive preservation project.
- [LCE-MultiTool](https://github.com/AITYunivers/LCE-MultiTool) - Work-in-progress suite of tools for previewing Minecraft Legacy Console Edition files (preview-only, no editing yet), based on file formats documented by Team LodeStone and the OMI Filetype Library.
- [bedrock-viz](https://github.com/bovercash/bedrock-viz) - Minecraft Bedrock Edition world visualization and reporting tool with a web app frontend, reading Bedrock's LevelDB-based world save data. Active fork (206 commits ahead) of the original [paulgrahek/bedrock-viz](https://github.com/paulgrahek/bedrock-viz), which has been stale since 2020.
- [nbtui](https://github.com/respectZ/nbtui) - Terminal viewer and editor for Minecraft Bedrock Edition `.mcstructure` NBT files, with a 3D block-grid navigator, block-palette editing, validation, and undo/redo.

##### Minecraft Dungeons

- [DungeonsModMerger](https://github.com/LukeFZ/DungeonsModMerger) - Merges Minecraft: Dungeons custom level mods (`.levelmod` files) into a single `.pak` file for use with DungeonsLevelLoader.
- [DungeonsLevelLoader](https://github.com/LukeFZ/DungeonsLevelLoader) - Custom level loader for Minecraft: Dungeons, reading merged `.pak`/`customlevels.json` mod data at runtime; modified version of flat20's dungeoneer.

##### Minecraft Legends

- [LegendsToolbox](https://github.com/LukeFZ/LegendsToolbox) - Work-in-progress tool for parsing Minecraft: Legends save files and its custom serialization format, including Xbox/Store save files, `level.dat` + LevelDB world storage, and serialized "badger" ECS world-database components, with (de)serialization code generation for C# component representations.

#### Monolith Productions

##### F.E.A.R

- [F.E.A.R. 3dsmax 7 model import plugin](https://www.moddb.com/games/fear/downloads/3dsmax-7-model-import-plugin)
- [F.E.A.R. 2 unofficial extraction tools](https://www.moddb.com/games/fear-2/downloads/fear-2-unofficial-extraction-tools) - Unofficial tools for extracting F.E.A.R. 2 archives, textures, and sounds.
- [Fear2Tools](https://github.com/Nenkai/Fear2Tools) - F.E.A.R 2 Project Origin LTArchive extractor/packer & database editor.
- [LithTechLokiResearch](https://github.com/miccTronic/LithTechLokiResearch) - Research materials for the LithTech 5 ("Loki") engine used in F.E.A.R. 2 and Condemned 2. Includes 010 Editor templates and code examples for parsing world files.
  - Formats: .wld (world/map), .WldSrvr, .WldClnt, .bndl (bundle archives), .inst (prefab/instances), .mdl (models), .txanim (animated materials).
- [FEAR Online 3dsmax script (F.E.A.R. 2)](https://www.moddb.com/games/fear-2/downloads/fear-online-3dsmax-script)
- [Video Tutorial: 3DSMax Plugin (F.E.A.R.)](https://www.moddb.com/games/fear/downloads/video-tutorial-3dsmax-plugin)
- [FEAR Database Extractor](https://www.moddb.com/games/fear/downloads/fear-database-extractor)
- [FEAR Public Tools v2](https://www.moddb.com/games/fear/downloads/fear-public-tools-v2) - FEAR sdk v2, allows making singleplayer levels on the Steam version
- [FEAR Tweaking Tool and Guide](https://www.moddb.com/games/fear/downloads/fear-tweaking-tool-and-guide) - Designed to squeeze more FPS from the game without doing any drastic changes.
- [ltar](https://github.com/cmbasnett/ltar) - Python CLI for I/O on LTAR archive files found in games using the Lithtech Jupiter engine.
- [Lithtech Jupiter Ex FX Decompiler (F.E.A.R.)](https://www.moddb.com/games/fear/downloads/lithtech-jupiter-ex-fx-decompiler)

##### Condemned 2: Bloodshot

- [Condemned2Recomp](https://github.com/psxrestore/Condemned2Recomp) - Static recompilation of Condemned 2: Bloodshot (Xbox 360) to a native PC executable using RexGlue, requiring assets extracted from a legitimately owned copy.

##### Trespasser

- [Blender 2.6 Trespasser Exporter](https://www.moddb.com/games/trespasser/downloads/blender-26-trespasser-exporter-10) - Rewrite of the exporter to work with Blender 2.6 . This script exports models into trespasser formats. Supports writting TPM files as well as values.txt files. Also adds UI elements to configurate the export easily. For the individual types of meshes a basic set of values is exported. For meshes,...
- [Blender3D Trespasser Exporter 1.0](https://www.moddb.com/games/trespasser/downloads/blender3d-trespasser-exporter-10) - Blender script for exporting models to Trespasser formats. Exports TPM files and values.txt files with mesh type filtering (v1.0).

##### Blood

- [BLOOD ULTIMATE BUNDLE TOOLS KIT](https://www.moddb.com/mods/blood-modern-voxels-pak-for-mappers-and-moders/downloads/blood-ultimate-bundle-tools-kit) - A complete collection of editors for creating your own mod or even a full-fledged Total Conversion.
- [BLOOD UNOFFICIAL TOOLS](https://www.moddb.com/games/blood/downloads/blood-unofficial-tools) - Unofficial toolkit for Blood with documentation for DOS tools (Mapedit, EditArt, ArEdit). Includes professional-style documentation for users of DOS tools or those seeking nostalgia.
- [Spill Some: The Blood Tool](https://www.moddb.com/games/blood/downloads/spill-some-the-blood-tool) - Launcher and demo utility for Blood/Cryptic Passage running under DOS/DOSBox. Enables playback of user-recorded demo files by automatically renaming default demos.
- [BlooM](https://github.com/thomasrogers03/bloom) - Modern modding suite for Blood, reading and editing the original Build engine MAP/ART/RFF/GRP game data while preserving compatibility with the retail engine's limitations.
- [XMAPEDIT](https://github.com/NoOneBlood/xmapedit) - Extended, modernized version of the original Blood map editor for Windows: edits maps plus QAV/SEQ animation and ART graphics files, with widescreen support and new object types while staying compatible with vanilla Blood. Built on nuke.YKT's [SAMapedit](https://github.com/nukeykt/samapedit), a JFBuild-based port of the original DOS Blood MAPEDIT.

##### Blood 2: The Chosen

- [Updated 3dsmax plugin (Blood 2: The Chosen)](https://www.moddb.com/games/blood-2-the-chosen/downloads/updated-3dsmax-plugin) - Updated 3dsmax plugin for Blood 2 and Shogo. Obtained from Monolith's old FTP server
- [Blood 2 Modding tools](https://www.moddb.com/games/blood-2-the-chosen/downloads/blood-2-modding-tools) - Complete modding toolkit for Blood 2: The Chosen, including ABC exporter and other essential tools.
- [Blood 2 Toolset 64 bit fix](https://www.moddb.com/games/blood-2-the-chosen/downloads/blood-2-toolset-64-bit-fix) - 64-bit compatible version of Blood 2 toolset. The default installer doesn't work on 64-bit Windows, so these are the extracted files.
- [Milkshape ABC Plugin (Blood 2: The Chosen)](https://www.moddb.com/games/blood-2-the-chosen/downloads/milkshape-abc-plugin) - Milkshape ABC plugin for Blood 2. Includes import/export plugins

##### No One Lives Forever

- [Lithtech Jupiter Maya/3dsmax plugins (No One Lives Forever 2)](https://www.moddb.com/games/no-one-lives-forever-2-a-spy-in-harm/downloads/lithtech-jupiter-maya3dsmax-plugins) - Collection of Lithtech Jupiter model and level import/export plugins for 3DS Max 3-7 and Maya 4-7.
- [Lithtech 2.2 toolset (No One Lives Forever)](https://www.moddb.com/games/no-one-lives-forever/downloads/lithtech-22-toolset) - Updated version of the Lithtech 2.0 tools with enhancements including .lta support and rebinding buttons (v2.2).
- [NOLF Tools (No One Lives Forever)](https://www.moddb.com/games/no-one-lives-forever/downloads/nolf-tools) - Official modding tools for No One Lives Forever.
- [No One Lives Forever 2 Toolkit](https://www.moddb.com/games/no-one-lives-forever-2-a-spy-in-harm/downloads/no-one-lives-forever-2-toolkit) - Complete toolkit for No One Lives Forever 2 including editing tools and source code. Provided as-is without official support.
- [No One Lives Forever (Source Code)](https://github.com/osgcc/no-one-lives-forever) - Official source code release (v1.003) of No One Lives Forever, containing game engine code with file format implementations.
- [ps2rezdecoder](https://github.com/haekb/ps2rezdecoder) - PS2 REZ format decoder and extractor for Lithtech games.
- [io_scene_abc](https://github.com/cmbasnett/io_scene_abc) - Blender addon for importing ABC model files from Lithtech 2.1 engine games.

##### Shogo: Mobile Armor Division

- [Shogo Mobile Armor Division Modding Tools](https://www.moddb.com/games/shogo-mobile-armor-division/downloads/shogo-mobile-armor-division-modding-tools) - Modding tools for Shogo Mobile Armor Division. Includes help for Shogo API:s used in the Source Code.
- [Shogo tools 64 bit](https://www.moddb.com/games/shogo-mobile-armor-division/downloads/shogo-tools-64-bit) - 64-bit compatible SDK files for Shogo: Mobile Armor Division. The official SDK installer only works on 16-bit and 32-bit systems, so these are the extracted files for 64-bit systems.

##### Captain Claw

- [OpenClaw](https://github.com/pjasicek/OpenClaw) - Multiplatform C++ reimplementation of Captain Claw (1997), written from scratch but reading assets from the original game's CLAW.REZ archive.

#### Monolith Soft

*Japanese studio (distinct from Monolith Productions, USA).*

##### Xenoblade Chronicles

- [xenoblade (decomp)](https://github.com/xbret/xenoblade) - Matching decompilation of Xenoblade Chronicles (Wii, JP).
- [XenoTools](https://github.com/Nenkai/XenoTools) - Tools for Xenoblade Chronicles file formats.
- [XbTool](https://github.com/Thealexbarney/XbTool) - Tool for reading, processing and exporting data from Xenoblade Chronicles, Xenoblade Chronicles X and Xenoblade Chronicles 2.
  - Features: ARD/ARH archive extraction and replacement, BDAT decryption and conversion to HTML/JSON/PSQL, XB2 save reading, script reading, and CATEX texture decoding.
  - Companion: [xenoblade2-data](https://github.com/Thealexbarney/xenoblade2-data) - HTML data tables from Xenoblade Chronicles 2.
- [bdat-rs](https://github.com/roccodev/bdat-rs) - Rust library for reading and writing BDAT format used in Xenoblade Chronicles games for data tables.
- [xcnx-file-loader](https://github.com/roccodev/xcnx-file-loader) - File replacement mod for Switch Xenoblade games allowing custom files to be loaded from RomFS instead of ARD archives.
- [ard-tools](https://github.com/roccodev/ard-tools) - Tools for working with ARD/ARH archive files from Switch Xenoblade Chronicles games. Includes ardain library, ard-tools CLI, and fuse-ard FUSE driver.
- [XCXDE-ModLoader](https://github.com/masagrator/XCXDE-ModLoader) - Mod loader for Xenoblade Chronicles X: Definitive Edition (Switch) that loads replacement files without repacking ARD/ARH archives.
- [xb3tool](https://github.com/vaxherd/xb3tool) - Tools and notes for researching/analyzing Xenoblade Chronicles 3 data. Supports BDAT database format and map generation.
- [Xenoblade3](https://github.com/turtle-insect/Xenoblade3) - Save data editor for Xenoblade Chronicles 3 (Switch).
- [XenobladeSave](https://github.com/Thealexbarney/XenobladeSave) - Save parser for Xenoblade Chronicles (Wii) that renames saves from their contents, converts the embedded RGB565 TPL images to BMP, and documents the big-endian save layout.
- [Xenoblade-Switch-Model-Importer-Noesis](https://github.com/Turk645/Xenoblade-Switch-Model-Importer-Noesis) - Noesis plugin for importing 3D models from all 3 Xenoblade Chronicles Switch titles (Definitive Edition, X, 3), with mesh/material/texture export, morph support, and LOD toggles.
- [XenoLib](https://github.com/PredatorCZ/XenoLib) - Independent serialization library and CLI toolset for Xenoblade Engine formats.
  - Formats: MXMD models (camdo/wimdo), DRSM/MXMD streams (casmt/wismt), MTXT/LBIM textures (witex/catex), XBC1 compression, SAR archives, BDAT data, MTHS shaders, BC (SKEL/ANIM/ASM), ARH/ARD archives, MSMD streamed maps (casm/wism).
- [XenoMax](https://github.com/PredatorCZ/XenoMax) - 3ds Max plugin built on XenoLib for importing Xenoblade Engine models, built on the same format support.
- [xc3_lib](https://github.com/ScanMountGoat/xc3_lib) - Rust libraries and tools for Xenoblade Engine rendering file formats across Xenoblade Chronicles X, 1 (Definitive Edition), 2, 3, and X Definitive Edition (Switch/PC/Wii U). Covers MXMD models (wimdo/pcmdo/camdo), MSRD/MSMD streaming data (wismt/pcsmt/casmt), BC skeletal animations, and more; complements XenoLib above with broader multi-title/platform coverage. See also [xc3_model_py](https://github.com/ScanMountGoat/xc3_model_py) for Python bindings.
- [xenoblade_blender](https://github.com/ScanMountGoat/xenoblade_blender) - Blender addon built on xc3_lib for importing Xenoblade Engine models, maps, and animations.
- [recordkeeper](https://github.com/roccodev/recordkeeper) - Save file editor for Xenoblade Chronicles 3 and Future Redeemed.
- [xeno-lvb](https://github.com/roccodev/xeno-lvb) - Extracts gimmick disposition data from `.lvb` files in Xenoblade Chronicles 2 and 3, dumping enemy/field gimmick placement data to JSON by hash ID, name, or BDAT ID.
- [xc3fr-unlock-kit-balance](https://github.com/roccodev/xc3fr-unlock-kit-balance) - Edits Xenoblade Chronicles 3: Future Redeemed's unlock kit distribution by patching a BDAT dump (extracted with bdat-rs above) to make kits character-specific, then repacking for use with xcnx-file-loader above.

#### Monster Jam

- [Monster-Jam-Unpack](https://github.com/zbirow/Monster-Jam-Unpack) - Documents and unpacks the custom "PAK" .dat archive format used by Monster Jam (2007), covering the main header/directory/file tables, the pointer-table chunk index, and both zlib-compressed and raw data chunks.

#### Moorhuhn

- [MHLIB](https://github.com/Theaninova/mhlib) - Engine reimplementation for classic Moorhuhn games written in Rust and Godot; preprocesses and loads original game assets from installed game copies.
- [MoorhuhnSDP](https://github.com/Helco/MoorhuhnSDP) - Reverse engineering research on the file formats of "Moorhuhn Adventure - Der Schatz des Pharaos" (Crazy Chicken Adventure - The Pharao's Treasure).

#### Mucky Foot Productions

- [MuckyFoot-UrbanChaos](https://github.com/dizzy2003/MuckyFoot-UrbanChaos) - Recovered source code snapshot for Urban Chaos (1999, PC/PSX/Dreamcast), including the game's map/animation editor and the shared MFlib1/MFStdLib libraries also used by Startopia.

#### MumboJumbo

- [LuxorDecomp](https://github.com/HW12Dev/LuxorDecomp) - Work-in-progress decompilation of Luxor 1, based on the latest Steam release of the game.

#### BeeWorks (Mushroom Garden Neo)

- [NamekoNeoExtractor](https://github.com/m2jean/NamekoNeoExtractor) - Data extractor and WPF viewer for Mushroom Garden Neo's (なめこ栽培NEO) iOS ipa package, decoding the MessagePack-based `library.bin` nameko (mushroom) data and its WebP sprite images.

#### Amistech Games (My Summer Car)

- [MSCEditor](https://github.com/durkhaz/MSCEditor) - Feature-packed save-file editor for My Summer Car.

#### N-LOG Soft (Mystic Nights)

- [Mystic-Nights-Online](https://github.com/jeremydecola/Mystic-Nights-Online) - Open-source private server reviving the online multiplayer of Mystic Nights (PS2), a Korea-exclusive N-LOG Soft survival horror title, reverse-engineered from the client binaries via Ghidra decompilation and packet analysis.
- [Mystic-Nights-Translation](https://github.com/jeremydecola/Mystic-Nights-Translation) - English fan translation of Mystic Nights (PS2), reverse engineering the Korea-exclusive N-LOG Soft survival horror title's text and archive formats; companion project to Mystic-Nights-Online above.
