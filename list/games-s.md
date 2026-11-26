### S
#### Saber Interactive

- [saber-file-formats](https://github.com/AlexKimov/saber-file-formats) - File formats and viewer plugins for Saber Interactive games.
- [SnowRunner-Save-Editor](https://github.com/MrBoxik/SnowRunner-Save-Editor) - Desktop save editor for SnowRunner (also a website version) that edits money, rank, game rules, difficulty and time settings, completes missions/tasks/contests, unlocks upgrades, watchtowers and garages, and edits fog of war and achievements; supports the base maps and Seasons 1-18.

#### Sachi Soft

- [pikachu-volleyball](https://github.com/gorisanson/pikachu-volleyball) - JavaScript reimplementation of Pikachu Volleyball (1997 Windows game by SACHI SOFT/SAWAYAKAN Programmers), reverse-engineered from the original machine code.
  - Methods: Ghidra decompilation of the physics engine and AI, Cheat Engine for locating key variables, OllyDbg for machine-code patching, and Resource Hacker for extracting the original sprites and sound assets.
- [pikachu-volleyball-p2p-online](https://github.com/gorisanson/pikachu-volleyball-p2p-online) - Peer-to-peer online multiplayer add-on for the same reverse-engineered Pikachu Volleyball above, by the same author.

#### Ascaron Entertainment (Sacred)

- [sacred-sdk](https://github.com/bssth/sacred-sdk) - Lua scripting framework and bytecode toolchain for Sacred Gold (2004), enabling mods without patching the game's EXE.
  - Format: FunkCode.bin bytecode baking, achieving byte-perfect roundtrip against all 132 vanilla game .bin files.
- [sacred-minimap-viewer](https://github.com/Qronikarz/sacred-minimap-viewer) - Tool to view the whole minimap of Sacred.
- [grn2glb](https://github.com/ancaria-dev/grn2glb) - C++ library (64-bit DLL with a C ABI) that converts Sacred Gold Granny 1.2 `.grn` models to binary glTF in memory.
  - Features: meshes, skeleton, skin weights, materials and embedded raw/compressed VTex textures as PNG.

#### Southend Interactive (Sacred Citadel)

- [SC.VFS.Tool](https://github.com/Ekey/SC.VFS.Tool) (archived) - Tool for extracting and repacking VFS archives from Sacred Citadel.

#### Safari Software

- [LineWarsII-DOS](https://github.com/fredangstadt-lang/LineWarsII-DOS) - Reconstruction in C of LineWars II (1994, DOS space-combat game by Patrick Aalto, published by Safari Software), rebuilt from the shipped binary and held to the original by dozens of test gates, several of which execute the 1994 machine code in an emulator for comparison.

#### Sakura Dungeon

- [zngconv](https://github.com/TheGameratorT/zngconv) - Converts Sakura Dungeon ZNG images (custom container using double LZ4 compression) to PNG.
- [vfsindex](https://github.com/TheGameratorT/vfsindex) - Dumps the contents of Sakura Dungeon's VFS ~INDEX file and generates a new one from a directory.

#### Ska Studios (Salt and Sanctuary)

- [Basil & Basilica](https://github.com/operatorofthings/basil-and-basilica) - Modernized save editor for Salt and Sanctuary, built on the original "Pepper and Church" tool; inventory helper, backup manager, and skill-tree builder.

#### San Guo Ba Ye (三国霸业)

- [SanMapEditor](https://github.com/mzhinf/SanMapEditor) - Map/scenario editor for the Chinese strategy game San Guo Ba Ye (三国霸业), with Kaitai Struct (.ksy) format descriptors and binary read/write support for the game's .m/.dor/.stg map and scenario files.

#### Coffee Stain Studios (Satisfactory)

- [satisfactory-data](https://github.com/dax-dot-gay/satisfactory-data) - Rust crate and binary tool that extracts and parses Satisfactory game files.

#### SCEE London Studio

- [scee-london](https://github.com/EdnessP/scee-london) - Extracts and decrypts SCEE London Studio's PS3 package formats (.PKF/.PKD/.PKG/.PAK/.THEMES) used in SingStar, EyePet, DanceStar Party, and TV Superstars.

#### TVGS (Schedule I)

- [S1Atlas](https://github.com/madjagstudios/S1Atlas) - Local, offline developer-intelligence platform for Schedule I mod development; turns the game's compiled internals into a searchable, provenance-tracked map for modders and coding agents.
- [Schedule-1-Save-File-Editor](https://github.com/N0edL/Schedule-1-Save-File-Editor) - Save file editor for Schedule I; edits money, rank, properties, and other save data.

#### 0verflow (School Days)

- [sd_video_hook](https://github.com/hiroshil/sd_video_hook) - Fixes School Days (gEngine) video playback on modern GPUs, based on reverse engineering FILMEngine.gem's render-target/DrawPrimitiveUP pipeline; implemented as a Direct3D 9 vtable hook DLL.

#### Zyrinx (Scorcher)

- [reverse-engineering-scorcher](https://github.com/carlmartus/reverse-engineering-scorcher) - Extraction scripts for Scorcher (1996, DOS/Windows/Sega Saturn), decoding the `TAGDEN.BIN` asset archive and converting `.r0v` 15-bit images to PNG; documents additional in-house formats (`.wl3` 3D models, `.hmp` heightmaps, `.pal` palettes) not yet fully decoded. See also [saturn-sound-player](https://github.com/sozud/saturn-sound-player), which plays the Saturn version's `.MUS` songs.

#### Secrets of Grindea

- [SoG-Savegame-Editor](https://github.com/tolik518/SoG-Savegame-Editor) - C# editor for Secrets of Grindea character savegames; edits nickname, skill points, gold, equipment, inventory and pets.
  - [sog-character-editor](https://github.com/tolik518/sog-character-editor) - Stripped-down companion that only changes the character name and gender in Secrets of Grindea character savegames.

#### Sega

##### Homebrew & Audio/Video Format Tools

- [segacd-fmv-cavc](https://github.com/akiyan/segacd-fmv-cavc) - Decoder/tools for the Sega CD's Cinepak-derived CAVC full-motion-video codec used by Sega CD FMV games.
- [midi2vgm](https://github.com/akiyan/midi2vgm) - Converts MIDI files into VGM (Video Game Music) format used by Sega Genesis/Mega Drive and Sega CD sound drivers.
- [buram](https://github.com/superctr/buram) - Mega CD/Sega CD backup RAM cartridge/image management tool.
- [MDSDRV](https://github.com/superctr/MDSDRV) - Widely-used sound driver for Sega Mega Drive/Genesis homebrew, with its own MDSDRV (.mds) music data format. See also [ctrmml](https://github.com/superctr/ctrmml), its MML compiler, and [mmlgui](https://github.com/superctr/mmlgui), a GUI for composing/editing MDSDRV MML source.
- [dmf2esf](https://github.com/superctr/dmf2esf) - Converts DefleMask DMF modules to ESF files for use with the Echo Mega Drive sound driver.
- [MDPlayer](https://github.com/kuma4649/MDPlayer) - Player and emulator for Mega Drive/Genesis sound chip music formats (VGM, XGM, XGM2, ZGM).
- [mml2vgm](https://github.com/kuma4649/mml2vgm) - Compiles MML music source into Mega Drive/Genesis VGM/XGM/XGM2/ZGM sound files.
- [sms-hq-samples](https://github.com/maxim-zhao/sms-hq-samples) - Patches Sega Master System games with high-quality audio samples.
- [Dreamcast FMV Auto-Subber](https://github.com/DerekPascarella/Dreamcast-FMV-Auto-Subber) - Batch re-encodes Dreamcast SFD video files with SRT or ASS subtitle files baked in, producing new subtitled SFD videos as output.

##### Model 2 Arcade Games

- [m2me](https://github.com/belaw/m2me) - Sega Model 2 Music Extractor, extracting audio samples from Model 2 arcade sample ROMs (tested with Daytona USA).

##### Golden Axe

- [rewolf-golden-axe-explorer](https://github.com/rwfpl/rewolf-golden-axe-explorer) - Parser and viewer for the graphic resource files of the PC version of Golden Axe.

##### maimai

- [MaiConverter](https://github.com/donmai-me/MaiConverter) - Python library for reading and writing maimai chart formats.
  - Formats: Simai, Ma2, and SDT (and predecessor formats).
- [SimaiSharp](https://github.com/reflektone-games/SimaiSharp) - C# serializer/deserializer for the maimai community chart format simai.
  - See also the author's [simai.js](https://github.com/reflektone-games/simai.js) (JavaScript) and [simai-rs](https://github.com/reflektone-games/simai-rs) (Rust) ports of the same parser.
- [maidata-rs](https://github.com/xen0n/maidata-rs) - Rust library for working with `maidata.txt` files from the simai chart-authoring community.
- [ultimai-score](https://github.com/djzmo/ultimai-score) - Score format converter between simai (3simai specification) and ma2 maimai chart formats.
- [AstroDX_ChartCat](https://github.com/launchcore/AstroDX_ChartCat) - Converts charts for AstroDX (a maimai-compatible rhythm game using the `maidata.txt` community chart format) from its legacy storage structure into the newer one. See also the [Rust rewrite](https://github.com/Momoko-Ayase/AstroDX_ChartCat_rs).

##### Project DIVA

- [DSC Merger](https://github.com/jozsefsallai/dsc-merger) - Command-line utility for merging multiple Project DIVA `.dsc` script files into one, useful for patching charts exported from Comfy Studio with additional commands.
- [DIVAFILE Tool](https://github.com/s117/DIVAFILE_Tool) - Command-line tool for extracting and creating the DIVAFILE container used by Project DIVA F2 and X (PS3/PSV), documenting its header layout and AES-128-ECB encryption reverse-engineered from the game executable.
- [DIVA Mod Loader](https://github.com/blueskythlikesclouds/DivaModLoader) - File replacement mod loader for Hatsune Miku: Project DIVA Mega Mix+, used as the backend by front-ends like DIVA Mod Manager, d4m, and Rust4Diva.
- [RGTC_decompress](https://github.com/Brolijah/RGTC_decompress) - Lua module reversing the raw, header-stripped RGTC2/BC5 textures found in Project DIVA F 2nd's containers back to RGBA bitmaps, including channel swizzle control and YCbCr mipmap restoration.
- [objset](https://github.com/diva-rust-modding/objset) - Rust library with Python FFI for SEGA's `_obj.bin` model object-set format, used by Virtua Fighter 5, the VF5-based Project DIVA releases (Arcade, Dreamy Theater, F) and After Burner Climax; does not read the newer OSD format of Project DIVA F2nd and X/XHD.
- [diva_exp_gen](https://github.com/thtrandomlurker/diva_exp_gen) - Python script converting an MMD morph animation exported as CSV (from VMD) into Project DIVA DSC script expression commands.

##### Project Sekai

- [SekaiToon](https://github.com/festivities/SekaiToon) - Unity (Built-in Render Pipeline) shader replicating Project Sekai: Colorful Stage!'s in-game character shading, for datamined assets. (Archived)
- [sekai-exporter](https://github.com/StarMoe-org/sekai-exporter) - Rust exporter that converts Project SEKAI Unity asset bundles and game data tables into open formats.
  - Outputs: images, audio, video, story scenes, Live2D models, 3D costumes, virtual lives, MySekai furniture.

##### Crazy Taxi

- [Crazy Taxi Reverse Engineering](https://wretched.computer/post/crazytaxi) - Detailed retrospective series on reverse engineering the GameCube version of Crazy Taxi.
  - Formats: Archive (.all), 3D models (.shp), textures (.tex), audio (.adp).
  - **Topics**: Rendering, file formats, GameCube.
- [noclip.website (Crazy Taxi)](https://github.com/magcius/noclip.website/tree/main/src/CrazyTaxi) - In-browser Crazy Taxi viewer (GameCube).
- [Crazy Taxi Dreamcast Restoration](https://github.com/CookiePLMonster/CT-DC) - Restores removed Dreamcast exclusive content (music, licensing) to the PC version.
- [SilentPatch for Crazy Taxi](https://github.com/CookiePLMonster/SilentPatchCT) - Fixes common issues in the PC version of Crazy Taxi, including frame rate and resolution fixes.

##### Initial D

- [Initial-D-VFS-tools](https://github.com/NekoMimiOfficial/Initial-D-VFS-tools) - Extracts and repacks the virtual filesystem (VFS) used by Initial D Street Stage (PSP) and other Initial D titles, including XBB and ANA files.
- [IDCardEditor](https://github.com/Yonokid/IDCardEditor) - Web-based editor for the arcade IC card save data used by Lindbergh/RingEdge-based Initial D games.

##### Panzer Dragoon Saga

- [Azel](https://github.com/yaz0r/Azel) - Reverse engineering toolkit for Panzer Dragoon Saga (Sega Saturn), covering the game's executable and file formats.

##### Ryu Ga Gotoku Studio (Dragon Engine)

- [ParManager](https://github.com/Kaplas80/ParManager) - Tools for Yakuza series PAR archive files.
- [yk_gmd_io](https://github.com/theturboturnip/yk_gmd_io) - Import/export addon for Blender 3.2+ that allows .gmd files from the Yakuza game series to be imported/exported.
- [FighterCommander](https://github.com/HeartlessSeph/FighterCommander) - Extractor and repacker for Yakuza Dragon Engine `fighter_command.cfc` and `hact.chp` files.
- [ogre-decomp (decomp)](https://github.com/hamzaxx370/ogre-decomp) - Matching decompilation of Yakuza 1 (PS2).
- [Gibbed.Yakuza0](https://github.com/gibbed/Gibbed.Yakuza0) - Archive unpacking/packing tools for Yakuza 0 (.par archives).
- [pxdArchiverCE](https://github.com/Ret-HZ/pxdArchiverCE) - Open-source recreation of Ryu Ga Gotoku Studio's pxdArchiver tool for extracting PXD archives used in Yakuza/Like a Dragon games.
- [YAMP](https://github.com/CookiePLMonster/YAMP) - Yakuza Arcade Machine Player, letting Virtua Fighter 5: Final Showdown run on PC using the Dragon Engine files from Yakuza 6.
- [LibARMP](https://github.com/Ret-HZ/LibARMP) - Library to read and write Ryu Ga Gotoku Studio's proprietary ARMP file format.
- [Sakazuki](https://github.com/EusthEnoptEron/Sakazuki) - C# library for working with Yakuza Kiwami 2 files (and possibly other Dragon Engine entries in the series).
- [Yakuza MT Texture Creator](https://github.com/PixelIndieDev/Yakuza-MT-Texture-Creator) - Windows tool for Yakuza/Like a Dragon modders that merges up to three PNG images into the RGB channels of a single texture.
- [Unity-Yakuza-CustomImporters](https://github.com/Fronkln/Unity-Yakuza-CustomImporters) - Unity ScriptedImporter for various Yakuza/Ryu Ga Gotoku Studio formats.
- [HActLib](https://github.com/Fronkln/HActLib) - Library for reading and modifying Yakuza HAct/BEP animation-event data across engine generations (YAct in Yakuza 1-2, hact_tev.bin in Yakuza 3-4, CMN HAct in Yakuza 5-current), including the AuthEdit editing tool.
- [PIB-Library](https://github.com/Fronkln/PIB-Library) - Library to read and write Yakuza series .pib (particle) files.
- [SoundLib](https://github.com/Fronkln/SoundLib) - Library for reading the sound_def sound-definition format used in Yakuza 0 and Yakuza 5.
- [OgreCommand](https://github.com/Fronkln/OgreCommand) - Editor (Ogre Commander) for Yakuza 3 and Yakuza 4's Player Fighter Command `.ofc` files.
- [gmt_lib](https://github.com/Fronkln/gmt_lib) - Library for reading/writing Yakuza series GMT animation files; maintained continuation of mosamadeeb's archived original.
- [yakuza-gmt-blender](https://github.com/Fronkln/yakuza-gmt-blender) - Blender import/export script for Yakuza series GMT animation files, built on gmt_lib above; maintained continuation of mosamadeeb's archived original.
- [Yakuza-010-Editor-Templates](https://github.com/Fronkln/Yakuza-010-Editor-Templates) - 010 Editor templates for file formats used in the Yakuza games; extends [Ret-HZ's original template set](https://github.com/Ret-HZ/Yakuza-010-Editor-Templates).
- [reARMP](https://github.com/Ret-HZ/reARMP) (archived) - ARMP `.bin` file exporter/importer for Dragon Engine games, built on LibARMP above.
- [Lib20070319](https://github.com/Ret-HZ/Lib20070319) - Library to read/write Ryu Ga Gotoku Studio's proprietary "20070319" data-table format used across Yakuza games.
- [DungeonMaster](https://github.com/Ret-HZ/DungeonMaster) - Dungeon layout editor for Like a Dragon: Infinite Wealth's DGRF format, covering grid and room-type mechanics.
- [rELPKckr](https://github.com/Ret-HZ/rELPKckr) (archived) - ELPK archive extractor/packer for Kurohyou: Ryu Ga Gotoku Shinsho and Kurohyou 2: Ryu Ga Gotoku Ashura Hen, RGG Studio's syn Sophia-developed PSP spin-offs.
- [yagami-decryption-agency](https://github.com/mosamadeeb/yagami-decryption-agency) (archived) - Decrypts/encrypts Judgment and Lost Judgment's PC `chara.par` archives. See also [PARCrypt](https://github.com/Ret-HZ/PARCrypt), a companion PXD Archive (PARC) decryptor/encryptor built on this library.
- [kuma](https://github.com/Timo654/kuma) - Python GUI karaoke editor for Dragon Engine games (Like a Dragon/Yakuza series). Imports maps from Lost Judgment dancing, Persona Dancing, old-engine karaoke, Yakuza 5 Princess League, Ishin dancing, Zero disco, Project DIVA MegaMix+ beatmaps and Project Heartbeat JSON; exports JSON and experimental Lost Judgment dbd.
- [karaConv](https://github.com/Timo654/karaConv) - Converts karaoke song bin files between Yakuza 4/Dead Souls and Yakuza 5/Ishin/Zero/Kiwami.
- [YakuzaPythonExtractor](https://github.com/LinuxJessi/YakuzaPythonExtractor) - Pure-Python unpacker, converter and repacker for the Yakuza (PS2, SLUS-21348) disc.
  - Formats: CVM/OGREDIR volumes, AVLZ compression, textures to PNG, models to OBJ/Blender, audio to WAV, movies to MP4; writes back into a bootable ISO.

##### Shenmue

- [ShenmueDKSharp](https://github.com/Shenmue-Mods/ShenmueDKSharp) - Shenmue I & II HD Modding SDK for C#. See also [ShenmueModTools](https://github.com/Shenmue-Mods/ShenmueModTools), a GUI modding tool suite built on this library as a centralized file-format reader/writer.
- [new-yokosuka](https://github.com/brynnb/new-yokosuka) - Asset extractor and web-based model viewer for Shenmue 1 (Dreamcast).
- [Shenmunity](https://github.com/brynnb/Shenmunity) - Lets you use Shenmue assets in Unity; automatically finds the Shenmue install via Steam.
- [wudecon](https://github.com/LemonHaze420/wudecon) - Multi-purpose tool built with ShenmueDKSharp to convert/unpack a variety of file formats used in Shenmue I and Shenmue II.
- [Shenmue-Export-Tools](https://github.com/seiche/Shenmue-Export-Tools) - Tools for exporting meshes from Shenmue for Blender and Noesis.
- [ShenmueDK](https://github.com/Shenmue-Mods/ShenmueDK) - Shenmue I & II HD Modding SDK for C++, a port of ShenmueDKSharp above.
- [event_sdk](https://github.com/LemonHaze420/event_sdk) - Cross-compiler toolchain (GCC/binutils) for writing custom EV1/2/3 event scripts used by Shenmue II (Dreamcast) to drive game logic.
- [GhidraSCN3](https://github.com/LemonHaze420/GhidraSCN3) - Work-in-progress Ghidra processor module for Shenmue's Scenario Script v3 (`.d3t`) bytecode format.
- [S3TextDataAssetEditor](https://github.com/LemonHaze420/S3TextDataAssetEditor) - CLI utility to extract and modify strings inside S3TextDataAsset files from Shenmue III.
- [IMGExtractor](https://github.com/LemonHaze420/IMGExtractor) - Extracts IMG/IDX archive files found only in "What's Shenmue" prototype builds (not seen in released Shenmue I/II builds).
- [ShenmueHDTools](https://github.com/derplayer/ShenmueHDTools) - Modding and tweak tools for the Shenmue I & II HD release, unpacking, editing, and exporting .tad/.tac files.
- [DTPKUtil](https://github.com/Shenmue-Mods/DTPKUtil) - Extracts and decompresses samples from Dreamcast AM2 DTPK `.SND` audio files used in Shenmue, converting ADPCM to PCM and expanding decompressed `.SND` files for playback in the 2018 HD ports.
- [shenmue-translation-pack](https://github.com/sizious/shenmue-translation-pack) - Mirror of the original Pascal/Delphi Shenmue Translation Pack, a toolset for translating What's Shenmue (DC), Shenmue (DC) and Shenmue 2 (DC/Xbox).
- [pvrx2png](https://github.com/sizious/pvrx2png) - Converts PVR-X texture images used by some original Xbox games (e.g. Shenmue II) to PNG; supports GBIX/PVR-X, plain PVR-X and DDS variants.

##### Phantasy Star

- [PSO2-Aqua-Library](https://github.com/Shadowth117/PSO2-Aqua-Library) - Library for handling Phantasy Star Online 2 Aqua formats, with a focus on models. Functional in grabbing model data from the game's format.
- [Phantasy-Star-Online-2-Model-Tools](https://github.com/Shadowth117/Phantasy-Star-Online-2-Model-Tools) - Tools for handling PSO2 model and texture formats.
- [PSO2-Salon-Tool](https://github.com/Shadowth117/PSO2-Salon-Tool) - Program to edit and convert between Phantasy Star Online 2 .xxp and .cml files.
- [FpkTool](https://github.com/Shadowth117/FpkTool) - Unpacks and repacks Phantasy Star Online 2 FPK archives (pre NGS).
- [PSO2 Tools](https://github.com/dummycount/blender_pso2_tools) - Blender add-on for Phantasy Star Online 2 assets (`.aqp`, `.aqn`, ICE archives). Features model search, archive browsing, and automatic texture assignment.
- [Aqua-Toolset](https://github.com/Shadowth117/Aqua-Toolset) - Toolkit primarily for Phantasy Star Online 2 file formats.
- [PSO2Downloader](https://github.com/Shadowth117/PSO2Downloader) - Official patch downloader for Phantasy Star Online 2.
- [PSOBMLExtract](https://github.com/Shadowth117/PSOBMLExtract) - Tool to extract and repack PSO .bml and .gsl files using PRS compression.
- [PigPSO2Cam](https://github.com/Lapig/PigPSO2Cam) - Camera/FOV tool for PSO2 NGS (JP+NA).
- [NgsPacker](https://github.com/logue/NgsPacker) - Pack and Unpack tool for PSO2 New Genesis (NGS) archives.
- [PSO2-CRID-Player](https://github.com/zmbkilla/PSO2-CRID-Player) - Tool to play CRIware audio files from PSO2.
  - [PSO2USMHandler](https://github.com/zmbkilla/PSO2USMHandler) - C# DLL library for decoding PSO2 and NGS USM video files (USM demuxing via GI-cutscenes, decoding via FFmpeg.Autogen), with a WPF test app.
- [phantasmal-world](https://github.com/DaanVandenBosch/phantasmal-world) - Web-based suite of tools for PSO.
  - Features: Model viewer, quest editor, floor viewer, and proxy server.
- [pso-blender](https://github.com/jtuu/pso-blender) - Blender plugin for Phantasy Star Online Blue Burst (PSOBB).
- [pso-pac](https://github.com/jtuu/pso-pac) - Extract and create .pac files for PSO.
- [gasetools](https://github.com/essen/gasetools) - Original set of command-line tools to manipulate SEGA game file formats, including Phantasy Star Universe.
- [gasetoolsWin](https://github.com/Shadowth117/gasetoolsWin) - Windows port of essen/gasetools, rebuilt with Visual Studio for easy Windows builds.
- [tenora-works](https://github.com/Agrathejagged/tenora-works) - PSULib and PSU Generic Parser for Phantasy Star Universe.
- [PSO2 CLI Tools](https://github.com/dummycount/Pso2Cli) (archived) - Command-line tools for parsing and editing Phantasy Star Online 2 game data files (character making index, color channels, game formats).
- [newserv](https://github.com/fuzziqersoftware/newserv) - Game server, proxy, and reverse-engineering tool for Phantasy Star Online (PC, GameCube, Blue Burst, Episode 3). Handles quest files, client patch files, item tables, and GameCube DOL binaries.
- [rust-ages-prs](https://github.com/HybridEidolon/rust-ages-prs) - PRS compression/decompression library for Rust, used across SEGA game formats including Phantasy Star Online.
- [yaqp](https://github.com/jtuu/yaqp) - Phantasy Star Online Blue Burst (PSOBB) quest file (.qst) parser with a disassembler; dumps binary quest data and outputs enemy counts as JSON.
- [psobbaddonplugin](https://github.com/HybridEidolon/psobbaddonplugin) - Plugin enabling graphical UI addons for Phantasy Star Online Blue Burst.
  - Addons built on it: [PSOBBMod-Addons](https://github.com/Solybum/PSOBBMod-Addons) and [psobb-dropbox-tracker](https://github.com/X9Z0-M2/psobb-dropbox-tracker) (shows drop contents and on-screen location).
- [Blue-Burst-Patch-Project](https://github.com/Solybum/Blue-Burst-Patch-Project) - Collection of client patches for Phantasy Star Online Blue Burst.
- [PSO-Tools](https://github.com/Solybum/PSO-Tools) - Phantasy Star Online tool collection, including PSOCT, a console `unitxt` text editor with Dreamcast, GameCube, and Xbox variants and JSON support, multi-language `unitxt` JSON dumps, and a link to the author's [PRS](https://github.com/Solybum/PRS) compression library.
- [rust-ages-ice-archive](https://github.com/HybridEidolon/rust-ages-ice-archive) - Rust library (with CLI utilities `agesice`/`agesdeice`) for loading and writing ICE archives, the asset storage format used by Phantasy Star Online 2.
- [PSO2_SymbolArt_ThumbnailHandler](https://github.com/usagirei/PSO2_SymbolArt_ThumbnailHandler) - Windows Explorer shell extension that renders thumbnails and previews for Phantasy Star Online 2 SymbolArt (.sar) files.
- [psrp](https://github.com/maxim-zhao/psrp) - Phantasy Star Retranslation Project.
- [prsutil](https://github.com/essen/prsutil) - Archive of fuzziqer's original PRS compression/decompression tool (C), the reference implementation behind later PRS ports (prs.net, rust-ages-prs). PRS is used in numerous SEGA games since the Saturn, including Phantasy Star Universe's .nbl format.
- [pso-character-editor](https://github.com/decswxaqz/pso-character-editor) - Online JavaScript character editor for Phantasy Star Online.
- [PStarSaveEditor](https://github.com/Fuindin/PStarSaveEditor) - Windows Forms save state editor for Phantasy Star, Phantasy Star 2, Phantasy Star 3, and Phantasy Star 4 (Sega Master System/Genesis).
- [Zipper](https://github.com/Shadowth117/Zipper) - Decryptor/decompressor for Phantasy Star Zero's (Nintendo DS) ZPR format, with .narc/.zarc extraction support.

##### Sonic Team (Hedgehog Engine)

###### Decompilations & Reconstructions

- [Sonic-1-2-2013-Decompilation (decomp)](https://github.com/RSDKModding/RSDKv4-Decompilation) - Matching decompilation of Sonic 1 & 2 (2013 mobile) and Retro Engine v4.
- [Sonic-CD-11-Decompilation (decomp)](https://github.com/RSDKModding/RSDKv3-Decompilation) - Matching decompilation of Sonic CD (2011 mobile) and Retro Engine v3.
- [sa1 (decomp)](https://github.com/SAT-R/sa1) (archived) - Matching decompilation of Sonic Advance (GBA, Europe).
- [sa2 (decomp)](https://github.com/SAT-R/sa2) - Matching decompilation of Sonic Advance 2 (GBA).
- [sa3 (decomp)](https://github.com/SAT-R/sa3) - Matching decompilation of Sonic Advance 3 (GBA).
- [SA-Trilogy-Animation-Exporter](https://github.com/JaceCear/SA-Trilogy-Animation-Exporter) - Extracts animation data from Sonic Advance 1-3 ROMs.
- [tiled-advance](https://github.com/MainMemory/tiled-advance) - Tiled map editor projects for the Sonic Advance games (GBA) that load data from a supplied ROM file (US ROMs).
- [Sonic-Mania-Decompilation (decomp)](https://github.com/RSDKModding/Sonic-Mania-Decompilation) - Matching decompilation of Sonic Mania (2017).
- [RunnersDecomp (decomp)](https://github.com/itsmattkc/RunnersDecomp) - Matching decompilation of Sonic Runners.
- [SonicRushAdventure-Decomp (decomp)](https://github.com/RushRE/SonicRushAdventure-Decomp) - Matching decompilation of Sonic Rush Adventure.
- [UnleashedRecomp](https://github.com/hedge-dev/UnleashedRecomp) - Unofficial PC port of the Xbox 360 version of Sonic Unleashed created through static recompilation.
- [OpenLW](https://github.com/Radfordhound/OpenLW) - Open-source recreation of Sonic Lost World for Wii U/PC, built from Ghidra decompilations of both versions and reading the original CRIWARE/Havok-formatted game assets; also hosts the LWAPI DLL-modding library.
- [re-Sonic06Demo](https://github.com/PranchaD/re-Sonic06Demo) - Static recompilation of the Sonic the Hedgehog (2006) demo (Xbox 360) built on the ReXGlue SDK, running from the demo's extracted package files.
- [MarathonRecomp](https://github.com/sonicnext-dev/MarathonRecomp) - Unofficial PC port of the Xbox 360 version of Sonic the Hedgehog (2006) created through static recompilation (via the companion XenonRecomp/XenosRecomp tools); requires original game files (`.xex`, `.ar.00`, `.arl`, and others) to install.
- [Sonic 3 A.I.R.](https://github.com/Eukaryot/sonic3air) - Reconstruction of Sonic 3 & Knuckles from the original Genesis ROM, extracting sprites, audio, and level data via decompilation-adjacent ROM analysis.
- [RSDKv5-Decompilation](https://github.com/RSDKModding/RSDKv5-Decompilation) - Complete decompilation of Retro Engine v5/v5Ultimate (used by Sonic Mania and other games). See also [SaturnSH2x2's fork](https://github.com/SaturnSH2x2/RSDKv5-Decompilation) with a built-in mod loader/API (save file redirection, XML asset loading), shader compiler, and extra backends.
- [sonicriders](https://github.com/doldecomp/sonicriders) - WIP decompilation of Sonic Riders (USA) with original DOL file reconstruction. See also [Riders.Tweakbox](https://github.com/Sewer56/Riders.Tweakbox), a discontinued all-in-one mod adding online multiplayer, widescreen, and controller support to the PC version.
- [RunnersAssetBundleDecomp](https://github.com/itsmattkc/RunnersAssetBundleDecomp) - Decompilation of Sonic Runners' Unity AssetBundles, companion to RunnersDecomp for restoring the game's client-delivered assets.
- [s1disasm](https://github.com/sonicretro/s1disasm) - Disassembly of Sonic the Hedgehog (1991, Sega Genesis/Mega Drive).
- [s2disasm](https://github.com/sonicretro/s2disasm) - Disassembly of Sonic the Hedgehog 2 (1992, Sega Genesis/Mega Drive).
- [stfdecomp](https://github.com/biggestsonicfan/stfdecomp) - Decompilation attempt of Sonic the Fighters (arcade).
- [RSDKv2-Decompilation](https://github.com/RSDKModding/RSDKv2-Decompilation) - Decompilation of the 2008 Retro Engine v2 demo of Sonic Nexus.
- [RSDKv3-Script-Decompilation](https://github.com/RSDKModding/RSDKv3-Script-Decompilation) - Decompilation of Retro Engine v3 (Sonic CD) scripts.
- [RSDKv4-Script-Decompilation](https://github.com/RSDKModding/RSDKv4-Script-Decompilation) - Decompilation of Retro Engine v4 scripts, covering Sonic 1 & 2 (2013 mobile) and Sonic CD (Sega Classics release).
- [CD-Proto-Diffs](https://github.com/RSDKModding/CD-Proto-Diffs) (archived) - Ghidra-diff analysis documenting binary changes across a sequence of leaked Sonic CD (2011 mobile) prototype builds.
- [RSonic3D-Decompilation](https://github.com/RSDKModding/RSonic3D-Decompilation) - Decompilation of *Retro-Sonic 3D: Sky Worlds* (2005), an early Retro Engine tech demo fan game; requires original assets and adds a mod loader plus an OpenGL/SDL renderer replacing the original DirectX 7 code.
- [SoniCPort](https://github.com/cuckydev/SoniCPort) - C port of Sonic the Hedgehog (1991, Sega Genesis/Mega Drive), built on the s1disasm disassembly.
- [stfdisasm](https://github.com/biggestsonicfan/stfdisasm) - Disassembly of Sonic the Fighters (arcade), the basis for the stfdecomp decompilation attempt above.
- [SonicCD-WindowsPhone-Decompilation (decomp)](https://github.com/tge-was-taken/SonicCD-WindowsPhone-Decompilation) - Decompilation and PC port of the Windows Phone version of Sonic CD (archived).
- [s2smsdisasm](https://github.com/sonicretro/s2smsdisasm) - Disassembly of Sonic the Hedgehog 2 (1992, Sega Master System).
- [Sonic-1-Prototype](https://github.com/Mega-Drive-Developers-Collective/Sonic-1-Prototype) - Research disassembly of the Sonic 1 (Genesis) prototype released by Hidden Palace in 2020.
- [skdisasm](https://github.com/sonicretro/skdisasm) - Disassembly of Sonic & Knuckles (Sega Genesis/Mega Drive).
- [scddisasm](https://github.com/sonicretro/scddisasm) - Incomplete disassembly of Sonic CD (Sega CD) that builds a working ISO when the remaining original files are supplied; covers the main and system programs, SMPS Z80 sound driver and SMPS-PCM banks, title screen, special stage, FMVs, and a couple of levels.
- [s3ddisasm](https://github.com/sonicretro/s3ddisasm) - Disassembly of Sonic 3D Blast (Sega Genesis/Mega Drive) as IDA64 database IDC dumps, with the SMPS sound driver source.
- [sonic2mod](https://github.com/djyt/sonic2mod) - Converts SMPS Sonic music files to Amiga MOD format.
- [smps-rips](https://github.com/sonicretro/smps-rips) - Raw SMPS sound driver data ripped from Sega Genesis/Mega Drive games.

- [SR2Wii](https://github.com/bluisblu/SR2Wii) - Decompilation of the Wii prototype build of Sonic Riders: Zero Gravity.
- [SonicBattleDecomp](https://github.com/cypressru/SonicBattleDecomp) - Matching decompilation of Sonic Battle (GBA).
- [sbhs](https://github.com/phase/sbhs) - Sonic Battle Hack Suite: GUI program for reverse engineering and patching Sonic Battle (GBA).
- [SR2 (PS2 prototype)](https://github.com/KidWizardOfTheWeb/SR2) - Decompilation of the PS2 prototype build of Sonic Riders: Zero Gravity, distinct from the Wii prototype decompilation (SR2Wii) above.
- [sonicriderste](https://github.com/RidersBoulevard/sonicriderste) - Disassembly and decompilation of Sonic Riders: Tournament Edition.
- [Sewer56.Patcher.Riders](https://github.com/Sewer56/Sewer56.Patcher.Riders) - Extensible GameCube/Wii ROM patcher originally built for the Riders Regravitified conversion project, also supporting SRDX and SRTE (Sonic Riders: Tournament Edition) conversion modes.
- [sonic_riders_lzss](https://github.com/romhack/sonic_riders_lzss) - LZSS compression tool for Sonic Riders games.

###### Retro Engine (RSDK)

- [RetroED](https://github.com/RSDKModding/RetroED) - All-in-one editor suite for Retro Engine (RSDKv1 through v5U) games, covering scenes, tilesets, animations, palettes, gameconfigs, models, and scripts. "v2.0" successor to [Rubberduckycooly's original RetroED](https://github.com/Rubberduckycooly/RetroED).
  - Tools: Scene Editor, Animation Editor, GameConfig Editor, Palette Editor, Model Manager, Script Compiler, GFX Manager, UserDB Manager, RSV Manager.
  - See also [RSDK-Export-CLI](https://github.com/RSDKModding/RSDK-Export-CLI), a companion CLI for exporting Retro Engine file data to common formats, and [S3KOEditorLink](https://github.com/RSDKModding/S3KOEditorLink), which loads Sonic 3 & Knuckles data from Sonic Origins into RetroED-compatible editors.
- [SonicMania-SaveEditor](https://github.com/Erik-JS/SonicMania-SaveEditor) - Save editor for Sonic Mania.
- [SonLVL-RSDK](https://github.com/Lavesiime/SonLVL-RSDK) - Level editor for RSDK v3/v4 games (Sonic CD, Sonic 1, Sonic 2).
- [RSDK-Reverse](https://github.com/Rubberduckycooly/RSDK-Reverse) - Reverse engineering tools for Retro Engine games (Sonic CD, Sonic 1, Sonic 2).
- [rsdkv6-extract](https://github.com/RSDKModding/rsdkv6-extract) - Extractor for RSDK v6 format files.
- [Retro-Engine-Animation-Editor](https://github.com/Rubberduckycooly/Retro-Engine-Animation-Editor) - Animation file editor for every Retro Engine/Retro Sonic Engine game.
- [ModelManiac](https://github.com/Rubberduckycooly/ModelManiac) - Importer/exporter for RSDK model formats.
- [PDN-RSDK-GFX-Plugin](https://github.com/Rubberduckycooly/PDN-RSDK-GFX-Plugin) - Paint.NET plugin for direct editing of RSDK `.gfx` files.
- [ConfigManiac](https://github.com/Rubberduckycooly/ConfigManiac) - Editor for RSDKv5 Config files.
- [Tile-Maniac](https://github.com/Rubberduckycooly/Tile-Maniac) - RSDKv5 collision editor.
- [ObjectTypeFixer](https://github.com/Rubberduckycooly/ObjectTypeFixer) - Re-aligns RSDK object types when a gameconfig's object count has changed.
- [Sonic-1-2-Save-Editor](https://github.com/Rubberduckycooly/Sonic-1-2-Save-Editor) - Save file editor for the Retro Engine Sonic 1 & 2 Remasters.
- [SonicCD-SaveEditor](https://github.com/Rubberduckycooly/SonicCD-SaveEditor) - Save file editor for Sonic CD (2011).
- [RSDK](https://github.com/Xeeynamo/RSDK) - Reverse engineering of the Retro Engine RSDK format, including a Sonic Mania animation editor.
  - See also [vscode-rsdk](https://github.com/RSDKModding/vscode-rsdk), a Visual Studio Code extension providing syntax highlighting for decompiled RSDK (RetroScript) script files; forked and actively maintained from [Xeeynamo's original](https://github.com/Xeeynamo/vscode-rsdk).
- [rsdkv5_extract](https://github.com/koolkdev/rsdkv5_extract) - Extraction/packing tools for Sonic Mania's RSDK v5 archive format, plus MDL (3D model), SPR (sprite info), and SCN (scenario/scene) sub-formats.
- [ManiacEditor](https://github.com/koolkdev/ManiacEditor) - Scene editor for Sonic Mania, reading and writing RSDK scene/tileset formats.
- [ManiaBSEdit](https://github.com/sonicretro/ManiaBSEdit) - Blue Spheres bonus stage editor for Sonic Mania, opening `Scene*.bin` files through the RSDKv5 library.
- [ManiaPal](https://github.com/thesupersonic16/ManiaPal) - Palette editor for Sonic Mania with extensions for `GameConfig.bin`/`StageConfig.bin`, the Player, ChaosEmerald and UIBackground object `.bin` files, `.pal` palettes and Adobe Color Table (`.act`) files.

- [spindisasm](https://github.com/sonicretro/spindisasm) - Disassembly of Sonic Spinball (Sega Genesis/Mega Drive).
- [chaotix](https://github.com/sonicretro/chaotix) - Disassembly and toolkit for Knuckles' Chaotix (32X).
- [ristar](https://github.com/sonicretro/ristar) - Disassembly of Ristar (Sega Genesis/Mega Drive).

###### Sonic Adventure

- [SCHG:Sonic_Adventure](https://info.sonicretro.org/SCHG:Sonic_Adventure) - Sonic Community Hacking Guide documentation for Sonic Adventure.
- [sadtools](https://github.com/FraGag/sadtools) (archived) - Command-line tools for Sonic Adventure file formats.
- [sa_tools](https://github.com/X-Hax/sa_tools) - Modding toolkit for Sonic Adventure series. Supports Sonic Adventure DX (SADX) and Sonic Adventure 2 PC (SA2PC).
  - Companion repo [sa_tools_research](https://github.com/X-Hax/sa_tools_research): command-line tools moved out of SA Tools for advanced users, including MLTExtract, RecreatePVM, GBIXScan, njConvert and SoundBankEditor.
  - [SACompGC](https://github.com/X-Hax/SACompGC): Decompressor library/CLI for the `SaCompGC`-headed `.rel` files of the GameCube version of Sonic Adventure DX.
- [sadx-mod-loader](https://github.com/X-Hax/sadx-mod-loader) - Sonic Adventure DX PC mod loader, patching the game at runtime to load community mods from loose files.
- [SonicAdventureBlenderIO](https://github.com/X-Hax/SonicAdventureBlenderIO) - Blender 4.0+ add-on for exporting Sonic Adventure 1 & 2 3D formats.
  - Formats: .nj, .gj, .njm, .nja.
- [Sonic Retro (SA2 Hacking Guide)](https://info.sonicretro.org/SCHG:Sonic_Adventure_2) - Sonic Hacking Guide for Sonic Adventure 2.
- [Sonic-Adventure-Animation-.JSON-Input-Output](https://github.com/Shadowth117/Sonic-Adventure-Animation-.JSON-Input-Output) - Imports and exports Sonic Adventure, Sonic Adventure DX, Sonic Adventure 2, and Sonic Adventure 2 Battle animations extracted with SA Tools into and out of 3ds Max.
- [SA3D.Modeling](https://github.com/X-Hax/SA3D.Modeling) - .NET library for handling Sonic Adventure/Sonic Adventure 2 model and animation data.
  - Companion libraries: [SA3D.Archival](https://github.com/X-Hax/SA3D.Archival) (PRS, PAK, PVM/PVR/PVP, GVM/GVR/GVP and PVMX/PVRX archive and texture reader/writer), [SA3D.Modeling.Convert](https://github.com/X-Hax/SA3D.Modeling.Convert) (converts SA3D.Modeling data between formats and to an intermediate format), [SA3D.Texturing](https://github.com/X-Hax/SA3D.Texturing) (texture handler) and [SA3D.SA2Event](https://github.com/X-Hax/SA3D.SA2Event) (SA2 event data handler).
  - [SA3DEditor](https://github.com/X-Hax/SA3DEditor): Work-in-progress SA3D model, level and animation viewer/editor loading all Sonic Adventure model formats, intended to replace SAMDL and SALVL.
  - [SA3DFileCartographer](https://github.com/X-Hax/SA3DFileCartographer): Command-line tool that maps which bytes of model, level, animation and SA2 event files belong to which structure type and exports the result as a colored image.
- [ChaoConvert](https://github.com/TheGag96/ChaoConvert) - Converts Fusion's Chao Editor .chao files exported from the GameCube version of Sonic Adventure 2 Battle so they work on the PC version, byte-swapping the affected fields.

###### Sonic Heroes & Shadow

- [HeroesPowerPlant](https://github.com/igorseabra4/HeroesPowerPlant) - Full-featured level editor for Sonic Heroes and Shadow the Hedgehog.
- [Renderware-.anm-IO-Tool](https://github.com/Shadowth117/Renderware-.anm-IO-Tool) - Tool for importing and exporting RenderWare .anm animation files into and out of 3ds Max.
- [rwio](https://github.com/Shadowth117/rwio) - 3ds Max plugin for importing and exporting RenderWare models and animations.
- [Blender-3D-STH-Mtn-plugin](https://github.com/Psycrow101/Blender-3D-STH-Mtn-plugin) - Blender animation plugin for Shadow the Hedgehog (STH) mountain files (.mtn).
- [Heroes.SDK](https://github.com/Heroes-Hacking-Central/Heroes.SDK) - Unified library for manipulating Sonic Heroes at runtime and definitions for internal data structures and functions. Includes format parsers for creating/extracting various game formats.
- [HeroesCollisionTool](https://github.com/igorseabra4/HeroesCollisionTool) - Collision tool for Sonic Heroes.
  - [Heroes-Collision-Library](https://github.com/Sewer56/Heroes-Collision-Library): .NET library for generating Sonic Heroes collision files from a vertex and triangle list or Wavefront OBJ, with a simple importer/exporter example tool.
- [HeroesVisibilityEditor](https://github.com/igorseabra4/HeroesVisibilityEditor) - Visibility editor for Sonic Heroes.
- [HeroesSPLTool](https://github.com/igorseabra4/HeroesSPLTool) - RenderWare Spline (`.SPL`) converter for Sonic Heroes.
- [HeroesTweaker](https://github.com/igorseabra4/HeroesTweaker) - EXE editor for Sonic Heroes. Legacy tool, but useful for extracting splines from the executable.
- [ShadowSETIDTBLEditor](https://github.com/igorseabra4/ShadowSETIDTBLEditor) - SET ID Table editor for Shadow the Hedgehog.
- [ShadowSplineTool](https://github.com/igorseabra4/ShadowSplineTool) - Extracts `.PTP` splines from Shadow the Hedgehog.
- [HeroesONE-R](https://github.com/Heroes-Hacking-Central/HeroesONE-R) - C# library for reading and writing .ONE archive files from Sonic Heroes and Shadow the Hedgehog.
  - [HeroesONE-Reloaded](https://github.com/Sewer56/HeroesONE-Reloaded) (archived): Rewrite of HeroesONE with a C# library and GUI for parsing, modifying and saving `.ONE` archives from Sonic Heroes and Shadow the Hedgehog. Succeeded by [ShadowONE](https://github.com/ShadowTheHedgehogHacking/ShadowONE), a cross-platform `.ONE` editor with search/filter, in-archive file moves and compression metadata display.
- [Heroes-Disassembly](https://github.com/Heroes-Hacking-Central/Heroes-Disassembly) - Community-maintained IDA disassembly of Sonic Heroes.
- [Blender-3D-SH-Dma-plugin](https://github.com/Psycrow101/Blender-3D-SH-Dma-plugin) - Blender plugin to import and export Sonic Heroes Delta Morph animation (.dma) files.
- [prs-rs](https://github.com/Sewer56/prs-rs) - Fast compressor/decompressor for the Sega PRS compression scheme used by Sonic Heroes and other Sega titles.
  - [dlang-prs](https://github.com/Sewer56/dlang-prs) (archived): Earlier D-language PRS compressor/decompressor with a C# wrapper, superseded by prs-rs.
- [HeroesLayoutEditor](https://github.com/igorseabra4/HeroesLayoutEditor) - Layout editor for Sonic Heroes.
- [HeroesModelTool](https://github.com/igorseabra4/HeroesModelTool) - BSP model file importer/exporter for Sonic Heroes.
- [HeroesCameraEditor](https://github.com/igorseabra4/HeroesCameraEditor) - Camera editor for Sonic Heroes.
- [HeroesSETIDTBLEditor](https://github.com/igorseabra4/HeroesSETIDTBLEditor) - SET ID Table editor for Sonic Heroes.
- [PACTool](https://github.com/Sewer56/PACTool) - Library and front-end for archiving and unarchiving `.PAC` archives in the PC and Xbox versions of Sonic Heroes and Shadow the Hedgehog.
- [Heroes.Hint.Editor](https://github.com/Sewer56/Heroes.Hint.Editor) - Message editor for Sonic Heroes hint and talk-trigger text (`hint001e.bin` and similar), with filtering and English, French, German, Italian and Spanish ANSI text support.
- [rail-canyon](https://github.com/DeadlyFugu/rail-canyon) - Level viewer/editor for Sonic Heroes.
- [ShadowMTP](https://github.com/Sewer56/ShadowMTP) - Unpacks and repacks Shadow the Hedgehog `.MTP` motion package animation archives.
- [HeroesPS2BetaToolkit](https://github.com/Sewer56/HeroesPS2BetaToolkit) - Scripts and notes for working with the PS2 Sonic Heroes 2nd of October prototype, with a workflow for extracted ISO, CVM, `.ONE` and `.AFS` contents.
- [ShadowCollisionTool](https://github.com/igorseabra4/ShadowCollisionTool) - BSP collision importer/exporter for Shadow the Hedgehog.
- [sonicheroes](https://github.com/Jovinull/sonicheroes) - WIP matching decompilation of Sonic Heroes (GameCube), complementing the community disassembly above.

###### Sonic Riders

- [SonicRiders.Index](https://github.com/Sewer56/SonicRiders.Index) - Work-in-progress community wiki for modding the PC version of Sonic Riders, documenting file formats and other resources ([online version](https://sewer56.dev/SonicRiders.Index/)).
- [srdx-gear-format](https://github.com/Sewer56/srdx-gear-format) - Packer/unpacker for Sonic Riders DX 2.0 Extreme Gear archives, with an 010 Editor template (`srdx-gear.bt`) specifying the format.

###### Classic & Handheld Sonic

- [BBSonicDSTool](https://github.com/efimandreev0/BBSonicDSTool) - Tool for Sonic DS file formats.
- [blue-sphere](https://github.com/scurest/blue-sphere) - Tool for Sonic 3 & Knuckles special stage files.
- [S3KSE](https://github.com/Xeeynamo/S3KSE) - Save editor for the PC Sonic & Knuckles Collection, editing Sonic 3 & Knuckles and Sonic the Hedgehog 3 save slots (emeralds, lives, continues, zones) and toggling options such as debug mode and the frame counter.
- [sonic-rush-tools](https://github.com/BLiNXthetimesweeperGOD/sonic-rush-tools) - Map ripper for the Sonic Rush series (Nintendo DS), extracting and decompressing NARC-packed level map data from ROMs and converting it to image files.
- [mdcomp](https://github.com/flamewing/mdcomp) - Compressors and decompressors for the assorted compression formats used by Sega Mega Drive games (Kosinski, Nemesis, Enigma, Saxman, and more).
- [SMPSPlay](https://github.com/ValleyBell/SMPSPlay) - Player for SMPS files, the sound driver format commonly used in Sega Mega Drive games. See also [SMPSPlay-DLL](https://github.com/sonicretro/SMPSPlay-DLL), a library for playing SMPS music from Mega Drive Sonic games.
- [libsonassmd](https://github.com/Clownacy/libsonassmd) - Library for reading and writing the assets of Mega Drive Sonic the Hedgehog games.
- [ClownMapEd](https://github.com/Clownacy/ClownMapEd) - Portable clone of Xenowhirl's SonMapEd, a sprite editor for Mega Drive Sonic games.
- [STH1EDWV](https://github.com/zeroKilo/STH1EDWV) - ROM editor for Sonic the Hedgehog (Sega Master System) for editing levels and related data.
- [tales](https://github.com/suppertails66/tales) - Qt-based level editor suite for Tails Adventures, with a manual included.
- [CaptainPlaneEd](https://github.com/Clownacy/CaptainPlaneEd) - Enhanced SDL2 port of PlaneEd, a classic Sonic level/plane-map editor.
- [s2ssedit](https://github.com/flamewing/s2ssedit) - Editor for Sonic 2 Special Stage data.
- [SoniConverter](https://github.com/sonicretro/SoniConverter) - Converts object and ring layout data between Sonic 1 and Sonic 3 & Knuckles formats in both directions, with optional conversion of known objects and splitting or packing of ring strings.
- [mdtools](https://github.com/flamewing/mdtools) - Suite of Mega Drive format tools: plane-map converter, art-chunk splitter/census, SMPS-to-assembly converter, FM voice-bank dumper, and special-stage expander.
- [FW-KENSC-ShellExt](https://github.com/MainMemory/FW-KENSC-ShellExt) - Windows shell extension exposing flamewing's mdcomp Mega Drive compression codecs (Kosinski, Nemesis, and more) for right-click compress/decompress.
- [KENSSharp](https://github.com/sonicretro/KENSSharp) - C# port of KENS: compression and decompression library for Kosinski, Kosinski+, Nemesis, Enigma, Saxman, and Comper, with a GUI front end and a Windows shell extension.
- [clownnemesis](https://github.com/Clownacy/clownnemesis) - Compressor and decompressor library and executable (ANSI C) for the Nemesis format, with Shannon-Fano mode matching Sega's original compressor output and a Huffman mode for smaller files.
- [SonicCPTDecryptor](https://github.com/Nenkai/SonicCPTDecryptor) - Decrypts .CPT files from Sonic Mega Collection Plus.
- [SonicTheHedgehogRecomp](https://github.com/mstan/SonicTheHedgehogRecomp) - Native x64 static recompilation of Sonic the Hedgehog (Genesis).
- [SonicTheHedgehog2Recomp](https://github.com/mstan/SonicTheHedgehog2Recomp) - Static recompilation of Sonic the Hedgehog 2 (Genesis) into native code.
- [Sonic3AndKnucklesRecomp](https://github.com/mstan/Sonic3AndKnucklesRecomp) - Native x64 static recompilation of Sonic the Hedgehog 3 and Sonic & Knuckles (Genesis).
- [SonicTheHedgehogSMSRecomp](https://github.com/mstan/SonicTheHedgehogSMSRecomp) - Static recompilation of Sonic the Hedgehog (Sega Master System, 1991) into native code.
- [SonicBlastGGRecomp](https://github.com/mstan/SonicBlastGGRecomp) - Static recompilation of Sonic Blast (Sega Game Gear, 1996) into native code.

###### Modern Hedgehog Engine & Mod Managers

See also: [Hedgehog Engine](engines.md#hedgehog-engine) under Engines, including HedgeLib and other engine-wide libraries.

- [Sonic-Colors-Set-Editor](https://github.com/thesupersonic16/Sonic-Colors-Set-Editor) - Set editor for Sonic Colors.
- [Glitter](https://github.com/crash5band/Glitter) - Format library and editor application to open, modify, and resave GTE/GTM particle files for Sonic Generations.
- [libgens-sonicglvl](https://github.com/DarioSamo/libgens-sonicglvl) - Level editor and formats library for the PC version of Sonic Generations; parses and edits .GEN level format files.
- [ModelConverter](https://github.com/blueskythlikesclouds/ModelConverter) - Converts 3D model files (e.g. FBX) to and from Hedgehog Engine `.model` formats for Sonic Unleashed, Generations, Lost World, Forces, and Frontiers/Shadow Generations.
- [Marathon](https://github.com/hyperbx/Marathon) - Toolkit and library for Sonic The Hedgehog file formats.
- [noclip.website (Sonic Colors)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Sonic Colors viewer.
- [AllStarsRacingTools](https://github.com/tge-was-taken/AllStarsRacingTools) - Unfinished tools for Sonic & Sega All Stars Racing. Incomplete and mostly for reference purposes.
- [Shuriken](https://github.com/crash5band/Shuriken) - XNCP/YNCP UI Editor for Sonic games.
- [mst06](https://github.com/GerbilSoft/mst06) - Sonic '06 MST string table file format converter supporting XML and MST formats for game localization data.
- [Sonic '06 Randomiser Suite](https://github.com/Knuxfan24/Sonic-06-Randomiser-Suite) - Software suite for randomizing game elements in Sonic '06 (Xbox 360, PS3).
- [Sonic Next Mod Manager](https://github.com/hyperbx/SonicNextModManager) - Mod manager for Sonic games with game file format and asset management.
- [Hedge Mod Manager](https://github.com/thesupersonic16/HedgeModManager) - Mod manager for Hedgehog Engine PC games (Sonic Generations, Lost World, Forces, Colours Ultimate, Origins). See also [Hedge Mod Manager 8](https://github.com/hedge-dev/HedgeModManager), an in-development multiplatform rewrite adding Linux/Steam Deck support and further games (Puyo Puyo Tetris 2, Olympic Games Tokyo 2020).
- [HedgeMatEdit](https://github.com/hedge-dev/HedgeMatEdit) - Material editor for Hedgehog Engine Sonic games.
- [HMMCodes](https://github.com/hedge-dev/HMMCodes) - Hedge Mod Manager community codes and tools for Sonic game modding and file format work.
- [Converse](https://github.com/NextinMono/converse) - Editor for .fco (Font Converse) files from Sonic Unleashed.
- [kunai](https://github.com/NextinMono/kunai) - Editor for Ninja CSD Project files (XNCP, YNCP, GNCP) used by Sonic games.
- [SharpNeedle](https://github.com/hedge-dev/SharpNeedle) - Format library for Hedgehog Engine, covering models, animations, and other game data.
- [libHSON-csharp](https://github.com/hedge-dev/libHSON-csharp) - C# serialization library for the Hedgehog Set Object Notation (HSON) format used by modern Hedgehog Engine games.
- [KnuxLib](https://github.com/Knuxfan24/KnuxLib) - Library and CLI tools for miscellaneous Sonic-related file formats, with conversion utilities where applicable.
- [Sonic-06-Character-Swapper](https://github.com/hyperbx/Sonic-06-Character-Swapper) - Character swapping tool for Sonic the Hedgehog (2006), built on the Marathon toolkit's file format APIs.
- [RFL2HMM](https://github.com/hyperbx/RFL2HMM) - Converts Hedgehog Engine 2 reflection (RFL) data into Hedge Mod Manager code definitions.
- [PXDAnimationTools](https://github.com/WistfulHopes/PXDAnimationTools) - Blender addon for importing and exporting compressed Hedgehog Engine 2 `.anm.pxd` animations and `.skl.pxd` skeletons (batch import/export as actions, root motion support), with a C++ ACL-based decompression helper for Sonic Frontiers animations (not archived).
- [Unleashed-Mod-Manager](https://github.com/hyperbx/Unleashed-Mod-Manager) (archived) - Tool to handle mod copying and organisation for Sonic Unleashed.
- [HavokAnimationExporter](https://github.com/blueskythlikesclouds/HavokAnimationExporter) - Tool for generating animation and skeleton data for Sonic games that use Havok.
- [SonicUnleashed_ModToolbox](https://github.com/PTKay/SonicUnleashed_ModToolbox) - Batch-script toolbox automating common Sonic Unleashed modding tasks.
- [ForcesModInstaller](https://github.com/PTKay/ForcesModInstaller) - Installs mods into Sonic Forces using PackCPK.exe.
- [ShadowToGensSetConverter](https://github.com/PTKay/ShadowToGensSetConverter) - Converts Shadow the Hedgehog set (object placement) data into Sonic Generations-compatible set data.
- [CompressAR](https://github.com/PTKay/CompressAR) - Tool to compress and decompress Sonic Generations AR archive files, using makecab/expand.
- [GenerationsSkillEdit](https://github.com/sonicretro/GenerationsSkillEdit) - Skill set editor for Sonic Generations `.sav` save files.
- [HedgeGI](https://github.com/blueskythlikesclouds/HedgeGI) - Global illumination baker for Hedgehog Engine games.
- [sonic06 (decomp)](https://github.com/rjkiv/sonic06) - Matching decompilation of Sonic the Hedgehog (2006).
- [BlueBlur](https://github.com/blueskythlikesclouds/BlueBlur) - Modding API for the Steam version of Sonic Generations, interfacing with the game's original C++ types for DLL mods.

##### Creative Assembly

###### Alien: Isolation

- [Alien Isolation Animation Exporter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-animation-exporter) - Exports animations and bone structures from Alien Isolation.
- [Alien Isolation Model Exporter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-model-exporter) - Exports models from Alien Isolation for re-import into Blender.
- [Alien Isolation Texture Exporter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/texture-extractor) - Extracts textures from Alien Isolation. By Cra0kalo, modified by MattFiler.
- [Alien Isolation Audio Converter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-audio-converter) - Converts audio in Alien Isolation. Includes revorb, bnkextr, ww2ogg, and instructions.
- [Alien Isolation BML Converter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-bml-converter) - BML file converter for Alien Isolation enabling modding of behaviors, weapons, and more.
- [Alien Isolation UI Mod Tool](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-ui-mod-tool)
- [Alien Isolation Audio Extractor](https://github.com/MattFiler/Alien-Isolation-Audio-Extractor) - Extracts and names sound files from Alien: Isolation's Wwise BNK/WEM audio banks, outputting files with human-readable names derived from the game's sound event data.
- [AssetEditor](https://github.com/OpenCAGE/AssetEditor) (archived) - Browse and modify Alien: Isolation's asset PAK archives.
  - Formats: PAK2 (UI.PAK, ANIMATIONS.PAK), Texture PAK (LEVEL_TEXTURES.ALL.PAK, GLOBAL_TEXTURES.ALL.PAK), Models PAK (LEVEL_MODELS.PAK, GLOBAL_MODELS.PAK), Shaders PAK (*_SHADERS_DX11.PAK), Material Mappings PAK (MATERIAL_MAPPINGS.PAK).
- [AlienBML](https://github.com/x1nixmzeng/AlienBML) - Command-line C# tool converting Alien: Isolation's XML to and from its binary BML format.
- [LevelViewer](https://github.com/OpenCAGE/LevelViewer) - Views Alien: Isolation levels in Unity, companion to the OpenCAGE modding toolkit and AssetEditor above.
- [OpenIsolation](https://github.com/OpenIsolation/OpenIsolation) - Reverse-engineering project for Alien: Isolation's CATHODE engine, publishing headers and a growing SDK for the entity/resource-database and composite-file runtime structures underlying the same asset PAK archives handled by OpenCAGE/AssetEditor above.

###### Total War Series

- [Texture 2 DDS Converter (Medieval II: Total War)](https://www.moddb.com/games/medieval-2-total-war/downloads/texture-2-dds-converter)
- [Vercengetorix's CAS Import/Export (Medieval II: Total War)](https://www.moddb.com/games/medieval-2-total-war/downloads/vercengetorix-s-cas-import-export) - Allows you to import and export .CAS files to and from 3ds Max.
- [CAS Exporter (Medieval II: Total War)](https://www.moddb.com/games/medieval-2-total-war/downloads/cas-exporter) - Public release of model and animation exporter for Rome: Total War and Medieval II: Total War.
- [Community Modding Framework (Total War: Warhammer II)](https://www.moddb.com/games/total-war-warhammer-ii/downloads/community-modding-framework-1104) - Community Modding Framework v1.10.4, authored by Crynsos. This mod acts as a central compatibility manager for all script mods that have been registered to prevent any potential conflicts.
- [Symphony Sound Packer (Empire: Total War)](https://www.moddb.com/mods/foothold-in-india/downloads/symphony-sound-packer) - British Line Infantry starts shouting "Revolutionary Guard!" when you click them after installing a mod with new units? This tool should help you. All credits to crux3D.
- [OpenCAGE](https://github.com/MattFiler/OpenCAGE) - Modding toolkit for Alien: Isolation supporting model, texture, material import/export, and comprehensive asset management.
- [IDX-extractor](https://github.com/londonhargrove/IDX-extractor) - Assembles and disassembles IDX/DAT compressed audio archive pairs used by Total War games including Rome and Medieval II.

##### Puyo Puyo

- [puyotools](https://github.com/nickworonekin/puyotools) - Collection of tools and libraries for accessing contents of various game files. Initially built for Puyo Puyo games but can handle files from other games as well.
- [puyo-pac](https://github.com/nickworonekin/puyo-pac) - Command-line app for creating and extracting PAC archives used in Puyo Puyo Tetris 2.
- [PP20thDataExtractor](https://github.com/nickworonekin/PP20thDataExtractor) - Extracts and builds GAME.DAT in the Wii and PSP versions of Puyo Puyo!! 20th Anniversary.
- [OSBExtract](https://github.com/nickworonekin/OSBExtract) - Extracts OSB archives from Puyo Puyo~n; also extracts OSBs from MLT files and converts P04/P16 files to WAV.
- [puyo20-text-tool](https://github.com/52871299hzy/puyo20-text-tool) - Extracts and rebuilds font and text files for translating the Wii version of Puyo Puyo!! 20th Anniversary.
- [PuyoEdit](https://github.com/ArMM1998/PuyoEdit) - Animation editor for the ncsc format used by Sega in Puyo Puyo games.
  - Games: Puyo Puyo 15th Anniversary, Puyo Puyo 7, Puyo Puyo 20th Anniversary, Puyo Puyo!! Quest, Puyo Puyo Touch.
  - Requires the companion [Puyo-Puyo-Animation-Converter](https://github.com/ArMM1998/Puyo-Puyo-Animation-Converter) to convert to/from the games' binary ncsc files.
- [Puyo-Puyo-Animation-Converter](https://github.com/ArMM1998/Puyo-Puyo-Animation-Converter) - Converts Puyo Puyo animation files to and from JSON.
  - Formats: .snc (PS2/PSP), .dncs (DS/3DS/mobile), .gncs (Wii).
- [Puyo-Sprite-Editor](https://github.com/ArMM1998/Puyo-Sprite-Editor) - Sprite viewer/editor for Puyo Puyo animation files (15th Anniversary through 20th Anniversary, excluding DS/3DS).
- [Puyo-Puyo-lesson-scripts](https://github.com/ArMM1998/Puyo-Puyo-lesson-scripts) - Documentation and tooling for the .pss lesson-script format found in Puyo Puyo Champions and other Puyo Puyo games, including a field-data builder tool.
- [puyopuyotetris-3ds-english-patch](https://github.com/Akoi89/puyopuyotetris-3ds-english-patch) - Ports Sega's official English text and voices from the Steam release of Puyo Puyo Tetris (DLC included) onto the Japanese Nintendo 3DS release.

##### System & Middleware

- [NaomiMod/games-ExtractTools](https://github.com/NaomiMod/games-ExtractTools) - QuickBMS scripts to extract NaomiLib models from Dreamcast/Naomi arcade games. Supports Dead or Alive 2, Initial D3, Mortal Kombat 4, Super Monkey Ball, Virtua Tennis, Castlevania Resurrection, Rent-A-Hero, and more.
- [NaomiLib Blender Addon](https://github.com/NaomiMod/blender-NaomiLib) - Blender addon for importing NaomiLib 3D models from SEGA Dreamcast and Naomi arcade games.
- [Sega_NN_tools](https://github.com/Argx2121/Sega_NN_tools) - Python library for Blender with tools for games using Sega's NN libraries.
- [gpgx_debugger](https://github.com/lab313ru/gpgx_debugger) - Sega Mega Drive/Genesis reverse-engineering toolkit and debugger built on top of Genesis Plus GX.
- [megapack-megadrive](https://github.com/lab313ru/megapack-megadrive) - Source code for the Sega Mega Drive MEGAPACK, including Jon Menzies' original 68k decompression algorithm used by the compilation's game data.
- [smd_ida_tools2](https://github.com/lab313ru/smd_ida_tools2) - IDA Pro tools for reverse-engineering Sega Mega Drive/Genesis ROMs.
- [xgm-standalone](https://github.com/andwn/xgm-standalone) - Standalone build of SGDK's XGM sound driver and xgmtool, converting VGM music data into the Sega Mega Drive's native XGM sound format.
- [gdisofs](https://github.com/snickerbockers/gdisofs) - FUSE module for mounting Sega Dreamcast GD-ROM (.gdi) disc images. See also [gdi_mgr](https://github.com/snickerbockers/gdi_mgr), Perl scripts by the same author that verify a `.gdi` dump's track files against a TOSEC XML MD5 list and convert `.gdi` dumps to CHD with `chdman`.
- [ds2png](https://github.com/drojaazu/ds2png) - Converts Sega Digitizer System III data files to split PNG images.
- [lzkn](https://github.com/lab313ru/lzkn) - Compression/decompression tools for the LZ Konami algorithm used across Konami's Sega Mega Drive/Genesis games. See also [zida80](https://github.com/lab313ru/zida80), a Z80 sound driver debugger for IDA Pro targeting the same platform.
- [konami-compression-tools](https://github.com/vladikcomper/konami-compression-tools) - Compressor, decompressor, and recompressor for Konami Compression variant 1 (LZKN1), found in 1990s Konami Mega Drive/Genesis games and based on research into Contra: Hard Corps, with a disassembly of the original M68K decompression routine.
- [gdworkbench](https://github.com/lhsazevedo/gdworkbench) - CLI tool for inspecting, extracting, and building Sega Dreamcast GD-ROM (.gdi) images.
- [gdiextract](https://github.com/MachXNU/gdiextract) - Cross-platform command-line tool that lists and extracts the contents of Sega Dreamcast GD-ROM dumps in `.gdi` + `.bin` + `.raw` format.
- [GDIbuilder](https://github.com/Sappharad/GDIbuilder) - Cross-platform (Windows/macOS/Linux) GUI and CLI utility for building, patching, and extracting Sega Dreamcast GD-ROM (.gdi) images, including IP.BIN bootsector generation and CDDA track handling.
- [AicaADPCM2WAV](https://github.com/Sappharad/AicaADPCM2WAV) - Command-line tool that converts Sega Dreamcast AICA ADPCM audio data to WAV or raw PCM.
- [AFS2WAV](https://github.com/sizious/afs2wav) - GUI for ADXUtil that converts CRI ADX audio, typically embedded in AFS archives on the Dreamcast, PlayStation 2 and GameCube, to WAV.
- [pvr2image](https://github.com/VincentNLOBJ/pvr2image) - Converts Sega Dreamcast/NAOMI PVR texture files to PNG, TGA, and BMP.
- [spvr2png](https://github.com/nextgeniuspro/spvr2png) - Command-line converter from Sega Dreamcast PVR images to PNG, for single files or whole directories.
- [pvrtool](https://github.com/buhman/pvrtool) - Dreamcast image format and VQ conversion tool, originally authored by Sega of Europe and Imagination Technologies.
- [dcdis](https://github.com/sizious/dcdis) - Simple disassembler for Sega Dreamcast binaries.
- [HopperSH4-Plugin](https://github.com/Sappharad/HopperSH4-Plugin) - Hitachi SH4 disassembly plugin for the Hopper Disassembler, used for reverse-engineering Sega Dreamcast (and other SH4-based) binaries.
- [jc-bootrom-font](https://github.com/japanese-cake/jc-bootrom-font) - Python script that unpacks the embedded glyph fonts from the Sega Dreamcast bootROM.
- [Rings of Saturn](https://github.com/AlexIII/rings-of-saturn) - Compilation of reverse-engineering knowledge on the Sega Saturn system disc format, and a method for replicating it (making bootable Saturn discs from a burner) dubbed the "Rings of Saturn".
- [vcdextract](https://github.com/cyberwarriorx/vcdextract) - Extracts files out of Sega Saturn disc images for later rebuilding.
- [Ninja_Extractor](https://github.com/VincentNLOBJ/Ninja_Extractor) - Extracts SEGA Ninja model files (.NJ, .NJM, .NJL, .NJD), used across Dreamcast and Saturn-era games, from any uncompressed archive.
- [SegaAFSTools](https://github.com/enovales/SegaAFSTools) - Libraries and tools for working with Sega's own AFS archive format, used across a number of Sega-published titles.
- [PDN-FileTypePVR](https://github.com/derplayer/PDN-FileTypePVR) - Paint.NET plugin for reading and writing Sega Dreamcast PVR texture files.
- [Universal Dreamcast Patcher](https://github.com/DerekPascarella/UniversalDreamcastPatcher) - Cross-platform GUI toolkit for Dreamcast disc image operations: applying/building patches, editing IP.BIN, and converting between disc image formats.
- [Orbital Organizer](https://github.com/DerekPascarella/Orbital-Organizer) - Cross-platform GUI SD card management tool for the SEGA Saturn optical drive emulators Rhea and Phoebe.
- [openMenu Virtual Folder Bundle](https://github.com/DerekPascarella/openMenu-Virtual-Folder-Bundle) - Rewrite of the openMenu GDEMU frontend adding virtual folder/subfolder support, bundled with a modified GD MENU Card Manager to build compatible SD cards.
- [Convert GDEMU SD Card to MODE](https://github.com/DerekPascarella/Convert-GDEMU-SD-Card-to-MODE) - Converts a GDEMU-formatted Dreamcast/Saturn ODE SD card to the layout expected by the MODE optical drive emulator, including single-folder multi-disc support.
- [VMU Disc Builder](https://github.com/DerekPascarella/VMU-Disc-Builder) - Compiles a custom CDI containing Dreamcast VMU save files (VMI/VMS pairs), covering game save data, mini-games, or icons.
- [VMU Tool PC](https://github.com/sizious/vmu-tool-pc) - Windows explorer for managing Sega Dreamcast saves (VMI/VMS and DCI/Nexus files) on a PC, showing and editing VMU icons, copyright and size information.
- [Potato Tool](https://github.com/RossMeikleham/Potato-Tool) - Portable Haskell command-line toolset for the Dreamcast VMU filesystem: view and remove files, extract and inject Nexus DCI data files, and unlock the 41 unused blocks.
- [Saturn 4bpp Graphics Converter](https://github.com/DerekPascarella/Saturn-4bpp-Graphics-Converter) - Converts between the SEGA Saturn's 4bpp graphic format and bitmaps for editing, and back again.
- [Saturn 15bpp Graphics Converter](https://github.com/DerekPascarella/Saturn-15bpp-Graphics-Converter) - Converts between the SEGA Saturn's 15bpp graphic format and bitmaps for editing, and back again.
- [unsegaREBORN](https://github.com/proeren2002/unsegaREBORN) - Toolkit for decrypting and extracting modern SEGA arcade cabinet system images: APP/PACK archives and OPT images (including the APM3 variant), with AES-NI-accelerated decryption, NTFS/exFAT parsing, and differencing-VHD update merging.
- [PyPVR](https://github.com/VincentNLOBJ/PyPVR) - Python encoder/decoder for Dreamcast/NAOMI PowerVR2 textures and archives (AFS/BIN/DAT/PVM/TEX), with palette conversion via [PVP2ACT](https://github.com/VincentNLOBJ/PVP2ACT) (.PVP to PNG/.ACT); by the same author as pvr2image/Ninja_Extractor above.

##### Camelot Software Planning (Shining Force)

- [SF1DISASM](https://github.com/ShiningForceCentral/SF1DISASM) - Documentation disassembly of Shining Force (Genesis). See also [SF1RE](https://github.com/ShiningForceCentral/SF1RE), the IDA Pro IDC scripts used to reverse-engineer the ROM and regenerate this disassembly from scratch.
- [SF2DISASM](https://github.com/ShiningForceCentral/SF2DISASM) - Documentation disassembly of Shining Force II. See also [SF2RE](https://github.com/ShiningForceCentral/SF2RE), the IDA Pro IDC scripts used to reverse-engineer the ROM and regenerate this disassembly from scratch, and [SF2JavaToolSuite](https://github.com/ShiningForceCentral/SF2JavaToolSuite), the project's consolidated collection of Java-based disassembly/reassembly tools, split out to keep the tooling maintainable separately from the disassembly repo.
- [SFCDDISASM](https://github.com/ShiningForceCentral/SFCDDISASM) - Documentation disassembly of Shining Force CD (Mega-CD), reassembling to a bit-perfect original ISO.
- [SITDDISASM](https://github.com/ShiningForceCentral/SITDDISASM) - Documentation disassembly of Shining in the Darkness (Genesis), reassembling to a bit-perfect original ROM.
- [SFFCRE](https://github.com/ShiningForceCentral/SFFCRE) - Shining Force Final Conflict reverse-engineering notes and tools, with text docs on cutscenes, scripts, and map, music, portrait, and sprite indexes, plus a Java cutscene manager (SFFCCutsceneManager).
- [goldensun](https://github.com/gsret/goldensun) - Disassembly of Golden Sun (GBA).
- [goldensun-decomp](https://github.com/Coaltergeist/goldensun-decomp) - Work-in-progress decompilation of Golden Sun (GBA) building a byte-identical ROM, complementing the goldensun disassembly above.
- [camelot-gcc](https://github.com/Coaltergeist/camelot-gcc) - Recreation of the C compiler used to build Golden Sun (GBA) and Golden Sun: The Lost Age, supporting the goldensun-decomp matching decompilation above.
- [GoldenSunTLA_Editor](https://github.com/nikitalita/GoldenSunTLA_Editor) - Golden Sun: The Lost Age (GBA) map editor by Josh "Atrius" VH, archived source-only reference.
- [GoldenSunCompression](https://github.com/romhack/GoldenSunCompression) - Compression tools for Golden Sun (GBA) and Golden Sun: The Lost Age.
- [ShiningEditor](https://github.com/Fuindin/ShiningEditor) - Genesis/Mega Drive save state editor for Shining in the Darkness, Shining Force, Shining Force II, and Shining Force CD.

##### Other Games

- [tbg-decomp (decomp)](https://github.com/lhsazevedo/tbg-decomp) - Matching decompilation of Tokyo Bus Guide (Dreamcast).
- [SkiesofArcadiaLegends (decomp)](https://github.com/rainchus/SkiesofArcadiaLegends) - Matching decompilation of Skies of Arcadia Legends (GameCube).
- [JSRGraffitiTool](https://github.com/chrisderwahre/JSRGraffitiTool) - Tool for modding Jet Set Radio's graffiti files.
- [ArfAFS](https://github.com/XAYRGA/ArfAFS) - Utility for Jet Set Radio's `.AFS` files, with parsers for its demo and scene bin data.
- [SGGGE](https://github.com/VincentNLOBJ/SGGGE) - Texture editor for Segagaga (Dreamcast): unpacks a GDI dump, lets you browse and replace container images, and rebuilds a modified GDI (LZ-compressed assets handled via bundled tools).
- [noclip.website (Jet Set Radio)](https://github.com/magcius/noclip.website/tree/main/src/JetSetRadio) - In-browser Jet Set Radio viewer.
- [noclip.website (Mario & Sonic at the London 2012 Olympic Games)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser viewer for the Wii Mario & Sonic Olympic Games title, built on noclip's NW4R/BRRES loader.
- [PCSX2 Patches](https://github.com/PCSX2/pcsx2_patches) - Game patches for PCSX2 emulator including widescreen and interlacing fixes.
- [clownlzss](https://github.com/Clownacy/clownlzss) - LZSS compression framework with compressors for Sega Mega Drive game formats. Supports Kosinski, Saxman, Chameleon, and Rocket compression formats.
- [SegaRally2006FAHTools](https://github.com/igorciz777/SegaRally2006FAHTools) - Tools for 'FAH' file archives found in Sega Rally 2006 (PS2, SLPM-66212); extracts files with filenames and subdirectories preserved.
- [sega-vr-disasm](https://github.com/matiaszanolli/sega-vr-disasm) - Complete static recompilation of Virtua Racing for the Sega 32X.
- [or2-tools](https://github.com/JayFoxRox/or2-tools) - Reads OutRun 2 (Original Xbox) proprietary file formats: CVM disc images, gzip-compressed game files, CS_*_SIN/CS_*_BIN index streams, and OBJ_*_SMT/CS_*_SMT mesh and texture data. Extraction only, no repacking yet.
  - Games: OutRun 2, OutRun 2006: Coast to Coast.
- [daytona-xbla-recomp](https://github.com/Subarasheese/daytona-xbla-recomp) - Static recompilation of Daytona USA (Xbox 360/XBLA, 2011).
- [AmyStudio](https://github.com/gdkchan/AmyStudio) - Sonic 2 level viewer written in VB.NET.
- [cannonball](https://github.com/djyt/cannonball) - Enhanced C++ rewrite of the OutRun arcade engine, requiring the original OutRun ROM set for its graphics, audio, and level data.
- [system16_sprite_viewer](https://github.com/djyt/system16_sprite_viewer) - Sprite viewer for Sega System 16, System 16B, X-Board, and Y-Board arcade hardware, covering OutRun and related titles.
- [mmlr](https://github.com/djyt/mmlr) - Decompiles OutRun's Sega MML (Music Macro Language) audio data, from both the original arcade ROMs and the 3DS/Switch ports, into an editable/recompilable format.
- [akmw](https://github.com/lhsazevedo/akmw) - Disassembly of the original Alex Kidd in Miracle World (Sega Master System).
- [satellite7](https://github.com/lhsazevedo/satellite7) - Labelled and commented disassembly of Satellite 7 (Sega Master System, 1985).
- [SR2Tools](https://github.com/Spreit/SR2Tools) - Python modding tools for Sega Rally 2, including a SAR archive extractor, texture converter/classes, a model tool (sr2mdl), and batch BINDATA conversion.
- [sms-super-tennis](https://github.com/FlorianCassayre/sms-super-tennis) - Full matching disassembly of Super Tennis (Sega Master System, also released in Japan as "Great Tennis"), covering both known ROM revisions.
- [Knowledgebase](https://github.com/Shenmue-Mods/Knowledgebase) - Modding knowledgebase for Shenmue, documenting the game's original file formats.
- [genipak-magicard-tool](https://github.com/SONIC3D/genipak-magicard-tool) - Tool for Genipak and Magicard archive formats used in Sonic games.
- [st3-translation-notes](https://github.com/TheOpponent/st3-translation-notes) - Translation notes documenting the data formats used by the Dreamcast game Sakura Taisen 3: Paris wa Moeteiru ka.
- [Dramatic-Dungeon-Sakura-Wars-Tool](https://github.com/gopicolo/Dramatic-Dungeon-Sakura-Wars-Tool) - Tool for extracting, editing, and reinserting text in Dramatic Dungeon: Sakura Taisen.
- [SALSA](https://github.com/SoAModTools/SALSA) - Skies of Arcadia Legends Script Assistant, a GUI-based tool to assist in editing the game's script files.
- [SPICE](https://github.com/SoAModTools/SPICE) - Skies Package Interchange and Content Encoder, a successor to the author's Skies of Arcadia tooling covering SCT script parsing, MLD entry-list export, content-graph export, and SA3D-backed geometry/Blender IR support.
- [ALX](https://github.com/Taikocuya/ALX) - Cross-platform command-line tool to export and import game data for Skies of Arcadia, Skies of Arcadia Legends, Eternal Arcadia, and Eternal Arcadia Legends.
- [shino-legion-decomp](https://github.com/kazuyette/shino-legion-decomp) - In-progress decompilation project for Shinobi Legions.
- [JSRF Dialog Font](https://github.com/jsrf-tool/jsrf-dialog-font) - Tool for working with the dialog font format used in Jet Set Radio Future (Xbox).
- [OllieKingRETools](https://github.com/KidWizardOfTheWeb/OllieKingRETools) - Reverse engineering tools for Ollie King (Sega Naomi arcade), building on scripts credited to the Xentax community.
- [JewelMasterCompression](https://github.com/romhack/JewelMasterCompression) - Tools for the Sega Genesis game Jewel Master's compressed data: RLE-compressed name tables and arithmetic-coded tile sets.

##### SEGA AM2

- [HoneyPatcher](https://github.com/coatlessali/HoneyPatcher) - Mod installer and tool for SEGA AM2 arcade ports on RPCS3 (Windows/macOS/Linux/SteamOS).
  - Games: Sonic the Fighters, Fighting Vipers, Virtua Fighter 2, Cyber Troopers Virtual-On: Operation Moongate, Daytona USA.
  - Built on MikuMikuLibrary, SonicAudioTools, and xdelta-sharp.
- [Obj2StF](https://github.com/coatlessali/Obj2StF) - Converts Blender-exported Wavefront OBJ models into Sonic the Fighters' native .stfmdl/.stfmat 3D model/material format, for injecting custom character models via hex-edited pointer tables. GUI-adding fork of [GophUndMe/Obj2StF](https://github.com/GophUndMe/Obj2StF).
- [stf-tools](https://github.com/coatlessali/stf-tools) - Small utility collection for Sonic the Fighters (Sonic Championship), including a DDS header fixer and a wrapper around MikuMikuLibrary's FarcPack archive tool.
- [libHoneyBadger](https://github.com/coatlessali/libHoneyBadger) - Utilities for SEGA Model 2 games on PS3, including DDSFixHeader for repairing DDS texture headers so the game reads them correctly.

#### Septerra Core

- [Septerra](https://github.com/xyx0826/Septerra) - Septerra Core tools that unpack the game's resources and convert known formats: AM animations to and from TIFF, TX text to TXT, and VSSF audio to and from MP3.
  - Includes 010 Editor templates for the AM, CH, GV, IL and LV formats.

#### Serial Experiments Lain

- [lainTSX](https://github.com/ad044/lainTSX) - Browser-based reimplementation of the Serial Experiments Lain PSX game using three.js, with multi-language subtitle support.
  - Ships no game assets; a companion extraction script pulls and reformats video, image, and text assets directly from the original disc images.
- [lain-bootleg-bootleg](https://github.com/ad044/lain-bootleg-bootleg) - Reverse engineering and remake of Lain Bootleg, a minigame from the Serial Experiments Lain PSX game.
- [SEL-SaveFile-Editor](https://github.com/justKherty/SEL-SaveFile-Editor) - Python command-line editor for Serial Experiments Lain save files: converts the raw save file, marks viewed chapters, and writes the final JSON.

#### Shadow of Mordor & Shadow of War

- [MordorUnpacker](https://github.com/WarpZephyr/MordorUnpacker) - Drag-and-drop unpacker for Shadow of Mordor and Shadow of War files; Shadow of War needs the game's Oodle library (oo2core_5_win64.dll) copied next to the tool.
  - [MordorFormats](https://github.com/WarpZephyr/MordorFormats) - C# library for the LTAR archives (.arch05, .arch06) used by both games.

#### Wolfpack Studios (Shadowbane)

- [ShadowbaneCacheViewer](https://github.com/shoff/ShadowbaneCacheViewer) - Work-in-progress viewer application for parsing and displaying the contents of Shadowbane's .cache client data files.

#### Shadowverse: Worlds Beyond

- [Wizard2AssetsUnpacker](https://github.com/SVGWBTools/Wizard2AssetsUnpacker) - Cross-platform .NET CLI that downloads and decrypts Shadowverse: Worlds Beyond asset bundles and the asset manifest, and decrypts the game's meta database.

#### L2 Games (She Will Punish Them)

- [SwptEditor](https://github.com/CrystalFerrai/SwptEditor) - Unofficial save game editor for She Will Punish Them.

#### Infogrames Lyon House (Sheep, Dog 'n' Wolf)

- [sheep-dog-n-wolf-decomp](https://github.com/lace22l/sheep-dog-n-wolf-decomp) - Active decompilation project for Sheep, Dog 'n' Wolf (PS1/PC), reverse-engineering the original game binary; research coordinated on the Sheep Raider Speedrunning Discord.
- [Sheep-N-Dog-DAV-Texture-Viewer](https://github.com/lace22l/Sheep-N-Dog-DAV-Texture-Viewer) - Inspects and extracts textures from Sheep, Dog 'n' Wolf's `.dav` files, built from Ghidra decompilation as part of the decompilation effort above.

#### Shin Hayarigami

- [ShinHayarigamiExt](https://github.com/Manicsteiner/ShinHayarigamiExt) - Extraction tool for Shin Hayarigami (PS3, BLJS10279) `.dat` archives, decoding its image assets; view the extracted `.at9` audio files with vgmstream.
- [ShinHayarigami2Ext](https://github.com/Manicsteiner/ShinHayarigami2Ext) - Extraction tool for Shin Hayarigami 2 (PS3, BLJS10336) `.dat` archives, decoding DDS/TGA images and AT3/VAG audio; includes a separate script to strip a 16-byte header from sound archives before use with vgmstream.

#### Marvelous (Shinobi Master Senran Kagura: New Link)

- [bpy_smsk_new_link](https://github.com/coreynguyen/bpy_smsk_new_link) - Blender addon for importing models from Shinobi Master Senran Kagura: New Link.

#### Shiny Entertainment

- [MPON_RE](https://github.com/SwatGetmann/MPON_RE) - Reverse-engineering project for The Matrix: Path of Neo (PC), with finished audio extraction (identifying the format as Xbox ADPCM), 010 Editor templates for the game's packages, and in-progress work on textures, 3D models, and subtitle ('Louie') data.

#### Shiro Games

- [qbms_shirogames](https://github.com/Sviat/qbms_shirogames) - QuickBMS scripts for Shiro Games' RES.PAK archive format, covering Northgard's res.client.pak (textures, models, sounds, data.cdb) and Farever, building on an earlier community script originally written for Evoland 2.
  - Games: Northgard, Farever.
- [Wartales-pak-modding-Toolkit](https://github.com/An-on-im/Wartales-pak-modding-Toolkit) - Unpacker and repacker for Wartales' RES.PAK archives, extracting and modifying game resources with full preservation of the original archive structure.

#### Shuttle: The Space Flight Simulator

- [shuttle-tools](https://github.com/yuv422/shuttle-tools) - Unpacks and repacks data assets from Vektor Grafix Ltd's 90s game Shuttle: The Space Flight Simulator, using the `_INDEX` and `_data1` files in its `RESOURCE` directory.

#### Sierra On-Line

- [SCI-Decompilation-Archive](https://github.com/EricOakford/SCI-Decompilation-Archive) - Archive of decompiled source code for Sierra's SCI engine games, covering SCI0, SCI1, and SCI2 eras.

##### Quest for Glory V: Dragonfire

- [QFG5Extractor](https://github.com/sariousness/QFG5Extractor) - C# toolkit for extracting and modifying assets from Quest for Glory V: Dragonfire.
  - Formats: `.SPK` game archives, `.MDL` meshes (Hakenberg format + BMP textures), panorama backgrounds.
  - Features: Batch extraction, asset modification, cross-platform unified GUI.
- [qfg5model](https://github.com/bairesearch/qfg5model) - Command-line tool to export and import textures and meshes from Quest for Glory V, with support for importing high-resolution replacement textures and meshes.
- [qfg5-reenigne](https://github.com/zhmu/qfg5-reenigne) (archived) - Reverse engineering notes and tools for Quest for Glory V: Dragonfire.

##### Leisure Suit Larry

- [leisuresuitlarry (historical source)](https://github.com/historicalsource/leisuresuitlarry) - Collection of original script and definition files for Leisure Suit Larry in the Land of the Lounge Lizards (1987) by Al Lowe, documenting the game's Sierra AGI-era resource/script data.
- [agi (historical source)](https://github.com/lanceewing/agi) - Recovered original source code of Sierra On-Line's AGI adventure game interpreter, found in unused portions of original game disks (primarily Space Quest II v2.0D), documenting how the AGI engine reads its resource/script data.
- [sci-scripts](https://github.com/sluicebox/sci-scripts) - 100% decompiled scripts for 300+ versions of Sierra's SCI games (King's Quest IV through Leisure Suit Larry 7), across DOS, Amiga, Atari ST, Macintosh, PC-98, and FM-Towns, generated with the author's own SCI bytecode decompiler.

#### Sigma Team

- [locoland-formats](https://github.com/AlexKimov/locoland-formats) - File formats for Locoland/Steamland and Alien Shooter (2003).

#### Silicon Knights

##### Eternal Darkness: Sanity's Requiem

- [Eternal-Darkness---Decompile](https://github.com/psdwizzard/Eternal-Darkness---Decompile) - Matching decompilation of Eternal Darkness: Sanity's Requiem (GameCube, GEDE01 revision 0), targeting a byte-identical rebuild of the original Metrowerks CodeWarrior binary.

#### Joymax (Silkroad Online)

- [xSROMap](https://github.com/JellyBitz/xSROMap) - Interactive world map explorer for Silkroad Online, built from NPC, teleport, and region data extracted from the client's media.pk2 archive.
- [SRO.PK2API](https://github.com/JellyBitz/SRO.PK2API) - C# library for reading and writing Silkroad Online's PK2 archive format.
- [JMX-File-Editor](https://github.com/JellyBitz/JMX-File-Editor) - Opens, edits, and saves Silkroad Online's JMX model/data files.
- [JMXVDDJConverter](https://github.com/JellyBitz/JMXVDDJConverter) - Converts between Silkroad Online's DDJ and DDS texture file formats.
- [NVMTerrainExtractor](https://github.com/JellyBitz/NVMTerrainExtractor) - Extracts terrain data from Silkroad Online's navmesh (.nvm) files.
- [SR_Db2Media](https://github.com/JellyBitz/SRO.Db2Media) - Extracts, encrypts, and imports Silkroad Online's database files directly into the client's media (PK2) archive.
- [SroPk2Studio](https://github.com/aloneanqel1453/SroPk2Studio) - Editor and viewer for Silkroad Online client archives with live 3D model, effect and UI previews.
  - Formats: JMXPACK `.pk2`/`.pk3`/`.lib`, SailSafe PK2, PK2v2 (read-only), VSROPLUS `.vp`, `.2dt` interface files, textdata tables.

#### Spiral House (Silver)

- [silver-reversing-sct](https://github.com/nadavshemesh/silver-reversing-sct) - Reverse-engineering and modding tool for Silver (1999 action RPG, developed by Spiral House and published by Infogrames), decompiling the game's `.sct` script files to a readable `.tsct` format and recompiling them back.

#### SingStar

- [singstar-toolbox](https://github.com/ravenDS/singstar-toolbox) - Custom SingStar disc creator; converts between UltraStar and SingStar song formats, with PS2/PS3 and FTP support.

#### Sir-Tech

##### Jagged Alliance 2

- [ja2-stracciatella](https://github.com/ja2-stracciatella/ja2-stracciatella) - Actively maintained continuation of the JA2-Stracciatella source port, making Jagged Alliance 2 available on modern platforms while reading the original game's data files.
- [ja2-open-toolset](https://github.com/ja2-stracciatella/ja2-open-toolset) - Python library and tools for reading and writing Jagged Alliance 2 game resources: SLF archives, STI sprite files, and GAP files.
##### Wizardry 8

- [Wizardry8Editor](https://github.com/anonidiot/Wizardry8Editor) - Qt-based save game editor for Wizardry 8.

#### Copysoft (Skunny: Back to the Forest)

- [pc-skunnybacktotheforest-doc](https://github.com/vs-sr-dev/pc-skunnybacktotheforest-doc) - Format documentation for Skunny: Back to the Forest (MS-DOS, 1993): the `.LID` archives, `S*` sprite banks and index tables, PCX assets and symbol tables, with scripts to reproduce the analysis from your own copy.

#### thatgamecompany (Sky)

- [sky-browser](https://github.com/mablay/sky-browser) - Web-based asset explorer for Sky: Children of the Light, decoding the game's ETC2-compressed KTX textures and mesh data directly in the browser.

#### Digital Illusions (SkyRoads / Pinball Fantasies)

##### SkyRoads

- [skyhigh_releases](https://github.com/kaimitai/skyhigh_releases) - Releases for the Sky High SkyRoads editor, covering the 1993 DOS game's level and graphics data.
- [SkyRoads-Codex](https://github.com/ammaarreshi/SkyRoads-Codex) - Reverse engineering of SkyRoads (1993, DOS) with no original source code available, recovering the game's level and asset data formats.
- [OpenRoads](https://github.com/anprogrammer/OpenRoads) - Modern TypeScript/HTML5 reimplementation of SkyRoads (1993, DOS), reading all of the original game's data files (art, music, levels) rather than remaking them from scratch; also runs under Node.js with Oculus Rift support.

##### Pinball Fantasies

- [pfr](https://github.com/wanda-phi/pfr) - Rust reimplementation of Pinball Fantasies (1993, DOS) that reads the original game's `.PRG`/`.MOD` data files.

#### Mega Crit (Slay the Spire)

- [SimTheSpire](https://github.com/kartoFlane/SimTheSpire) - Reverse-engineer Slay the Spire and simulate gameplay to automatically balance cards.
- [spire-codex](https://github.com/ptrlrd/spire-codex) - Decompiling Slay the Spire 2 and creating an API from game data.
- [spireslayer](https://github.com/rnazali/spireslayer) - Save file editor/tool for Slay the Spire.
- [sts-editor (STS Save Editor)](https://github.com/lemehmet/sts-editor) - Terminal-based save file editor for Slay the Spire, built with Python and Textual; can be used locally or over SSH.
- [SaveTheSpire](https://github.com/GoodManWEN/SaveTheSpire) - Python save editor for Slay the Spire, run from the game's save folder.

#### Slitherine / Proxy Studios

- [Blender Gladius Addon v1.1 (Warhammer 40,000: Gladius - Relics of War)](https://www.moddb.com/mods/blender-gladius-addon/downloads/blender-gladius-addon-v11) - The first release. It should mostly work but may still have some bugs.
- [blender_gladius](https://github.com/amorgun/blender_gladius) - Blender addon importing Warhammer 40,000: Gladius - Relics of War units from their `.xml`, with meshes (`.msh`), animations (`.anm`) and textures.

#### Super Creative (Smilegate)

- [Chaos Zero Nightmare ASSet Ripper](https://github.com/cznrip/ChaosZeroNightmare-AssetRipper) - Extracts encrypted assets from Chaos Zero Nightmare's data.pack (including the Chinese client, 卡厄思梦境), previewing and exporting SCT images as PNG, encrypted databases as JSON, and Spine (SCSP) animation data as JSON via a built-in Spine viewer.
- [SCTParser](https://github.com/formagGinoo/SCTParser) - Parses the SCT custom image format shared by Chaos Zero Nightmare and Epic Seven into PNGs; superseded for Chaos Zero Nightmare by the ASSet Ripper above but still useful standalone, including for Epic Seven assets.

#### SNK

##### Crystalis

- [gbc2Tga](https://github.com/romhack/gbc2Tga) - Converts GBC Crystalis's Hicolour-technique tiles and palettes to a single .tga file for editing; see also the reverse tool TGA2GBC by Jeff Frohwein.

##### King of Fighters XIII

- [TKOF-XIII-Text-Tool](https://github.com/OAleex/TKOF-XIII-Text-Tool) - Extractor, text inserter, and file manipulator for The King of Fighters XIII.

##### The Last Blade

- [lastblad-rom-extractor](https://github.com/DrRetroMod/lastblad-rom-extractor) - Python script to extract MAME-compatible ROM archives from the DotEmu re-release of The Last Blade. Fork of mslug-rom-extractor (below) adapted for a different game.

##### Metal Slug

- [mslug-rom-extractor](https://github.com/terminatorhex/mslug-rom-extractor) - Python script to extract MAME-compatible ROM archives from the DotEmu releases of Metal Slug 1, 2, and X.

##### Neo Geo Pocket

- [NGPCEdit](https://github.com/nfroggy/NGPCEdit) - Tile editor for the Neo Geo Pocket Color, with bitmap import support for 8-bit greyscale images.

##### Samurai Shodown

- [samsho5_fe](https://github.com/Feilakas/samsho5_fe) - Python conversion tool for Samurai Shodown V Special (Final Edition), extracting files from SNK's Samurai Shodown NeoGeo Collection release.

##### SNK Heroines

- [SNK.WAD.Tool](https://github.com/Ekey/SNK.WAD.Tool) (archived) - Tool for extracting WAD archives from SNK Heroines: Tag Team Frenzy.

#### Snowblind Studios

##### Baldur's Gate: Dark Alliance

- [bgda-explorer](https://github.com/bigianb/bgda-explorer) - Data file explorer for Baldur's Gate: Dark Alliance (PS2).
- [jbgda](https://github.com/bigianb/jbgda) - Java-based tools for Baldur's Gate: Dark Alliance (PS2).
- [frostbite](https://github.com/bigianb/frostbite) - Experimental implementation of the Snowblind engine.

#### SoftClub

##### Treasure Island (2005)

- [TI.DAT.Tool](https://github.com/Ekey/TI.DAT.Tool) (archived) - Extractor for RC4-encrypted DAT/PACK archives from Treasure Island (2005), a Russian PC adventure game published by SoftClub.

#### SoftLab-NN

- [HardTruck-RignRoll-file-formats](https://github.com/AlexKimov/HardTruck-RignRoll-file-formats) (archived) - File formats, specs, and script tools for Hard Truck 1/2 and Rig'n'Roll.
- [SeelTools](https://github.com/Zvetkov/SeelTools) - Work-in-progress Python/Qt GUI toolkit for Ex Machina / Hard Truck Apocalypse that loads the game's XML prototypes, resources, affixes and faction relationships and displays them as a tree for inspecting prototype properties. Read-only viewer in practice (data can be written back, but not edited from the GUI); the author describes it as mostly abandoned.

#### SoftStar Entertainment

*Publisher of the classic Chinese RPG series Legend of Sword and Fairy (仙剑奇侠传), also known as PAL.*

- [SDLPAL](https://github.com/sdlpal/sdlpal) - SDL-based, cross-platform reimplementation of the original PAL engine, reading the original game's proprietary data files (purchased separately, not included) across Windows, Linux, macOS, mobile, and console ports.
- [palresearch](https://github.com/palxex/palresearch) - Research and reference tooling for PAL's file formats.
  - Formats: MKF archives, RIX music, save/script/battlefield/shop data.
  - Tools: MapEditor, PackageUtils, Pal95Tools, PalLibrary, PalScript, PalTools.NET.
- [fd2sdl](https://github.com/soarqin/fd2sdl) - SDL3 reimplementation of Flame Dragon 2: Legend of Golden Castle (炎龙骑士团 2, Hantang International, DOS 1995), reading the original 11 `.DAT` archives and `FD2.SAV` saves, with format documentation, EXE address and function mapping, and IDA/Ghidra analysis scripts.

#### Software Projects

##### Manic Miner

- [manicminer](https://github.com/skoolkid/manicminer) - SkoolKit-based disassembly of Manic Miner (ZX Spectrum), created by SkoolKit's author.
- [ManicMiner](https://github.com/TobyLobster/ManicMiner) - Disassembly of the original BBC Micro version of Manic Miner.
- [ManicMiner2021](https://github.com/TobyLobster/ManicMiner2021) - Manic Miner remastered on the BBC Micro, built on the ManicMiner disassembly above.
- [Manic-Miner-Source-Code](https://github.com/WHumphreys/Manic-Miner-Source-Code) - Source code disassembly of Manic Miner for the ZX Spectrum.

##### Jet Set Willy

- [jetsetwilly](https://github.com/skoolkid/jetsetwilly) - SkoolKit-based disassembly of Jet Set Willy (ZX Spectrum), created by SkoolKit's author.
- [jsw](https://github.com/TobyLobster/jsw) - Disassembly of Jet Set Willy for the BBC Micro.
- [jsw2021](https://github.com/TobyLobster/jsw2021) - Jet Set Willy remastered on the BBC Micro, built on the jsw disassembly above.

#### Sonic Boom: Rise of Lyric

- [SynergyTools](https://github.com/Soreepeong/SynergyTools) - Modding tool for Sonic Boom: Rise of Lyric (Wii U paths). Extracts and repacks `.wiiu.stream` archives, exports models as glTF, converts glTF models into shareable `.wiiu.stream` mod files, and imports mods made by others. Fork of ik-01/WiiUStreamTool with these additions.

#### Sony PlayStation Studios

##### Guerrilla Games (Decima Engine)

- [ProjectZeroDawn](https://github.com/neptuwunium/ProjectZeroDawn) (archived) - File format research and tools for Horizon Zero Dawn.
- [decima-workshop](https://github.com/ShadelessFox/decima-workshop) - GUI application for viewing and editing resources found in games powered by Decima Engine. Supports browsing and editing core objects, previewing models/textures/shaders, exporting assets, and repacking archives. Works with Horizon Zero Dawn, Death Stranding, and other Decima Engine games.
- [decima-native](https://github.com/ShadelessFox/decima-native) - Native library components for Decima Engine tools.
- [Decima Explorer](https://github.com/Jayveer/Decima-Explorer) - Unpacker and packer for games using the Decima engine (Horizon Zero Dawn, Death Stranding).
- [DecimaTools](https://github.com/Wunkolo/DecimaTools) - Tools, notes, and research related to reverse engineering the Decima Game Engine.
- [decima-rpcs3-dumper](https://github.com/ShadelessFox/decima-rpcs3-dumper) - Tool for dumping Decima Engine resources from RPCS3 emulator.
- [odradek](https://github.com/ShadelessFox/odradek) - Horizon Forbidden West asset viewer and extractor. Reincarnation of Decima Workshop specifically targeting Horizon Forbidden West for modding purposes.
- [forbidden-west-localizer](https://github.com/ShadelessFox/forbidden-west-localizer) - Modification that allows changing any localized text in Horizon Forbidden West. Supports text replacement via JSON configuration files.

- [cauldron](https://github.com/cauldronloader/cauldron) - Mod loader for Decima engine games (Horizon Zero Dawn/Forbidden West, Death Stranding, etc). Rust-based modding framework with game detection, DLL proxy loading, and RTTI symbol dumping capabilities.
- [stormbird](https://github.com/neptuwunium/stormbird) - Interop library for Horizon Zero Dawn. Provides interfaces for working with Horizon Zero Dawn file formats and game data.
- [decima-dmf](https://github.com/REDxEYE/decima-dmf) - Blender addon for importing DMF files produced by Decima Workshop. Supplementary addon for working with Decima Engine models in Blender.
- [ProjectDecima](https://github.com/spammydavis/ProjectDecima) - GUI application for previewing, exporting and modifying game resources in Decima Engine games. Archive explorer with texture preview and export capabilities. (Fork)
- [HZDCoreEditor](https://github.com/Nukem9/HZDCoreEditor) - Editor for Horizon Zero Dawn's Decima engine core/asset files.
- [decima-loc](https://github.com/YouKnow-sys/decima-loc) - Rust CLI and library for exporting and importing game text from Horizon Zero Dawn (PC) and Death Stranding (PC and PS4) core files as TXT, JSON, or YAML for localization, with batch processing and per-language selection.
- [hfw-raw-mesh-point-inspector](https://github.com/lorenfa99/hfw-raw-mesh-point-inspector) - Inspector for unknown raw mesh point-cloud binary streams in Horizon Forbidden West's Decima Engine data.
- [DeciWaves](https://github.com/prekabreki/DeciWaves) - Read-only tool that extracts recorded voice lines from installs of Death Stranding (Director's Cut), Horizon Zero Dawn Remastered and Horizon Forbidden West, attaches speaker and subtitle where derivable, and encodes them in story order into MP3 audiobook reels.

##### Insomniac Games

- [RatchetLevelEditor](https://github.com/badger41/RatchetLevelEditor) - Level editor for Ratchet & Clank games.
- [ALERT](https://github.com/Tkachov/ALERT) - Amazing Luna Engine Research Tools. Python toolkit for researching and modifying Insomniac Games assets with dat1lib library and web-based Assets Browser.
  - Games: Sunset Overdrive, Marvel's Spider-Man (Remastered, Miles Morales, 2), Marvel's Wolverine, Ratchet & Clank: Rift Apart.
  - Features: Model conversions (.model/.ascii/.gltf), animation application, soundbank audio injection, DSAR archive compression, asset extraction.
- [rivet](https://github.com/neptuwunium/rivet) (archived) - File format research project for Ratchet & Clank: Rift Apart.
- [ripped_apart](https://github.com/chaoticgd/ripped_apart) (archived) - Modding toolkit for Ratchet & Clank: Rift Apart.
- [insomniac-model](https://github.com/sleepyzay/insomniac-model) - Research and tools for Insomniac Games model formats.
- [DDLParser](https://github.com/macton/DDLParser) - Parser for Insomniac's Data Definition Language (DDL) format.
- [replanetizer](https://github.com/RatchetModding/replanetizer) - Full-featured level editor for PS3 Ratchet & Clank games.
- [slimseditor](https://github.com/RatchetModding/slimseditor) - Savegame editor for the Ratchet & Clank games, written in Python with a Dear ImGui frontend.
- [RaCSaveEditor](https://github.com/zyzalfors/RaCSaveEditor) - GUI save editor for the PlayStation 2 Ratchet & Clank 1, 2, 3 and Deadlocked/Gladiator `.bin` saves (all versions/regions): bolts, nanotech, weapons/items, ammo, skill points, crystals and raritanium.
- [RaCTrilogy-PS3-Tools](https://github.com/thtrandomlurker/RaCTrilogy-PS3-Tools) - Python scripts for extracting armor and model meshes from Ratchet & Clank PS3 Trilogy.
  - [io_mesh_rctrilogy](https://github.com/thtrandomlurker/io_mesh_rctrilogy) - WIP Blender importer for the Ratchet & Clank Trilogy `armor*.ps3` model files (PS3 and Vita).
- [wrench](https://github.com/chaoticgd/wrench) (archived) - Set of modding tools for the Ratchet & Clank PS2 games.
- [noclip.website (Ratchet & Clank)](https://github.com/magcius/noclip.website/tree/main/src/RatchetAndClank) - In-browser level viewer for Ratchet & Clank and Ratchet & Clank: Going Commando (PS2). Parses the level `.bin` TOC/core/gameplay containers and renders tfrag terrain, tie and shrub instances, moby actors, collision meshes, and skies, including a VIF/VU microcode unpacker for the PS2 display lists.
- [horizon-forge](https://github.com/Horizon-Private-Server/horizon-forge) - Map editor for Ratchet: Deadlocked Multiplayer (PS2).
- [Overstrike](https://github.com/Tkachov/Overstrike) - Open-source mod manager for PC ports of Insomniac Games' games.
- [disruptor_ripper](https://github.com/Yagotzirck/disruptor_ripper) - Resource extractor for Disruptor (1996, PS1 PAL), Insomniac Games' debut title.
- [MobyViewer](https://github.com/CreepNT/MobyViewer) - Real-time visualizer for Moby (game object) tables in Ratchet & Clank games.
- [RacREpo](https://github.com/CreepNT/RacREpo) - Research hub collecting reverse-engineering scripts, tools, and documentation for the Ratchet & Clank series.
- [RCHooker](https://github.com/CreepNT/RCHooker) - Plugin for reverse engineering and modding Ratchet & Clank (PS Vita).
- [RCFiosOverlay](https://github.com/CreepNT/RCFiosOverlay) - SceFios2 filesystem overlay for loading modded assets in Ratchet & Clank HD (PS Vita).
- [ReChimera](https://github.com/Mrroboto9819/ReChimera) - Offline level inspector and asset extractor for Insomniac's PS3 titles (Resistance: Fall of Man, Resistance 2, Resistance 3, Ratchet & Clank: Tools of Destruction, A Crack in Time, All 4 One); decodes level meshes, textures, skeletons, animations and sound banks for preview and export from extracted `.psarc` contents.
- [Insomniac_Blender](https://github.com/Tzeentchnet/Insomniac_Blender) - Blender 5.2+ extension importing models, materials, animations and levels from Resistance: Fall of Man, Resistance 2/3 and Ratchet & Clank Future: Tools of Destruction (PS3), plus experimental Resistance: Burning Skies (PS Vita) support; reads from a decrypted disc image or extracted PSARC archives.

###### Spyro the Dragon

- [spyroedit](https://github.com/LXShades/spyroedit) - Emulator plugin for modifying Spyro the Dragon games on PlayStation 1. Compatible with Windows emulators such as ePSXe and PCSX. Features include editing level textures and colors, replacing level skies, modifying object properties, and editing scenery positions.
- [spyro-1 (decomp)](https://github.com/TheMobyCollective/spyro-1) - Matching decompilation of Spyro the Dragon.
  - Same organization's matching decompilations of the other PS1 games: [spyro-2](https://github.com/TheMobyCollective/spyro-2) (Spyro 2: Ripto's Rage!, NTSC-U) and [spyro-3](https://github.com/TheMobyCollective/spyro-3) (Spyro: Year of the Dragon, NTSC-U).
- [noclip.website (Spyro)](https://github.com/magcius/noclip.website/tree/main/src/Spyro) - In-browser level viewer for the PS1 Spyro trilogy (Spyro the Dragon, Spyro 2: Ripto's Rage!, Spyro: Year of the Dragon), parsing the games' WAD subfile geometry, sky, and texture-tile data. Data structures derived from Kly_Men_COmpany's Spyro World Viewer.
- [Spyro-Scope](https://github.com/FranklyGD/Spyro-Scope) - Program that peers into the PS1 Spyro games' data, converting it for easier viewing and analysis (archived).
- [game-re-patterns](https://github.com/egartley/game-re-patterns) - ImHex patterns for file formats of the PS1 Spyro games and Spyro: Enter the Dragonfly (`dat1`, `geom`, `list`, `mrb`, `pxt`), plus Meet the Robinsons `.dbl`; incomplete and not fully accurate by the author's own account.
- [RCRA Forge](https://github.com/ROStudios25/RCRA-Forge) - Standalone Python/PyQt6 asset browser and model exporter for Ratchet & Clank: Rift Apart (PC), browsing 340,000+ assets and exporting models/zones to glTF/GLB/OBJ/FBX with correct skeletons, skin weights, UVs, and textures, without Ninja Ripper.
- [rac-modding-resources](https://github.com/RatchetModding/rac-modding-resources) - Curated list of resources for modding and reverse engineering the Ratchet & Clank series.
- [Mr.Zurkon](https://github.com/Ret-HZ/Mr.Zurkon) - Multi-tool for Ratchet & Clank: Size Matters and Secret Agent Clank (PSP), including PAKTool for PAK archives containing GIM images and Relocalizer for LOC_DATA localization files.

##### SIE Japan Studio (Ape Escape)

- [ApeEscapeRecomp](https://github.com/mstan/ApeEscapeRecomp) - Static recompilation of Ape Escape (PS1) into native code.
- [salvatoreExtract](https://github.com/hypermegacrash/salvatoreExtract) - Extractor for the PackInfo archive files (DATA0/DATA2/DSKIMG.BIN) used by Ape Escape: Pumped & Primed and Ape Escape: Million Monkeys (PS2).
- [MMTextGadget](https://github.com/hypermegacrash/MMTextGadget) - English fan translation patch for Ape Escape: Million Monkeys (PS2, Japan-only), building a patched ISO from extracted DATA0/DATA1 game files.

##### Gravity Rush 2

- [EVD Editor](https://github.com/LyokoUnite/EVD-Editor) - PyQt5 GUI tool for browsing, editing, and exporting Japan Studio's Gravity Rush 2 `.evd` files.
- [GR2-gfx-extractor](https://github.com/Team-Alua/GR2-gfx-extractor) - Noesis plugin for Gravity Rush 2 GFX model files: meshes, bones, weights, normals, vertex colors, texture names, and object locators; needs the GravityRush-Common plugin.

##### Flipnic

- [FlipnicDecomp](https://github.com/MarkusMaal/FlipnicDecomp) - Decompilation of Flipnic: Ultimate Pinball (PS2, Sony Computer Entertainment Japan/SIE Japan Studio), created with Ghidra; not a full decompilation, aimed at reverse engineering file formats and cheat codes.
- [FlipnicFileTools](https://github.com/MarkusMaal/FlipnicFileTools) - Command-line tools with a GUI front-end for Flipnic's file formats, covering ISO disc images, `.BIN` blob virtual filesystem containers, and `.PSS` movie containers (demuxing/remuxing FMVs, including custom video). Supersedes the author's earlier FlipnicBinExtractor and flipnicfs tools.
- [FlipnicPatterns](https://github.com/MarkusMaal/FlipnicPatterns) - ImHex hex patterns documenting Flipnic's file formats.
  - Formats: BIN/folder (virtual filesystem), FPC (camera sequences), HD (VAB soundbank header), IPU (video streams), LP4 (3D models/2D text animations), MSG (strings), PSS (audio/video container), save file, SST (stage definitions), SVAG/INT (Sony ADPCM audio), TM2 (textures), save icon.
- [FlipnicSaveEditor](https://github.com/MarkusMaal/FlipnicSaveEditor) - JavaFX GUI save file editor for Flipnic, covering rank/options/unlock editing, checksum regeneration for corrupted saves, and creating hybrid saves across regions.

##### Naughty Dog

###### Crash Bandicoot Series

- [ReBandicoot](https://github.com/kohtep/ReBandicoot) - Reverse engineering tools for Crash Bandicoot.
- [Crash-Bandicoot-Resources](https://github.com/Helias/Crash-Bandicoot-Resources) - Comprehensive collection of resources for Crash Bandicoot file formats and reverse engineering. Covers N. Sane Trilogy, Twinsanity, Crash Team Racing, Crash Bash, and original PS1 trilogy. Includes documentation for extracting/modifying PAK archives, IGZ models, NSD/NSF files, plus links to 30+ specialized tools, character mods, decompilation projects, and modding frameworks.
- [CTR-tools](https://github.com/CTR-tools/CTR-tools) - Toolkit for Crash Team Racing (PlayStation 1) file formats.
- [HowlDataExtractor](https://github.com/xan1242/HowlDataExtractor) - Extracts the NDI HOWL audio files used in Crash Team Racing (currently offset tables and sequence packs; the format is not fully documented), with HowlSeq2Midi to convert the sequence packs to MIDI (unfinished).
- [CrashEdit](https://github.com/cbhacks/CrashEdit) - Level and graphics editor for PlayStation 1 Crash Bandicoot games.
- [crash-bandicoot-nsf](https://github.com/dehodson/crash-bandicoot-nsf) - NSF (Naughty Dog Streaming File) format tools for Crash Bandicoot.
- [Crash-Bandicoot-2-Modelexport](https://github.com/warenhuis/Crash-Bandicoot-2-Modelexport) - Model exporter for Crash Bandicoot 2.
- [crashutils](https://github.com/wurlyfox/crashutils) - Collection of utilities for Crash Bandicoot file formats.
  - Same author's [disgool](https://github.com/wurlyfox/disgool), a disassembler/decompiler for Crash Bandicoot 1 GOOL bytecode (type 11 entries extracted from NSF files), and [c1](https://github.com/wurlyfox/c1), a C port of the game that loads the original disc's NSD/NSF files and documents their entry item formats.
- [noclip.website (Crash Bandicoot: Warped)](https://github.com/magcius/noclip.website/tree/main/src/CrashWarped) - In-browser Crash Bandicoot: Warped viewer.
- [c2c (decomp)](https://github.com/ughman/c2c) - Matching decompilation of Crash Bandicoot 2: Cortex Strikes Back.
- [ctr-native](https://github.com/CTR-tools/ctr-native) - Native (C++) reverse-engineering of Crash Team Racing (PS1).
- [io_ctr_tools](https://github.com/CTR-tools/io_ctr_tools) - Blender plugin for importing CTR: Crash Team Racing (PS1) levels with vertex colors, parsing LEV format via Kaitai Struct.
- [Crash-NST-Level-Editor](https://github.com/kishimisu/Crash-NST-Level-Editor) - Level editor, archive editor, and mod manager for Crash Bandicoot N. Sane Trilogy.
- [CrashBashEx](https://github.com/xan1242/CrashBashEx) - Extractor for Crash Bash archive/music files.
- [OpenSanityNeo](https://github.com/NeoKesha/OpenSanityNeo) (archived) - Crash Twinsanity (Xbox, PAL) decompilation/disassembly project using Ghidra and code generation, aiming for an accurate rebuildable disassembly.
- [crash-ps2 (decomp)](https://github.com/calmsacibis995/crash-ps2) - Matching decompilation of Crash Bandicoot: The Wrath of Cortex (PS2).
- [LibTWOC](https://github.com/Open-Travelers/LibTWOC) - C# library for reading and writing the file formats used by Crash Bandicoot: The Wrath of Cortex. See also [twoc-tools](https://github.com/NoahStolk/twoc-tools), a cross-platform tool built on this library.
- [travelers-toolkit](https://github.com/Open-Travelers/travelers-toolkit) - C++/ImGui level viewer for Crash Bandicoot: The Wrath of Cortex, parsing compressed `.gsc` (or raw `.nus` on GameCube) scene files extracted from the disc; aims to grow into a full level editor.
- [C1 Browser Runtime](https://github.com/metadate1/c1-browser-runtime) - C/WebAssembly runtime building the original 1996 PlayStation Crash Bandicoot's engine lineage to run in a browser, using data read from your own game disc.
- [CRUST](https://github.com/metadate1/crust) - Independent Rust/WebAssembly compatibility runtime for the original 1996 PlayStation Crash Bandicoot, also running in a browser and reading data from your own game disc.

###### Jak and Daxter

- [jak-project](https://github.com/open-goal/jak-project) - OpenGOAL: reimplementation of the GOAL compiler/runtime and a native PC port for the Jak and Daxter series, built by reverse-engineering the original game code and data.
- [goaldis](https://github.com/rmitton/goaldis) - Standalone disassembler that dumps all code and data from a PlayStation 2 Jak & Daxter disc into GOAL assembly listings.
- [jak1-vag-splitter](https://github.com/blahpy/jak1-vag-splitter) - Tool for splitting VAG audio files from Jak and Daxter 1.
- [JakAndDaxter1Sound](https://github.com/efimandreev0/JakAndDaxter1Sound) - Sound extraction and playback tool for Jak and Daxter 1.
- [Blender-Script-JaD-Actors](https://github.com/innocentmiau/Blender-Script-JaD-Actors) - Blender script for importing Jak and Daxter actor models.
- [JakAudioTools](https://github.com/jwetzell/JakAudioTools) - Audio extraction and conversion tools for Jak and Daxter series.
- [JakAudioTool](https://github.com/LuminarLight/JakAudioTool) - GUI tool for working with Jak and Daxter audio files.
- [pcsx2-opengoal-texture-port-tools](https://github.com/lorenfa99/pcsx2-opengoal-texture-port-tools) - Scripts for mapping PCSX2 HD texture packs to OpenGOAL/native PC texture replacements for the Jak and Daxter series.

###### Uncharted

- [U4.PSARC.Tool](https://github.com/Ekey/U4.PSARC.Tool) - PSARC archive extractor for UNCHARTED: Legacy of Thieves Collection (requires Oodle library).
- [big2-ps3-pak-research](https://github.com/icemesh/big2-ps3-pak-research) - PAK format specification and loader function for Uncharted 2: Among Thieves (PS3).
- [big4-pak-research](https://github.com/icemesh/big4-pak-research) - PAK format specification and loader function for Uncharted 4.
- [big4-dc-disasm](https://github.com/icemesh/big4-dc-disasm) - Disassembler for Uncharted 4 scripts.

###### The Last of Us

- [t1-ps3-pak-research](https://github.com/icemesh/t1-ps3-pak-research) - PAK format specification and loader function for The Last of Us (PS3).
- [t1x-pak-research](https://github.com/icemesh/t1x-pak-research) - PAK format specification and loader function for The Last of Us Part I.
- [t1ps4-dc-disasm](https://github.com/icemesh/t1ps4-dc-disasm) - Disassembler for The Last of Us (PS4) scripts.
- [t2-dc-disasm](https://github.com/icemesh/t2-dc-disasm) - Disassembler for The Last of Us Part II scripts.
- [TLOU_PSARC_Tool](https://github.com/amrshaheen61/TLOU_PSARC_Tool) - Imports and exports raw assets from The Last of Us PSARC archives.
- [t2-pak-research](https://github.com/icemesh/t2-pak-research) - PAK format specification and loader function for The Last of Us: Part II.
- [tlou-factions-server](https://github.com/comradesean/tlou-factions-server) - Self-hosted revival server and protocol reverse-engineering project bringing The Last of Us: Factions (PS3, BCUS98174) back online under RPCS3.

###### Engine & Format Tools (Multi-Game)

- [drnsf](https://github.com/cbhacks/drnsf) - Format research tool for Naughty Dog games including Crash.
- [nd_pak.bt](https://github.com/alphazolam/nd_pak.bt) - 010 Editor template for Naughty Dog PAK files.
- [fmt_nd_pak](https://github.com/alphazolam/fmt_nd_pak) - Noesis plugin for Naughty Dog PAK assets.
- [UnPSARC](https://github.com/rm-NoobInCoding/UnPSARC) - Python tool for extracting PSARC files.
- [StringId](https://github.com/icemesh/StringId) - Code for generating valid stringIds for various Naughty Dog games.
- [dc](https://github.com/icemesh/dc) - Format specification (work in progress) for the script files used in the Naughty Dog Engine.
- [sidbase-dumper](https://github.com/icemesh/sidbase-dumper) - Extracts data from sidbase.bin files used in the Naughty Dog engine.
- [TLOU_PSARC_Tool](https://github.com/5l41dev/TLOU_PSARC_Tool) - Extraction/repacking tool for The Last of Us PSARC archives.
- [NaughtyDogLocalizationTool](https://github.com/rm-NoobInCoding/NaughtyDogLocalizationTool) (archived) - Exports and imports localization files (`.subtitles`, `.common`, `.subtitles-systemic`, `.web`) across all Naughty Dog games (Uncharted and The Last of Us series) on PS3, PS4, PS5, and PC.

##### Polyphony Digital

- [GTAllPaintEditor](https://github.com/Nenkai/GTAllPaintEditor) - Tool to edit Gran Turismo 6's allpaint.bin file for assigning custom paints to cars through GT Auto.
- [gt2-reversing](https://github.com/ginryuoku/gt2-reversing) - Reverse engineering tools for Gran Turismo 2.
- [PDTools](https://github.com/Nenkai/PDTools) - Utilities for extracting and modifying Gran Turismo game files.
- [GranTurismoENGNEditor](https://github.com/TheAdmiester/GranTurismoENGNEditor) - Editor for creating and editing ENGN (.es) files, containers of Sony HEVAG engine and exhaust sound loops, for PS1 and PS2 Gran Turismo games.
  - Newer games: [GTESGXEditor](https://github.com/TheAdmiester/GTESGXEditor) extracts, edits and builds the .esgx vehicle sound files of Gran Turismo 5/6 (the format PSP, 5 and 6 use), and [GTESDExtractor](https://github.com/TheAdmiester/GTESDExtractor) extracts audio banks (.sxd) and RPM data from Gran Turismo Sport's GTESD files.
- [GT4SaveEditor](https://github.com/Nenkai/GT4SaveEditor) - Save editor for Gran Turismo 4.
- [esprima-dotnet](https://github.com/Nenkai/esprima-dotnet) - Fork of Esprima .NET to target the scripting language for Gran Turismo series, Adhoc.
- [GT-File-Specifications-Documentation](https://github.com/Nenkai/GT-File-Specifications-Documentation) - File specifications and documentation for various Gran Turismo file types.
- [gtseq2midi](https://github.com/xan1242/gtseq2midi) - Converts Gran Turismo sequence files to MIDI.
- [gtarctool](https://github.com/xan1242/gtarctool) - Extracts and repacks Polyphony Digital GT-ARC archives, with filename-list support for archives that ship one (such as MENU_RAW.ARC); tested only with Gran Turismo 1 NTSC-J, and LZSS compression/decompression is not implemented.
- [GT2SaveEditor](https://github.com/zyzalfors/GT2SaveEditor) - Save file editor for Gran Turismo 2.
- [GT3SaveEditor](https://github.com/zyzalfors/GT3SaveEditor) - Save file editor for Gran Turismo 3.
- [GT5SaveEditor](https://github.com/zyzalfors/GT5SaveEditor) - Save file editor for Gran Turismo 5.
- [gt7tool](https://github.com/flatz/gt7tool) (archived) - Decrypts and unpacks files from Gran Turismo 7 archives.
- [gttool](https://github.com/flatz/gttool) - Earlier unpacking/decryption tool for Gran Turismo volume archives, predating gt7tool.
- [Blender-GT-Tonemapper](https://github.com/festivities/Blender-GT-Tonemapper) - Blender implementation of the Gran Turismo series' in-game tone mapping, for previewing datamined assets under the game's actual color grading.

##### Santa Monica Studio

- [god_of_war_browser](https://github.com/mogaika/god_of_war_browser) - WebGL-based in-browser viewer for God of War I/II (PS2/PS3/Vita) models and textures. See also [god_of_war_editor](https://github.com/mogaika/god_of_war_editor), the same author's newer version with an improved interface (God of War I, PS2 NTSC only); both are maintained in parallel as god_of_war_editor doesn't yet implement all of god_of_war_browser's features.
- [GOWTool](https://github.com/kainotoa/GOWTool) - Asset browser and extractor for God of War (2018). Supports viewing and extracting meshes, textures, and other resources.
- [God of War 2018 PS4 Tools](https://forum.xentax.com/viewtopic.php?f=16&t=22897) - XeNTaX forum discussion and extraction tools for God of War (2018) on PlayStation 4. *(Link archived/dead)*
- [GowUnreal](https://github.com/Inori/GowUnreal) - Exports God of War (2018) scene resources with correct positioning and imports them into Unreal Engine 5, with an accompanying UE5 plugin to save resources as uasset files.

##### Sucker Punch

- [sly1 (decomp)](https://github.com/TheOnlyZac/sly1) - Matching decompilation of Sly Cooper and the Thievius Raccoonus (PS2).
- [SlyTools](https://github.com/VelocityRa/SlyTools) - Sly Cooper (PS2/PS3 games) modding tools & research
- [Sly2ModelRE](https://github.com/froggestspirit/Sly2ModelRE) (archived) - Researching the model format in Sly 2: Band of Thieves.
- [sly_dec.py](https://github.com/yukinogatari/Reverse-Engineering/blob/573fc1c20796fb40a982f11dfda4039eb480a34e/Sly%20Cooper/sly_dec.py) - Python script for decrypting Sly Cooper files.
- [fmt_GoT_SPS-Noesis-Plugin](https://github.com/SilverEzredes/fmt_GoT_SPS-Noesis-Plugin) - Noesis plugin for Ghost of Tsushima assets.
- [PS23DFormat (Sly 2)](https://web.archive.org/web/20160205080914/http://ps23dformat.wikispaces.com/Sly+2+Band+of+Thieves) - Archived documentation for Sly 2 3D format.
- [PS23DFormat Wiki Archive](https://archive.org/details/wiki-ps23dformat.wikispaces.com) - Complete archive of PS23DFormat wiki covering PS2 3D formats.
- [cane](https://github.com/detolly/cane) - Work-in-progress level editor for Sly Cooper series with reverse-engineered level format parsing for modding.
- [SlyCineTrainer](https://github.com/slynders/SlyCineTrainer) - Trainer for creating camera animations in Sly Cooper games.

##### Other First Party / Japan Studio

- [medievil-decomp (decomp)](https://github.com/medievildecompilation/medievil-decomp) - Matching decompilation of MediEvil (PS1).
- [DriveClubFS](https://github.com/Nenkai/DriveClubFS) - Unpacks files from DriveClub .ndx + .dat file system (PS4). Also supports extracting binary resources, XMLs and textures from .rpk resource packs. Supports versions 1.00, 1.28, and NPXX51272 (Alpha/Proto Build).
- [RORPSPTOOL](https://github.com/leeao/RORPSPTOOL) - Cars Race-O-Rama PSP/DS .mif/.rbh archive tools.
- [pysx](https://github.com/cmbasnett/pysx) - Python Final Fantasy VII (PSX) file extraction and conversion tools.
- [Severed Chains](https://github.com/Legend-of-Dragoon-Modding/Severed-Chains) - Decompilation and reverse-engineered reimplementation of Legend of Dragoon (PS1), ported to PC/Mac/Linux/Steam Deck, reading and parsing the original game's disc data files.
  - Ecosystem: [Dragoon-Modifier](https://github.com/Legend-of-Dragoon-Modding/Dragoon-Modifier) (RAM editor), [lodmods](https://github.com/Legend-of-Dragoon-Modding/lodmods) (modding tools), [Script-Recompiler](https://github.com/Legend-of-Dragoon-Modding/Script-Recompiler) (disassembler for the game's scripting engine), and [Font-Editor](https://github.com/Legend-of-Dragoon-Modding/Font-Editor) (font viewer/editor, WIP).
- [libxb](https://github.com/kiwi515/libxb) - Python library for the ClapHanz XB archive format, used by Everybody's Golf/Hot Shots Golf and other ClapHanz-developed titles.

###### Team Ico (Ico / Shadow of the Colossus)

- [ico-decomp (decomp)](https://github.com/rossydoubleunderscore/ico-decomp) - Matching decompilation of Ico (PS2).
- [SOTC (decomp)](https://github.com/Fantaskink/SOTC) - In-progress decompilation of the preview build of Shadow of the Colossus (PS2).
- [ICOview](https://github.com/aap/ICOview) - Map viewer for Ico (PS2), reading the game's original level data files.
- [SotC-XFF-Analyzer](https://github.com/InconspicuousCactus/SotC-XFF-Analyzer) - Reads XFF symbol files from Shadow of the Colossus (PS2), merging them into a Ghidra-loadable binary and generating disassembly for comparison against a recompilation on decomp.me.
- [dormin](https://github.com/Lenbok/dormin) - Character animation player, geometry viewer and audio decoder for Shadow of the Colossus; indexes models, textures, skeletons and animations from the game's data files (clone of the original repo.or.cz repository).

###### LittleBigPlanet

- [NLG-File-Editor-Tool](https://github.com/KillzXGaming/NLG-File-Editor-Tool) - Simple tool to extract and edit files from .dict/data archives used in LittleBigPlanet 2.
- [RSBR.PAK.Tool](https://github.com/Ekey/RSBR.PAK.Tool) - Tool for extracting PAK (OBB) archives from mobile game Run Sackboy! Run! (Android/iOS).
- [Craftworld Toolkit](https://github.com/ennuo/toolkit) - Extended version of [philosophofee's farctool2](https://github.com/hellfire3d/farctool2) for modding the mainline LittleBigPlanet series. Reads and edits gamedata files/resources, views/exports textures and models (OBJ, glTF 2.0), edits saves and story/extra-content packs, and installs/exports mod files.
- [ufg](https://github.com/ennuo/ufg) - Tools for working with games made by United Front Games (ModNation Racers, LittleBigPlanet Karting). See also [ufg.js](https://github.com/ennuo/ufg.js), a JavaScript port of the format library.
- [lbparc](https://github.com/ennuo/lbparc) - Unpacks archives from LittleBigPlanet PSP.
- [TLoD-Texture-Converter](https://github.com/dragoonsouls/TLoD-Texture-Converter) - Texture converter/previewer for The Legend of Dragoon (PS1), decoding TIM, MCQ (skybox), and PXL (submap object) texture formats to PNG from Severed Chains file dumps.
- [TLoD-Assets-Manager](https://github.com/dragoonsouls/TLoD-Assets-Manager) - Manages The Legend of Dragoon (PS1) game assets (textures, models, animations).
- [TLoD-TMD-Converter](https://github.com/dragoonsouls/TLoD-TMD-Converter) - Converts The Legend of Dragoon's TMD model format to DAE.
- [Blender-Anim-To-TLoD](https://github.com/dragoonsouls/Blender-Anim-To-TLoD) - Blender 2.80 addon for converting object animations into The Legend of Dragoon's SAF (Simple Animation Format).
- [DEFF-Basic-Unpacker](https://github.com/dragoonsouls/DEFF-Basic-Unpacker) - Unpacker for The Legend of Dragoon's DEFF archive format.

##### Sony Online Entertainment

- [Holocore](https://github.com/ProjectSWGCore/Holocore) - Star Wars Galaxies server emulator for the Combat Upgrade (CU) era.
- [Sanctuary](https://github.com/Open-Source-Free-Realms/Sanctuary) - Server emulator for Free Realms research, and [LibSOE](https://github.com/Joshsora/LibSOE) networking library.
- [FreeRealmsUnpacker](https://github.com/Udaya-X2/FreeRealmsUnpacker) - Browses and extracts assets from Free Realms asset files (.pack/.dat, including the PS3 and TCG assets), with GUI and CLI. Also creates and appends asset files, adds/deletes/validates assets, and repairs corrupted .pack.temp files.
  - [FreeRealmsLocaleTools](https://github.com/Udaya-X2/FreeRealmsLocaleTools) - .NET library reading and writing text entries in Free Realms locale files (`<locale>_data.dat`/`.dir`), with name-ID lookup and locale metadata editing.
  - [FreeRealmsMapMaker](https://github.com/Udaya-X2/FreeRealmsMapMaker) - Console tool that creates maps from Free Realms `*_TileInfo.txt` and `*_Tile_*.dds` tile assets.
- [FLATool](https://github.com/psforever/FLATool) - Extractor and packer for FlatFile archives (.FAT), used by PlanetSide 1 to store .DDS files.
- [PSPack](https://github.com/psforever/PSPack) - Extracts and repacks PlanetSide 1 Pack files (.PAK).
- [ADBExtractor](https://github.com/psforever/ADBExtractor) - Extracts PlanetSide 1's .ADB ASCII database file format.
- [Raxicore Editor](https://github.com/psforever/raxicore-editor) - Cross-platform viewer/editor/unpacker for PlanetSide 1's client-side asset formats.
  - Formats: PACK archives (.pak, LZO1X-compressed), FLAT archives (.fat/.fdx), UberMesh models and skeletal animations (.ubr), ASCII databases (.adb), surface-type tiles (.srf), map manifests (contents_mapNN.mpo), and DDS textures.
  - Features: offscreen-Vulkan 3D viewport, continent assembly from map manifests, per-material texture picker with faction (NC/TR/VS) skin swapping, skeletal animation playback, and OBJ+MTL mesh export.
- [warpgate](https://github.com/ryanjsims/warpgate) - C++ model exporter for PlanetSide 2's Forgelight engine assets.
  - [synthium](https://github.com/ryanjsims/synthium) - C++ library for extracting assets from PlanetSide 2's `.pack2` archive files, used by warpgate above.
  - [dbg-pack](https://github.com/ryanjsims/dbg-pack) - Python library for reading PlanetSide 2's legacy `.pack` and `.pack2` archive formats; actively-maintained fork adding convenience search/save methods and multiprocessing for faster loading.
- [vanguard-saga-of-heroes-asset-extractor](https://github.com/brynnb/vanguard-saga-of-heroes-asset-extractor) - Extracts, converts, and exports 3D models, animations, audio, and other assets from Vanguard: Saga of Heroes, an Unreal Engine 2.5 MMORPG.
- [eqsage](https://github.com/knervous/eqsage) - Converts EverQuest S3D/EQG assets on the fly to render them in the browser; includes a zone database editor and viewer.
- [eqrequiem](https://github.com/knervous/eqrequiem) - Brings EverQuest to the browser using the BabylonJS engine and Go, converting and extracting the original game's assets.
- [eq-three-js-zone-viewer](https://github.com/brynnb/eq-three-js-zone-viewer) - Python-based converter for extracting, converting, and viewing classic EverQuest game assets in a browser with three.js.
- [EYE_extractor](https://github.com/ExIfDev/EYE_extractor) - Extracts .eye archives from Lords of EverQuest.
- [SWGMayaPlugin](https://github.com/janglesworthy/SWGMayaPlugin) - Autodesk Maya 2024/2027.2 plugin package for Star Wars Galaxies asset import/export, including helper executables, blend shape and POB (portal object block) tooling, and batch queue support.
- [SchematicDump](https://github.com/ProjectSWGCore/SchematicDump) - Dumps ingredient slots and crafting attribute data from Star Wars Galaxies' draft schematic .iff files to text.
- [LanternExtractor](https://github.com/LanternEQ/LanternExtractor) - EverQuest Trilogy client S3D asset extractor, converting encoded game data into formats usable in modern game engines.
- [quail](https://github.com/xackery/quail) - Command-line EverQuest asset manager (archived, early-preview status): zip/unzip PFS archives (EQG, S3D, PAK, PFS), converts between PFS archives and the .quail/WCE (WorldCom Emu) folder format, and inspects binary WLD/MOD/MDS files.
- [LanternUnityTools](https://github.com/LanternEQ/LanternUnityTools) - EverQuest zone/object/character/equipment importer and visualization toolset for the Unity engine, built on intermediate format exports from LanternExtractor above.
- [EQZip](https://github.com/Shendare/EQZip) - Windows EverQuest archive manager that creates, loads, and saves .S3D, .EQG, .PFS, and .PAK packages, with texture thumbnails (RGB16/24/32, DXT1-5, V8U8) and automatic conversion between .dds and PNG/GIF/BMP/JPG on import and export.
- [eqgzi](https://github.com/xackery/eqgzi) (archived) - Command-line EverQuest .eqg zone importer for EQEmu zone making, converting Blender-exported .obj zones to EQG (water, lava, PvP, and zoneline regions, material shader properties); based on Zaela's EQG zone importer and requires Blender 3 or older.
- [EQGWeaponModelImporter](https://github.com/Zaela/EQGWeaponModelImporter) - Windows GUI viewer and importer for EQEmu that builds EverQuest .eqg weapon and shield models (.mod) with particle effects (.prt/.pts) from .obj and .ply meshes.
- [ascii-blender](https://github.com/xackery/ascii-blender) - Blender scripts that parse EverQuest ASCII WLD data (WCE, WorldCom Emu format) into Blender assets, handling material and sprite definitions, hierarchical skeletons, tracks, and polyhedra.
- [OpenEQ (Rust)](https://github.com/daeken/OpenEQ) - Rust and Bevy EverQuest client that reads the original game assets, including classic WLD zones, EQG zones (EQGZ v1/v2), EQTZP heightmap terrain, EQG models and water materials, and original UI and audio.

##### Evolution Studios

- [motorstorm-modding-resources](https://github.com/regallll/motorstorm-modding-resources) - WIP modding resources and filetype notes for MotorStorm games (PS3, PS Vita).
- [mspr-save-uncorrupter](https://github.com/regallll/mspr-save-uncorrupter) - Fixes corrupted MotorStorm: Pacific Rift save files, including the common freeze-on-load issue for the Wreckreation event.
- [WRCEvoTools](https://github.com/igorciz777/WRCEvoTools) - Tools for files found in WRC games developed by Evolution Studios (PS2).

##### Bend Studio

- [HG2PatchCreator](https://github.com/icemesh/HG2PatchCreator) - Tool for creating a valid patch.bin for Uncharted: Golden Abyss (PS Vita).
- [SFTOS-TDX-Converter](https://github.com/RaiRaiTheRaichu/SFTOS-TDX-Converter) - Converts `.txd` texture files (4bpp, 8bpp, and swizzled) from Syphon Filter: The Omega Strain (PS2) to PNG.
- [hogger](https://github.com/rajkosto/hogger) - Packer/unpacker for the HOG archive format used by Syphon Filter: The Omega Strain (PS2).
- [SF3UNP](https://github.com/DenGameRU/SF3UNP) - Delphi extractor for the sector-based `.HOG` and `.FOG` resource containers of the PS1 game Syphon Filter 3.

##### SuperBot Entertainment

- [PSAS-Vita-Noesis](https://github.com/Cri4Key/PSAS-Vita-Noesis) - Noesis import script for PlayStation All-Stars Battle Royale models.

#### CampFire Studio (Soulmask)

- [SoulmaskDataMiner](https://github.com/CrystalFerrai/SoulmaskDataMiner) - Command-line program for gathering data from Soulmask's Unreal Engine game assets.
- [EditSoulmaskSave](https://github.com/CrystalFerrai/EditSoulmaskSave) - Command-line tool for querying and modifying Soulmask save files.

#### Bugbyte (Space Haven)

- [Space-Haven-Save-Game-Editor](https://github.com/moragar360/Space-Haven-Save-Game-Editor) - Save editor suite for Space Haven, covering new-game setup, save file management, and ship blueprint editing.
- [space-haven-editor](https://github.com/MoltenCoffee/space-haven-editor) - Browser-based savegame editor for Space Haven (versions 0.12.2/0.12.3), reading and rewriting save data without installing a desktop app.

#### Elemental Games (Space Rangers)

- [SRHD XenoModKit](https://github.com/Xenomorphchyma/SRHD-XenoModKit) - Headless modding toolkit for Space Rangers HD: A War Apart.
  - Formats: BlockPar DAT, RSON, modular RSM, legacy SVR/SCR, GI/PNG image conversion, GAI/HAI/PKG archives, QM/QMM text quests.
  - Features: Full mod validation with a reproducible SHA-256-manifested ZIP build, deterministic GAI/PKG packing, CacheData/Main.dat script-registration consistency checks, and CP1251/UTF-8 corrupted-text detection.

#### NoriaWorks Entertainment (Speed Haste)

- [SpeedHasteSrc](https://github.com/TheJare/SpeedHasteSrc) - Original C source code for Speed Haste (1995), released into the public domain by the game's own developer, Javier Arevalo Baeza.
- [Speed](https://github.com/jval1972/Speed) - Remake/source port of Speed Haste (1995, NoriaWorks Entertainment, published by Friendware), reading the original DOS game's data files.
- [SpeedEd](https://github.com/jval1972/SpeedEd) - Tile/level editor for Speed Haste.

#### Speed Racer

- [SpeedRacerTool](https://github.com/Kermalis/SpeedRacerTool) - Tool to rip models from Speed Racer (PS2/Wii).

#### Spike Chunsoft

- [nonary-mods-tools](https://github.com/samsungapore/nonary-mods-tools) - Extracts, translates, rebuilds and checks the 60 system messages in `data/etc/sysmes.dat` of the Nintendo DS release of Nine Hours, Nine Persons, Nine Doors (fixing the byte-position references that text edits would break), and adds accented font characters to four system-font files and replaces the Yes/No and empty-save labels.

##### Danganronpa

- [ronpaTool](https://github.com/LinkOFF7/ronpaTool) - Tool for extracting files from .wad, .obb, and .ab containers for Danganronpa 1 and 2 (Android versions).
- [Danganronpa-Another-Tool](https://github.com/Liquid-S/Danganronpa-Another-Tool) - Romhacking tool for extracting and repacking PAK archives (both text/script and texture variants) across Danganronpa: Trigger Happy Havoc, Danganronpa 2, and Danganronpa Another Episode (PSP/PSVita/PC/PS4), with PNG-to-BTX texture conversion.
- [RSCTTool](https://github.com/LinkOFF7/RSCTTool) - Converter between Danganronpa V3/SS RSCT and TXT files.
- [DRV3-Sharp](https://github.com/CaptainSwag101/DRV3-Sharp) - Tool and library for working with various file formats from Danganronpa V3 for PC, actively maintained successor to the archived DRV3-Tools.
- [DRV3-STX-TOOL](https://github.com/Liquid-S/DRV3-STX-TOOL) - Extracts and repacks Danganronpa V3's STX dialogue files to/from gettext `.po` for translation, given STX/WRD pairs obtained via DRV3-Sharp or SpiralFormats above.
- [Harmony-Tools](https://github.com/redssu/Harmony-Tools) - Collection of tools to help translate Danganronpa V3: Killing Harmony.
- [V3SaveManager](https://github.com/IndacoSub/V3SaveManager) - C# save editor with a GUI for Danganronpa V3: Killing Harmony; work in progress, tested with the legacy Steam PC version.
- [SpiralFormats](https://github.com/UnderMybrella/SpiralFormats) - Core format library for SPIRAL, a Danganronpa modding framework.
- [Danganronpa-Modding](https://github.com/BitesizeBird/Danganronpa-Modding) - Documentation of Danganronpa 2's DAT/LIN opcode formats, GMO model format, and other file structures, with Nonstop Debate DAT converters and voice-line extraction utilities.
- [danganronpa-tools](https://github.com/vn-tools/danganronpa-tools) - LIN script compiler/decompiler (Danganronpa 1 and 2) plus WAD and PAK archive packers/unpackers for the Danganronpa PC releases (archived).
- [Ultra-Despair-Extractor](https://github.com/ContinualDissapointment/Ultra-Despair-Extractor) - Open native extractor for Danganronpa Another Episode: Ultra Despair Girls (PC), converting .cpk/.bnc/.btx files to posed, UV-mapped, textured .obj models.

##### Kamaitachi no Yoru

- [kamaitachi-sfc-english](https://github.com/ButThouMust/kamaitachi-sfc-english) - Fan translation project for Kamaitachi no Yoru (Chunsoft, SNES), working with the game's original script and ROM data formats.
- [otogirisou-english](https://github.com/ButThouMust/otogirisou-english) - Fan translation patch project for Otogirisou (Chunsoft, Super Famicom, 1992), reverse-engineering the original sound novel's script and font data.
- [otogirisou-tools](https://github.com/ButThouMust/otogirisou-tools) - Translation tooling (script and font extraction/repacking utilities) supporting the Otogirisou (Super Famicom) fan translation project.
- [DRV3-Tools](https://github.com/CaptainSwag101/DRV3-Tools) (archived) - Toolset for Danganronpa V3's original archive and script formats.

##### Fushigi no Dungeon: Fuurai no Shiren Gaiden

- [Shiren_DataBG_ext](https://github.com/VincentNLOBJ/Shiren_DataBG_ext) - Extracts and converts all images from the Dreamcast game's `DATABG.bin` and rebuilds it with LZ40 compression, preserving the palettes of indexed map-name images.

#### 1047 Games (Splitgate)

- [SplitgateReplayReader](https://github.com/Shiqan/SplitgateReplayReader) - C# parser for Splitgate's replay files.

#### THQ Studio Australia (SpongeBob SquarePants: Lights, Camera, Pants!)

- [PakTool](https://github.com/seilc/PakTool) - Qt-based archive editor for the `.pak` files used by SpongeBob SquarePants: Lights, Camera, Pants! (GameCube/PS2/Xbox).
- [gm-lcp](https://github.com/seilc/gm-lcp) - Compiles and extracts the GameMonkey Script debug library files embedded in Lights, Camera, Pants!'s archives, supporting both the GameCube and PS2 versions.

#### Sprite

- [Sprite4SteamExtractor](https://github.com/hktkqj/Sprite4SteamExtractor) - Command-line extractor and CG composer for Sprite's encrypted `.dat` visual novel archives. Supersedes the author's earlier single-game Aokana-Extractor, Aokana-Ex2-Extract, and Koichoco-Extractor tools.
  - Games: Aokana: Four Rhythms Across the Blue (base game, Extra 1, Extra 2), Koichoco (Love, Election, and Chocolate).
  - Features: Archive entry listing/extraction (`--list`/`--extract`), multi-game decryption key selection (`--game`), and CG composition from extracted sprite layers (`--combine`).
- [aokana_extra2ct](https://github.com/starjet/aokana_extra2ct) - Extracts files from Aokana `.dat` archives (e.g. `evcg.dat`, `sprites.dat`, `adult.dat`) and composes complete CGs and character sprites with Magick.NET, using bundled face and CG definition data; the author notes parts of the code were copied from the game's assembly via dnSpy and makes no guarantees of correct functionality.

#### Square Enix

*Many titles use [CRI](middleware.md#cri) or [Havok](middleware.md#havok) middleware.*

- [S3Extract](https://github.com/hypermegacrash/S3Extract) - Extractor for the custom PS1 filesystem used by Square Product Development Division 3, covering Xenogears, Chrono Cross, and Dewprism / Threads of Fate (retail .BIN images and demo .IMG/.HED builds).
- [OctopathTraveler](https://github.com/turtle-insect/OctopathTraveler) - Save data editor for Octopath Traveler (Switch).
  - Same author's editors for the sequels: [OctopathTraveler2](https://github.com/turtle-insect/OctopathTraveler2) (Octopath Traveler II, Switch) and [OctopathTraveler0](https://github.com/turtle-insect/OctopathTraveler0) (Octopath Traveler 0).
- [LegendofMana](https://github.com/turtle-insect/LegendofMana) - Save data editor for Legend of Mana (Switch).
- [Setsuna](https://github.com/turtle-insect/Setsuna) - Save data editor for I Am Setsuna (Switch).

##### Final Fantasy

- [FFCC-Decomp (decomp)](https://github.com/zcanann/FFCC-Decomp) - Matching decompilation of Final Fantasy Crystal Chronicles.
- [CrystalEditor](https://github.com/Cuyler36/CrystalEditor) - Savegame editor for the WiiWare title Final Fantasy Crystal Chronicles: My Life as a King.
- [ff7tool](https://github.com/jkbenaim/ff7tool) - Tool for viewing Final Fantasy VII world maps.
- [FF16Tools](https://github.com/Nenkai/FF16Tools) - Tools & Library for Final Fantasy XVI / 16 Engine games (FFXVI, FINAL FANTASY TACTICS - The Ivalice Chronicles).
  - Features: PAC unpacker/repacker, TEX to DDS conversion, DDS/image to TEX, NXD (Nex/ExcelDB) conversion, PZD (Panzer dialogue) conversion, save file unpack/pack, FlatBuffer schemas for KDB (KineDriver) & BNMB (Bonamik).
- [ffxvi-nex-layouts](https://github.com/Nenkai/ffxvi-nex-layouts) - Nex sheet layouts for FINAL FANTASY XVI, for use with FF16Tools.
- [fftivc-nex-layouts](https://github.com/Nenkai/fftivc-nex-layouts) - Nex sheet layouts for FINAL FANTASY TACTICS - The Ivalice Chronicles, for use with FF16Tools.
- [ff16.utility.modloader](https://github.com/Nenkai/ff16.utility.modloader) - Final Fantasy XVI / 16 Mod Loader for Reloaded-II using FF16Tools.
- [fftivc.utility.modloader](https://github.com/Nenkai/fftivc.utility.modloader) - FINAL FANTASY TACTICS - The Ivalice Chronicles Mod loader for Reloaded-II using FF16Tools.
- [FaithFramework](https://github.com/Nenkai/FaithFramework) - Mod Framework for FFXVI using Reloaded-II. Features: ImGui API, Nex Runtime Interface API, Resource Manager, Camera Manager (WorldToScreen/Camera Pos).
- [Lumina](https://github.com/NotAdam/Lumina) - A .NET library for reading and interacting with game data files from Final Fantasy XIV.
- [SaintCoinach](https://github.com/xivapi/SaintCoinach) - A .NET library for extracting and reading game assets from Final Fantasy XIV. Supports SqPack extraction, EXH/EXD data parsing, and texture conversion.
- [Sapphire](https://github.com/SapphireServer/Sapphire) - Research-focused Final Fantasy XIV server emulator (targets version 3.3).
- [FFXIV Explorer](https://github.com/goaaats/ffxiv-explorer-fork) - Modern fork of FFXIV-Explorer with updated support for recent game patches.
- [sharlayan](https://github.com/FFXIVAPP/sharlayan) - Memory reading and scanning library for Final Fantasy XIV.
- [machina](https://github.com/ravahn/machina) - Network capture library for realtime TCP/IP decoding and FFXIV data capture.
- [aetherometer](https://github.com/ff14wed/aetherometer) (archived) - Framework for processing network-level information from Final Fantasy XIV via a GraphQL API.
- [xiv-datamining](https://github.com/xivapi/ffxiv-datamining) - Repository for sharing Final Fantasy XIV datamining information, including CSV exports and documentation on various systems.
  - See also [ffxiv-datamining-ko](https://github.com/Ra-Workspace/ffxiv-datamining-ko) for Korean version specific data.
- [FFNx](https://github.com/julianxhokaxhiu/FFNx) - Next-generation modding platform and graphics enhancement framework for Final Fantasy VII (Steam, 2026 Rerelease, GOG, Windows Store) and Final Fantasy VIII (Steam), supporting DirectX 11/12, OpenGL, and Vulkan.
- [ffvii (decomp)](https://github.com/Drahsid/ffvii) (archived) - In-progress matching decompilation of Final Fantasy VII (PSX).
- [FF16FontMaker](https://github.com/eprilx/FF16FontMaker) - GUI tool for modding fonts in Final Fantasy XVI / 16 Engine games, built on FF16Tools.
- [FFPRSaveEditor](https://github.com/Anub1sR0cks/FFPRSaveEditor) (archived) - Save game editor for the Final Fantasy Pixel Remaster series (FF I-VI).
- [FFPixelRemaster](https://github.com/turtle-insect/FFPixelRemaster) - Save data editor for Final Fantasy Pixel Remaster (Switch).
- [FF1](https://github.com/turtle-insect/FF1) - Save data editor for Final Fantasy (3DS).
- [FF12](https://github.com/turtle-insect/FF12) - Save data editor for Final Fantasy XII (Switch).
- [FFCC](https://github.com/turtle-insect/FFCC) - Save data editor for Final Fantasy Crystal Chronicles (Switch).
- [FF6](https://github.com/camgunz/ff6) - Python library for parsing and declaratively modifying a Final Fantasy VI SNES ROM, including basic first-slot save game editing.
- [ff6 (disasm)](https://github.com/everything8215/ff6) - Disassembly of Final Fantasy VI (Super Famicom, released overseas as Final Fantasy III), building the original ROMs from source.
- [FinFan](https://github.com/aldonunez/FinFan) - Remake of Final Fantasy (NES) in C++/Allegro, with tools that extract resources from the original game into a format usable by the remake's code. See also [FinFan_script](https://github.com/aldonunez/FinFan_script), a fork replacing the C++ NPC event-handling code with a custom scripting language.
- [FF16Converter](https://github.com/KillzXGaming/FF16Converter) - Tools for converting Final Fantasy XVI file formats, including textures (.tex) and subtiles (.pzd).
- [q-gears](https://github.com/q-gears/q-gears) - Cross-platform RPG engine reimplementation targeting Squaresoft's Final Fantasy VII, VIII, IX, and Xenogears. Inactive since 2017.
- [final-fantasy-save-utils](https://github.com/jstephenperry/final-fantasy-save-utils) - Cross-platform save editor for retro Final Fantasy SNES titles, built with .NET and Avalonia.
- [FF3jSRAMEditor](https://github.com/Binarynova/FF3jSRAMEditor) - Save game (SRAM) editor for Final Fantasy III (NES, Japanese release).
- [ff4 (disasm)](https://github.com/everything8215/ff4) - Disassembly of Final Fantasy IV (Super Famicom, released overseas as Final Fantasy II), building the original ROM from source.
- [ff4kster](https://github.com/pinkpuff/ff4kster) - ROM editor and hacking tool for Final Fantasy IV (FF2US v1.1), covering spells, characters, jobs, items, shops, maps/tilesets, monsters, battle formations, and event scripts, reading graphics directly from the ROM.
- [gamingway](https://github.com/pinkpuff/gamingway) - Python library for reading and modifying Final Fantasy IV (FF2US v1.1) SNES ROMs, exposing spells, spellbooks, items, equips, characters, monsters, map/tileset, and overworld tile data as structured objects for building custom rom-hacking tools and randomizers.
- [ff5 (disasm)](https://github.com/everything8215/ff5) - Disassembly and ROM documentation for Final Fantasy V (Super Famicom), building the original ROM from source.
- [FFTools](https://github.com/everything8215/fftools) - Browser-based data editor for 8-bit and 16-bit Final Fantasy ROMs; extracts ROM data to JSON for editing, then reassembles a new ROM via a full game disassembly and cc65.
- [FF6Tools](https://github.com/everything8215/ff6tools) - Browser-based editor covering NES/Famicom, SNES/Super Famicom, and GBA Final Fantasy ROMs (FF I-VI and their Advance ports), editing maps, battles, monsters, characters, items, attacks, and event/AI scripts, with graphics import/export.
- [ff5reader](https://github.com/Birdulon/ff5reader) - Python/Qt ROM reader for Final Fantasy V (SNES), with string-block, struct, and glyph definitions for the SNES and RPGe translation ROMs, plus FF4/FF6 helper modules and an SPC700 analyser.
- [mystic-editor](https://github.com/arathron123/mystic-editor) - Python editor for Mystic Quest (Final Fantasy Adventure, Game Boy) that decodes the ROM into editable maps, scripts, sprites, and audio files, re-encodes them, and can build an expanded ROM.


##### Final Fantasy XI

- [XiPackets](https://github.com/atom0s/XiPackets) - Reverse-engineered documentation and tools related to packet functions, data, and systems for Final Fantasy XI.
- [XiEvents](https://github.com/atom0s/XiEvents) - Reverse-engineering information and tools related to event data for Final Fantasy XI.
- [LandSandBoat](https://github.com/LandSandBoat/server) - Open-source server emulator for Final Fantasy XI, reimplementing retail server behavior alongside reverse-engineered game data tables (dats) for the game's client.
- [FFXI-NavMesh-Builder](https://github.com/LandSandBoat/FFXI-NavMesh-Builder) - Builds navigation meshes (via RecastNavigation) from Final Fantasy XI's collision data for retail-accurate mob/pet pathing on LandSandBoat servers, exporting intermediate .OBJ files. See also [xiNavmeshes](https://github.com/LandSandBoat/xiNavmeshes) (the generated navmesh dataset) and [xiNavmeshOBJs](https://github.com/LandSandBoat/xiNavmeshOBJs) (hand-cleaned intermediate OBJ output from the builder).
- [UpdateExtractor](https://github.com/LandSandBoat/UpdateExtractor) - Extracts and sanitizes Final Fantasy XI client update data (produced by POLUtils' MassExtractor) and applies it in-place to a LandSandBoat server install, avoiding manual fixes for shifted IDs and content changes.
- [FFXINAV](https://github.com/xathei/FFXINAV) - DLL that exports pathfinding using DSP navmeshes or custom navmeshes for Final Fantasy XI.
- [POLUnpack](https://github.com/pmgr/POLUnpack) - Unpacks Square Enix's PlayOnline (POL1) custom-packed PE binaries used by the Final Fantasy XI client, outputting a clean, research-friendly executable.
- [ffxi-macro-editor](https://github.com/ejouanchicot/ffxi-macro-editor) - Windows editor for Final Fantasy XI macro books and sets in the `USER` folder, showing auto-translate phrases as text, with search across all books and characters, drag-and-drop move/copy, and plain text/JSON export and import.

##### Final Fantasy XV

- [FFXVTemplates](https://github.com/Kizari/FFXVTemplates) - 010 Editor templates for Final Fantasy XV files.
- [Flagrum-Blender](https://github.com/Kizari/Flagrum-Blender) - Blender add-on for Final Fantasy XV and Forspoken asset import/export integration with Flagrum.
- [Flagrum](https://github.com/Kizari/Flagrum) - All-in-one asset browser and converter for Final Fantasy XV and Forspoken, with asset preview and export capabilities.
- [FFXV_NavMeshToObj](https://github.com/AlexPlaceres/FFXV_NavMeshToObj) - Converts Recast navmeshes in Final Fantasy XV .nav files to Wavefront OBJ files.
- [ffxv (RE research)](https://github.com/Xeeynamo/ffxv) - Reverse-engineering research and libraries for Final Fantasy XV (PC, PS4, Xbox One), covering EARC archives, EXML data, and other Luminous Engine formats.
- [ffxv-flatbuffers](https://github.com/AlexPlaceres/ffxv-flatbuffers) - FlatBuffers schemas for Final Fantasy XV's binary data formats.
- [EbonySnapsManager](https://github.com/Surihix/EbonySnapsManager) - Views, exports, replaces and adds snapshot (.ss) files in Final Fantasy XV's photo storage menu; adding and removing snaps modifies the save file and snapshotlink.sl.
- [FFXVSaveCrypt](https://github.com/Surihix/FFXVSaveCrypt) - Decrypts and encrypts Final Fantasy XV save data files such as gameplay0.save, system_data.save and snapshotlink.sl.

##### Final Fantasy XIII

- [Fang](https://github.com/neptuwunium/Fang) - Command-line extraction tool for the PC version of Lightning Returns: Final Fantasy XIII.
- [WhiteBinTools](https://github.com/Surihix/WhiteBinTools) - Extracts and repacks game resource archive files (WHITE.BIN) from the Final Fantasy XIII trilogy.
  - See also [WhiteBinTools_dll](https://github.com/Surihix/WhiteBinTools_dll), the C# reference library containing the functions WhiteBinTools uses.
- [WhiteFilelistManager](https://github.com/Surihix/WhiteFilelistManager) - Manages the filelist files of the Final Fantasy XIII trilogy: unpacks them to JSON or text, converts them back, and can add paths for new sequential files (needs a layeredFS plugin).
  - See also [WhiteCryptTool](https://github.com/Surihix/WhiteCryptTool), which decrypts and encrypts the XIII-2 and XIII-LR filelist files as well as the clb files from all three games.
- [WPDtool](https://github.com/Surihix/WPDtool) - Unpacks and repacks WPD-type files (.bin, .wdb, .wpd, .wpk, .xfv, .xgr, .xwb, .xwp) from the Final Fantasy XIII trilogy; paired IMGB image data is unpacked with a valid DDS header attached. Repacking is limited to PC files.
- [TRBtool](https://github.com/Surihix/TRBtool) - Unpacks and repacks TRB IMGB files from the Final Fantasy XIII trilogy. Repacking is limited to PC files.
  - Both TRBtool and WPDtool use [IMGBlibrary](https://github.com/Surihix/IMGBlibrary) (.NET Framework; a [.NET Core build](https://github.com/Surihix/IMGBlibrary_Core) also exists), a C# library for handling the trilogy's IMGB image headers.
- [ZTRtool](https://github.com/Surihix/ZTRtool) - Extracts and converts the ZTR text files from the Final Fantasy XIII trilogy.
- [WDBJsonTool](https://github.com/Surihix/WDBJsonTool) - Converts WDB database files from the Final Fantasy XIII trilogy to JSON and back, with separate game codes for XIII-1 and XIII-2/Lightning Returns.
  - Siblings: [WDBXlsxTool](https://github.com/Surihix/WDBXlsxTool) (same conversion to and from xlsx) and [WDBXlsxConverter](https://github.com/Surihix/WDBXlsxConverter) (one-way WDB to xlsx).
- [TxbImageTool](https://github.com/Surihix/TxbImageTool) - Extracts and converts image files to a format supported by the Final Fantasy XIII trilogy.
- [FFXIIIWMPtool](https://github.com/Surihix/FFXIIIWMPtool) - Unpacks and repacks the WMP movie archive files from Final Fantasy XIII (PC and Xbox 360 movies unpack as .bik, PS3 as .pam).
- [010-binary-templates](https://github.com/LR-Research-Team/010-binary-templates) - 010 Editor templates for Lightning Returns: Final Fantasy XIII's TRB/MTB formats.
- [LRFF13-Internal-ID-Extractor](https://github.com/LR-Research-Team/LRFF13-Internal-ID-Extractor) - Extracts Lightning Returns: Final Fantasy XIII's internal IDs and maps them to display names from the US ZTR text files, parsing WTB/ZTR game data.
- [ff13-save-editor-software](https://github.com/KiraTheReaper435/ff13-save-editor-software) - Save editor and decryptor for Final Fantasy XIII (Steam/Xbox/Windows Store version).

##### Final Fantasy VII

- [ff7tk](https://github.com/sithlord48/ff7tk) - Qt-based toolkit that makes programming Final Fantasy VII tools easier. Used as a shared parsing/editing base by other FF7 modding tools.
- [blackchocobo](https://github.com/sithlord48/blackchocobo) - Save editor for Final Fantasy VII, supporting PC, PSX, PS3, PSP/PS Vita, and Switch save formats (including the 2012 Steam release's metadata.xml), built on ff7tk.
- [FF7](https://github.com/turtle-insect/FF7) - Save data editor for Final Fantasy VII (Switch).
- [makoureactor](https://github.com/myst6re/makoureactor) - Final Fantasy VII field archive editor.
- [ff7-scarlet](https://github.com/petfriendamy/ff7-scarlet) - Multipurpose editor for Final Fantasy VII.
  - Formats: kernel.bin/kernel2.bin (command, attack, battle, character, item, equipment, materia, and key item data), scene.bin (enemy data, enemy attacks, formations), ff7.exe (in-game text, shop data, limit breaks, character names, audio data).
- [touphScript](https://github.com/ser-pounce/touphscript) - Text editor for the Final Fantasy VII PC release, for editing in-game dialogue/field text.
- [CaitSith](https://github.com/julianxhokaxhiu/CaitSith) - Final Fantasy VII CAM editor.
- [Palmer](https://github.com/julianxhokaxhiu/Palmer) - Final Fantasy VII field background editor. Initial source code release by Aali132.
- [Aeris](https://github.com/LaZar00/Aeris) - Tool for working with Final Fantasy VII background files.
- [FF7ToBlender](https://github.com/Kor-Hal/FF7ToBlender) - Blender addon to import/export Final Fantasy VII animation files.
- [FF7PSXtoPC](https://github.com/julianxhokaxhiu/FF7PSXtoPC) - Final Fantasy VII PSX-to-PC model converter (WIP).
- [FF7SND](https://github.com/julianxhokaxhiu/FF7SND) - Final Fantasy VII audio extraction app, originally made by Qhimm.com.
- [KimeraCS](https://github.com/LaZar00/KimeraCS) - C# rewrite of Borde's original Kimera tool for modding Final Fantasy VII models.
  - See also [tsunamods-codes/kimera](https://github.com/tsunamods-codes/kimera) for Borde's original VB6/OpenGL tool.
- [Braver](https://github.com/ficed/Braver) - Open-source reimplementation of the original Final Fantasy VII game engine, run alongside an existing FF7 install.
- [DoCTextTool](https://github.com/Surihix/DoCTextTool) - Extracts and re-converts text files for Dirge of Cerberus: Final Fantasy VII.
- [DoCCryptTool](https://github.com/Surihix/DoCCryptTool) - Decrypts and encrypts the text bin, class (script), kelstr.bin and .at3 bgm files from Dirge of Cerberus: Final Fantasy VII.
- [DoCMovieTool](https://github.com/Surihix/DoCMovieTool) - Unpacks and repacks the movie archive files of Dirge of Cerberus: Final Fantasy VII (can only replace existing files within an archive).
- [DoCPathsGenerator](https://github.com/Surihix/DoCPathsGenerator) (archived) - Companion tool that generates paths for Dirge of Cerberus: Final Fantasy VII files that have no path defined in the game's filelist.
- [ff7-decomp (decomp)](https://github.com/xeeynamo/ff7-decomp) - Matching decomp of Final Fantasy VII for PlayStation 1
- [Gaia](https://github.com/LaZar00/Gaia) - Command-line tool for exporting/importing Final Fantasy VII world map .MAP files to/from .OBJ format.
- [ff7-worldmap](https://github.com/ergonomy-joe/ff7-worldmap) - Decompiled Final Fantasy VII world map engine.
- [ff7-coaster](https://github.com/ergonomy-joe/ff7-coaster) - Decompiled code for the Final Fantasy VII "Jet Coaster" minigame.
- [ff7-chocobo](https://github.com/ergonomy-joe/ff7-chocobo) - Decompiled code for the Final Fantasy VII chocobo racing minigame.
- [FFVIISE_Modding_Tool](https://github.com/NfgOdin/FFVIISE_Modding_Tool) - All-in-one editor for Final Fantasy VII Steam Edition, covering textures, battle scene enemy stats, materia properties/AP, dialog text, equipment stats, and raw hex data.

- [kujata](https://github.com/picklejar76/kujata) - Translates Final Fantasy VII PC assets to web-friendly JSON/glTF/PNG: field character models and animations (char.lgp), field scene data (flevel.lgp) including scripts/tiles/textures, kernel data (kernel.bin/kernel2.bin), window.bin icons, and TIM/TEX textures.
- [Elena](https://github.com/Shojy/Elena) - .NET Standard library for reading Final Fantasy VII data: KERNEL.BIN/kernel2.bin stats and text, LGP archive listing/extraction, and TEX texture conversion.

###### Final Fantasy VII Remake / Rebirth

- [FF7R-UMAP](https://github.com/frostbone25/FF7R-UMAP) - Work-in-progress map (.umap) extractor for Final Fantasy VII Remake Intergrade (PC), built on Unreal Engine.
- [FF7R-font-mod-tools](https://github.com/matyamod/FF7R-font-mod-tools) - Font modding tools for Final Fantasy VII Remake.
- [ff7tools](https://github.com/cebix/ff7tools) - Suite of command-line translation and hacking tools for the PlayStation 1 version of Final Fantasy VII, focused on dumping and editing in-game text.
- [ff7-okteta](https://github.com/davidknoll/ff7-okteta) - Structure definition plugin for the Okteta hex editor, describing the Final Fantasy VII save game format.
- [ff7r-subtitle-exporter](https://github.com/jordanbtucker/ff7r-subtitle-exporter) - Exports Final Fantasy VII Remake subtitles to CSV files by reading the game's extracted text files.
- [ff7r-data-editor](https://github.com/jordanbtucker/ff7r-data-editor) - Editor for modifying `.uasset`/`.uexp` `DataObject` files for Final Fantasy VII Remake, changing numeric values, FNames, and array elements in unpacked game files without altering file size.
- [FF7R2-DataObject-Parser](https://github.com/Synthlight/FF7R2-DataObject-Parser) - C# library (NuGet `FF7R2.DataObject.API`) for reading and writing Final Fantasy VII Rebirth DataObject files from the original IoStore assets (not Zen-extracted `.uasset`/`.uexp`), with a byte-patching save mode and a full parsed-data save mode that allows resizing arrays.
- [FF7RebirthDataObjectEditor](https://github.com/Yoraiz0r/FF7RebirthDataObjectEditor) - Editor for Final Fantasy VII Rebirth `DataObject` `.uasset` files in their extracted IOStore state: edit primitives, FNames and array sizes, and export/import `.csv`.
- [FF7R-mesh-importer](https://github.com/matyamod/FF7R-mesh-importer) - Blender import tool for Final Fantasy VII Remake mesh/asset files.

##### Final Fantasy VIII

- [FF8-Rinoa-s-Toolset](https://github.com/MaKiPL/FF8-Rinoa-s-Toolset) (archived) - All-in-one modding toolkit for Final Fantasy VIII. Supports ripping/viewing battle stages, world map segments, models, and texture mixing.
- [Esthar](https://github.com/Albeoris/Esthar) - Resource editor for Final Fantasy VIII.
- [ff8-garden](https://github.com/Keyaku/ff8-garden) (archived) - Final Fantasy VIII editor based on Qhimm's source. Supports decompiling data files, editing game text, and recompiling.
- [maelstrom](https://github.com/sleepeybunney/maelstrom) - Seed randomizer for Final Fantasy VIII PC (Remastered and 2013 Steam release).
- [FF8](https://github.com/marfsama/FF8) - Python tools for reading various Final Fantasy VIII file formats including TIM textures, MCH character models, and battle models.
- [deling](https://github.com/myst6re/deling) - Final Fantasy VIII field/worldmap archive editor.
- [hyne](https://github.com/myst6re/hyne) - Final Fantasy VIII save editor.
- [FF8](https://github.com/turtle-insect/FF8) - Save data converter for Final Fantasy VIII (Switch) that exports the ff8slot save files for editing in tools such as Hyne and imports them back.
- [ChocoEdit](https://github.com/suloku/ChocoEdit) - Savegame editor for Final Fantasy VIII's Chocobo World minigame on PSX and PC, handling `.mcs` saves and `CHOCORPG` files; edits Boko's level, weapon, items, and flags, and can re-associate the save with another Final Fantasy VIII save.
- [Field-Map-Editor](https://github.com/Sebanisu/Field-Map-Editor) - Editor for Final Fantasy VIII field `.map` files, including tile data management and texture swizzling/deswizzling.
- [OpenVIII_CPP_WIP](https://github.com/Sebanisu/OpenVIII_CPP_WIP) - C++ library providing an API to read Final Fantasy VIII's `ZZZ` and `FIFLFS` archive formats.
- [zzzDeArchive](https://github.com/Sebanisu/zzzDeArchive) - Tool to create, extract, and merge `.zzz` archives for Final Fantasy VIII Remastered.
- [ff8_mch](https://github.com/julianxhokaxhiu/ff8_mch) - Blender plugin for importing/exporting Final Fantasy VIII field MCH character models.
- [Moomba](https://github.com/julianxhokaxhiu/Moomba) - Final Fantasy VIII CAM editor.
- [PuPuSharp](https://github.com/julianxhokaxhiu/PuPuSharp) (archived) - C# port of the original PuPu Project, a Final Fantasy VIII field importer/exporter. *(Deprecated, superseded by Field-Map-Editor)*
- [FF8SND](https://github.com/julianxhokaxhiu/FF8SND) - Final Fantasy VIII audio extraction app, originally made by Qhimm.com.
- [ff8-decomp](https://github.com/roengstrom/ff8-decomp) - Decompilation of Final Fantasy VIII.
- [FF8ModdingWiki](https://hobbitdur.github.io/FF8ModdingWiki/) - Wiki documenting Final Fantasy VIII file formats and modding techniques. ([source](https://github.com/HobbitDur/FF8ModdingWiki))
- [FF8UltimateEditor](https://github.com/HobbitDur/FF8UltimateEditor) - All-in-one editor for modding Final Fantasy VIII game data.
- [ShumiTranslator](https://github.com/HobbitDur/ShumiTranslator) (archived) - Universal translator tool for Final Fantasy VIII text files.
- [FF8GameData](https://github.com/HobbitDur/FF8GameData) (archived) - Python library exposing Final Fantasy VIII game data structures, used by several other HobbitDur FF8 tools.
- [IfritAI](https://github.com/HobbitDur/IfritAI) (archived) - Editor for Final Fantasy VIII monster AI data.
- [pandemona](https://github.com/HobbitDur/pandemona) - Editor for Final Fantasy VIII Guardian Force (GF) capability data.
- [CC-Group](https://github.com/HobbitDur/CC-Group) (archived) - Editor for Final Fantasy VIII's Triple Triad card game data.
- [charone_extractor](https://github.com/klavierworks/charone_extractor) - Blender plugin for importing the chara.one model format (meshes and animations) used in Final Fantasy VIII.
- [ff8-sound-remixed](https://github.com/myst6re/ff8-sound-remixed) - Reader for Final Fantasy VIII audio.dat and audio.fmt sound archive files.
- [JumboCactuar](https://github.com/Nihil-1/JumboCactuar) - Easy-to-use editor for Final Fantasy VIII .out data files.
- [nsw2ff8](https://github.com/AnalogMan151/nsw2ff8) - Python3 script to import/export Final Fantasy VIII Remastered save data from Nintendo Switch save files.
- [DDSZ_Tool](https://github.com/AnalogMan151/DDSZ_Tool) - Decompresses and recompresses the LZ4-based DDSZ texture format found in Final Fantasy VIII Remastered's Nintendo Switch game files.
- [phantasia-tools](https://github.com/rjricken/phantasia-tools) - Text extraction and injection utilities for Final Fantasy VIII (PS1).

##### Final Fantasy IX

- [Memoria](https://github.com/Albeoris/Memoria) - Open-source community rewrite of the Final Fantasy IX engine. Adds a mod manager/downloader, model viewer, widescreen support, and framerate/camera/audio improvements on top of the original game data.
- [FF9](https://github.com/turtle-insect/FF9) - Save data editor for Final Fantasy IX (Switch).

##### Chrono Trigger

- [CTNx](https://github.com/julianxhokaxhiu/CTNx) - Next-generation modding platform for Chrono Trigger (native Steam 2018 release support), inspired by FFNx.
- [ct-fmv](https://github.com/davidluzgouveia/ct-fmv) - Encoder/decoder for the FMV files in the Steam version of Chrono Trigger.
- [CTViewer](https://github.com/GitExl/CTViewer) - Displays Chrono Trigger scene and world maps with tile/palette animation and debug info, supporting both the SNES and Steam versions.
- [ChronoTrigger](https://github.com/turtle-insect/ChronoTrigger) - Save data editor for Chrono Trigger (Nintendo DS).

##### Chrono Cross

- [chrono-cross-decomp (decomp)](https://github.com/jdperos/chrono-cross-decomp) - Matching decompilation of Chrono Cross (100%, based on Radical Dreamers version).
- [ChronoCross](https://github.com/turtle-insect/ChronoCross) - Save data editor for Chrono Cross (Switch).

##### Xenogears

- [xenogears-decomp (decomp)](https://github.com/ladysilverberg/xenogears-decomp) (archived) - Matching decompilation of Xenogears.
- [Noah (decomp)](https://github.com/yaz0r/Noah) - Non-matching decompilation of Xenogears.
- [xenogears-recomp](https://github.com/OpokXeno/xenogears-recomp) - Static recompilation of Xenogears (PS1) into a native executable.

##### Xenosaga

- [xenosaga (decomp)](https://github.com/squareman/xenosaga) - Matching decompilation of Xenosaga Episode 1 (PS2, USA).
- [Xenosaga-2-Editor](https://github.com/TheSparda/Xenosaga-2-Editor) - ISO and save editor for Xenosaga Episode II (PS2, USA SLUS-20892/SLUS-21133); local web app built with stdlib Python only.
- [Xenosaga1PythonExtractor](https://github.com/LinuxJessi/Xenosaga1PythonExtractor) - Pure-Python disc extractor and mod kit for Xenosaga Episode I (PS2, SLUS-20469) that writes changes back to a bootable ISO.
  - Formats: textures to PNG, models to glTF, audio to WAV, movies to MP4, game text, cutscene scripts, fonts.
  - See also: [Xenosaga2PythonExtractor](https://github.com/LinuxJessi/Xenosaga2PythonExtractor), [Xenosaga3PythonExtractor](https://github.com/LinuxJessi/Xenosaga3PythonExtractor).

##### Vagrant Story

- [rood-reverse (decomp)](https://github.com/ser-pounce/rood-reverse) - Matching decompilation of Vagrant Story.
- [Vagrant-Story-Noesis-Python-Plugin](https://github.com/korobetski/Vagrant-Story-Noesis-Python-Plugin) - Noesis plugin for Vagrant Story models and animations.
- [blender-vagrant-story](https://github.com/korobetski/blender-vagrant-story) - Blender add-on for Vagrant Story: imports and exports `.WEP` weapon models, with work-in-progress import of `.SHP`, `.SEQ`, `.ZUD`, and `.MPD` files.
- [Vagrant-Story-Unity-Parser](https://github.com/korobetski/Vagrant-Story-Unity-Parser) - Unity editor script that reads data from the original Vagrant Story game files to build prefabs and databases. See also the author's earlier [Vagrant-Story-Scripted-Importer](https://github.com/korobetski/Vagrant-Story-Scripted-Importer), an initial pass at the same file format support in Unity.
- [Vagrant-Story-Patcher](https://github.com/redd2213/Vagrant-Story-Patcher) - Open-source, universal patch utility for Vagrant Story.
- [VSViewer](https://github.com/MercurialForge/VSViewer) - Model viewer and exporter for Vagrant Story, rendering the game's original character, weapon, and level models beyond their native 256x224 in-game resolution.

##### Parasite Eve

- [parasite-eve-decomp](https://github.com/khasinski/parasite-eve-decomp) - Source-only decompilation of Parasite Eve (PS1), work in progress.

##### Soul Blazer

- [RustyBlazer (decomp)](https://github.com/hellow554/RustyBlazer) - Matching decompilation of Soul Blazer.
- [RandoBlazer](https://github.com/randoblazer/RandoBlazer) - Randomizer for Soul Blazer; shuffles enemy/lair types, item and NPC rewards, and edits in-game text directly in the ROM.

##### Sleeping Dogs

- [TheoryEngine](https://github.com/SDmodding/TheoryEngine) (archived) - WIP reverse-engineered reimplementation of the Sleeping Dogs: Definitive Edition engine using shipped debug symbols (PDB); header-focused for embedding in tools and mods.
- [Gibbed.SleepingDogs](https://github.com/gibbed/Gibbed.SleepingDogs) - Archive unpacking and packing tools for Sleeping Dogs game files.
- [MXS_Sleeping_Dogs_Definitive_Edition_PC](https://github.com/coreynguyen/MXS_Sleeping_Dogs_Definitive_Edition_PC) - MaxScript for importing and exporting 3D character models from Sleeping Dogs: Definitive Edition (PC), building on format research from the SDmodding project.
- [CPP_Sleeping_Dogs_Definitive_Edition_PC](https://github.com/coreynguyen/CPP_Sleeping_Dogs_Definitive_Edition_PC) - Archive manager for Sleeping Dogs: Definitive Edition's `.big`/`.bix` data buffer and index files, supporting file export/import with CRC32-based file identification.
- [SD-BigFileExplorer](https://github.com/sneakyevil/SD-BigFileExplorer) - GUI for browsing, extracting, and creating `.BIG`/`.BIX` archives across Sleeping Dogs builds (early prototypes, the original game, Definitive Edition) with Triad Wars browse/extract support; ships filename lists for the PC/Steam release.
- [PermToFBX](https://github.com/SDmodding/PermToFBX) - Exports models from Sleeping Dogs: Definitive Edition's `perm.bin` resource files to FBX; companion tool [ModelScriber](https://github.com/SDmodding/ModelScriber) writes new FBX models back into `perm.bin`, with a Blender front-end in [ModelScriberBlender](https://github.com/SDmodding/ModelScriberBlender).
- [TextureExporter](https://github.com/SDmodding/TextureExporter) - Exports textures from Sleeping Dogs: Definitive Edition's `perm.bin` files to PNG; [TextureScriber](https://github.com/SDmodding/TextureScriber) and [TextureScriberOBJ](https://github.com/SDmodding/TextureScriberOBJ) build texture pack resources back from PNG or OBJ material inputs. [SD-UltimateTexTool](https://github.com/sneakyevil/SD-UltimateTexTool) is a GUI front end that imports a `perm.bin`/`temp.bin` pair, replaces same-size textures with PNGs, and exports new files via the Triad Wars TextureScriber.
- [ShaderBin](https://github.com/SDmodding/ShaderBin) - Unpacks and rebuilds Sleeping Dogs: Definitive Edition's `.temp.bin` HLSL shader binaries.
- [UIScreenConv](https://github.com/SDmodding/UIScreenConv) - Converts Sleeping Dogs: Definitive Edition SWF/GFX UI assets to and from the game's UIScreen format.
- [TCDatabaseConv](https://github.com/SDmodding/TCDatabaseConv) - Converts Sleeping Dogs: Definitive Edition's True Crowd Database resource to and from XML.
- [SymbolTableScriber](https://github.com/SDmodding/SymbolTableScriber) - Builds Sleeping Dogs: Definitive Edition Symbol Table Resource binaries from a plain-text symbol list.

##### The World Ends With You

- [twewy (decomp)](https://github.com/Yotona/twewy) - Matching decompilation of The World Ends With You (NDS).

##### Babylon's Fall

- [BabylonsFallTools](https://github.com/Nenkai/BabylonsFallTools) - Extraction tools for Babylon's Fall PKZL/.pkz and DAT files.

##### Hitman

- [re47 (decomp)](https://github.com/0danny/re47) (archived) - Matching decompilation of Hitman: Codename 47 (2000).
- [HiTMAN Archive Manager](https://www.moddb.com/games/hitman-world-of-assassination/downloads/hitman-archive-manager) - Use this tool to install HiTMAN mods or extract the *.rpkg archives in which HiTMAN files are stored.
- [ZHM5PatchBuilder](https://github.com/pawREP/ZHM5PatchBuilder) - Patch builder for Hitman 2 (2018) Rpkg archives.
- [HMC47](https://github.com/americusmaximus/HMC47) - Open source implementation of Hitman: Codename 47, parsing and rendering original game data, resource files, models, and textures.
- [hitman-file-formats](https://github.com/AlexKimov/hitman-file-formats) (archived) - Documentation and research on IO Interactive (Hitman) game file formats.
- [Hitman2Loc](https://github.com/x1nixmzeng/Hitman2Loc) - Command-line C# tool converting Hitman 2: Silent Assassin locale (.loc) files to and from XML language exports.
- [Glacier Modding Resources](https://github.com/glacier-modding/Modding-Resources) - Community-maintained collection of file format templates, structure definitions, and research tools for IO Interactive's Glacier 2 engine, by the Glacier 2 Modding organization.
  - Formats: 010 Editor templates and C-style structure definitions for RPKG resources across Hitman: Absolution, Hitman (2016), Hitman 2, and Hitman 3/World of Assassination.
- [ReHitman](https://github.com/ReGlacier/ReHitman) - Reverse engineering project for Hitman: Codename 47 (the Glacier engine's original "Gen 1"), covering the game's file formats and internals.
  - Tools: [ReHitmanTools](https://github.com/ReGlacier/ReHitmanTools) (utilities for Glacier-engine game files), [GlacierPropertiesExtractorIDAPlugin](https://github.com/ReGlacier/GlacierPropertiesExtractorIDAPlugin) (IDA Pro plugin extracting RTTI properties from Glacier 1 engine classes), [PS2CPPExtractorIDAPlugin](https://github.com/ReGlacier/PS2CPPExtractorIDAPlugin) (IDA plugin generating C++ class definitions from PS2 ELF vtables).
- [BMEdit](https://github.com/ReGlacier/BMEdit) - Level editor for Hitman: Blood Money (2006), by the same ReGlacier team behind ReHitman above.
  - Formats: PRP entity properties (via companion [HBM_PRPTool](https://github.com/ReGlacier/HBM_PRPTool)), GMS scene data (via [HBM_GMSTool](https://github.com/ReGlacier/HBM_GMSTool), preview).
  - See also [BloodMoneySaveEditorWeb](https://github.com/ReGlacier/BloodMoneySaveEditorWeb), a browser-based `Profile.pro` save editor for both the PC and PS2 builds, and [ReHitman.ScriptingRuntime](https://github.com/ReGlacier/ReHitman.ScriptingRuntime), a C# scripting/modding runtime embedded via Mono.
- [h2sa-arsenal-editor](https://github.com/Darithos/h2sa-arsenal-editor) - Desktop editor for the weapon and ammunition tables inside Hitman 2: Silent Assassin (2002).
- [hitman-contracts-toolkit](https://github.com/Darithos/hitman-contracts-toolkit) - Free camera and weapon-table editor for Hitman: Contracts (2004), patching a compiled-out camera routine into the retail PC exe and exposing all 58 weapons/10 ammo types with automatic backups before any file write.

##### Kingdom Hearts

- [OpenKH](https://github.com/OpenKH/OpenKh) - Comprehensive reverse-engineering toolkit for Kingdom Hearts series. Handles MDLX/PMO models, PAM/ANB animations, TXA textures, map data, battle configs, and message files. Includes 50+ specialized editors and converters. Supports KH1, KH2, Birth by Sleep, Re:Coded, and Dream Drop Distance.
- [AudioMog](https://github.com/Yoraiz0r/AudioMog) - Free all-in-one audio modding tool that allows users to unpack and repack supported game's audio binary files. Created for Kingdom Hearts III modding and works on other games such as Melody of Memory, Final Fantasy XV, and more.
- [KH2Suite](https://github.com/Truthkey/KH2Suite) - Suite of programs made to assist the user in Kingdom Hearts 2 or 2 Final Mix modding.
- [KHBBS_EXA_Editor](https://github.com/Truthkey/KHBBS_EXA_Editor) - Editor for EXA events in Kingdom Hearts: Birth by Sleep.
- [KH1FM_Toolkit](https://github.com/GovanifY/KH1FM_Toolkit) - Tool used for modding the game Kingdom Hearts: 1 Final Mix.
- [RECOM_Toolkit](https://github.com/GovanifY/RECOM_Toolkit) - Tool used for modding the game Kingdom Hearts: Re Chain of Memories.
- [BBSPluginNoesis](https://github.com/Truthkey/BBSPluginNoesis) - Updated Noesis plugin for Kingdom Hearts Birth by Sleep working with modern versions of Visual Studio.
- [BBS-Modding-Station](https://github.com/Truthkey/BBS-Modding-Station) - Windows Forms tool for modifying Kingdom Hearts: Birth by Sleep files, with PMO model extract/pack and PMP handling plus bundled Extract, Insert, AnimEx and AnimIn helper executables.
- [EAD_Editor](https://github.com/Truthkey/EAD_Editor) - Program to edit EAD files in Kingdom Hearts: Birth by Sleep.
- [KH_1.5_MSELF_EXTRACTOR](https://github.com/Truthkey/KH_1.5_MSELF_EXTRACTOR) - Small C++ tool that extracts all files from Kingdom Hearts 1.5 MSELF containers.
- [KH-ReCOM-Tools](https://github.com/Murugo/KH-ReCOM-Tools) - Set of experimental tools for Kingdom Hearts Re:Chain of Memories (PS2).
- [Murugo/Misc-Game-Research (Kingdom Hearts II)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Kingdom%20Hearts%20II%20Final%20Mix) - Reverse engineering notes for Kingdom Hearts II Final Mix (PS2).
- [kh1](https://github.com/ethteck/kh1) - WIP Decompilation of Kingdom Hearts (PS2, JP).
- [noclip.website (Kingdom Hearts)](https://github.com/magcius/noclip.website/tree/main/src/KingdomHearts) - In-browser Kingdom Hearts viewer.
- [noclip.website (Kingdom Hearts II Final Mix)](https://github.com/magcius/noclip.website/tree/main/src/KingdomHearts2FinalMix) - In-browser Kingdom Hearts II Final Mix viewer.
- [kh2mdlx](https://github.com/GovanifY/kh2mdlx) - Tool for importing and exporting Kingdom Hearts 2 3D models.
- [kh2vif](https://github.com/GovanifY/kh2vif) - Model importer for Kingdom Hearts 2 (OBJ to VIF format converter).
- [Hypercrown](https://github.com/Some1fromthedark/Hypercrown) - Tool for converting models from Kingdom Hearts 1 into more common model formats. Also converts back to the native format so that edited models can be patched into the game.
- [KH1FM_Re_Toolkit](https://github.com/Some1fromthedark/KH1FM_Re_Toolkit) - Python scripts that patch a Kingdom Hearts 1 Final Mix (PS2) ISO from JSON configs, inserting, replacing, or modifying files in the ISO; includes an optional cutscene-skipping ELF patch. Compression is not yet supported.
- [KH1_BD_Parser](https://github.com/Some1fromthedark/KH1_BD_Parser) - Python script for parsing Kingdom Hearts 1 `.bd` files using supplied syscall tables, with an interactive mode.
- [khdays-decomp (decomp)](https://github.com/Yokimitsuro/khdays-decomp) - Work-in-progress matching decompilation of Kingdom Hearts 358/2 Days (Nintendo DS).
- [khdays-port](https://github.com/Yokimitsuro/khdays-port) - Experimental native PC runtime for Kingdom Hearts 358/2 Days, developed alongside khdays-decomp above; requires no copyrighted game data of its own.
- [KH1 Hex Editor](https://github.com/Yokimitsuro/Kh1HexEditor) - Windows hex editor for Kingdom Hearts 1 that extracts text sequences from binary files and edits them alongside the hex view using TBL character tables, with highlighting of modified bytes and automatic backups.
- [KHMoMVideoReplacer](https://github.com/Yokimitsuro/KHMoMVideoReplacer) - Standalone GUI tool for replacing the movie video in Kingdom Hearts: Melody of Memory Unity asset bundles (decrypted bundles only) with an H.264 MP4, updating the frame count and size and swapping the `.resource` file.
- [KH3-UASSET-SWF-Export-Import](https://github.com/kh0shn4w/KH3-UASSET-SWF-Export-Import) - Export/import tool for SWF movie data embedded in Kingdom Hearts III UASSET files.
- [SabfMabfExtract](https://github.com/Rikux3/SabfMabfExtract) - Extracts `.sab`/`.mab` files from Kingdom Hearts 0.2 and Kingdom Hearts III (archived).
- [KH_PS4_Misc-Tools](https://github.com/Rikux3/KH_PS4_Misc-Tools) - Collection of PS4-specific Kingdom Hearts modding utilities (archived): GnfHelper (converts images to/from the PS4 GNF texture format), ShimEditor (edits, extracts, and deletes shim files), and ShimEx (drag-and-drop shim file extractor).

##### Dragon Quest

- [noclip.website (Dragon Quest VIII)](https://github.com/magcius/noclip.website/tree/main/src/DragonQuest8) - In-browser Dragon Quest VIII viewer.
- [SlimeMoriMori](https://github.com/onepiecefreak3/SlimeMoriMori) - Reverse engineering tool for the custom compression format used in Slime Mori Mori (Dragon Quest spinoff) on Game Boy Advance.
- [fptTool](https://github.com/LinkOFF7/fptTool) - Dragon Quest VII FPT text converter.
- [dq6-sfc](https://github.com/ButThouMust/dq6-sfc) - Font and script dumpers for Dragon Quest VI and the Dragon Quest III Super Famicom remake, adapted from the author's Otogirisou translation tooling.
- [DQHEditor](https://github.com/marcussacana/DQHEditor) - DLL library for building extractor/repacker and editor tools for .strs and .lx files from Dragon Quest Heroes: Slime Edition. See also [IdxTool](https://github.com/marcussacana/IdxTool) for extracting/repacking the game's .IDX/.BIN archives.
- [Dragon-Quest-8-Tools](https://github.com/Fire-Cube/Dragon-Quest-8-Tools) - Python toolset for Dragon Quest VIII (PS2), covering HD6/PAK archive extraction and repacking (`HD6Tools.py`, `PakTools.py`) and monster parameter data extraction/modification (`MonsterParams.py`, `modify_monster_param.py`).
- [Dragon-Quest-IX-Decompilation-.spr-item-textures](https://github.com/nathanjplaw/Dragon-Quest-IX-Decompilation-.spr-item-textures) - Converts between Dragon Quest IX's .spr item-icon sprite format and 24x24 PNGs, supporting both extraction and re-injection back into the ROM.
- [rocketslime-3ds-english-fixup](https://github.com/Akoi89/rocketslime-3ds-english-fixup) - Unofficial fix-up patch (single xdelta file, no game data) on top of Team Rocket Slime's English translation of Slime MoriMori Dragon Quest 3 (3DS).
- [DQ5SaveEditor](https://github.com/Fuindin/DQ5SaveEditor) - Save state editor for Dragon Quest V: Hand of the Heavenly Bride save states created in the melonDS emulator.
- [DQ8SaveEditor](https://github.com/Fuindin/DQ8SaveEditor) - WinForms save state editor for Dragon Quest VIII save states from the PCSX2 emulator.
- [dwsrame](https://github.com/jdratlif/dwsrame) - SRAM save data editor for Dragon Warrior (NES).
- [torneko_lz_tool](https://github.com/romhack/torneko_lz_tool) - LZ compression tool for the PS1 game World of Dragon Warrior - Torneko: The Last Hope (Dragon Quest spinoff).
- [DQ7](https://github.com/turtle-insect/DQ7) - Save data editor for Dragon Quest VII (3DS).
  - Same author's 3DS save data editors: [DQ1](https://github.com/turtle-insect/DQ1) (Dragon Quest), [DQ2](https://github.com/turtle-insect/DQ2) (Dragon Quest II), [DQ3](https://github.com/turtle-insect/DQ3) (Dragon Quest III), [DQ8](https://github.com/turtle-insect/DQ8) (Dragon Quest VIII) and [DQ11_3DS](https://github.com/turtle-insect/DQ11_3DS) (Dragon Quest XI).
- [DQB2](https://github.com/turtle-insect/DQB2) - Save data editor for Dragon Quest Builders 2 (Switch and Steam).
  - Same author's Switch save data editors: [DQB1](https://github.com/turtle-insect/DQB1) (Dragon Quest Builders), [DQ11_NS](https://github.com/turtle-insect/DQ11_NS) (Dragon Quest XI S) and [DQTreasure](https://github.com/turtle-insect/DQTreasure) (Dragon Quest Treasures).
- [DQMJoker3Pro](https://github.com/turtle-insect/DQMJoker3Pro) - Save data editor for Dragon Quest Monsters: Joker 3 Professional (3DS).
  - Same author's Dragon Quest Monsters save data editors: [DQM2IruRuka](https://github.com/turtle-insect/DQM2IruRuka) (Dragon Quest Monsters 2: Iru & Ruka, 3DS), [DQMTerry3D](https://github.com/turtle-insect/DQMTerry3D) (Terry's Wonderland 3D, 3DS) and [DQMCH](https://github.com/turtle-insect/DQMCH) (Caravan Heart, GBA).

##### Final Fantasy X

- [noclip.website (Final Fantasy X)](https://github.com/magcius/noclip.website/tree/main/src/FinalFantasyX) - In-browser Final Fantasy X viewer.
- [Final Fantasy X HD translation tools](https://www.moddb.com/games/final-fantasy-x/downloads/final-fantasy-x-hd-translation-tools) - Tools for Final Fantasy X HD (PC) to extract and import game data for translation (texts and graphics).
- [FFX-Phyre-Tool](https://github.com/NfgOdin/FFX-Phyre-Tool) - GUI and CLI utility for extracting and repacking 3D models and textures from Final Fantasy X/X-2 HD Remaster `.phyre` files, converting to glTF 2.0 for Blender import; auto-detects DXT1/DXT3/DXT5 texture compression.
- [Spira_Text_Tool](https://github.com/NfgOdin/Spira_Text_Tool) - Editor for Final Fantasy X text/dialogue binary tables (`item_txt.bin`, `arms_txt.bin`, `status_txt.bin`, etc.); decodes the game's proprietary character encoding and control codes, with safe repacking.
- [FFX_Shop_Tool](https://github.com/NfgOdin/FFX_Shop_Tool) - Editor for Final Fantasy X shop inventory, rate, and equipment data files (`item_shop.bin`, `arms_shop.bin`, `item_rate.bin`, etc.).
- [FFX_Sphere_Grid_Tool](https://github.com/NfgOdin/FFX_Sphere_Grid_Tool) - Visual editor for Final Fantasy X's Sphere Grid data, supporting both the HD Remaster and classic PS2 file formats.
- [FFX_AI_Tool](https://github.com/NfgOdin/FFX_AI_Tool) - Editor for Final Fantasy X monster stats and battle AI scripts (Atel), with disassembly/decompilation and repacking into the original game chunk structure.
- [FFX_Audio_Tool](https://github.com/NfgOdin/FFX_Audio_Tool) - Browser/editor for FMOD Sound Bank (`.fsb`) files, for browsing, exporting, and injecting custom audio in Final Fantasy X/X-2 HD Remaster and other FSB5-based games.
- [FFXView](https://github.com/yaz0r/FFXView) - Historical (2005) source of the Final Fantasy X/X-2 model viewer, which visualizes models from files extracted with FFXDumper (original releases are hosted on archive.org). Archived.
- [FF10](https://github.com/turtle-insect/FF10) - Save data editor for Final Fantasy X (Switch).
- [FF10-2](https://github.com/turtle-insect/FF10-2) - Save data editor for Final Fantasy X-2 (Switch).

##### World of Final Fantasy

- [WOFFington](https://github.com/neptuwunium/WOFFington) - Library to process and manage World of Final Fantasy files.
- [WoFFCshTool](https://github.com/Surihix/WoFFCshTool) - Converts World of Final Fantasy csh database files to csv and back.
- [WOFF](https://github.com/turtle-insect/WOFF) - Save data editor for World of Final Fantasy (Switch).

##### Final Fantasy Tactics

- [ExMateria-Sound (smd-player)](https://github.com/timbermania/ExMateria-Sound) - Godot 4 addon reproducing Final Fantasy Tactics (PSX) sound output, both `.SMD` music and battle effect SFX, driven by a native C++ SPU core.
- [ExMateria-Map](https://github.com/timbermania/ExMateria-Map) - Blender add-on for editing Final Fantasy Tactics (PSX) maps: imports `MAP###.GNS` map files extracted from the disc, supports repainting the texture sheet and reshaping geometry, and exports the edited map bundle (GNS + textures) back.
- [ExMateria-ISO-Patcher](https://github.com/timbermania/ExMateria-ISO-Patcher) - Patcher for Final Fantasy Tactics (PSX) disc images that replaces music slots through a guided TUI or a TOML recipe, with deterministic byte-identical output, and extracts the disc file tree for the rest of the ExMateria tools.
- [ExMateria-DAW-Plugin](https://github.com/timbermania/ExMateria-DAW-Plugin) - VST3 plugin that loads Final Fantasy Tactics (PSX) `WAVESET.WD` and `.SMD` files from the disc to play and edit its music in a DAW through PSX SPU emulation. See also [ExMateria-SPU-Core](https://github.com/timbermania/ExMateria-SPU-Core), the portable C++20 SPU/SMD sequencer library it builds on.
- [FFTAUtils](https://github.com/spiiin/FFTAUtils) - Utilities for hacking the Final Fantasy Tactics Advance (GBA) ROM: a map editor/viewer, an arrange-data decoder, height-map and arrange-map renderers, a map-parameter printer, and Python helpers including conversion of arrange data for CadEditor.

##### Musashi: Samurai Legend

- [Murugo/Misc-Game-Research (Musashi: Samurai Legend)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Musashi%20Samurai%20Legend) - Reverse engineering notes for Musashi: Samurai Legend (PS2).

##### Final Fantasy XIV

- [BlenderAssist](https://github.com/0ceal0t/BlenderAssist) - Blender add-on for importing and exporting FFXIV animations (.pap format).
- [Physis](https://github.com/redstrate/Physis) - Rust library for reading and writing FFXIV data, supporting SqPack archives and game formats (MDL models).
- [MultiAssist](https://github.com/ilmheg/MultiAssist) - GUI tool for extracting and repacking FFXIV animation files (.pap format) with support for multiple animations and FBX export.
- [Novus](https://github.com/redstrate/Novus) - Suite of unofficial FFXIV tools including model/gear viewer, map editor, Excel data editor, and archive explorer.
- [ZoneFbx](https://github.com/Hengle/ZoneFbx) - Driver program and C++/CLI library using the Autodesk FBX SDK to export Final Fantasy XIV zone/territory data to FBX, including textures and object hierarchy.
- [FFXIVClientStructs](https://github.com/aers/FFXIVClientStructs) - Reverse-engineering resources for Final Fantasy XIV client's native classes and structures; C# library for interop with native game objects and functions.
- [AnimAssist](https://github.com/0ceal0t/AnimAssist) - Basic animation modding workflow tool for Final Fantasy XIV, from the same author as BlenderAssist.
- [ff14-strategyboard-decode](https://github.com/wtw0212/ff14-strategyboard-decode) - Reverse-engineered Python/TypeScript codec for Final Fantasy XIV's in-game Strategy Board binary serialization format, documenting its DEFLATE compression, CRC32 checksum, and obfuscation/substitution layers, with a web interface for creating diagrams and exporting them as in-game strategy codes.
- [seventhumbral](https://github.com/adarec1994/seventhumbral) - Explorer for Final Fantasy XIV 1.0 (the original pre-A Realm Reborn release), previewing levels, animations, and models.
- [FFXIV Model Viewer](https://github.com/nohbdy/ffxivmodelviewer) - Stand-alone viewer for the original 2010 Final Fantasy XIV (pre-A Realm Reborn) client's assets.
  - Formats: GTEX (textures), MDLC (models), skl (skeletons/animation), Vorbis/ADPCM (audio), DirectX shaders, Lua scripts.
  - Features: NPC/monster model browsing, skeleton visualization, map viewer (Cartographer), screenshot capture.
- [ffxiv-tex-converter](https://github.com/kartoffels123/ffxiv-tex-converter) - Batch converter between FFXIV's TEX texture format and DDS, with Kaitai Struct definitions for the DDS, TEX, and MTRL formats.
- [FFXIVChnTextPatch](https://github.com/reusu/FFXIVChnTextPatch) - Original (2019) tool that injects a Chinese/Traditional Chinese text and font localization patch into the FFXIV international client by replacing its SqPack `0a0000.win32.dat0`/`.index`/`.index2` resource files.
  - See also [FFXIVChnTextPatch-Souma](https://github.com/Souma-Sumire/FFXIVChnTextPatch-Souma), an actively maintained GUI rewrite building on the above, with macOS support via Launch4j/Java.
- [ffxiv_7_0_toolbox](https://github.com/kartoffels123/ffxiv_7_0_toolbox) - Companion scripts/documentation to ffxiv-tex-converter above: an ID-texture upscaler GUI, a Penumbra mod path deobfuscator for making obfuscated mod files human-readable, and Penumbra EQP format documentation/scripts.
- [ironworks](https://github.com/ackwell/ironworks) - Modular Rust toolkit for FFXIV data, with separate features for reading Excel databases, parsing SeString rich text, navigating/extracting SqPack packages, and working with ZiPatch update files. See also the same author's [kobold](https://github.com/ackwell/kobold), a modular SqPack reader written in TypeScript, and [boilmaster](https://github.com/ackwell/boilmaster), an FFXIV data web service built on ironworks.
- [xivres](https://github.com/Soreepeong/xivres) - C++ library for FFXIV resource files. See also companion projects [FFXIV-FontChanger](https://github.com/Soreepeong/FFXIV-FontChanger) (replacement font generation), [FFXIV-ExcelMerge](https://github.com/Soreepeong/FFXIV-ExcelMerge) (multi-language Excel text merging), [FFXIV-scdtool](https://github.com/Soreepeong/FFXIV-scdtool) (builds replacement `.scd` music files from your own audio tracks and extracts `.scd` files to Ogg), and [CruiseChaserExporter](https://github.com/Soreepeong/CruiseChaserExporter) (exports FFXIV models with their `.sklb` skeletons and `.pap` Havok animations to glTF).
- [libxivdat](https://github.com/carriejv/libxivdat) - Rust library for reading and writing Final Fantasy XIV client `.DAT` configuration files.
- [EXDSchema](https://github.com/xivdev/EXDSchema) - Community-maintained schema repository defining the structure of FFXIV's Excel (EXD/EXH) data sheets, used by Lumina, Physis, ironworks, and other libraries above.
  - Same organization's [EXDTools](https://github.com/xivdev/EXDTools), a C# command-line tool that reads column definitions from the game directory and exports, compares, merges, migrates, and validates EXDSchema definitions.
- [XIViewer](https://github.com/WorkingRobot/XIViewer) - Cross-platform (web and native) viewer for FFXIV's Excel (EXD/EXH) data files, showing structured in-game data tables such as item stats and NPC data, with EXDSchema integration and filtering.
  - Same author's [xiv-fuse](https://github.com/WorkingRobot/xiv-fuse), which mounts every FFXIV game file for any region and patch as a read-only directory tree streamed from the CDN, [ffxiv-downloader](https://github.com/WorkingRobot/ffxiv-downloader), a tool/GitHub Action that downloads regex-selected FFXIV files, and [ExdGenerator](https://github.com/WorkingRobot/ExdGenerator), generating Lumina sheet bindings from EXDSchema.
- [XivExdUnpacker](https://github.com/Souma-Sumire/XivExdUnpacker) - Command-line tool that uses Lumina to export FFXIV Excel (EXD/EXH) sheets to CSV for chosen languages (en, ja, de, fr, cn, tc, ko), with optional raw hexcode or human-readable decoding of embedded string tags; a replacement for the `rawexd` function of SaintCoinach.Cmd.
- [file-formats (xivdev)](https://github.com/xivdev/file-formats) - 010 Editor templates, ImHex patterns, and FlatBuffer schemas documenting FFXIV file formats.
- [Meddle](https://github.com/PassiveModding/Meddle) - Dalamud plugin providing a GUI for exporting full FFXIV character models (multiple meshes at once) for use in external 3D tools; see also its companion [MeddleTools](https://github.com/PassiveModding/MeddleTools) Blender add-on.
- [Icarus](https://github.com/redstrate/Icarus) - Auto-generated high-level Rust API for FFXIV Excel data, built on EXDSchema and Physis.
- [Kawari](https://github.com/redstrate/Kawari) (archived) - Modern unofficial FFXIV server emulator (patch 7.x+), from the author of Physis and Novus.
- [Auracite](https://github.com/redstrate/Auracite) - Dalamud plugin that archives an FFXIV character into a portable, machine-readable JSON format, importable by other tools such as Kawari.
- [ZiPatchLib](https://github.com/pmgr/ZiPatchLib) - C# library for parsing and applying Final Fantasy XIV: A Realm Reborn `.patch` update files (the ZiPatch format).
- [Ouroboros](https://github.com/PassiveModding/Ouroboros) - Extraction/rebuilding tool and HLSL decompiler pipeline for Final Fantasy XIV's ShPk shader package format, covering character, hair, and iris shaders.

##### Tactics Ogre: Let Us Cling Together

- [Gibbed.LetUsClingTogether](https://github.com/gibbed/Gibbed.LetUsClingTogether) - File packing and unpacking tool for Tactics Ogre: Let Us Cling Together (.pac archives) supporting asset extraction on PSP and Reborn versions.
- [Gibbed.EFX](https://github.com/gibbed/Gibbed.EFX) - Tools and code for use with EFX files found in Final Fantasy XII and Tactics Ogre.

##### Tactics Ogre: The Knight of Lodis

- [totkol (disasm)](https://github.com/jiangzhengwenjz/totkol) - Work-in-progress disassembly of Tactics Ogre: The Knight of Lodis (Game Boy Advance, USA).

##### Valkyrie Anatomia

- [vato_mdl_tool](https://github.com/eArmada8/vato_mdl_tool) - Model extraction and conversion tool for Valkyrie Anatomia: The Origin, extracting mesh, animation, and texture data to standard 3D formats (glTF/glb).

##### Bravely Default

- [BDFE.ARC.Tool](https://github.com/Ekey/BDFE.ARC.Tool) (archived) - Tool for extracting archives from the mobile game Bravely Default: Fairy's Effect.
- [BravelyDefault2](https://github.com/turtle-insect/BravelyDefault2) - Save data editor for Bravely Default 2 (Switch); recommends the same author's GvasViewer.

##### Romancing SaGa

- [RS.BIN.Tool](https://github.com/Ekey/RS.BIN.Tool) (archived) - Tool for extracting and repacking BIN archives from the Romancing SaGa series.
- [RS2_snes](https://github.com/turtle-insect/RS2_snes) - Save data editor for Romancing SaGa 2 (SNES).
  - Same author's Switch editors: [RS2_NS](https://github.com/turtle-insect/RS2_NS) (Romancing SaGa 2) and [RS3](https://github.com/turtle-insect/RS3) (Romancing SaGa 3).

##### Drakengard

- [Drakengard1and2Extractor](https://github.com/Surihix/Drakengard1and2Extractor) - C# WinForms GUI for extracting and repacking several PS2 file types from Drakengard 1 and 2, with 010 Editor templates documenting the formats and a bundled minilzo decompressor.
- [Drakengard3xxxToMp3](https://github.com/Surihix/Drakengard3xxxToMp3) - Extracts the audio from Drakengard 3's .XXX sound files to mp3 without transcoding, since the audio inside is already mp3 (mono or stereo only).
- [Drakengard3MusicMaker](https://github.com/Surihix/Drakengard3MusicMaker) - C# WinForms app for replacing the in-game music tracks of Drakengard 3 with custom audio, tested on RPCS3 with the US and EU PSN versions.
- [Drakengard-3-.xxx-Importer](https://github.com/SlowpokeVG/Drakengard-3-.xxx-Importer) - Re-imports edited files into Drakengard 3 UE3 `.xxx` archives (after decompressing and extracting them with Gildor's Unreal Package tools); may work with other UE3 UPK archives.

##### Star Ocean

- [Star-Ocean-2](https://github.com/lifebottle/Star-Ocean-2) - Documents unpacking and repacking Star Ocean: Second Evolution (PS Vita) and Star Ocean 2 (PSP), created as part of an English fan translation effort.
  - Formats: PSVita PKG/PSARC package extraction, PSP `so2pack.bin` archives with nested SLZ-compressed files, `APAC` sound/script archives.
  - Tools: pkg2zip, psvpfsparser, QuickBMS scripts (`star_ocean_kcpa.bms`, `so2pack.bms`, `slz.bms`) for extraction and repacking on both platforms.
- [so4pc_pack](https://github.com/RikuKH3/so4pc_pack) - Unpacker/repacker for archive files used in the PC port of Star Ocean 4: The Last Hope.
- [StarOcean2](https://github.com/turtle-insect/StarOcean2) - Save data editor for Star Ocean: The Second Story R (Switch).

##### Secret of Evermore

- [SOE-SRAM-Editor](https://github.com/HunterStanton/SOE-SRAM-Editor) - SRAM (save RAM) editor for the SNES game Secret of Evermore.
- [soerominfo](https://github.com/millanzarreta/soerominfo) - Extracts information from Secret of Evermore ROMs in CSV format.
- [SoETilesViewer](https://github.com/black-sliver/SoETilesViewer) - Viewer/editor for tile, block, and palette resources of Secret of Evermore (SNES), with import/export via right-click on tiles (US/NTSC, uncompressed ROM only).
- [SoEScriptDumper](https://github.com/black-sliver/SoEScriptDumper) - Dumps and annotates Secret of Evermore's ROM script/trigger data into human-readable listings, decoding sub-instructions where possible; pairs with SoETilesViewer above for a GUI front-end.
- [evermizer](https://github.com/black-sliver/evermizer) - SNES ROM randomizer/patcher for Secret of Evermore, shuffling item locations, alchemy formulas, boss drops, and the Energy Core within the ROM data; produces a patched ROM via CLI, browser (WASM), or Windows executable. Python bindings: [pyevermizer](https://github.com/black-sliver/pyevermizer).

##### Seiken Densetsu 3

- [sd3save_editor](https://github.com/rrooij/sd3save_editor) - Save editor for Seiken Densetsu 3 (SNES).
- [seiken_densetsu_3](https://github.com/rofferom/seiken_densetsu_3) - Partial extraction toolset for the Japanese SNES release of Seiken Densetsu 3; documents the text compression scheme and extracts font data and simple dialog sequences (complex dialogs and graphics remain unsupported).

##### Another Mind

- [anothermind-decomp](https://github.com/halkuncode/anothermind-decomp) - Decompilation of Squaresoft's PlayStation visual novel Another Mind.

##### Einhänder

- [einhanderTools](https://github.com/romhack/einhanderTools) - Collection of tools used to translate the PSX game Einhänder.

#### Strategic Simulations (SSI)

##### Red Lightning

- [ssi-img](https://github.com/canadianavenger/ssi-img) - Tools and documentation for the IMG file format used by Red Lightning; decodes both the PC and Amiga versions of the game.

##### Gold Box Series

- [wish](https://github.com/malcyon/wish) - Save editor and automapper for the Commodore 64 version of Pool of Radiance, with in-progress support for other Gold Box titles (Curse of the Azure Bonds, Secrets of the Silver Blades).
- [Gold Box Explorer](https://github.com/bsimser/Gold-Box-Explorer) - Windows Explorer-style tool to decrypt, view, and export the contents of SSI's Gold Box game files, covering titles such as Pool of Radiance and Curse of the Azure Bonds as well as Forgotten Realms: Unlimited Adventures.
- [PoR_L10n](https://github.com/grannypron/PoR_L10n) - Localization toolkit for the GOG release of Pool of Radiance, with a binary string-replacement tool for the game's EXE/OVR files and its compressed ECL resource files, plus a fork of Gold Box Explorer adapted for translation work.

##### Forgotten Realms: Unlimited Adventures

- [Dungeon Craft (UAF)](https://github.com/grannypron/uaf) - Enhanced continuation of Forgotten Realms: Unlimited Adventures (FRUA, 1993), built on the Gold Box engine and its dungeon design tools; reads and extends the original module/dungeon data formats with higher-resolution graphics and raised hard-coded limits.

##### Dark Sun

- [dsun_music](https://github.com/JohnGlassmyer/dsun_music) - Tools for extracting music, images, and other data from SSI's Dark Sun: Shattered Lands and its sequels (Dark Sun 2: Wake of the Ravager, Dark Sun Online: Crimson Sands); gff-tool extracts/replaces the games' GFF resource archives, xmi-tool describes and modifies their PSEQ/LSEQ/GSEQ music sequences.
- [Sol Oscuro](https://github.com/dsoageofheroes/soloscuro-archive) - Engine recreation project for Dark Sun: Shattered Lands, Dark Sun 2, and Crimson Sands that reads the original games' GFF resource files, including a GFF asset viewer.
- [libgff](https://github.com/dsoageofheroes/libgff) - Standalone C library and gfftool CLI for the Dark Sun games' GFF resource files, extracting images/palettes to RGBA, XMI music (with MIDI conversion), VOC sound effects, and map/text/GPL script data.

##### Birthright: The Gorgon's Alliance

- [Birthright-RE](https://github.com/minexew/Birthright-RE) - Extractor for Birthright: The Gorgon's Alliance (1996)'s RES resource archives, decompressing LZSS-compressed entries and converting the game's NOVA-format bitmaps to PNG using its palette file.

#### Exbo (Stalcraft)

- [sc-file](https://github.com/onejeuu/sc-file) - Python library, CLI and GUI converting Stalcraft assets to standard formats: `.mcsb`/`.efkmodel` models to OBJ/GLB/FBX, `.mcvd`/`.mcal` animations to GLB, `.ol` textures to DDS, `.mic` images to PNG, `.mdat` regions to Minecraft `.mca` and data files to JSON.

#### Cloud Imperium Games (Star Citizen)

- [SCExporter](https://github.com/Kjasi/SCExporter) - Blender tools for exporting Star Citizen models.
- [StarBreaker](https://github.com/diogotr7/StarBreaker) - Reverse engineering and analyzing Star Citizen's game files (P4k, DataCore, chf, etc.).
- [DataCapture](https://github.com/starcitizendotguide/DataCapture) (archived) - Captures meta-data packets from Star Citizen for statistics.

#### Trese Brothers (Star Traders: Frontiers)

- [startradersdecryptor](https://github.com/johndoe31415/startradersdecryptor) - Decryptor for Star Traders: Frontiers savegames, reverse-engineering the game's SQLite-database save format (Twofish256 in XTS mode, page-based CMAC-Twofish nonces derived via PBKDF2-SHA1) for its `core`/`data`/`game`/`map` database files.

#### Star Trek: 25th Anniversary

- [startrek25_rtools](https://github.com/Stewmath/startrek25_rtools) - C# tools for dumping and modifying Star Trek: 25th Anniversary files, decompressing the DATA.DIR/DATA.001/DATA.RUN archives (LZSS), recompressing files into a patches folder the game loads, and dumping RDF text tables and scripts.

#### Star Trek: Armada

- [Blender_ST_Armada_Tools](https://github.com/SomaZ/Blender_ST_Armada_Tools) - Blender add-on for importing SOD mesh files (versions 1.4 to 1.93) and exporting SOD versions 1.8 and 1.93 for Star Trek: Armada and Star Trek: Armada II; previews Armada I materials, with Armada II material settings only partly implemented. See also [BZNTools](games-b-c.md#big-boat-interactive-battlezone-combat-commander) for the BZN map format.

#### Star Trek: Voyager - Across the Unknown

- [stvoy-save-editor](https://github.com/ianneub/stvoy-save-editor) - Python toolkit for Star Trek: Voyager - Across the Unknown saves, reverse-engineered from the proprietary bit-packed binary (C3Serialize/FunIO, not GVAS) `.sav` format; shows chunk structure and edits resources and hull integrity.

#### Chucklefish (Starbound)

- [py-starbound](https://github.com/blixt/py-starbound) - Python package for parsing Starbound's binary save/world/universe file formats (BTreeDB5 key-value stores, versioned entity data).
  - See also the same author's earlier prototype parsers: [js-starbound-files](https://github.com/blixt/js-starbound-files) (JavaScript), [js-starbound-assets](https://github.com/blixt/js-starbound-assets) (asset loading via Web Worker), [js-starbound-player](https://github.com/blixt/js-starbound-player) (player file reader/renderer), [go-starbound](https://github.com/blixt/go-starbound) (Go), and [starbound-info](https://github.com/blixt/starbound-info) (web tool for inspecting and repairing corrupted `.fail` worlds).
- [starbounded](https://github.com/blixt/starbounded) - Chrome app for opening a Starbound install and browsing its worlds, universe, and player files.
- [starcheat](https://github.com/wizzomafizzo/starcheat) - Starbound player save editor built on py-starbound.
- [starbound-map](https://github.com/txxia/starbound-map) - GUI viewer for exploring Starbound world and universe map files, built on py-starbound.
- [Starstructor](https://github.com/Starstructor/starstructor) - Graphical editor for Starbound `.dungeon` and `.structure` (ship) files.
- [starbound-research](https://github.com/McSimp/starbound-research) - Scripts and reverse-engineered data structures documenting Starbound's file formats for modding.
- [StarDB](https://github.com/McSimp/StarDB) - Python library for reading/writing Starbound's BTree database files. See also [TinyWolfGirl's Java port](https://github.com/TinyWolfGirl/StarDB-for-Java).
- [starbound-minimap](https://github.com/lxhmsk/starbound-minimap) - Generates a map image from Starbound's saved world/player data (built on py-starbound), with optional live player tracking via process memory.
- [SBSE](https://github.com/Kazyyk/SBSE) - Desktop Starbound save file editor built with Node-Webkit.
- [kt-starbound](https://github.com/DanilaFe/kt-starbound) - Kotlin/Java library for parsing Starbound's file formats.
- [starfuse](https://github.com/Qix-/starfuse) - Mounts Starbound `.pak` archives as a FUSE filesystem; reference implementation for reading and writing the modern Starbound pak format.

#### Starbreeze Studios

- [sbengine](https://github.com/hogsy/sbengine) - Source code for Starbreeze Studios' in-house engine (1996–2012), November 2006 snapshot. Used in The Chronicles of Riddick: Escape from Butcher Bay, The Darkness, and other Starbreeze titles.
- [DieselBundleViewer](https://github.com/Luffyyy/DieselBundleViewer) (archived) - Viewer for the Diesel Engine bundle format shared across PAYDAY: The Heist, PAYDAY 2, and RAID: World War II, with search/sort, grid view, and on-the-fly WEM-to-WAV playback/conversion. No longer maintained.
- [Diesel-Bundle-Modder](https://github.com/Luffyyy/Diesel-Bundle-Modder) - Modding tool for Diesel Engine bundle files, complementing DieselBundleViewer above.
- [DieselEngineFormats](https://github.com/Luffyyy/DieselEngineFormats) - Library for reading and writing Diesel Engine file formats. Actively maintained fork of [simon-wh/DieselEngineFormats](https://github.com/simon-wh/DieselEngineFormats).
- [DieselToolbox](https://github.com/Luffyyy/DieselToolbox) - Diesel Engine asset browser. Actively maintained fork of [simon-wh/DieselToolbox](https://github.com/simon-wh/DieselToolbox).

##### The Darkness

- [TheDarkness](https://github.com/birabittoh/TheDarknessReborn) - Static recompilation of The Darkness (Xbox 360), built on the ReXGlue SDK, converting the game's `default.xex` PowerPC code into native x86_64 code at build time.

##### Payday 2

- [PD2-SuperBLT-Hasher](https://github.com/Strappazzon/PD2-SuperBLT-Hasher) - GUI and CLI tool to calculate the content hashes PAYDAY 2's SuperBLT mod loader uses to identify and load mod files/folders.
- [payday2-model-tool](https://github.com/kythyria/payday2-model-tool) - Diesel Model importer/exporter for Payday 2, with bone/rigging support in progress. See also [HW12Dev's Calcium Edition fork](https://github.com/HW12Dev/payday2-model-tool) with an improved UI, XML-based model/bone-structure scripting, and Collada/glTF import-export support.
- [payday2-tools-rust](https://github.com/kythyria/payday2-tools-rust) - Miscellaneous Rust tools for Payday 2's Diesel Engine data.
  - Features: `Idstring` hash function and hashlist search/scanning, a Dokany-based virtual filesystem exposing bundle contents as a mountable volume, and a scriptdata converter between the `Binary`, `Custom_xml`, and `Generic_xml` formats.
- [payday2-bundle-webdav](https://github.com/kythyria/payday2-bundle-webdav) - WebDAV server exposing the contents of Payday 2 `.bundle` files as a mountable network drive, avoiding extraction to disk.
  - Formats: Optionally converts on the fly — `texture` to DDS, `movie` to BIK, `strings` to JSON.
- [PAYDAY-2-Hashlist](https://github.com/Luffyyy/PAYDAY-2-Hashlist) - Hashlist of known file paths for reversing PAYDAY 2's hashed Diesel Engine bundle filenames, extending Frankelstner's original hashlist with bruteforced and manually-guessed entries; used by DieselBundleViewer and payday2-model-tool above.
- [huffin](https://github.com/echo000/huffin) - Work-in-progress Diesel Engine asset extractor, tested with Payday 2.

##### Payday 3

- [wwise_pd3](https://github.com/MoolahModding/wwise_pd3) - Open-source tool to encode PCM WAV audio to WEM and decode WEM back to WAV, for use with Payday 3's Wwise audio.
- [PD3AudioModder](https://github.com/Snoozeds/PD3AudioModder) - GUI tool for replacing PAYDAY 3 audio: converts input audio to WAV with ffmpeg, encodes it to WEM using wwise_pd3, swaps it into the `.ubulk`, fixes the size in the `.uexp`, and can pack the result with repak.
  - Uses [PD3WwiseMappings](https://github.com/Snoozeds/PD3WwiseMappings), JSON lists of PAYDAY 3 Wwise sound IDs (Media and Localized Media), to sort files when auto sort is enabled.

#### ConcernedApe (Stardew Valley)

- [StardewValley](https://github.com/veywrn/StardewValley) - Decompiled Stardew Valley source, based on the Steam release.
- [stardew-mp-save-editor](https://github.com/tfitz237/stardew-mp-save-editor) - Standalone save editor that adds and manages more than four players (up to 8) in a vanilla Stardew Valley multiplayer save without mods; its README warns it is likely no longer stable since Stardew Valley 1.5.
- [xnbcli](https://github.com/LeonBlade/xnbcli) - Node.js command-line tool that unpacks LZX-compressed Stardew Valley `.xnb` content files and packs them back, with groundwork for XACT.

#### 5pb. / Nitroplus (Steins;Gate)

- [pksgnpa](https://github.com/lennylxx/pksgnpa) - Tool for creating NPA archives used by the visual novel Steins;Gate, built for a Chinese fan translation. Bundles asmodean's exsgnpa NPA archive extractor/creator for the same format.
- [sg-unpack](https://github.com/rdavisau/sg-unpack) - Unpacker for the Mages Engine `.mpk` content files used by STEINS;GATE (Steam edition) and STEINS;GATE 0.
- [MagesPack](https://github.com/DanOl98/MagesPack) - Unpacker/repacker for Mages Engine `.mpk` archives, covering Steins;Gate (Steam), Steins;Gate 0, Steins;Gate Elite, Chaos;Child, and other titles.
- [mpk-tools](https://github.com/spaceskynet/mpk-tools) - Python CLI to pack and unpack Mages Engine `.mpk` archives (v1 and v2) for Steins;Gate, Chaos;Child, and similar games, with CSV file lists and optional compression.
- [SGLBPhenogramConverter](https://github.com/DanOl98/SGLBPhenogramConverter) - Converter for the raw 8-bit indexed "Linear Bounded Phenogram" image format used inside Steins;Gate's Mages Engine archives, reversed and documented by the author (header, 256-color map, then raw pixel data).

##### Re:Zero: -Starting Life in Another World- Death or Kiss

- [psv-rz-tool](https://github.com/hiroshil/psv-rz-tool) - Extraction/repacking tool for the PS Vita visual novel *Re:Zero kara Hajimeru Isekai Seikatsu: Death or Kiss* (5pb.).

##### Memories Off: -Innocent Fille-

- [Innocent-Fille-MPK](https://github.com/master801/Innocent-Fille-MPK) - Tool to extract and create MPK archives for the PS Vita game Memories Off: -Innocent Fille-.

#### MIST Games (Stella Maiden: Girls of the Stars)

- [SM.PKG.Tool](https://github.com/Ekey/SM.PKG.Tool) (archived) - Tool for extracting PKG archives from the mobile game Stella Maiden: Girls of the Stars (스텔라 메이든).

#### Stern Pinball

- [ske-spk-tools](https://github.com/JayFoxRox/ske-spk-tools) - Extracts and packs Stern Spike (Spike 1/2/3) pinball machine software update archives (.spk), including tar.gz-wrapped early titles and LUKS2/squashfs-wrapped Spike 3 packages.
- [ske-radium](https://github.com/JayFoxRox/ske-radium) - Decoder and player for scene.radium scene files used by the UI/animation engine of modern Stern Spike pinball machines.
- [ske-scanners](https://github.com/JayFoxRox/ske-scanners) - Tools to extract data from Stern Spike pinball machine game binaries as part of reverse-engineering the platform.
- [ske-dumper](https://github.com/JayFoxRox/ske-dumper) - Backs up Stern Spike 1/2 pinball machine EEPROMs and hardware fuses over a debug connection.
- [ghidra_whitestar_loader](https://github.com/c0rner/ghidra_whitestar_loader) - Ghidra extension that loads Sega/Stern Whitestar pinball game ROMs, building a complete navigable memory map including banked ROM overlays and I/O registers.

#### Shooting Game Builder (STGB)

- [Old-Shooting-Game-Builder-Game-Unpack-Tool-STGB](https://github.com/vihithr/Old-Shooting-Game-Builder-Game-Unpack-Tool-STGB) - Unpacks pre-Steam Shooting Game Builder (STGBuilder) `.gamedat` archives and restores the project structure, reading the packed index and the `.sbd` string table to recover original Shift_JIS file names.

#### Sting

##### Baroque

- [BaroqueArchiveTool](https://github.com/HunterStanton/BaroqueArchiveTool) - Extractor for DATA.DIR/DATA.BIN archives from the PS2 game Baroque.

#### Marvelous (Story of Seasons)

- [sosawl-font-data-edit](https://github.com/Giza/sosawl-font-data-edit) - Tool for extracting and repacking the font parameter `.bin` files in Story of Seasons: A Wonderful Life.
- [SOSSE](https://github.com/RainThunder/SOSSE) - C# save editor for Story of Seasons, working on decrypted save files extracted with homebrew or SaveDataFiler.

#### Guard Crush Games / Lizardcube (Streets of Rage 4)

- [bigfile_tools](https://github.com/JadingTsunami/bigfile_tools) - Tools for editing Streets of Rage 4's proprietary bigfile game data format.
  - Features: Bigfile Editor (imports/exports compressed and uncompressed bigfiles, browses and edits annotated game data tables in a GUI), Level Editor (individually swaps enemy, pickup, and breakable spawn points in any playable level).
- [SOR4TEX](https://github.com/Jayveer/SOR4TEX) - Extracts textures from Streets of Rage 4 texture and texture-table files.

#### Streets of Rogue

- [Rogue_Save_Editor_UnlockTool](https://github.com/Dere3046/Rogue_Save_Editor_UnlockTool) - .NET tool that exports Streets of Rogue `GameUnlocks.dat` to JSON, repacks it to the game's binary format, creates new unlock files and edits statistics.

#### Studio Pixel

##### Cave Story

- [Booster's Lab](https://github.com/taedixon/boosters-lab) - Cross-platform level editor for Cave Story.
- [Cave Story MD](https://github.com/andwn/cave-story-md) - Fan port of Cave Story to the Sega Mega Drive/Genesis, converting the original game's tilesets, sprites, and music data for Sega Genesis hardware.
- [NXEngine-evo](https://github.com/nxengine/nxengine-evo) - Actively maintained refactor of NXEngine, an open-source reimplementation of the Cave Story engine that reads the original game's PXA/TSC/Organya data files.
- [NXEngine (EXL's port)](https://github.com/EXL/NXEngine) - Multi-platform port of the original NXEngine Cave Story engine rewrite, targeting additional platforms (including MotoMAGX feature phones) not covered by the mainline nxengine-evo fork.
- [doukutsu-rs](https://github.com/doukutsu-rs/doukutsu-rs) - Cross-platform reimplementation of the Cave Story engine in Rust, reading the original game's PXA/TSC/Organya data files.
- [vanilla-extractor](https://github.com/doukutsu-rs/vanilla-extractor) - Extracts the original Cave Story game assets (PXA/TSC/Organya data) embedded in the vanilla Doukutsu.exe executable.
- [organism](https://github.com/doukutsu-rs/organism) - Converts Cave Story's Organya (.org) music format to WAV audio.
- [OrgPtcop](https://github.com/taedixon/OrgPtcop) - Java converter from Cave Story's Organya (.org) music, notes and drum tracks, to the PxTone PtCop (.ptcop) format, one-way only. Includes a document describing the .ptcop binary format.
- [DoukutsuPSX](https://github.com/fgsfdsfgs/doukutsupsx) - Port of Cave Story to the PlayStation, built on the CSE2 decompilation and converting the original freeware game's data into a bootable PSX ISO.
- [organya (Organya Twei)](https://github.com/shbow/organya) - Original Organya music sequencer source code, created by Studio Pixel in 1999 and used to compose Cave Story's soundtrack in the .org format.
- [libpxtone](https://github.com/Wohlstand/libpxtone) - Library to play and edit music in the PTTUNE and PTCOP (pxtone) formats, a modified version of Pixel's pxtone 220910a with bug fixes and big-endian processor support.
- [node-chie](https://github.com/jozsefsallai/node-chie) - Node.js library and CLI tool for decrypting/encrypting Cave Story's TSC script files.

##### Ikachan

- [ikachan (hax0kartik)](https://github.com/hax0kartik/ikachan) - Matching decompilation of the Nintendo 3DS port of Ikachan. See also [Ikachan Decomp](https://github.com/Cuckydev/Ikachan) for the original freeware PC release.

##### Guxt

- [GuxtDecomp](https://github.com/alula/GuxtDecomp) - Matching decompilation of Guxt (v1.0.2.0), Studio Pixel's 2007 freeware shoot-'em-up; 100% playable, built largely on prior reverse engineering work by tilderain.

##### Kero Blaster / Pink Hour / Pink Heaven

- [KeroMaster](https://github.com/Gota7/KeroMaster) - Level editor for Studio Pixel games. Works with proprietary game file formats for level data and tile assets.

#### Geoff Crammond (Stunt Car Racer)

##### Stunt Car Racer

- [stunt-car-racer-ste](https://github.com/jonathanopalise/stunt-car-racer-ste) - Experimental patches for the Atari ST version of Stunt Car Racer (1989), reverse-engineered to offload CPU-driven rendering routines onto the STE's Blitter chip.

##### The Sentinel

- [sentland](https://github.com/simonowen/sentland) - Python script reverse-engineering The Sentinel's (aka The Sentry) landscape generation algorithm, reproducing the exact tile-height/shape map data and object placement for any of the game's landscapes.
- [sentcode](https://github.com/simonowen/sentcode) - Python script reverse-engineering the secret landscape-access codes for every version of The Sentinel (BBC, C64, CPC, Spectrum, ST, PC, Amiga), replicating each version's RNG and digit-encoding differences.
- [Augmentinel](https://github.com/simonowen/augmentinel) - Enhanced remake of The Sentinel that emulates the original Spectrum Z80 game code for authentic logic and landscape data, while adding accelerated 3D rendering, VR support, and assets/music from other original ports.

#### Stunt GP

- [stunt_gp_tools](https://github.com/stuntkit/stunt_gp_tools) - Go tools for Stunt GP file formats, packing and unpacking the PC and Dreamcast texture files, with links to a wiki documenting the game's formats.

#### Distinctive Software (Stunts)

- [restunts2](https://github.com/dstien/restunts2) (archived) - Reverse engineering and modernization effort for Stunts (1990, DOS), using Ghidra analysis and Open Watcom to port the original executable to portable C while preserving behavior; supports building fully-ported or hybrid original/ported executables.

#### Sudden Attack

- [mxs_sudden_attack_mobile](https://github.com/coreynguyen/mxs_sudden_attack_mobile) - MaxScript for importing LithTech Binary (LTB) models with bone hierarchies from the mobile game Sudden Attack.

#### Suikoden

- [Suikoden-5-Editor](https://github.com/TheSparda/Suikoden-5-Editor) - Browser-based save and ISO editor for Suikoden V (PS2). Edits saves from `.ps2`/`.mc2`/`.mcd`/`.bin` memory cards, `.psu`, `.xps`/`.sps` and `.cbs` exports (NTSC-U, PAL, NTSC-J) and edits game data on NTSC-U (`SLUS-21291`) and PAL (`SLES-54087`) disc images, with a field reference in `docs/editing-guide.md`.
- [Suikoden-4-Editor](https://github.com/TheSparda/Suikoden-4-Editor) - Browser-based save and ISO editor for Suikoden IV (PS2). Edits recruitment, levels, stats, runes, equipment and unite attacks in NTSC-U and PAL saves, re-checksumming and re-ECCing them, and scales the random-encounter rate on the NTSC-U disc.
- [Suikoden-3-Editor](https://github.com/TheSparda/Suikoden-3-Editor) - Browser-based ISO and save editor for Suikoden III (PS2, USA `SLUS-20387`). Rebalances spells, runes, unite attacks, gear, weapons, foods, shops, enemies, war units and characters in the disc image, and edits playthroughs from PS2 memory cards or standalone save exports.
- [Suikoden-Tactics-Editor](https://github.com/TheSparda/Suikoden-Tactics-Editor) - Browser-based save and ISO editor for Suikoden Tactics (USA `SLUS-21245`, PAL `SLES-53769`). Edits `.sps`/`.xps`/`.cbs`/`.max`/`.psu` exports and raw `.ps2` memory cards, and edits character growth, weapons, runes, items, shop and enemy tables on the disc in place, exporting a `.stmod` recipe or an `.xdelta` patch.

#### Double Cross (Sultan's Game)

- [kismet](https://github.com/crimzonlilia/kismet) - Reverse-engineering and save/asset documentation project for Sultan's Game, a text-driven strategy game developed by Double Cross (Double-Headed Dragon Studio).

#### Sunsoft

- [atlantis-no-nazo](https://github.com/Xkeeper0/atlantis-no-nazo) - Work-in-progress disassembly of Atlantis no Nazo (Mystery of Atlantis, Famicom/NES), building a 1:1 copy of the ROM including its rarely-seen sample release.
- [Quest-RPG-Brians-Journey-Decompilation](https://github.com/nefelibatacfg/Quest-RPG---Brian-s-Journey-USA-Decompilation.) - Byte-identical decompilation of Quest RPG: Brian's Journey (Atelier Double/Sunsoft, Game Boy Color, 2000), disassembled with mgbdis and reassembled with RGBDS.
- [Gimmick-ROM-extractor](https://github.com/Infinest/Gimmick-ROM-extractor) - Extracts the raw NES ROM from the encrypted `AR_win32.mdf` resource file of the Steam release of GIMMICK! Special Edition; alternate configs cover Abarenbo Tengu & Zombie Nation, F-117A Stealth Fighter and Streets of Kamurocho.

#### Assembly Line (Supaplex)

- [superplexed](https://github.com/kaimitai/superplexed) - Supaplex level and graphics editing suite.

#### McLeodGaming (Super Smash Flash 2)

- [ssf2_modloader](https://github.com/phase/ssf2_modloader) - Compressor/decompressor for Super Smash Flash 2's `.ssf` data files, which are zlib-compressed `.swf` (Shockwave Flash) assets.

#### Qcplay (Super Snail)

- [Super_Snail_Decrypt_-_Convert_Tool](https://github.com/Randombirdnoise/Super_Snail_Decrypt_-_Convert_Tool) - Python script to decrypt and convert the encrypted image assets of Super Snail (Qcplay Limited).

#### Supercell

- [SCEditor](https://github.com/ToxicLand/SCEditor) - Create or edit Supercell (Clash of Clans, Clash Royale, Brawl Stars, Boom Beach) SC files. Add or edit an existing or custom character, building, or other game object.
- [SCP-Unpacker](https://github.com/baraklevy20/SCP-Unpacker) - Unpacker for Supercell's new packer (SCP) format.
- [Supercell-Extractor](https://github.com/baraklevy20/Supercell-Extractor) - Fastest tool to extract graphics from Supercell games (Clash of Clans, Clash Royale, etc.).
- [sc-compression](https://github.com/jeanbmar/sc-compression) - Node.js module to decompress and compress game assets from Supercell games. Supports multiple compression signatures: lzma, sc, sclz, sig, sc2, and zstd. Automatically infers compression signature when decompressing.
- [gltf-Supercell-IO](https://github.com/Daniil-SV/gltf-Supercell-IO) - glTF Blender IO plugin for import/export Supercell Odin (.glb) files. Supports Blender 5.0+ and Android/iOS games.
- [SupercellFlash](https://github.com/sc-workshop/SupercellFlash) - C++ library for loading and processing Supercell 2D (.sc) assets.
- [SupercellTexture](https://github.com/sc-workshop/SupercellTexture) - C++ library for reading, writing, and compressing Supercell games' packed texture formats.
- [X-coder](https://github.com/lilmuff2/X-coder) (archived) - Tool to decode and encode SC files from Supercell games. Decodes SC to PNG and encodes PNG to SC. Supports Clash Royale, Brawl Stars, and other Supercell games. Supports Zstandard and LZMA compression, ZKTX format, and batch processing.
- [scw-tool](https://github.com/danila-schelkov/scw-tool) - CLI tool for converting Supercell 3D model formats (*.scw) to COLLADA and other formats.
- [SC Editor](https://github.com/danila-schelkov/sc-editor) - Viewer and editor for Supercell SC proprietary graphics file format.
- [SC Tools](https://github.com/jeanbmar/sc-tools) - Unpacker, editor, and player for 2D animations and objects in Supercell games' SC file format.
- [SCW Tools](https://github.com/jeanbmar/scw-tools) - Converts Supercell games' SCW 3D model format to COLLADA (DAE), with format schema documentation.
- [scw_parse](https://github.com/BlaCoiso/scw_parse) - Node.js library to parse Brawl Stars' SCW (SC3D) 3D model files.
- [coc-messages](https://github.com/clugh/coc-messages) - Reverse-engineered protocol/message definitions for Clash of Clans' SC-based network format.
- [bb-messages](https://github.com/SC-DevTeam/bb-messages) - Reverse-engineered protocol/message definitions for Boom Beach's SC-based network format.
- [cocdp (Clash of Clans Documentation Project)](https://github.com/clanner/cocdp) - Documentation of the Clash of Clans network protocol and message formats.
- [Pinocchio](https://github.com/SC-DevTeam/Pinocchio) - All-in-one reverse engineering toolkit for Clash of Clans, Clash Royale, Boom Beach, and Hay Day.
- [GDumper](https://github.com/iGio90/GDumper) - Packet dumper, protocol parser, and encryption toolkit for Supercell games' SC-based network protocol.

#### SuperTuxKart

- [STK Blender Addons](https://github.com/supertuxkart/stk-blender) - Exporter/importer suite for SuperTuxKart `SPM` meshes and `Antarctica` engine assets.

#### Gas Powered Games (Supreme Commander)
- [dungeon-siege-re](https://github.com/glampert/dungeon-siege-re) - Tools and docs for Dungeon Siege and Legends of Aranna assets; opens Tank archives (`.dsres`/`.dsmap`), converts RAW textures to PNG/TGA, and converts Aspect (`.asp`) and Siege Node (`.sno`) geometry to Wavefront OBJ (the latter two partially).

- [supcom2-map-toolkit](https://github.com/plutonics72/supcom2-map-toolkit) - Reverse-engineered toolkit for creating Supreme Commander 2 custom maps, including navmesh editing so units path correctly.
  - Formats: hfield.win.bdf (heightfield), terrain.win.bdf, costs.win.bdf, collision2.win.bdf, waterDepth.dds — reverse engineered as a mutually-consistent five-file stack.

#### Surreal Software

- [Drakan Editing Tools v1.2](https://www.moddb.com/games/drakan-order-of-the-flame/downloads/drakan-editing-tools-v12) - Surreal Softwares, Level and model Editor for "Drakan Edition"
- [reo converter to obj (Drakan: Order of the Flame)](https://www.moddb.com/games/drakan-order-of-the-flame/downloads/reo-converter-to-obj) - by Roosen5 – useful for level editors and game mods. For developers only! - See more at: arokhslair

#### Kerberos Productions (Sword of the Stars)

- [Sots.Sots1.SavedGameEditor](https://github.com/BardezAnAvatar/Sots.Sots1.SavedGameEditor) - Saved game editor for Sword of the Stars (SotS).
- [SOTSedit](https://github.com/ghbplayer/SOTSedit) - C# save game editor for Sword of the Stars 1; the author notes a weak game parser and known issues.

#### Touch Foo (Swordigo)

- [swordigo-resources](https://github.com/DanielSpaniel8/swordigo-resources) - Community resource hub for Swordigo: original APK source files, converted/decompiled assets, ripping/speedrun tools, and a modding guide.

#### Synetic

- [wr_toolkit](https://github.com/Kromster80/wr_toolkit) - Modding toolkit for Synetic's racing games, covering model, map, and archive formats.
  - Games: Mercedes-Benz World Racing, World Racing 2, Mercedes-Benz Truck Racing (partial), and the Alarm für Cobra 11 series (Nitro, Crash Time, Burning Wheels, Highway Nights, The Syndicate, Undercover). See also [RoadTrain's fork](https://github.com/RoadTrain/wr_toolkit).
- [SyneticConverter](https://github.com/Grille/SyneticConverter) - Library and tool suite (SyneticPipelineTool, SyneticConverter, SyneticLib) for converting models and maps between Synetic engine games.
  - Games: Need for Speed II/Need for Speed: Porsche Unleashed engine-derived NICE1/NICE2 titles, Mercedes-Benz Truck Racing (MBTR), Mercedes-Benz World Racing/World Racing 2 (WR1/WR2), the Cobra 11 series (C11, CT1-5), and Ferrari Virtual Race (FVR).
- [MBTR-file-formats](https://github.com/AlexKimov/MBTR-file-formats) - File formats and tools for Mercedes-Benz Truck Racing (2000).

#### Synthetik

- [Synthetik_Python_Mod](https://github.com/Builder-roberts/Synthetik_Python_Mod) - Python save editor for Synthetik's `Save.sav`: edit class loadouts, pistol and module slots and power, and subclass level, with weapon and item spawn lists.
