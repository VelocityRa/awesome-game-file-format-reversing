### Graphics, Animation & Asset Technology
#### Fast3d/F3dex (N64)

*SGI's microcode format for defining 3D graphics on the Nintendo 64. Used in [Super Mario 64](games-n-o.md#super-mario-64), [Paper Mario 64](games-i-l.md#paper-mario-64), [Banjo-Kazooie](games-p-r.md#rare), and many other N64 titles.*

- [n64-fast3d-engine](https://github.com/Emill/n64-fast3d-engine) - N64 Fast3D engine implementation.
- [noclip.website (Banjo)](https://github.com/magcius/noclip.website/blob/main/src/BanjoKazooie/f3dex.ts) - F3DEX implementation for Banjo-Kazooie viewer.
- [MeltyTool (F3dzex2)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/F3dzex2) - F3DZEX2 format support.
- [F3DEX2Decoder](https://github.com/Mr-Wiseguy/F3DEX2Decoder) - Decoder for F3DEX2 display lists.
- [F3D2F3DEX](https://github.com/Trenavix/F3D2F3DEX) - Converter between F3D variants.
- [Hack64 Fast3D Commands](https://hack64.net/wiki/doku.php?id=super_mario_64:fast3d_display_list_commands) - Documentation for Fast3D display list commands.
- [CloudModding F3DZEX2](https://wiki.cloudmodding.com/oot/F3DZEX2) - Documentation for F3DZEX2 format.
- [fast64](https://github.com/Fast-64/fast64) - Blender plugin for exporting F3D display lists for N64 decompilation projects (Super Mario 64, Ocarina of Time).
- [pigment64](https://github.com/decompals/pigment64) - Rust library for converting N64 image data (Intensity, IA, CI, RGBA formats) between native and PNG formats, used by N64 decompilation projects.
- [F3DEX3](https://github.com/HackerN64/F3DEX3) - Modern, heavily rewritten F3D-family microcode for N64 romhacks; rewrites vertex/lighting code from scratch for higher performance, adds new visual features (simultaneous vertex colors + normals, ambient occlusion), and improves accuracy over F3DEX2.
- [RT64](https://github.com/rt64/rt64) - N64 graphics renderer implementing the RDP/F3D microcode family with enhancements (widescreen, higher resolutions, ray tracing) for emulators and native ports.
- [n64rawgfx](https://github.com/Octocontrabass/n64rawgfx) - Exports and imports uncompressed ("raw") N64 graphics (RGBA, CI, IA, I formats) to/from BMP files, e.g. for Super Mario 64 texture editing.

#### Granite SDK

*Texture streaming middleware (.gts/.gtp files) used across multiple titles.*

- [GraniteTextureReader](https://github.com/Nenkai/GraniteTextureReader) - Texture reader/extractor for Granite SDK files (.gts/.gtp).

#### Havok

*Physics and animation middleware used in hundreds of games across all platforms.*

- [Havok IO (Blender)](https://github.com/NewSkyLine-dev/havokmax-blender) - Havok tool for Blender (replaces legacy HavokMax 3ds Max plugin). Blender add-on that imports `.hkx`, `.hkt`, `.hka`, `.igz`, and `.pak` files from Havok XML and binary archives.
  - Capabilities: builds armatures and keyframed actions from animation data, constructs static meshes from geometry blocks, and unwraps PAK/IGZ containers.
- [HavokNoesis](https://github.com/PredatorCZ/HavokNoesis) - Noesis plugin for Havok format.
- [MapEditor](https://github.com/BF3RM/MapEditor) - Realtime map editor mod for Venice Unleashed (Battlefield 3).
- [HavokPreviewToolsBatch2018](https://github.com/asasasasasbc/HavokPreviewToolsBatch2018) - Batch conversion script for Havok Preview Tool 2018 that can automatically convert Havok HKX/HKT files' format.
- [hkxlib](https://github.com/aerisarn/hkxlib) - JAXB parser for editing TAGXML formatted Havok files.
- [hkxEdit](https://github.com/aerisarn/hkxEdit) - Visual editor for Havok 2010.2 files based on hkxlib, written in Java.
- [TagTools](https://github.com/blueskythlikesclouds/TagTools) - Tools for editing Havok 2015/2016 binary tag files. Includes TagTools converter and CollisionConverter for converting rigid bodies to static compound shapes with type and flag tags.
- [HKCLTool](https://github.com/VelouriasMoon/HKCLTool) - Editing tool for Havok `.hkcl` cloth files built on the HKX2 library. Merges, lists, removes cloth entries and converts platforms.
- [FF16-Model-Importer](https://github.com/KillzXGaming/FF16-Model-Importer) - Tool to export and import Final Fantasy XVI .mdl file binaries as .gltf or .dae.
- [FF16-010-Templates](https://github.com/KillzXGaming/FF16-010-Templates) - 010 Editor templates for Final Fantasy XVI file formats, covering MTL (material) and TEC (shader table) files.
- [SSE-Fallout-4-Animation-Converter](https://github.com/Backporter/SSE-Fallout-4-Animation-Converter) - Tool to convert animations to PS4 format for Skyrim Special Edition and Fallout 4.
- [hkxcmd (aerisarn fork)](https://github.com/aerisarn/hkxcmd) - Tool for working with HKX (Havok animation format) used in Elder Scrolls and Fallout series.
- [hkxcmd](https://github.com/BadDogSkyrim/hkxcmd) - Command-line tool for parsing, converting, and modifying Havok HKX animation format files.
- [Blender HKX](https://github.com/BadDogSkyrim/blender-hkx) - Blender addon for importing and exporting Havok HKX animation format.
- [HavokLib](https://github.com/PredatorCZ/HavokLib) - C++ library for reading, converting, and upgrading/downgrading Havok physics packfiles across versions (5.0.0-2017).
- [havok2fbx](https://github.com/Highflex/havok2fbx) - Converts Havok files to Autodesk FBX.
- [mayhem](https://github.com/ackwell/mayhem) - Pure Rust reader for Havok tagfile binary formats, currently focused on the Havok animation/physics data embedded in Final Fantasy XIV files.
- [HKLib](https://github.com/The12thAvenger/HKLib) - Library for reading and writing Havok files, currently supporting Havok 2018.
- [hkscdis-rs](https://github.com/Surasia/hkscdis-rs) - Rust disassembler for HavokScript 5.1 bytecode that outputs a human-readable listing, with optional support for structure-inheritance extensions.
  - Predecessor: [hksc-disassembler](https://github.com/Surasia/hksc-disassembler), a Python HavokScript 5.1 disassembler and bytecode parser with documentation of the largely undocumented HavokScript bytecode format.

#### JSYSTEM (GameCube/Wii)

*Nintendo's in-house middleware used to develop GameCube and Wii era games. Used in [Pikmin](games-n-o.md#pikmin), [Pikmin 2](games-n-o.md#pikmin-2), [Luigi's Mansion](games-n-o.md#luigis-mansion), [Super Mario Sunshine](games-n-o.md#super-mario-other), [Super Mario Galaxy](games-n-o.md#super-mario-other), [Wind Waker](games-n-o.md#zelda), [Twilight Princess](games-n-o.md#zelda), [Mario Kart: Double Dash](games-n-o.md#mario-kart-double-dash), and many other first-party GameCube/Wii titles.*

- [gclib](https://github.com/LagoLunatic/gclib) - Python implementations of several GameCube file formats for ROM hacking.
- [gcmtools (gcm.hpp)](https://github.com/jchv/gcmtools) - C++ library for reading and manipulating raw GameCube disc images (GCM) and their FST filesystem structure.
- [Amnoid GC Resources](http://amnoid.de/gc/) - Documentation and resources for GameCube file formats.
- [JStudio (LordNed)](https://github.com/LordNed/JStudio) - Classes for Wind Waker J* tools.
- [J3D-Model-Viewer](https://github.com/LordNed/J3D-Model-Viewer) - Viewer for J3D models.
- [Hack.io](https://github.com/SuperHackio/Hack.io) - Libraries for J3D Era formats.
- [noclip.website (JSYSTEM)](https://github.com/magcius/noclip.website/tree/main/src/Common/JSYSTEM) - In-browser viewer for JSYSTEM formats.
- [MeltyTool (JSystem)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/JSystem) - JSystem format viewer/exporter.
- [SuperBMD](https://github.com/Sage-of-Mirrors/SuperBMD) - BMD/BDL model converter for GameCube/Wii games.
- [SuperBMD-TPHD](https://github.com/RenolY2/SuperBMD-TPHD) - Fork of SuperBMD above with additional features, made for use with TPHD Model Helpers.
- [SuperBMD (RenolY2 fork)](https://github.com/RenolY2/SuperBMD) - Actively maintained continuation of Sage-of-Mirrors/SuperBMD above (325+ commits ahead), with additional fixes and features beyond the stale original.
- [p2setoolkit](https://github.com/NerduMiner/p2setoolkit) - Toolkit for disassembling/reassembling Pikmin 2 BMS sequenced music files.
- [BiMuSeq](https://github.com/RenolY2/BiMuSeq) - Player/interpreter for Pikmin 2's BMS sequenced music files.
- [Rain336/JSystem](https://github.com/Rain336/JSystem) - Rust libraries for parsing Nintendo Wii/GameCube file formats.
  - Formats: BCSV, RARC, U8.
- [picori](https://github.com/Julgodis/picori) - Picori (ピッコル) is a library for decompilation, modding, and rom-hacking with focus on GameCube and Wii games.
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
- [chutools](https://github.com/TwilitRealm/chutools) - Collection of tools for JAudio audio assets in Nintendo games, an updated version of XAYRGA's JAMTools.
  - Formats: JASE, JBST, IBNK (v1/v2), BMS (disassembler).
- [JaiSeqX](https://github.com/XAYRGA/JaiSeqX) - JAudio Engine (JAI Sequence) emulator and GameCube BMS player.
- [py-playBMS](https://github.com/RenolY2/py-playBMS) - Reads and plays back BMS sequenced music files from various GameCube games.
- [BMS-Analyzer](https://github.com/3e2j/BMS-Analyzer) - Nintendo Wii/Gamecube BMS to MIDI converter
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
- [btk-conv](https://github.com/RenolY2/btk-conv) - Converter between the BTK texture animation format (used in GameCube/Wii games such as Super Mario Sunshine and Pikmin 2) and a text-based format.
- [bark-conv](https://github.com/RenolY2/bark-conv) - Converter between the BRK register/constant color animation format (used in GameCube/Wii games such as Super Mario Sunshine, Mario Kart: Double Dash, and Super Mario Galaxy) and JSON for easier editing.
- [bck2bca](https://github.com/RenolY2/bck2bca) - Converts BCK keyframed character animations to BCA per-frame animation data, linearly interpolating keyframes.
- [bmdmaterializer](https://github.com/RenolY2/bmdmaterializer) - Tool for dumping and injecting BMD material data.
- [BmtInjectExtract](https://github.com/RenolY2/BmtInjectExtract) - Injects and extracts J3D BMT material files into and from BMD/BDL files (used in GameCube/Wii games such as Super Mario Sunshine and Zelda: Wind Waker).
- [RarcPack](https://github.com/Sage-of-Mirrors/RarcPack) - RARC archive packer.
- [pyjkernel](https://github.com/SunakazeKun/pyjkernel) - Python library for JKernel formats.
- [WiiExplorer](https://github.com/SuperHackio/WiiExplorer) - Wii filesystem explorer.
- [ARCTool](https://github.com/tpwrules/ARCTool) - Python script to extract RARC, Yaz0, and U8 archives.
- [atirut.bdl](https://github.com/atirutw/atirut.bdl) - JSYSTEM BMD/BDL model importer for Godot Engine.
- [wsystool](https://github.com/XAYRGA/wsystool) - WAVESYSTEM modification toolkit for JSYSTEM games.
- [jampacked](https://github.com/XAYRGA/jampacked) - BAA unpacker for JSYSTEM games.
- [bast](https://github.com/XAYRGA/bast) - JAudio soundtable (JASE/JBST) packer and unpacker.
- [SEBS](https://github.com/XAYRGA/SEBS) - Packs and unpacks JAudio `SE.BMS` sound-effect sequence files, with a BMS assembler and disassembler driven by per-game JSON definitions.
- [bastool](https://github.com/XAYRGA/bastool) - Edits `.bas` (binary audio sequence) files for GameCube games.
- [jatafc](https://github.com/XAYRGA/jatafc) - Encodes WAV audio to JAudio AFC streams (ADPCM4 or PCM16), with a loop option.
- [exaudme](https://github.com/XAYRGA/exaudme) - Extractor for `defaultme.bme` (BME/BMT) files from JSYSTEM games.
- [libJAudio](https://github.com/XAYRGA/libJAudio) - Library for interfacing with JAudio/BMS in GameCube games, listing Luigi's Mansion, Super Mario Sunshine, Mario Kart: Double Dash, Wind Waker, Twilight Princess and Four Swords Adventure as verified (archived).
- [aurora](https://github.com/encounter/aurora) - Source-level GameCube & Wii GX graphics compatibility layer, used by decompilation and static-recompilation projects to run original GC/Wii rendering code on modern backends (Dawn/WebGPU).
- [BMDCubed](https://github.com/Sage-of-Mirrors/BMDCubed) - Converts skinned COLLADA (.dae) files to the Binary Model Data (BMD) format used by first-party Nintendo GameCube and Wii games.
- [j3d-animation-editor](https://github.com/tarsa129/j3d-animation-editor) - Editor for a variety of J3D animation files.
- [GCFT](https://github.com/LagoLunatic/GCFT) - GUI multitool for viewing and modifying common GameCube file formats, built on the gclib library above. See also the author's fast Python compression/format libraries: [PyFastYaz0Yay0](https://github.com/LagoLunatic/PyFastYaz0Yay0) (Yaz0/Yay0) and [PyFastBTI](https://github.com/LagoLunatic/PyFastBTI) (BTI textures).

#### NW4R (Nintendo Wii Revolution SDK)

*Nintendo's Wii-era NW4R middleware, covering models, UI layouts, textures, and sound archives used across first-party and licensed Wii titles (and its NW4R/BRRES format family reused in later NintendoWare SDKs).*


#### SEAD (Nintendo EAD/EPD Engine)

*Decompilation of Nintendo EAD/EPD's internal engine and standard library, used across many first-party Wii U and Switch titles including New Super Mario Bros. U.*

- [sead (open-ead)](https://github.com/open-ead/sead) - Actively maintained decompilation of the sead engine/library developed by Nintendo EAD (now EPD), the standard C++ library underpinning many first-party Wii U and Switch titles. See also [sead-ng](https://github.com/fruityloops1/sead-ng), targeting the headers used in newer games.
- [sead (aboood40091)](https://github.com/aboood40091/sead) - Earlier decompilation of the sead engine/library, covering New Super Mario Bros. U specifically. Includes the `agl` graphics library and an `nw_ptcl` wrapper for NintendoWareForCafe's Eft particle library.
- [agl (open-ead)](https://github.com/open-ead/agl) - Standalone, actively maintained decompilation of agl, Nintendo EAD/EPD's graphics, lighting, and parameter (AAMP) utility library used across many first-party games. See [sead](https://github.com/open-ead/sead) for the surrounding engine/build system.
- [EventFlow (open-ead)](https://github.com/open-ead/EventFlow) - Decompilation of EventFlow (evfl), Nintendo EAD/EPD's event/cutscene flowchart library used across Breath of the Wild and other Switch titles.
- [NintendoSDK-NEX (open-ead)](https://github.com/open-ead/NintendoSDK-NEX) - Decompilation of NEX, the Nintendo Switch networking library directly based on Quazal's Rendez-Vous middleware; used by Super Mario Odyssey and other titles for online multiplayer.
- [NW4F-Eft (open-ead)](https://github.com/open-ead/NW4F-Eft) - Decompilation of Eft, NintendoWare for Cafe's particle-effect library present in New Super Mario Bros. U; complements the `nw_ptcl` wrapper noted in the aboood40091 sead decompilation above.
- [AglLightProbeTool](https://github.com/KillzXGaming/AglLightProbeTool) - Tool for handling AGL lighting probe files (`.bglpbd`), the light-probe format used by Nintendo EAD/EPD's agl graphics library (see agl above).

#### Mii (RFL/FFL Face Library)

*Nintendo's Mii avatar creation/rendering libraries, used across the Wii, Wii U, 3DS, and Switch.*

- [RFL](https://github.com/koopthekoopa/RFL) - Decompilation of the Revolution Face Library (RFL), Nintendo's Mii avatar library for the Wii.
- [ffl](https://github.com/aboood40091/ffl) - Decompilation of FFL (Face Library), the successor to RFL used for Mii avatars on Wii U, 3DS, and Switch.
- [FFL-Testing](https://github.com/ariankordi/FFL-Testing) - Mii rendering sample and renderer server built on the FFL decompilation. Fork of [aboood40091/FFL-Testing](https://github.com/aboood40091/FFL-Testing) with added rendering server functionality.
- [FFL.js](https://github.com/ariankordi/FFL.js) - JavaScript bindings and Three.js renderer for FFL, enabling in-browser Mii rendering from the Wii U Mii renderer decompilation.
- [mii2studio](https://github.com/JimKatz/mii2studio) - Command-line tool converting Mii data between Wii, 3DS, Wii U, Miitomo, and Switch formats, outputting files loadable by Nintendo's Mii Studio and PNG renders via Nintendo's rendering API.
- [mii-assets](https://github.com/jaames/mii-assets) - Reverse-engineered Nintendo's Face Library rendering pipeline and extracts the textures/meshes it uses for Mii avatars.
- [MiiPort](https://github.com/Genwald/MiiPort) - Nintendo Switch homebrew application for importing and exporting Mii data.

#### Katana Engine (Koei Tecmo)

*Koei Tecmo's in-house engine and asset formats (G1M models, G1T texture archives, G1A/G2A skeletal animations), used across Team Ninja, Omega Force, and Gust titles as well as several external collaborations.*

- [Project-G1M](https://github.com/Joschuka/Project-G1M) - Native C++ Noesis plugin for G1M model, G1T texture, and G1A/G2A skeletal animation files. Used across Nioh, Dead or Alive 5/6, the Warriors series (Dynasty/Samurai Warriors, Hyrule Warriors, Fire Emblem Warriors), Atelier, Toukiden, Fire Emblem: Three Houses, and Persona 5 Scramble. Supersedes the same author's Python-based [fmt_g1m](https://github.com/Joschuka/fmt_g1m).

#### M3G (Mobile 3D Graphics API)

*Java Mobile 3D Graphics API (JSR-184) used by many J2ME mobile games in the 2000s.*

- [m3gcore](https://github.com/toaarnio/m3gcore) - Core engine implementation (in C) of the M3G (JSR-184) API, originally developed at Nokia Research Center and later released as open source through the Symbian Foundation.
- [m3x](https://github.com/toaarnio/m3x) - Java XML tools for M3G (JSR-184) 1.0 content, defining an XML schema (`.m3x`) that maps deterministically to the binary `.m3g` format, with an ANT task and CLI for XML-to-binary conversion.
- [M3G-Blender-Exporter](https://github.com/3dcinetv/M3G-Blender-Exporter) - Modern M3G (.m3g, JSR-184) exporter for Blender 3.6, implementing a byte-accurate full mobile 3D scene graph.
- [M3G2FBX](https://github.com/RaduMC/M3G2FBX) - Command-line M3G model converter, for Real Racing 3, NFS: Most Wanted, and NFS: No Limits.
- [desktop-m3g](https://github.com/vadosnaprimer/desktop-m3g) - Free C++ implementation of the M3G 1.1 (JSR-184) API for Linux and Android, with Java and Ruby bindings and a separate M3G-Reader-Writer library for reading/writing the .m3g format.
- [Juinness](https://github.com/BaalNetbek/Juinness) - Converts arbitrary 3D models into M3G models.

#### Murder Engine

*[Murder Engine](https://github.com/isadorasophia/murder), a 2D game engine/framework used by several indie titles.*

- [murder-unpack](https://github.com/yuna0x0/murder-unpack) - Reverse-engineers exported Murder Engine games back into editor-openable projects.
  - Features: C# decompilation of managed single-file bundles, sprite extraction from texture atlases, dialogue (.gum) export, localization CSV export, per-game engine-version fingerprinting, asset repacking.

#### NETLizard (J2ME Game Engine)

- [netlizard](https://github.com/glKarin/netlizard) - Parser utility and Qt4 GUI tool for NETLizard 3D J2ME game resource files (models, textures, fonts, text, sprites), reversed from decompiled Java source.
- [NETLizard_idTech4](https://github.com/glKarin/NETLizard_idTech4) - Converter from NETLizard 3D J2ME game resource files to idTech4 format.

#### Nebula Engine

*The Nebula Device/Nebula2 engine, used by Project Nomads and other early-2000s titles.*

- [nebula2-assets-extractor](https://github.com/vinceh121/nebula2-assets-extractor) - Extracts and converts asset packs for the Nebula Device 2 engine.
  - Formats: NPK0 archives, NTX1 textures, NOB0 scripts, NVX1 models, NAX0 animations (read, and read/write for most).
  - Features: NVX-to-OBJ/glTF conversion, NTX-to-image and image-to-NTX conversion, NOB script decompilation, NPK packing/unpacking.

#### MikuMikuDance

*Freeware animation program and its associated model and motion formats (.pmx, .pmd, .vmd).*

- [MikuMikuLibrary](https://github.com/blueskythlikesclouds/MikuMikuLibrary) - Library for working with MikuMikuDance formats.
- [MMD Tools](https://github.com/MMD-Blender/blender_mmd_tools) - Blender add-on for importing/exporting MikuMikuDance assets. Supports physics, bone constraints, and motion/pose data.
- [MMD Tools Append](https://github.com/MMD-Blender/blender_mmd_tools_append) - Companion extension for MMD Tools that provides material/scene controls, lighting presets, and Rigify helpers.
- [saba](https://github.com/benikabocha/saba) - C++ library and viewer for loading and playing MikuMikuDance PMD/PMX models, VMD motion, and VPD pose data, with OpenGL/DirectX 11/Vulkan example viewers.
- [MMD_modoki](https://github.com/togechiyo/MMD_modoki) - Browser-based MMD editing tool (Babylon.js/babylon-mmd) that loads PMX/PMD models plus VMD/VPD motion and pose data, and exports VMD, VPD, and image/video sequences.

#### Cal3D

*Cal3D, an open-source skeletal-based 3D character animation library used by several early-2000s indie games.*

- [Cal3d-Noesis](https://github.com/ExIfDev/Cal3d-Noesis) - Noesis addon for Cal3D models and animations.

#### Spine (2D Skeletal Animation Middleware)

- [Spine Magic Builder](https://github.com/Randombirdnoise/Spine_Magic_Builder) - Windows toolkit for reconstructing scattered or mislabeled Spine skeleton/atlas/texture assets by scanning a directory tree at the byte level and matching candidates, with a GUI picker for visual validation against SpineViewer.
- [Live2d-SpineViewer](https://github.com/promised-bytes/Live2d-SpineViewer) - Combined viewer for Live2D and Spine 2D skeletal animation assets.
  - Formats: Live2D `.moc`/`.moc3` (with `.moc.bytes` support), Spine `.skel`/`.json`/`.atlas` across versions 2.1 through 4.2, plus `.lpk`/`.wpk` archive packages.
  - Features: Texture atlas slicing and premultiplied-alpha (PMA) handling.
- [Spine-Asset-Py](https://github.com/isHarryh/Spine-Asset-Py) - Python library for parsing Spine skeletal animation asset files (`.skel`/`.atlas`).
- [Spine Skeleton Data Converter](https://github.com/wang606/SpineSkeletonDataConverter) - Command-line converter between Spine skeleton `.skel` (binary) and `.json` formats, with automatic version detection and cross-version conversion across Spine 3.5 through 4.2.
- [spine2d](https://github.com/Latias94/spine2d) - Experimental, pure Rust (unofficial) runtime for Spine 4.3, parsing skeleton/atlas data without FFI bindings to the official spine-c/spine-cpp runtimes; renderer-agnostic core with wgpu and Bevy integrations.

#### RenderWare

*Cross-platform 3D engine and middleware developed by Criterion Games. Powering the Grand Theft Auto trilogy (III, Vice City, San San Andreas), Burnout series, and many other titles.*

- [librw](https://github.com/aap/librw) - Re-implementation of the RenderWare Graphics engine.
- [DragonFF](https://github.com/Parik27/DragonFF) - Blender add-on for RenderWare `.dff` models, `.txd` textures, `.col` collisions, and `.ipl` map data.
- [DemonFF](https://github.com/spicybung/DemonFF) - Fork of DragonFF for Blender, importing and exporting RenderWare and Rockstar formats: DFF/MDL/RPF/RW4 models, textures, COL collision (including COL archives), IPL/IDE maps, IFP/ANIM animations (import only), and IMG archives (import only), plus SA-MP/open.mp and MTA workflow features.
- [Kams-Scripts-GTA-SAMP](https://github.com/spicybung/Kams-Scripts-GTA-SAMP) - 3ds Max MaxScripts for GTA RenderWare content (DFF, COL, IFP, and map I/O scripts), an updated version of Kam's scripts with SA-MP/open.mp adaptations.
- [ODFF](https://github.com/spicybung/ODFF) - DFF model conversion tool for SA-MP/open.mp: opens a DFF or folder of DFFs and embeds collision so the objects display and collide correctly in-game, loosely modeled on KDFF GUI.
- [Blender-3D-RW-Anm-plugin](https://github.com/Psycrow101/Blender-3D-RW-Anm-plugin) - Import and export RenderWare animations (.anm) into Blender 3D.
- [io_scene_gta_ifp](https://github.com/Psycrow101/io_scene_gta_ifp) - Blender add-on for importing and exporting GTA III, Vice City, and San Andreas animation (.ifp) files.
- [rwio](https://github.com/aap/rwio) - RenderWare import/export plugin for 3ds Max.
- [rwd3d9](https://github.com/aap/rwd3d9) - D3D9 extension of RenderWare for GTA III and Vice City.
- [RenderWareFile](https://github.com/igorseabra4/RenderWareFile) - Library for working with RenderWare binary files.
- [RenderWareNET](https://github.com/Venomalia/RenderWareNET) - Library to work with RenderWare 3 formats.
- [RW-Import](https://github.com/RobseK101/RW-Import) - Shared library for runtime streaming of RenderWare binary stream files (DFF models, TXD textures) found in GTA titles, aimed at (but not restricted to) importing them into the Unity game engine.
- [RWIDE2YTYP](https://github.com/Hancapo/RWIDE2YTYP) - RenderWare .IDE to Five .YTYP and NY .IDE converter.
- [rwfury](https://github.com/Hancapo/rwfury) - Python library for reading and writing RenderWare formats.
  - Games: GTA III, Vice City, San Andreas
  - Formats: DFF (3D models), TXD (textures), IMG (archives), COL (collision), IFP (animation)
- [g3DTZ](https://github.com/guard3/g3DTZ) - GAME.DTZ archive extraction utility for GTA: Liberty City Stories and Vice City Stories, supporting both the PSP and PS2 versions.
- [GTARW-BlenderMapExport](https://github.com/ajanhallinta/GTARW-BlenderMapExport) - Blender IPL/IDE map exporter for GTA San Andreas and Vice City, companion to the DragonFF add-on.
- [gtaRenderHook](https://github.com/petrgeorgievsky/gtaRenderHook) - Rendering hook/reimplementation for Grand Theft Auto: San Andreas, reading the original game's RenderWare model, texture, and world data.
- [RenderWare3Docs](https://github.com/electronicarts/RenderWare3Docs) - Official Electronic Arts release of RenderWare Graphics 3 white papers and user guides, covering the engine's file formats and APIs.
- [RWview](https://github.com/misternebula/RWview) - Console viewer for RenderWare binary stream file hierarchies.
- [install-renderware](https://github.com/Smooth-E/install-renderware) - Guide for installing the original RenderWare Graphics SDK and RenderWare Studio authoring tools.
- [rw-parser](https://github.com/Timic3/rw-parser) - TypeScript/npm library for parsing RenderWare binary streams (DFF models, TXD textures), used to render Grand Theft Auto: San Andreas models in the browser.

#### PSB (Persistent Serialized Binary)

*Serialized data/archive format used by many Japanese visual novel and mobile game engines (M2/Emote, CatSystem2, and others).*

- [psbfile](https://github.com/number201724/psbfile) - Decompiler and rebuilder for the galgame PSB file format.
- [FreeMote](https://github.com/UlyssesWu/FreeMote) - Toolset and managed library for EMT/PSB (M2 Packaged Struct Binary) files used by many Japanese visual novels and mobile games.
  - Tools: PsbDecompile/PsBuild (decompile PSB to JSON + resources and recompile), EmtConvert (convert PSB between engine/platform variants), FreeMote Viewer (renders unencrypted PSB).
  - Formats: PSB, PSZ, MDF, PIMG, SCN, MMO, EMTBYTES, MTN, DPAK.
- [emote-psb-rs](https://github.com/storycraft/emote-psb-rs) - Rust library and CLI for parsing, decoding and encoding M2 Emote PSB files.
- [FreeMote-SDK](https://github.com/Project-AZUSA/FreeMote-SDK) - SDK for "Special Emote" engines that take pure (unencrypted) PSB files as input, working around M2 Emote's per-version key isolation.

#### Aqualead

*Japanese middleware provider whose Aqualead LZSS (ALLZ) compression format appears across multiple mobile and console titles.*

- [Aqualead_LZSS](https://github.com/Brolijah/Aqualead_LZSS) - Decompresses Aqualead LZSS (ALLZ) files, a modified LZSS variant with Aqualead-specific tweaks used by several titles built on Aqualead's middleware.

#### SpeedTree

*Procedural vegetation middleware used in many AAA games.*

- [Spt2Fbx](https://github.com/VenoMKO/Spt2Fbx) - Converts SpeedTree `.spt` files (up to v4.1) to `.fbx` static meshes. Drag-and-drop tool that preserves UV sets for diffuse, leaf card dimensions, pivot data, and leaf dimming.

#### Prism3D

- [Prism3D-file-formats](https://github.com/AlexKimov/Prism3D-file-formats) - File formats and tools for games built on the Prism3D engine.
- [x64dbgPrism3DUnitResolver](https://github.com/Baldywaldy09/x64dbgPrism3DUnitResolver) - x64dbg plugin that resolves in-memory units for games built on the Prism3D engine (Euro/American Truck Simulator).
- [PrismTextureStreamer](https://github.com/Baldywaldy09/PrismTextureStreamer) - Prism3D engine plugin (Euro/American Truck Simulator) that hooks the engine's texture-queue processor and `ID3D11Device::CreateTexture2D` to redirect a truck's GPS/dashboard/custom `.tobj` screen textures to a live-captured external window.

#### Mobiclip

*Mobiclip is a video codec licensed by Actimagine and used in numerous Nintendo DS, 3DS, and Wii games.*

- [MobiclipDecoder](https://github.com/Gericom/MobiclipDecoder) - Disassembly-based, reverse-engineered decoder for the Mobiclip video codec, supporting 3DS Moflex, DS MODS, and Wii MOC5 files.

### Audio Technology
#### CRI

*CRI Middleware formats (CPK archives, ADX audio, etc.) used in many Japanese games across multiple platforms.*

- [CriPakTools](https://github.com/esperknight/CriPakTools) - Tools for extracting and repacking CRI CPK archives used in many Japanese games.
- [CriPakTools (GUI)](https://github.com/wmltogether/CriPakTools) - GUI version of CriPakTools with additional features including Shift-JIS support, 2GB+ CPK support for PS3, batch mode, compression support, and improved CPK header handling.
- [YACpkTool](https://github.com/Brolijah/YACpkTool) - Yet Another CPK Tool, for reading, extracting, packing, and patching CRIWARE CPK archives via drag-and-drop or command line.
- [Universal-CPK-Mod-Installer](https://github.com/PTKay/Universal-CPK-Mod-Installer) - Universal installer for CPK mod files.
- [CriFsV2Lib](https://github.com/Sewer56/CriFsV2Lib) - Library for working with CRI FileSystem V2 archives. See also [CriFs.V2.Hook.ReloadedII](https://github.com/Sewer56/CriFs.V2.Hook.ReloadedII), a Reloaded-II mod built on it for redirecting CRI archive reads to loose/modded files.
- [AfsLib](https://github.com/Sewer56/AfsLib) - Simple, relatively fast library for reading and writing CRIWare AFS archives.
- [AfsBatch](https://github.com/tge-was-taken/AfsBatch) - Batch AFS packer. Packs each subdirectory in a given directory into an AFS file of the same name.
- [AFSPacker](https://github.com/MaikelChan/AFSPacker) - Extracts files from AFS archives to a folder and builds new AFS archives from a folder, with workarounds for per-game quirks. Powered by AFSLib.
- [cri-archive-lib](https://github.com/rirurin/cri-archive-lib) - Rust library for reading and writing CRI CPK archives.
- [CriCodecs](https://github.com/Youjose/CriCodecs) - Python frontend for CRI codec tools.
- [SonicAudioTools](https://github.com/blueskythlikesclouds/SonicAudioTools) - Toolset for modifying CRIWARE file formats.
  - Features: ACB Editor, ACB Finder (link AWB to ACB), ACB Injector, CPK Unpacker.
  - Formats: .acb, .awb, .cpk, .adx, .adx2, .csb.
- [CriWareLibrary](https://github.com/MarshmallowAndroid/CriWareLibrary) - C# library for reading CRIWARE ACB/AWB formats, largely ported from vgmstream.
- [ACBExtractor](https://github.com/toyobayashi/ACBExtractor) - Extractor for CRI Middleware ACB files.
- [radx](https://github.com/Isaac-Lozano/radx) - ADX encoder/decoder written in Rust.
- [USM_Audio_chunks_rewriter](https://github.com/guzenco/USM_Audio_chunks_rewriter) - Java tool that rewrites the audio chunks of USM video files in a folder using the audio chunks from same-named USM files in another folder.
- [hca](https://github.com/Ishotihadus/hca) - Efficient, high-quality decoder for CRI's HCA (ADX2) audio format used by many CRIWARE-based games.
- [HCADecoder](https://github.com/Nyagamon/HCADecoder) - Original decoder for CRI's HCA (ADX2) audio format, the canonical reference implementation other HCA tools are based on.
- [GoldWave_HcaFile](https://github.com/esterTion/GoldWave_HcaFile) - HCA/ACB playback and export plugin for the GoldWave audio editor.
- [UsmToolkit](https://github.com/Rikux3/UsmToolkit) - Converts CRI USM video files into user-friendly formats, using ffmpeg and vgmstream. See also [UsmToolkitHandler](https://github.com/KojoBailey/UsmToolkitHandler), a companion tool that speeds up the conversion process.
- [WannaCRI](https://github.com/donmai-me/WannaCRI) - Python library and CLI for extracting and creating CRI USM video files (VP9/H.264, encrypted and unencrypted) with embedded HCA audio.
- [ACE](https://github.com/LazyBone152/ACE) - GUI tool (Audio Cue Editor) for editing and previewing CRIWARE ACB/AWB files.
- [CriTools](https://github.com/kohos/CriTools) - JavaScript tools for extracting audio from CRIWARE game files (ADX/HCA from CPK archives).
- [un-acb](https://github.com/starjet/un-acb) - Simple command-line program to extract HCA files from CRI ACB archives, using parts of VGMToolbox for extraction.
- [AtomicAudio](https://github.com/DarkPsydeOfTheMoon/AtomicAudio) - WIP tools and libraries (Avalonia GUI, C#/.NET library, Python CLI) for parsing, editing, and creating CRIWARE cuesheets (ACB), wavebanks (AWB), and materials (ADX).

#### Sappy (GBA Audio)

*SDK-provided formats for the Game Boy Advance sound engine. Used in [Pokémon Gen III](games-g-h.md#gen-iii) and many other GBA titles.*

- [gba-mus-ripper](https://github.com/berg8793/gba-mus-ripper) - GBA music ripper.
- [SapPy](https://github.com/mayhaps-perchance/SapPy) - Python-based GBA sound tool.
- [agbplay](https://github.com/ipatix/agbplay) - Music player and music ripper for GBA.
- [sappy](https://github.com/maddievision/sappy) - GBA sound tool.
- [Sappy (Touched)](https://github.com/Touched/Sappy) - Fork with additional features.
- [shinen-gax-python](https://github.com/beanieaxolotl/shinen-gax-python) - Python tools for Shin'en Multimedia's GAX Sound Engine used in Game Boy Advance games. Includes conversion, unpacking, waveform dumping, and song rendering tools. Also supports NAX Sound Engine format.
- [gsfopt](https://github.com/loveemu/gsfopt) - GSF (GBA Sound Format) optimizer tool. Optimizes GSF sets by removing unused code/data, converts minigsfs/gsflibs to single GSF files, and includes timing functionality for auto-tagging.
- [saptapper](https://github.com/loveemu/saptapper) - Automated GSF ripper for Game Boy Advance games using the Sappy driver. Extracts music from GBA ROMs automatically.
- [deadbeef_GSFdecoder](https://github.com/joshbarrass/deadbeef_GSFdecoder) - GSF decoder plugin for DeaDBeeF media player. Enables playback of GSF (GBA Sound Format) files in DeaDBeeF, based on viogsf/VBA-M.
- [engine-software-gba-tools](https://github.com/lunasorcery/engine-software-gba-tools) - Tools for interacting with music data in GBA games that use the Engine Software (developer) replayer.
- [gba-audio-tools](https://github.com/mudassarzahid/gba-audio-tools) - Tools for extracting and converting Game Boy Advance Sappy-driven audio.
- [gba-audio-extractor](https://github.com/DenSinH/gba-audio-extractor) - Tool for extracting audio from GBA ROMs.
- [m4a2s](https://github.com/ipatix/m4a2s) - Extracts music and sound data from GBA games using the mp2k/m4a sound driver, outputting assembly source for sequences, voicegroups, and samples while preserving pointer links via auto-generated global names.
- [wav2agb](https://github.com/ipatix/wav2agb) - Converts standard WAV files to GBA-compatible assembly (`.s`) sample data for the m4a sound engine.
  - See also [se2m4a](https://github.com/laqieer/se2m4a), a companion tool converting sound effects to m4a-compatible assembly source.
- [wav28ad](https://github.com/laqieer/wav28ad) - Converts WAV files to the `.8ad` ADPCM sample format used by GBA homebrew sound engines, per [pineight's 8ad format notes](https://pineight.com/gba/#8ad).

#### SID (Commodore 64 Sound Interface Device)

*Format and player-routine tooling for the Commodore 64's MOS 6581/8580 SID sound chip, whose custom music-player code is embedded in thousands of C64 games and demos.*

- [SIDdecompiler](https://github.com/Galfodo/SIDdecompiler) - Generates relocatable 6502 assembly source code from Commodore 64 .sid music files, recovering the original player routine and data.
- [player-id](https://github.com/WilfredC64/player-id) - Cross-platform utility to identify which Commodore 64 music player routine (driver) was used to create a given .sid file.
- [c64_6581_sid_players](https://github.com/realdmx/c64_6581_sid_players) - Collection of original and reverse-engineered SID music player routines recovered from many well-known Commodore 64 game tunes, reassembled with the ACME assembler to reproduce playable .sid files.

#### FMOD

*Audio middleware used in thousands of games for sound bank management and streaming.*

- [python-fsb5](https://github.com/HearthSim/python-fsb5) - Python library and command-line tool for extracting audio from FMOD FSB5 (FMOD Sample Bank) files. Decodes samples to WAV/OGG depending on codec.
- [Fmod5Sharp](https://github.com/SamboyCoding/Fmod5Sharp) - Managed C# library for decoding FMOD 5 sound banks (FSB5 and .bank files). Extracts individual audio samples and converts them to WAV or OGG.
  - Formats: PCM8, PCM16, PCM32, GCADPCM, IMAADPCM, VORBIS, FADPCM.
  - See also [AssetRipper's fork](https://github.com/AssetRipper/Fmod5Sharp) with additional fixes used by the AssetRipper project.
- [Fmod5Sharp (AssetRipper fork)](https://github.com/AssetRipper/Fmod5Sharp) - AssetRipper's maintained fork of SamboyCoding/Fmod5Sharp; a C# decoder for FMOD 5 FSB sound banks used internally by the AssetRipper Unity asset extraction pipeline.
- [FMODSoundBankEditor](https://github.com/TheAdmiester/FMODSoundBankEditor) - GUI editor for FSB4 version FMOD sound bank (.fsb) files. Supports viewing, replacing, and exporting audio samples. Primarily developed for Xbox 360 Forza titles.

#### Wwise

*Audio middleware by Audiokinetic used in many AAA titles for sound bank management.*

- [bnkextr](https://github.com/eXpl0it3r/bnkextr) - C++ command-line tool for extracting WEM audio files from Wwise BNK soundbank containers. Works with any game using Wwise audio middleware.
- [BnkExtractor](https://github.com/AssetRipper/BnkExtractor) - C# extraction library for Wwise audio containers. Extracts WEM audio files from BNK soundbanks and PCK file packages. Works with any game using Wwise audio middleware.
- [Unreal Engine Wwise Extractor](https://github.com/florensie/ue-wwise-extractor) - Python script to extract and convert Wwise BNK audio files from Unreal Engine pak files.
- [wwiser-utils](https://github.com/bnnm/wwiser-utils) - Companion utilities for wwiser, covering Wwise SoundBank (.bnk) and .wem audio files.
- [ExportUtilityWwise](https://github.com/djhaled/ExportUtilityWwise) - Console tool that exports Wwise audio events from Unreal Engine-based games (Valorant, Sea of Thieves, and others) to WAV files, automating sound extraction.
- [wemkit](https://github.com/coconutbird/wemkit) - Toolkit for working with Wwise WEM audio files.
- [BNK-Tools](https://github.com/JSleim/bnk-tools) - Command-line utility for Wwise `.bnk` soundbanks: lists audio IDs, extracts one or all `.wem` files, replaces single or multiple `.wem` files from a JSON map (optional big-endian), and includes an event parser mapping events and containers to audio file IDs.
### Platform SDKs & Hardware
#### XNA

*Microsoft XNA Framework model format used in various Xbox 360 and PC games.*

- [blender_xna](https://github.com/REDxEYE/blender_xna) - Blender import plugin for XNA model formats.
- [FNA](https://github.com/FNA-XNA/FNA) - Accuracy-focused reimplementation of the XNA4 framework for modern platforms, reading original .xnb content files; widely used to port XNA-based games (Terraria, Bastion, Fez, and others).
- [XNA-Noesis-Importer](https://github.com/ExIfDev/XNA-Noesis-Importer) - Noesis script to import Microsoft XNA, MonoGame, and FNA model files (.xnb).
- [xnb](https://github.com/Lekuruu/xnb) - Python library for reading XNA .xnb content files, currently deserializing Texture2D entries with the BGRA surface format.
- [py_xna_lib](https://github.com/REDxEYE/py_xna_lib) - Python library for parsing the XNA .mesh.ascii model format.
- [noe_xna](https://github.com/REDxEYE/noe_xna) - Noesis plugin for loading XNA .mesh.ascii meshes, built on py_xna_lib.
- [xnbview](https://github.com/mrkite/xnbview) - Command-line batch converter for XNA `.xnb` content files, turning Texture2D entries into PNGs, SoundEffects into WAVs, and Effect shaders into HLSL disassemblies; built to support the Terrafirma Terraria map viewer below.

#### Nintendo SDKs & Hardware

*Formats and tools generic to Nintendo consoles or SDKs.*

##### Switch

- [nxdumptool](https://github.com/DarkMatterCore/nxdumptool) - Generates XCI, NSP, HFS0, ExeFS, and RomFS dumps from Nintendo Switch gamecards and installed titles.
- [HACGUI](https://github.com/shadowninja108/HACGUI) - A comprehensive interface for extracting Nintendo Switch contents, deriving keys, and mounting filesystems (NAND, RomFS, Save).
- [nstool](https://github.com/jakcron/nstool) - General purpose tool to read and extract Nintendo Switch file formats (NSO, NRO, NCA, etc.).
- [TegraRcmSmash](https://github.com/rajkosto/TegraRcmSmash) - C++ reimplementation of fusee-launcher for Nintendo Switch RCM payloads.
- [hactool](https://github.com/SciresM/hactool) - Tool to view information about, decrypt, and extract Nintendo Switch file formats including NCA, XCI, PFS0, HFS0, RomFS, ExeFS, save data, and more.
- [XCI-Explorer](https://github.com/StudentBlake/XCI-Explorer) - Tool for viewing contents of Nintendo Switch XCI and NSP files. Features include viewing metadata, exploring partitions, checking NCA hashes, extracting NCA, and modifying certificates.
- [LegacySwitchLibraries](https://github.com/KillzXGaming/LegacySwitchLibraries) - Switch file format libraries for Switch Toolbox and other programs.
- [exefs_patches](https://github.com/misson20000/exefs_patches) - ExeFS patching tool for Nintendo Switch.
- [switch-reversing](https://github.com/SciresM/switch-reversing) - Reverse engineering resources for Nintendo Switch.
- [nxtik](https://github.com/jam1garner/nxtik) - Library and tool for parsing Nintendo Switch .tik (ticket) files.
- [NxFileViewer](https://github.com/Myster-Tee/NxFileViewer) - GUI viewer for the contents of Nintendo Switch container files.
- [nsz](https://github.com/nicoboss/nsz) - Homebrew-compatible NSP/XCI compressor and decompressor for Nintendo Switch game dumps.
- [CDNSP](https://github.com/AnalogMan151/CDNSP) - Python3 script to connect to Nintendo's CDN, print title info, download titles, and build them into installable NSP files.
- [FreeShopNX](https://github.com/AnalogMan151/FreeShopNX) - CDN title installer for the Nintendo Switch. (Archived.)
- [splitNSP](https://github.com/AnalogMan151/splitNSP) - Splits Nintendo Switch NSP files into 4GiB chunks for installation from FAT32 filesystems, a Python reimplementation of a PowerShell script found in the official Nintendo SDK.
- [switch-libpulsar](https://github.com/p-sam/switch-libpulsar) - Switch homebrew library to load, parse, and play sounds from BFSAR (binary sound archive) files and related audio file formats.
- [hac2l](https://github.com/Atmosphere-NX/hac2l) - Modern rewrite of hactool for viewing, decrypting, and extracting Nintendo Switch file formats, especially NCA (Nintendo Content Archive).
- [nut](https://github.com/blawar/nut) - Multi-purpose utility to organize, manage, and install Nintendo Switch NSP, NSZ, XCI and XCZ files, with USB/network install serving for Tinfoil.
- [goldbricks](https://github.com/blawar/goldbricks) - Homebrew Nintendo Switch client for installing NSP packages via USB, GDrive or a nut server.
- [nxo-parser](https://github.com/jam1garner/nxo-parser) - Rust parsers for Nintendo Switch executable formats (NSO/NRO).
- [SimpleModManager](https://github.com/nadrino/SimpleModManager) - Homebrew mod manager for the Nintendo Switch (Atmosphere CFW), organizing LayeredFS mod overlay folders per game title ID.
- [LibHakkun](https://github.com/fruityloops1/LibHakkun) - Modular C++ toolchain and library for building userspace Nintendo Switch mods (32/64-bit), providing symbol sourcing across firmware/game versions, memory patching/hooking (trampoline, replace, branch), and a constexpr AArch64 assembler. Used to build the Super Mario Odyssey modding example.
- [NX-Shell](https://github.com/joel16/NX-Shell) - Multi-purpose file manager homebrew for the Nintendo Switch, browsing and previewing images, audio, and archives on the filesystem.
- [Goldleaf](https://github.com/XorTroll/Goldleaf) - Multi-purpose homebrew tool for the Nintendo Switch, browsing/installing NSP and NCA titles and inspecting the filesystem.
- [hac-rs](https://github.com/DCNick3/hac-rs) - Rust library for reading some of the file formats used by the Nintendo Switch operating system.
- [shader-compiler-rs](https://github.com/DCNick3/shader-compiler-rs) - Recompiles binary Maxwell shaders (as found in Nintendo Switch executables) to GLSL.
- [nx-archive](https://github.com/RyouVC/nx-archive) - Rust library for reading and writing Nintendo Switch package archive formats.
- [sfrom-rs](https://github.com/RyouVC/sfrom-rs) - Rust library for reading and writing SFROM files, the container format used by Nintendo's official SNES emulator (as shipped on Nintendo Switch Online) to bundle ROM data with emulator compatibility/hack configuration.
- [NsoElfConverterDotNet](https://github.com/evandixon/NsoElfConverterDotNet) - .NET library to convert Nintendo Switch NSO executables to and from ELF.
- [Fuse-Nx](https://github.com/averne/Fuse-Nx) - FUSE driver (and supporting tools) for mounting various Nintendo Switch file formats as a browsable filesystem.
- [frhop](https://github.com/SmartBoy84/frhop) - Lightweight utility to serve Nintendo Switch archives over USB for installation.
- [ghidra-nn-stuff](https://github.com/averne/ghidra-nn-stuff) - Collection of Ghidra tools and data for reverse engineering Nintendo Switch sysmodule binaries.
- [NSC_BUILDER](https://github.com/julesontheroad/NSC_BUILDER) - Batch-oriented Nintendo Switch NSP/XCI tool for cleaning titlerights encryption and building multicontent NSP/XCI/NSZ/XCZ files.
- [mkbktr](https://github.com/rschlaikjer/mkbktr) - Generates BKTR update packages for Nintendo Switch titles.
- [NxNandManager](https://github.com/eliboa/NxNandManager) - Nintendo Switch NAND management tool: explore, backup, restore, mount, resize NAND images, and create emuNAND.
- [SAK (Switch Army Knife)](https://github.com/dezem/SAK) - GUI multi-tool for Nintendo Switch XCI/NSP files: split/merge, patch, update with game updates and DLC, convert between XCI/NSP/NSZ/XCZ, extract firmware, and extract savegames from a copied user partition. Archived/unmaintained.
- [MBI (Mohsaua Buoh Installer)](https://github.com/R-YaTian/MBI) - Homebrew installer for personal Nintendo Switch game dumps in NSP, NSZ, XCI, and XCZ formats, installing from SD card, USB MTP, USB storage, LAN/USB tools, or HTTP directory indexing, with NCA signature and hash verification.
- [nnheaders](https://github.com/open-ead/nnheaders) - Community-maintained collection of reverse-engineered nnsdk (Nintendo Switch SDK) headers, sourced from non-stripped binaries and debug info in Splatoon 2, Pokémon Sword/Shield, and other titles; actively maintained fork of [ultimate-research/nnheaders](https://github.com/ultimate-research/nnheaders).
- [BCAT-Manager](https://github.com/Random06457/BCAT-Manager) - GUI to manage BCAT (Background Application Communication Toolkit) save-data-delivery files used by Nintendo Switch games.

##### iQue Player

- [iQuePlayer-BootROM](https://github.com/decompals/iQuePlayer-BootROM) - Matching decompilation of the iQue Player (Chinese N64 variant) Boot ROM.
- [iQuePlayer-SecureKernel](https://github.com/decompals/iQuePlayer-SecureKernel) - Reverse engineering of the iQue Player Secure Kernel (SK).
- [iQuePlayer-SystemApp](https://github.com/decompals/iQuePlayer-SystemApp) - Reverse engineering of the iQue Player System App (SA).
- [iQueTool](https://github.com/emoose/iQueTool) - File manipulator for iQue Player (神游机) file formats.

##### NVIDIA Shield (iQiyi Nintendo Ports)

- [iQiPack](https://github.com/simontime/iQiPack) - Extracts assets from the Nintendo games ported to the NVIDIA Shield for iQiyi's Chinese streaming service. Based on an initial implementation by SciresM.

##### Wii U

- [WiiUTools](https://github.com/NWPlayer123/WiiUTools) - Collection of Python utilities for working with Wii U file formats including IPK packages, RPX executables, SARC archives, and texture editing (TexHaxU/TexHaxU2).
- [rpxlib](https://github.com/jhmaster2000/rpxlib) - General purpose library for reading and writing Wii U RPL/RPX executable files.
- [wfslib](https://github.com/koolkdev/wfslib) - WFS (WiiU File System) library and tools.
- [Cafe-Shader-Studio](https://github.com/KillzXGaming/Cafe-Shader-Studio) - Shader editor and viewer for Wii U games.
- [GTX-Extractor](https://github.com/Gota7/GTX-Extractor) - Wii U GX2 texture extraction tool. Converts GTX texture files to DDS format for use in modding and asset extraction.
- [noclip.website (Wii U Transfer Tool)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser viewer for the Wii U Transfer Tool's scenes, reading the app's NW4R/BRRES assets.
- [WiiUZip](https://github.com/jam1garner/WiiUZip) - Archive manager for Wii U filetypes.
- [wiiu-things](https://github.com/ihaveamac/wiiu-things) - Scripts and notes documenting the Wii U FST (filesystem table) format layout.
- [nuspacker](https://github.com/ihaveamac/nuspacker) - Packs files into an installable Wii U content format (NUS package).
- [nusserver](https://github.com/ihaveamac/nusserver) - Custom Nintendo Update Server (NUS) implementation, companion to nuspacker/nustool.
- [wfs-tools](https://github.com/koolkdev/wfs-tools) - Command-line tools for the Wii U WFS filesystem, built on wfslib. See also [wfs-tools-web](https://github.com/koolkdev/wfs-tools-web), a web-based version powered by WebAssembly.
- [fuse-wiiu](https://github.com/Maschell/fuse-wiiu) - FUSE filesystem for extracting data from Wii U titles in various formats.
- [wiiuqt](https://github.com/koolkdev/wiiuqt) - Qt-based Wii U NAND tools, built alongside koolkdev's wfs-tools.
- [wudump](https://github.com/FIX94/wudump) - Dumps raw images from a Wii U game disc. See also [disc2app](https://github.com/koolkdev/disc2app), a fork that extracts decrypted .app/.h3/.tmd/.cert/.tik content instead of a raw dump.
- [saviine](https://github.com/Maschell/saviine) - Dumps and injects Wii U save data, for use with the Homebrew Launcher.
- [JNUSLib](https://github.com/Maschell/JNUSLib) - Java library for handling Wii U NUS content (.app, tmd, tik, cert files) from local files, the NUS server, or .woomy/.wud/.wux/.wumad images, with decryption, extraction, and .wud-to-.wux compression.
- [TuneBloom](https://github.com/stupidestmodder/TuneBloom) - Editor for Wii U BFSAR (Binary caFe Sound ARchive) audio archive files.
- [wiiu-wudump-cemu-keygen](https://github.com/DrRetroMod/wiiu-wudump-cemu-keygen) - Generates Cemu-compatible keys.txt files from Wii U WUD dumps' game.key files, recursively scanning a WUD dump folder structure.
- [Wii_U_Bootsound_Extractor](https://github.com/DrRetroMod/Wii_U_Bootsound_Extractor) - Cross-platform Python tool for extracting Wii U title boot sounds from already-extracted Wii U game folders.

##### 3DS

###### Container & ROM Formats (CXI/CFA/CCI/CIA/NCCH/RomFS)

- [Project_CTR](https://github.com/3DSGuy/Project_CTR) - A collection of custom Nintendo 3DS tools.
  - [ctrtool](https://github.com/3DSGuy/Project_CTR/tree/master/ctrtool) - Read/extract 3DS file formats (CXI, CFA, CCI, CIA).
  - [makerom](https://github.com/3DSGuy/Project_CTR/tree/master/makerom) - Create 3DS file formats.
- [RomFS-Builder](https://github.com/SciresM/RomFS-Builder) - Program to convert a folder in Windows into a 3DS RomFS binary. For use with makerom.
- [3dstool](https://github.com/dnasdw/3dstool) - All-in-one tool for extracting and creating 3DS file formats.
  - Formats: CIA, CCI, NCCH, NCSD.
- [NDecrypt](https://github.com/SabreTools/NDecrypt) - Encryption/decryption utility for Nintendo cartridge images, supporting Nintendo DS, DSi, 3DS, and New 3DS cartridge formats.
- [3dsconv](https://github.com/ihaveamac/3dsconv) - Python script converting Nintendo 3DS CCI (.cci/.3ds) cart images to the CIA format, with support for decrypted, NCCH-encrypted, and zerokey-encrypted images.
- [pyctr](https://github.com/ihaveamac/pyctr) - Python library for reading Nintendo 3DS file formats (NCCH, ExeFS, RomFS, CIA, and more), used by several other 3DS tools.
- [Lemon](https://github.com/SceneGate/Lemon) - .NET library from the SceneGate framework for unpacking/packing Nintendo 3DS NCSD (CCI/CSU), CIA, NCCH (CXI/CFA), ExeFS, and RomFS containers, plus TMD (de)serialization.
- [3DS-rom-tools](https://github.com/ihaveamac/3DS-rom-tools) - Tools and guides for working with Nintendo 3DS game/application formats (.3ds, .cci, .app, .cxi, .cfa, .cia).
- [rofs_dumper](https://github.com/PabloMK7/rofs_dumper) - Dumps very early Nintendo 3DS ROFS containers.
- [3dsconv-c](https://github.com/soarqin/3dsconv-c) - C port of ihaveamac's 3dsconv, converting Nintendo 3DS CCI cart images to CIA format.
- [braindump](https://github.com/neobrain/braindump) - Early homebrew tool for dumping 3DS game cartridges and eShop titles. Archived, but has no already-listed direct successor for this specific niche.
- [3ds-banner-sound-extractor](https://github.com/DrRetroMod/3ds-banner-sound-extractor) - Cross-platform Python tool that extracts Nintendo 3DS banner audio from supported ROM/container files and converts it to a standard audio format.

###### Encryption, Keys, Save Data, Titles & CDN

- [otptool](https://github.com/SciresM/otptool) - Tool for Nintendo OTP (One-Time Programmable) files.
- [custom-install](https://github.com/ihaveamac/custom-install) - Installs a CIA title directly to an SD card for the Nintendo 3DS without needing to run an installer on-console.
- [rebuild-title-database](https://github.com/ihaveamac/rebuild-title-database) - Script to rebuild the contents of a Nintendo 3DS title.db Title Database, working alongside save3ds_fuse.
- [save-data-copy-tool](https://github.com/ihaveamac/save-data-copy-tool) - Copies Nintendo 3DS save data between gamecard and digital versions of the same game.
- [cmd-gen](https://github.com/ihaveamac/cmd-gen) - Experimental script to generate CMD files for Nintendo 3DS SD titles.
- [search-3ds](https://github.com/ihaveamac/search-3ds) - Searches the contents of encrypted/decrypted files used on the Nintendo 3DS system.
- [faketik](https://github.com/ihaveamac/faketik) - Generates and installs fake Nintendo 3DS ticket (.tik) files to make missing titles re-appear.
- [restore-overwritten-secureinfo](https://github.com/ihaveamac/restore-overwritten-secureinfo) - Restores a Nintendo 3DS console's SecureInfo_A/B file from inspect.log data.
- [gen-title-info-entry](https://github.com/ihaveamac/gen-title-info-entry) - Experimental script to generate the Title Info Entry structure used in a Nintendo 3DS title.db.
- [dumptik](https://github.com/ihaveamac/dumptik) - Dumps all ticket (.tik) files from a Nintendo 3DS console.
- [firmswap](https://github.com/ihaveamac/firmswap) - Python implementation of the hardmod downgrade for Nintendo 3DS, working directly with FIRM partition data.
- [save-crypto-finder](https://github.com/ihaveamac/save-crypto-finder) - Determines which titles a collection of encrypted Nintendo 3DS save files belong to, using boot9 and movable.sed.
- [save3ds](https://github.com/wwylele/save3ds) - Extract/import/FUSE tool for the Nintendo 3DS common save format (DISA/DIFF), covering save data, extdata, and the title database. Upstream of ihaveamac's save3ds fork.
- [3ds-save-tool](https://github.com/wwylele/3ds-save-tool) - Tools for parsing and extracting files from Nintendo 3DS save (DISA) and extdata (DIFF) containers.
- [3ds-snes-sc](https://github.com/foohyfooh/3ds-snes-sc) - Converts save data between the 3DS Virtual Console SNES format and the standard .SRM format used by SNES emulators.
- [HomeMenuEditor3DS](https://github.com/mrissaoussama/HomeMenuEditor3DS) - Tool for editing the Nintendo 3DS Home Menu layout database, moving/organizing/renaming titles and folders.
- [TYSS (RYaTian's Save Studio)](https://github.com/R-YaTian/TYSS) - GUI save manager for the Nintendo 3DS family, backing up and restoring cartridge/digital/DSiWare saves, ExtData, BOSS ExtData, Sys Saves, Shared ExtData, and GBA Virtual Console saves, with cloud upload/download support.
- [eshop-analysis](https://github.com/d0k3/eshop-analysis) - Python script to analyze and parse Nintendo 3DS eShop title-list data.
- [3dscrypto-tools](https://github.com/yellows8/3dscrypto-tools) - Nintendo 3DS crypto tools: decrypt NCCH, CDN titles/tickets, save images, SpotPass/BOSS containers, and New3DS FIRM ARM9 sections.
- [ctrcdnfetch](https://github.com/luigoalma/ctrcdnfetch) - Downloads title content from the Nintendo CDN for the 3DS without requiring a console, working around post-11.8 server-side checks.
- [CECTool](https://github.com/FlagBrew/CECTool) - Proof-of-concept tool for injecting data into the 3DS's CEC (StreetPass) message format.
- [MiiTube](https://github.com/RiiConnect24/MiiTube) - Kaitai Struct definition and download script for the MiiTube.dat file used via SpotPass by the 3DS game Miitopia (a package of Mii character data used for in-game roles).

###### Graphics, Models, Textures & Fonts (CTPK/BCH/CGFX/BCLIM)

- [ctpktool](https://github.com/dnasdw/ctpktool) - Tool for exporting/importing CTPK texture package files used in Nintendo 3DS games.
- [bchtool](https://github.com/dnasdw/bchtool) - Tool for exporting and importing BCH model files used in Nintendo 3DS games.
- [txobtool](https://github.com/dnasdw/txobtool) - Tool for exporting and importing CGFX graphics files used in Nintendo 3DS games.
- [3ds-bannertool](https://github.com/ihaveamac/3ds-bannertool) - Tool for creating Nintendo 3DS banners; fork of carstene1ns/3ds-bannertool adding Windows Unicode fixes and a CMake build system.
- [png2bclim](https://github.com/kwsch/png2bclim) - Converter between PNG and the Nintendo BCLIM texture format.
- [bclimtool](https://github.com/dnasdw/bclimtool) - Tool for decoding and encoding the Nintendo BCLIM texture format.
- [splashtool](https://github.com/profi200/splashtool) - Generates Nintendo 3DS splash screen files in a custom format, with support for compression and common pixel formats.
- [bclyt-stuff](https://github.com/Stary2001/bclyt-stuff) - Research and tools for the Nintendo BCLYT layout format, used across 3DS, Wii U, and Switch UI layouts.
- [bcmatools](https://github.com/LiquidFenrir/bcmatools) - Python scripts to unpack/repack Nintendo 3DS instruction manual files (.bcma) to/from an XML representation, handling the underlying DARC container and BCLYT layout data, for reinsertion into a CIA.
- [3DS-Font](https://github.com/JayFoxRox/3ds-font) - Extracts and recreates Nintendo 3DS shared BCFNT font files, for use in the Citra emulator or homebrew projects.
- [Ohana3DS-Rebirth](https://github.com/gdkchan/Ohana3DS-Rebirth) - Tool to view, extract, and replace models, textures, and animations from decrypted 3DS ROMs (BCH, CGFX).
- [BcmdlImporter](https://github.com/KillzXGaming/BcmdlImporter) - Tool to import DAE, FBX, and OBJ models into Nintendo 3DS BCMDL (CGFX-based) format without external libraries or toolkits.
- [pycgfx](https://github.com/skyfloogle/pycgfx) - Program for converting glTF models into the Nintendo 3DS's CGFX format.
- [NSMBHD Wiki (BCRES)](https://nsmbhd.net/wiki/BCRES/) - BCRES format documentation for 3DS games.
- [apk-tools](https://github.com/wrongbaud/3ds-apk-tools) - Python tools and a 010 Editor template for unpacking and repacking APK texture archive files found in various Nintendo 3DS game ROMs.
- [3DS Data Tools](https://github.com/ObsidianX/3dstools) - Suite of Python tools for extracting and packing resources found in Nintendo 3DS games.
  - Formats: MSBT (message text extraction/repacking, with color-code handling), SARC (archive extraction/creation with ZLIB compression), BFFNT (font atlas to/from PNG+JSON manifest), BFLIM (texture to/from PNG, with swizzle support).
- [tex3ds](https://github.com/devkitPro/tex3ds) - Converts images into the Nintendo 3DS homebrew `.t3x` texture format (and BCFNT fonts via the bundled mkbcfnt), with atlas, cubemap, skybox, mipmap, and compression options.
- [SPICA](https://github.com/KillzXGaming/SPICA) - H3D library/tool for serializing and deserializing Nintendo 3DS BCH model files; actively maintained continuation of gdkchan's original SPICA (stale since 2022), which underlies Ohana3DS-Rebirth above. Companion [3dsTools](https://github.com/KillzXGaming/3dsTools) provides a CLI for converting the formats SPICA supports.

###### Homebrew, CFW & Mod Tools

- [GodMode9](https://github.com/d0k3/GodMode9) - Full access file browser and manager for Nintendo 3DS handling game file formats and system files.
- [layeredFS](https://github.com/ihaveamac/layeredFS) - LayeredFS mod for OSX/Linux/UNIX, modified to work from a decompressed code.bin instead of exefs.bin.
- [videoinject](https://github.com/ihaveamac/videoinject) - Tool for injecting/creating Nintendo 3DS moflex video files.
- [Lasagna](https://github.com/BernardoGiordano/Lasagna) - LayeredFS patch manager for Luma3DS, organizing romfs/exefs mod overlay folder structures.
- [Checkpoint](https://github.com/BernardoGiordano/Checkpoint) - Fast and simple homebrew save management framework for 3DS and Switch.
- [crotools](https://github.com/shinyquagsire23/crotools) - Collection of tools for the Nintendo 3DS CRO/CRR shared-library binary format.
- [Magikoopa](https://github.com/RicBent/Magikoopa) - Compiles custom C code for Nintendo 3DS games and injects it into existing code.bin files, patching the exheader accordingly. See also [magwi](https://github.com/RicBent/magwi), a work-in-progress successor.
- [Anemone3DS](https://github.com/astronautlevel2/Anemone3DS) - Theme and splashscreen manager for the Nintendo 3DS, handling BCSTM audio and theme/splash archive formats.
- [libctru](https://github.com/devkitPro/libctru) - Reverse-engineered Nintendo 3DS system library (CTRULib) exposing OS/hardware services (filesystem, graphics, audio, networking) to homebrew, forming the base library underlying GodMode9, Checkpoint, and most other 3DS homebrew tools listed above.
- [python-exheader](https://github.com/RicBent/python-exheader) - Python library for loading, modifying, and saving Nintendo 3DS exheader (exheader.bin) files.

##### GameCube & Wii

###### Disc Images, Filesystem & Memory Card Formats

- [gc-gcm](https://github.com/jam1garner/gc-gcm) - Tool for GameCube GCM file format.
- [LibGCM](https://github.com/Sage-of-Mirrors/LibGCM) - Library for GameCube memory card formats.
- [gcmm](https://github.com/suloku/gcmm) - GameCube/Wii memory card manager, reading and writing the GCI save format and raw memory card images.
- [gci-bt](https://github.com/jam1garner/gci-bt) - GameCube GCI file tool with Bluetooth support.
- [nod](https://github.com/encounter/nod) - Rust library for reading and writing Nintendo Optical Disc images (GameCube and Wii). Includes nodtool CLI for extraction, conversion, and verification.
  - Formats: ISO (GCM), WIA/RVZ, WBFS, CISO, NFS (Wii U VC), GCZ, TGC.
- [GCReLink](https://github.com/Cuyler36/GCReLink) - Tool for unpacking and repacking GameCube and Wii relocatable modules (REL files).
- [triforce-nand-iso-extract](https://github.com/FIX94/triforce-nand-iso-extract) - Converts Triforce (Namco/Sega/Nintendo GameCube-based arcade board) NAND images to ISO files.
- [triforce-header-patcher](https://github.com/FIX94/triforce-header-patcher) - Verifies Triforce arcade disc images and patches in the correct headers.
- [pyisotools](https://github.com/JoshuaMKW/pyisotools) - Python library for working with GameCube ISOs (GCM).
- [py-nod](https://github.com/henriquegemignani/py-nod) - Python 3.8 bindings for the [nod](https://gitlab.axiodl.com/AxioDL/nod) library above, exposing the same GameCube/Wii optical disc traversal, dumping, and authoring functionality to Python code.
- [gcmod](https://github.com/Addisonbean/gcmod) - Command-line tool for extracting the contents of and rebuilding GameCube ROM/ISO images, and inspecting ROM metadata.
- [gcdiscbrowser](https://github.com/Sappharad/gcdiscbrowser) - Homebrew disc browser that runs directly on GameCube hardware, reading and navigating the original GameCube disc filesystem.

###### Executables, Code Injection & Modding

- [gc-c-kit](https://github.com/RenolY2/gc-c-kit) - Toolkit for compiling C code using devkitppc and injecting it into a GameCube Executable (DOL). Can be adapted to different GC games.
- [dolreader](https://github.com/RenolY2/dolreader) - Reader for GameCube/Wii DOL executable format.
- [ida-wii-loaders](https://github.com/heinermann/ida-wii-loaders) - IDA Pro loader plugins for the GameCube/Wii REL (relocatable module) and DOL executable file formats.
- [WiiRelocatorSP](https://github.com/sepalani/wii-relocator-sp) - Reads GameCube/Wii REL, RSO, and SEL relocatable module files and extracts their functions to binary, for disassembly with standard tools like objdump rather than an IDA-specific loader.
- [HopperPPC-Plugin](https://github.com/Sappharad/HopperPPC-Plugin) - GameCube/Wii .DOL loader and PowerPC (Gecko) disassembly plugin for the Hopper Disassembler.
- [Kamek](https://github.com/Treeki/Kamek) - Code injection engine for GameCube and Wii games, compiling and linking custom C++ code against the original DOL/REL executables.
- [GeckoLoader](https://github.com/JoshuaMKW/GeckoLoader) - Extends the available code space for Gecko codes on Wii/GameCube games, allowing thousands of lines of Gecko code per game.
- [mapdas](https://github.com/intns/mapdas) - Tools for working with Metrowerks symbol map (.map) and Gekko/Dolphin executable (.dol) files.
- [Kuribo](https://github.com/DotKuribo/Kuribo) - Embedded Wii Channel mod loader, installing mods from an SD card. Loads its own .kxe executable format (supporting GCC, Clang, and CodeWarrior) as well as legacy Kamek .kmk executables.
- [geckocode-libs](https://github.com/JoshuaMKW/geckocode-libs) - Python library for parsing and editing Gecko Codes for the Wii/GCN.
- [GekkoAssembler](https://github.com/CryZe/GekkoAssembler) - Assembles Gekko Assembly to Action Replay or Gecko Cheat Code format. Used for GameCube and Wii game modding.

###### SDK, System Libraries & Decompilations

- [WiiTools](https://github.com/Megazig/WiiTools) - Tools for Wii reverse engineering and function identification to help hacking Wii games.
- [Chihuahua](https://github.com/Sage-of-Mirrors/Chihuahua) - Tool for GameCube/Wii file formats.
- [cgrr-gamecube](https://github.com/sopoforic/cgrr-gamecube) - Tools for GameCube file formats.
- [dolsdk2001](https://github.com/doldecomp/dolsdk2001) - Decompilation of the 5-23-2001 version of the Dolphin (GameCube) SDK libraries.
- [open_rvl](https://github.com/kiwi515/open_rvl) - Decompilation of the RVL SDK (Nintendo's Wii operating system libraries), archived but a reference for the Wii's system-level formats.
- [EGG](https://github.com/vabold/EGG) - Decompilation of Nintendo's EGG library, a Wii-era in-house engine used across multiple first-party Wii games.
- [gc-ipl](https://github.com/ogamespec/gc-ipl) - Open source reimplementation of the GameCube IPL (boot ROM).
- [wii-shop-channel](https://github.com/vabold/wii-shop-channel) - Decompilation of the Wii Shop Channel, reading an existing WAD dump of the channel.
- [Kaitai-Files](https://github.com/RiiConnect24/Kaitai-Files) - Kaitai Struct definitions documenting proprietary Wii file formats, including WiiConnect24 channel data (e.g. the Forecast Channel), compilable into parsers for any Kaitai-supported language. See also [wc24-tools](https://github.com/RiiConnect24/wc24-tools) for standalone WiiConnect24 file encryption/decryption (archived).
- [tmdparse](https://github.com/InvoxiPlayGames/tmdparse) - Collection of command-line utilities (tmdparse, tikdecrypt, nus_download.sh, bindecrypt) to parse Wii TMD files and decrypt title contents.
- [WiiSigVerifySharp](https://github.com/InvoxiPlayGames/WiiSigVerifySharp) - .NET library to parse and verify signatures and certificates as used on the Wii.
- [xyzzy-mod](https://github.com/DarkMatterCore/xyzzy-mod) - Homebrew application for extracting the Wii's OTP and SEEPROM encryption keys, used as a console keys extractor. See also [InvoxiPlayGames's fork](https://github.com/InvoxiPlayGames/xyzzy-mod).
- [Wii.py](https://github.com/grp/Wii.py) - GPL-licensed Python library providing editors and classes for many Wii file types, especially the files present in banners; written as a replacement for the never-released pywii.
- [Sharpii](https://github.com/mogzol/sharpii) - Windows command-line tool built on libWiiSharp for packing/unpacking/editing WAD and U8 archives, patching IOS WADs, downloading titles from NUS, and converting between .wav/.bns and image/.tpl formats.
- [libWiiPy](https://github.com/NinjaCheetah/libWiiPy) - Python library for handling Wii file formats: TMD/Ticket/certificate-chain parsing with signature verification, WAD packing/editing with title content encryption/decryption, NUS title downloading, U8 archive (`.arc`/`.app`) packing/unpacking, ASH/LZ77 decompression, IOS patching, and NAND `content.map`/`setting.txt`/`uid.sys` editing. Companion [WiiPy](https://github.com/NinjaCheetah/WiiPy) CLI exposes all of its features; see also [rustwii](https://github.com/NinjaCheetah/rustwii), an in-progress Rust port of both.
- [ASH0-tools](https://github.com/NinjaCheetah/ASH0-tools) - Command-line compressor/decompressor for Nintendo's ASH0 format used on the Wii, including the distance-tree variant found in My Pokémon Ranch, based on Garhoogin's research into the compression algorithm.
- [dolsdk2004](https://github.com/doldecomp/dolsdk2004) - Decompilation of the 4-20-2004 version of the Dolphin (GameCube) SDK libraries.
- [wiifs](https://github.com/leoetlino/wiifs) - Wii NAND file system driver, supporting file read/write, HMAC verification/generation, and ECC data generation. See also [wiifsfuse](https://github.com/leoetlino/wiifsfuse), a FUSE client built on it.

###### Emulation, Audio, Video & Wii Channel Tools

- [libansnd](https://github.com/Oaisus/libansnd) - Audio library for Wii and GameCube homebrew with support for ADPCM audio decoding and arbitrary resampling. Supports up to 48 simultaneous voices with hardware ADPCM decoding.
- [Dolphin](https://github.com/dolphin-emu/dolphin) - GameCube and Wii emulator that parses and implements support for GameCube/Wii disc and asset file formats.
- [noclip.website (Wii Banners)](https://github.com/magcius/noclip.website/tree/main/src/Common/NW4R/lyt) - Renderer for NW4R LYT UI layouts, used to play back animated Wii channel banners from `banner.bin` archives. Parses BRLYT layouts, BRLAN animations, and NW4R bitmap fonts.
- [FunKii](https://github.com/AuroraWright/FunKii) - Command-line downloader for Wii content from the Nintendo CDN, packaging titles into installable WAD files (including DLC handling).
- [DTMText](https://github.com/heinermann/DTMText) - Converts Dolphin emulator DTM tool-assisted-speedrun movie files to and from a human-editable text format, to support diffing/version-controlling TAS inputs (GameCube, single controller only).
- [DTMEditor](https://github.com/lioncash/DTMEditor) - GUI editor for Dolphin emulator DTM tool-assisted-speedrun movie files.
- [wii-banner-sound-extractor](https://github.com/DrRetroMod/wii-banner-sound-extractor) - Python tool for extracting the Wii menu/banner sound from Wii game images, saving it as an MP3.
- [mo2mp4](https://github.com/RiiConnect24/mo2mp4) - Converts Wii Mobiclip `.mo` video files to `.mp4`, combining the Wii Mobiclip SDK with Gericom's MobiclipDecoder. See also [mobiclip-conversion-tool](https://github.com/RiiConnect24/mobiclip-conversion-tool) for the reverse (encoding) direction (binary-only release).
- [mpls_movie-decomp](https://github.com/RootCubed/mpls_movie-decomp) - Decompilation of the Wii Motion Plus Demo Video Player, the built-in Wii channel demonstrating Wii Motion Plus.
- [NUSGet](https://github.com/NinjaCheetah/NUSGet) - Modern Qt6 GUI NUS content downloader for Wii, vWii, and DSi built on libWiiPy/libTWLPy; decrypts contents and packs installable WAD/TAD archives, with vWii Common Key re-encryption support.
- [wii-menu-visual-patcher](https://github.com/NinjaCheetah/wii-menu-visual-patcher) - Shell script that unpacks the Wii System Menu's `diskBann.ash` banner, patches the Disc Channel to show its normally-hidden DVD icon, and repacks the banner and System Menu WAD with the modified files; includes a variant for Korean/Wii Mini consoles.
- [vcromclaim](https://github.com/Plombo/vcromclaim) - Extracts game ROMs, manuals and save files from an extracted Wii NAND filesystem containing Virtual Console games, automatically decompressing compressed ROMs; covers NES, SNES, TurboGrafx-16, Genesis, Master System and N64 titles.

##### Nintendo DS / DSi

- [Nitro Files](https://wiki.vg-resource.com/Nitro_Files) - Documentation for Nintendo DS file formats.
- [narchive](https://github.com/nickworonekin/narchive) - Tool for extracting and creating NARC archives used in DS games.
- [Tinke](https://github.com/pleonex/tinke) - Viewer, converter, and editor for Nintendo DS file formats (images, text, sounds, fonts, textures), extensible via .NET plugins. Deprecated by its author; see [TinkeDSi](https://github.com/R-YaTian/TinkeDSi) below for an actively maintained continuation with DSi support.
- [TinkeDSi](https://github.com/R-YaTian/TinkeDSi) - Viewer and extractor for Nintendo DS/DSi file formats.
- [NitroViewer](https://github.com/turtleisaac/NitroViewer) - In-browser (and Electron desktop) viewer and editor for Nintendo DS ROMs, a web replacement for Tinke powered by Nds4j. Browses the ROM filesystem and NARC archives; views NCGR/NCLR/NSCR/NCER/NANR 2D graphics, NSBMD/NSBTX models with NSBCA/NSBMA/NSBVA/NSBTP animations (glTF export) and SPA particles; browses SDAT and plays SSEQ/SWAV/STRM; replaces files or imports PNGs and downloads the modified .nds.
- [Hatenatools](https://github.com/pbsds/Hatenatools) - Python tools for Flipnote Studio (Nintendo DSi) file formats. Supports reading and writing .ppm (Flipnote files), .tmb (thumbnail files), .ugo (user data), and .ntft (image files). Can extract metadata, frames, and audio from Flipnote files.
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
- [nds_ida](https://github.com/R-YaTian/nds_ida) - IDA Pro 7.6+ loader and processor module for Nintendo DS ROMs, with automated segmentation, named IO registers, and address-mirroring support; complements NTRGhidra above for Ghidra users. Unmaintained.
- [NitroSharp](https://github.com/PlatinumMaster/NitroSharp) - Nintendo DS file format library.
- [nitrog3d](https://github.com/red031000/nitrog3d) - Nintendo DS 3D tools.
- [nitrogfx](https://github.com/red031000/nitrogfx) - Nintendo DS graphics tools.
- [TWLFontTools](https://github.com/chyyran/TWLFontTools) - Extracts NFTR fonts from a Nintendo DSi TWLFontTable.dat file and prepares them for reuse, with companion dumper/generator tools for the font's texture map, UV coordinates, and codepoint lookup table.
- [TWLFontTransferTool](https://github.com/R-YaTian/TWLFontTransferTool) - GodMode9 script/firm that transfers a Nintendo DSi TWLFont between console regions (iQue, Nintendo, KOR), fixing the white-screen font mismatch when booting DSiWare titles from another region.
- [Ekona](https://github.com/SceneGate/Ekona) - Nintendo DS file format library.
- [Nds4j](https://github.com/turtleisaac/Nds4j) - Java library for Nintendo DS formats.
- [REGames Editor](https://www.reddit.com/r/REGames/comments/12o004k/a_friend_and_i_made_a_full_editor_for_a_nintendo/) - Full-featured editor for Nintendo DS games.
- [NitroModel ConverterGUI](https://github.com/TheGameratorT/NitroModel_ConverterGUI) - Converts between Nintendo DS Nitro model formats (NSBMD/NSBTX from ASS/IMD).
- [NCPatcher](https://github.com/TheGameratorT/NCPatcher) - Universal Nintendo DS code maker/patcher that modifies a ROM's ARM7/ARM9 executable binaries for code injection, working on an already-extracted ROM filesystem.
- [Pacha](https://github.com/turtleisaac/Pacha) - Python region-agnostic Nintendo DS ROM patcher that creates patches replacing individual NARC files or NARC subfiles without touching the rest of the ROM; arm9/arm7/overlay patches use xdelta3 and are locked to the region of the ROM they were made from.
- [sdatxtract](https://github.com/oreo639/sdatxtract) - Command-line Nintendo DS Sound DATa (SDAT) extraction utility.
- [DSlash](https://github.com/ElementW/dslash) - Nintendo DS ROM viewing/extraction tool based on ndstrim (GitHub mirror of the original Google Code project).
- [Flipnote-Encoder](https://github.com/RinLovesYou/Flipnote-Encoder) - Cross-platform Flipnote Studio (Nintendo DSi) encoder and signer, producing valid .ppm files.
- [flipnote.js](https://github.com/jaames/flipnote.js) - JavaScript library for decoding, converting, and in-browser playback of Flipnote Studio (.ppm) and Flipnote Studio 3D (.kwz) animations.
- [flipnote-player](https://github.com/jaames/flipnote-player) - Web-based player and video converter for Flipnote Studio and Flipnote Studio 3D animations, built on flipnote.js above. See also [flipnote-video](https://github.com/jaames/flipnote-video), a command-line/Node.js counterpart for converting Flipnotes to video.
- [flipclip](https://github.com/jaames/flipclip) - Web tool converting Flipnote Studio / Flipnote Studio 3D animations to the Clipnote file format.
- [libugomemo](https://github.com/meemo/libugomemo) - C library for parsing and encoding Flipnote Studio and Flipnote Studio 3D files.
- [FSPDS](https://github.com/NotImplementedLife/FSPDS) - Homebrew Nintendo DS ROM for playing back Flipnote Studio (.ppm) files directly on DS/DSi hardware via flashcard.
- [kwz-restoration](https://github.com/Flipnote-Collective/kwz-restoration) - Restores corrupted audio in Flipnote Hatena animations converted to Flipnote Studio 3D's .kwz format.
- [playnote-studio](https://github.com/jaames/playnote-studio) - Unofficial Flipnote Studio animation player ported to the Panic Playdate handheld.
- [flipnote-studio-docs](https://github.com/Flipnote-Collective/flipnote-studio-docs) / [flipnote-studio-3d-docs](https://github.com/Flipnote-Collective/flipnote-studio-3d-docs) - Reverse-engineering documentation wikis for Flipnote Studio (DSiWare) and Flipnote Studio 3D (3DS eShop) respectively.
- [flipnote.py](https://github.com/meemo/flipnote.py) - Python library for Flipnote Studio and Flipnote Studio 3D files. See also [flippy](https://github.com/meemo/flippy), a Flipnote Studio 3D multitool by the same author.
- [flipnote-id](https://github.com/pummelator/flipnote-id) - Extracts names, Flipnote Studio IDs, and other metadata embedded in Flipnote files.
- [flipnote-audio-tool](https://github.com/jaames/flipnote-audio-tool) - Debugging tool for the audio data embedded in Flipnote Studio 3D's DSi Library notes.
- [Flipnote.NET](https://github.com/NotImplementedLife/Flipnote.NET) - Fan-made PC application for Flipnote Studio (formerly known as FlipnoteDesktop), for viewing, creating, and editing .ppm Flipnotes.
- [dsiflipencode](https://github.com/khang06/dsiflipencode) - Flipnote Studio (.ppm) encoder/decoder written in C++.
- [PPMLib](https://github.com/miso-xyz/PPMLib) - .NET library to read and write Flipnote Studio (.ppm) files. See also [RinLovesYou's cross-platform rewrite](https://github.com/RinLovesYou/PPMLib).
- [Ugomemo.NET](https://github.com/purifetchi/Ugomemo.NET) - C# library for parsing Flipnote Studio (.ppm) files, rendering frames/thumbnails via ImageSharp and exporting animations to GIF.
- [paracule](https://github.com/RinLovesYou/paracule) - Rust library for reading and writing Flipnote Studio animations: frame/thumbnail rendering, sound data parsing/resampling, and signature verification/signing.
- [nitromods](https://github.com/TheGag96/nitromods) - Project management tool for modding DS games: unpacks ROM filesystems, installs a custom overlay, compiles/assembles mod code (ASM, C, or D), and repacks everything into a new ROM. Supports Pokémon Diamond/Pearl/Platinum, HeartGold/SoulSilver, and Animal Crossing: Wild World.
- [NintendoNitro4DotNet](https://github.com/henke37/NintendoNitro4DotNet) - .NET libraries for working with file formats in Nintendo DS games.
- [dlpdump](https://github.com/Lesserkuma/dlpdump) - Nintendo DS homebrew project for preserving DS Download Play content in a verifiable way, dumping the Wi-Fi packets a DS Download Play host broadcasts.
- [DSDLP_Assembler](https://github.com/Lesserkuma/DSDLP_Assembler) - Assembles captured Wi-Fi packets, Nintendo Channel DLC files, and melonDS save states into DS Download Play binaries, complementing dlpdump above.
- [NDWCSHAP_Generator](https://github.com/Lesserkuma/NDWCSHAP_Generator) - Generates a Nintendo DS Wi-Fi Connection-style (NDWCSHAP) wireless access point that any Nintendo DS, DSi, or 3DS will auto-connect to, for local wireless testing without official infrastructure.
- [NFS (Nintendo File System Utils)](https://github.com/nfsu/NFS) - ROM hacking library and tools for reading/writing Nintendo DS file formats including NARC, NCLR, NCGR, and more.
- [editwl](https://github.com/XorTroll/editwl) - C++ libraries and desktop tool for reading, writing, and editing Nintendo DS(i) ROM formats: BMG message archives, DS(i) ROM headers/overlays/code/NitroFS filesystem, NARC/CARC archives, and DWC utility.bin archives, usable as a GUI or CLI.
- [TomoForge](https://github.com/CarlosA49/tomoforge) - Windows-first desktop toolkit for inspecting, validating, extracting, rebuilding, and patching Nintendo DS-family ROMs; works at the ROM-container level across retail games and homebrew. Reads NTR/TWL headers, verifies header/logo CRC values, exports/replaces files in the NitroFS filesystem, rebuilds standard NTR ROMs with structural verification, and applies xdelta/IPS/UPS/BPS patches with format auto-detection.
- [PlayMobic](https://github.com/pleonex/PlayMobic) - Documentation, .NET library, and command-line/GUI tools for the MODS video format used in Nintendo DS games (Mobiclip video, IMA-AD PCM and FastAudio v2 audio codecs). Converts to MP4, AVI, or raw streams.
- [NDS Banner Editor](https://github.com/TheGameratorT/NDS_Banner_Editor) - GUI editor for creating and previewing animated Nintendo DS icon/title banners, with an in-app animation player.
- [NDS BMG Editor](https://github.com/TheGameratorT/NDS_BMG_Editor) - PyQt5/ndspy GUI editor for Nintendo BMG (Binary Message) files from Nintendo DS games such as Mario Kart DS and New Super Mario Bros., with escape-sequence handling, character analysis, and text export/import.
- [NDS BNCL Editor](https://github.com/TheGameratorT/NDS_BNCL_Editor) - Windows (.NET) GUI with a 2D viewer for editing Nintendo DS BNCL files.
- [NitroWAV Tool](https://github.com/TheGameratorT/NitroWAV-Tool) - Converts PCM WAV and RAW audio to the custom NitroWAV (NWAV) streamed-audio format, with loop points and event markers.
  - Companion: [NitroWAV Player](https://github.com/TheGameratorT/NitroWAV-Player), the DS-side player for NWAV streams (New Super Mario Bros. DS, Mario Kart DS).
- [NitroPacker](https://github.com/haroohie-club/NitroPacker) - Cross-platform utility to unpack/repack Nintendo DS ROMs (filesystem, ARM9/ARM7 binaries, overlays), decompress/recompress the ARM9 binary, and apply ARM assembly hacks to the ARM9 or overlays via Ninja+LLVM or Make+devkitARM.
- [MelonRipper](https://github.com/scurest/MelonRipper) - 3D scene/model ripper capturing geometry from any Nintendo DS game running under melonDS, by the same author as apicula above.
- [palToRLCN](https://github.com/ravenDS/palToRLCN) - Converts .pal/.act/JASC-PAL palettes to Nintendo DS RLCN/NCLR format. (Archived.)
- [Aseprite-Nitro-Plugins](https://github.com/ravenDS/Aseprite-Nitro-Plugins) - Aseprite scripts for Nintendo DS Nitro-format tile/palette export.
- [PKMN-DS-Blender-ToolBox](https://github.com/PostMalloy/PKMN-DS-Blender-ToolBox) - Blender scripts for modeling Generation IV/V Pokémon DS game models.
- [libTWLPy](https://github.com/NinjaCheetah/libTWLPy) - Python library for Nintendo DSi files modeled on NinjaCheetah's libWiiPy for the Wii: TMD/Ticket/TAD parsing, TAD content extraction/decryption/re-encryption/packing, and NUS title downloading. Used by NUSGet above for DSi TAD support.

##### Nintendo 64

- [N64Recomp](https://github.com/N64Recomp/N64Recomp) - Tool to statically recompile N64 games into native executables. Converts N64 binaries into C code that can be compiled for any platform. See also [N64ModernRuntime](https://github.com/N64Recomp/N64ModernRuntime), the shared runtime library used by N64Recomp-based ports and recompilations.
- [AudiobankToC](https://github.com/sauraen/AudiobankToC) - Scripts for converting between N64 Audiobank bank files and C code. Matches on binary -> C -> binary for banks in OoT.
- [seq64](https://github.com/sauraen/seq64) - SEQ64 V2, a full-featured editor for first-party N64 music sequencing (MML format, `.com`/`.mus`/MIDI conversion). Supports Super Mario 64, Star Fox 64, Mario Kart 64, and The Legend of Zelda: Ocarina of Time.
- [ipl3checksum](https://github.com/Decompollaborate/ipl3checksum) - Python and Rust library to calculate the IPL3 (boot code) checksum for N64 ROMs, used to validate/patch ROMs in decompilation and recompilation workflows.
- [N64-IPL](https://github.com/decompals/N64-IPL) - Matching disassemblies of the N64 boot code (IPL1, IPL2, and IPL3).
- [UltraCIC](https://github.com/mikeryan/UltraCIC) - Reverse-engineered clone of the Nintendo 64 CIC lockout/authentication chip.
- [ido-static-recomp](https://github.com/decompals/ido-static-recomp) - Static recompilation of the SGI IDO 5.3/7.1 C compilers for modern platforms, letting N64 decompilation projects rebuild with the original toolchain to verify byte-matching output.
- [ultralib](https://github.com/decompals/ultralib) - Reverse engineering and matching decompilation of libultra (the N64 SDK), supporting multiple IDO/GCC compiler and library versions.
- [sdk-tools (decomp)](https://github.com/n64decomp/sdk-tools) - Decompilation of the Nintendo 64 SDK's developer tools, complementing ultralib above.
- [glankk/n64](https://github.com/glankk/n64) - Collection of N64 development tools.
  - Tools: `gfxdis` (F3DEX2 display list disassembler/decompiler), `gru` (Lua environment for manipulating raw binaries, N64 ROMs, Zelda64 file systems, UPS patches, and GameShark codes), `grc` (resource compiler for linkable N64 texture objects), `ed64rdb`/`gs` (remote debugging and GameShark upload utilities).
- [gzinject](https://github.com/krimtonz/gzinject) - WAD editing utility primarily used for patching N64 Virtual Console emulators and replacing the embedded ROM, with a documented patch file format.
- [ido-rs](https://github.com/EllipticEllipsis/ido-rs) - Rust programs for handling SGI IDO compiler data formats (st, ucode, binasm), complementing ido-static-recomp above in N64 decompilation toolchains.
- [n64soundtools](https://github.com/jsdf/n64soundtools) - Node.js reimplementation of the N64 SDK's SGI sound tools (sbc sequence bank compiler and related utilities) for building N64 homebrew audio data.
- [n64os-info](https://github.com/akopetsch/n64os-info) - Reverse-engineered and documented version history of the official Nintendo 64 OS (libultra, microcode, headers, release notes), based on SDK discs and leaks, complementing ultralib above.
- [ultra64](https://github.com/marijnvdwerf/ultra64) - Detects libultra (N64 SDK) library function signatures embedded in N64 ROM binaries.
- [n64-mr-backup-z64-python](https://github.com/gufranco/n64-mr-backup-z64-python) - Builds verified Mr. Backup Z64 Zip100 disk images from an N64 ROM collection: 8.3 naming, FAT16 layout, provably minimal disk count, and byte-reproducible output; ships no ROMs, only hashes to identify them.
- [N64SoundTools](https://github.com/derselbst/N64SoundTools) - Preservation mirror of old versions of Subdrag's original N64SoundTools, the official N64 SDK audio sequence/bank editor that n64soundtools above reimplements.

##### SNES / NES

- [SuperFamiconv](https://github.com/Optiroc/SuperFamiconv) - Command-line tool to convert graphics to Super Nintendo format.
- [M1TE2](https://github.com/nesdoug/M1TE2) - SNES Mode 1 Tile Editor for generating, editing, and arranging SNES tiles and tilemaps (2bpp/4bpp) with palette support. Designed for Mode 1 but works with any mode needing 2bpp or 4bpp graphics.
- [upernes](https://github.com/mandraga/upernes) - NES to Super NES recompiler; disassembles NES ROMs and converts 6502 code to SNES 65C816 assembly with hardware emulation.
- [nesrecomp](https://github.com/mstan/nesrecomp) - Static recompiler ecosystem for NES games (part of the R.A.I.D. community), converting 6502 ROM code into portable native code, similar in approach to upernes and GB Recompiled above.
- [jamulator](https://github.com/andrewrk/jamulator) - Early static recompiler converting NES ROMs into native executables via LLVM (unmaintained, historically notable predecessor to upernes/nesrecomp).
- [DiztinGUIsh](https://github.com/DizTools/DiztinGUIsh) - Super NES ROM disassembler with tracelog capture/analysis and a focus on collaborative workflow; exports .asm files that reassemble back into the original binary.
- [asar](https://github.com/RPGHacker/asar) - SNES assembler for applying patches to existing ROM images or building new ones from scratch; the long-standing standard assembler used across SNES ROM hacking projects.
- [nes-header-info](https://github.com/infval/nes-header-info) - Tool for parsing and displaying iNES/NES 2.0 header information from NES ROM files.
- [go-nes](https://github.com/zorchenhimer/go-nes) - Go library and CLI utilities for NES ROM and CHR data: unpacking/repacking iNES ROMs into PRG/CHR banks, converting between CHR tiles and PNG/bitmap, metatile and font conversion, and ROM usage-map visualization.
- [nesdump](https://github.com/StanHash/nesdump) - Small C++ tool that dumps info, PRG-ROM and CHR-ROM (whole or by bank, for known mappers) from iNES ROMs.
- [SatellaWave](https://github.com/LuigiBlood/sat_wave) - Satellaview (BS-X) server manager/tool exporting broadcast satellite data as BSX-*.bin files playable in bsnes-plus and snes9x, covering channels including Derby Stallion 96.
- [BSFlashManager](https://github.com/devinacker/BSFlashManager) - Tool for managing BS-X / Satellaview memory pack flash cartridges for the SNES, reading and writing the Satellaview's flash memory format.
- [bsnes-plus](https://github.com/devinacker/bsnes-plus) - Debug-oriented fork of bsnes with a tracer, memory/VRAM viewers, and breakpoints, widely used for SNES ROM hacking and reverse engineering.
- [snes-tile-tool](https://github.com/fo-fo/snes-tile-tool) - SNES tile graphics conversion tool.
- [nintendulatordx](https://github.com/fo-fo/nintendulatordx) - Modified version of the Nintendulator NES emulator adding source-level debugging capabilities for NES ROM reverse engineering.
- [Dispel](https://github.com/pelrun/Dispel) - Disassembler for 65816/SNES ROM images.
- [snes-assembly-book](https://github.com/Ersanio/snes-assembly-book) - 65c816 assembly guide covering opcodes and the inner workings of the SNES, aimed at ROM hacking and reverse engineering.
- [NES-Sprite-Editor](https://github.com/eonarheim/NES-Sprite-Editor) - Simple sprite editor for NES games.
- [NesBlockFinder](https://github.com/spiiin/NesBlockFinder) - Locates tile/block and screen-layout data within NES ROMs by matching an FCEUX PPU memory dump against the ROM's CHR/pattern data, to find offsets for graphics extraction/editing. Includes NesScreenFinder for locating screen-composition data built from those blocks.
- [snes-sdd1-python](https://github.com/gufranco/snes-sdd1-python) - Python reimplementation of the SNES S-DD1 compression coprocessor (used by Star Ocean and Street Fighter Alpha 2), checked against the snes9x reference decoder across 4,000 golden test vectors.
  - Same author also publishes patchers that rebuild [Street Fighter Alpha 2/Zero 2](https://github.com/gufranco/snes-street-fighter-alpha-2-nochip) and [two Star Ocean rebuilds](https://github.com/gufranco/snes-star-ocean-nochip-fix) as plain ROMs with the S-DD1 requirement designed out of the header, built from your own cartridge dump.
- [snes-driver-python](https://github.com/gufranco/snes-driver-python) - Recovers the command protocol a SNES cartridge uses to talk to its coprocessor, read directly out of the cartridge's own driver code; checked against 42 real cartridges.
- [snes-st-python](https://github.com/gufranco/snes-st-python) - Emulator for the Seta ST010/ST011 navigation coprocessors used in SNES racing cartridges, settled against their own reference implementation.
- [snes-rtc-python](https://github.com/gufranco/snes-rtc-python) - Emulator for the two real-time-clock coprocessors used in SNES cartridges (S-RTC), held to the chips' own reference implementations.
- [snes-obc1-python](https://github.com/gufranco/snes-obc1-python) - Emulator for the OBC1 sprite-remapper coprocessor carried by one SNES cartridge, validated byte-for-byte against its own reference across every addressing state.
- [snes-dsp-python](https://github.com/gufranco/snes-dsp-python) - Emulator for the SNES DSP-1/2/3/4 coprocessor family (built on the [nec-upd7725-96050-python](https://github.com/gufranco/nec-upd7725-96050-python) core), running the microcode dump you supply rather than a from-scratch reimplementation of it.
- [sony-s-dsp-python](https://github.com/gufranco/sony-s-dsp-python) - Sony S-DSP audio-unit model for the SNES sound engine, cross-checked sample-for-sample against register configurations taken from real SPC music dumps.
- [sony-spc700-python](https://github.com/gufranco/sony-spc700-python) - Cycle-accurate SPC700 CPU interpreter for the SNES's audio processor (all 256 opcodes), validated against the SingleStepTests conformance corpus.
- [snes-spc7110-python](https://github.com/gufranco/snes-spc7110-python) - Python reimplementation of the SNES SPC7110 decompression coprocessor (all three of its modes), checked against the chip's own reference implementation over 102,400 bytes of generated streams.
- [snes-graphics-python](https://github.com/gufranco/snes-graphics-python) - Encoder/decoder for the Super Nintendo's tile, tilemap, and palette graphics formats, validated bit-exact against the hardware's own behavior.
- [snes-mapper-python](https://github.com/gufranco/snes-mapper-python) - SNES cartridge memory map and DMA engine in Python, resolving every header-declared layout to its address-space mapping; checked against 5,145 real cartridges.
- [snes-rom-image-python](https://github.com/gufranco/snes-rom-image-python) - Python library treating a SNES cartridge dump as a file rather than an address space: strips copier stubs, joins split ROM sets, identifies a dump by digest, and rewrites the header to drop a declared coprocessor with the checksum recomputed across every mirror; validated against 7,317 real cartridges.
- [noiSNESs_Brr_Finder](https://github.com/noisecross/noiSNESs_Brr_Finder) - Statistically analyzes SPC dumps and SNES ROM images to rip embedded BRR (Bit Rate Reduction) sound sample data, exporting to WAV or raw BRR; builds on techniques from SNESSOR and BRRTools while filtering out false-positive matches.
- [snesify](https://github.com/furrykef/snesify) - Converts images into SNES-native tile graphics formats (2bpp/4bpp/8bpp), including a custom "scan16" 16-colors-per-scanline format that transfers to VRAM in half the time and space of 8bpp while looking better than 4bpp; used to make the large animations in the SNES port of Five Nights at Freddy's possible.
- [retrotool (SFCRetroTools)](https://github.com/danielburgess/SFCRetroTools) - SNES/SFC ROM hacking and development toolkit consolidating tooling scattered across multiple ROM-hacking projects into a single Python library.
- [noiSNESs_Sound_Editor](https://github.com/noisecross/noiSNESs_Sound_Editor) - Statistically searches for embedded sounds in BRR format within files, facilitating extraction and replacement; companion tool to noiSNESs_Brr_Finder above.
- [nes-util](https://codeberg.org/qalle/nes-util) - Collection of NES ROM hacking utilities: iNES header combine/info/split, CHR tile encode/decode, color-swapping, CPU/PRG address conversion, and Game Genie code encode/decode/conversion tools. Moved from GitHub to Codeberg; no longer updated at its former location.
- [nes-cdl-summary](https://codeberg.org/qalle/nes-cdl-summary) - Prints an FCEUX Code/Data Logger (.cdl) file in human-readable format, with a companion script to render CDL coverage as a PNG image. Moved from GitHub to Codeberg; no longer updated at its former location.
- [ggencoder-qt](https://github.com/jdratlif/ggencoder-qt) - Qt/C++ Game Genie cheat code encoder/decoder, supporting NES, SNES, Genesis, and Game Boy/Game Gear code formats.
- [SnesGFX](https://github.com/VitorVilela7/SnesGFX) - General-purpose SNES graphics format converter (C#/WinForms, codec-based).

##### Game Boy / GBA

###### ROM Tools, Disassemblers & Format Libraries

- [cgrr-gameboy](https://github.com/sopoforic/cgrr-gameboy) - Tools for Game Boy file formats.
- [HexManiacAdvance](https://github.com/haven1433/HexManiacAdvance) - Hex editor for Game Boy Advance ROMs with scripting support.
- [UnkrawerterGBA](https://github.com/MCJack123/UnkrawerterGBA) - Game Boy Advance ROM extractor and converter for games using the Krawall sound engine. Exports audio as XM or S3M module files. Supports automatic detection of instrument/sample lists and modules, direct rip mode for lossless extraction, and can be used as a library.
  - See also [krawall](https://github.com/sebknzl/krawall), the original XM/S3M player engine source used by these games.
- [GB Recompiled](https://github.com/arcanite24/gb-recompiled) - Static recompiler for Game Boy and Game Boy Color ROMs that translates LR35902 assembly directly to portable C code.
- [Tilemap-Creator](https://github.com/erandis-vol/Tilemap-Creator) - Tileset and tilemap editor for the Game Boy Advance.
- [gba_explorer](https://github.com/attilathedud/gba_explorer) - Explorer for Game Boy Advance ROMs, browsing and extracting embedded text, graphics, and sound data.
- [gba-lz77](https://github.com/lunasorcery/gba-lz77) - LZ77 compressor/decompressor producing byte-identical output to the GBA's LZ77 implementation, verified against LEGO Island 2 (GBA).
- [GBAC](https://github.com/RayCarrot/GBAC) - GBA compressed data finder; searches a ROM for compressed data and visualizes it as palettes, tiles, or maps, and can replace it by importing new compressed data.
- [gba_dumper](https://github.com/attilathedud/gba_dumper) - Set of utilities for text modifications in GBA ROMs. Since GBA games use homebrew text encodings rather than ASCII, streamlines building a translation table from search matches, dumping translated ROM text, and re-injecting edited strings.
- [mgbdis](https://github.com/mattcurrie/mgbdis) - Game Boy ROM disassembler with RGBDS-compatible output.
- [windfish](https://github.com/jverkoey/windfish) - Tracing disassembler and UI for Game Boy ROMs, integrated with SameBoy for emulation and debugging.
- [bub](https://github.com/StanHash/bub) - Game Boy ROM disassembler written in Rust, with bank-aware addressing, optional tags file input, and options for large ROMs, CGB RAM and SRAM bank count.
- [GameboyDisassembler](https://github.com/RetroReversing/GameboyDisassembler) - Disassembler that converts assembled Game Boy ROM code back into Z80-style assembly.
- [gbadisasm](https://github.com/camthesaxman/gbadisasm) - Game Boy Advance ROM disassembler.
- [luvdis](https://github.com/aarant/luvdis) - Pure-Python Game Boy Advance disassembler.
- [GhidraGBA](https://github.com/SiD3W4y/GhidraGBA) - Game Boy Advance ROM loader for Ghidra.
- [gba-ghidra-loader](https://github.com/pudii/gba-ghidra-loader) - Game Boy Advance ROM loader for Ghidra, targeting modern Ghidra versions.
- [gvasm](https://github.com/velipso/gvasm) - Assembler and disassembler designed specifically for Game Boy Advance homebrew.
- [gba-tileeditor](https://github.com/IanFinlayson/gba-tileeditor) - Simple tile editor for the Game Boy Advance.
- [gfx2agb](https://github.com/felixjones/gfx2agb) - Graphics converter for the Game Boy Advance, converting images to Mode 3/4/5 bitmap and palette data with configurable gamma, dithering, and output stride direction.
- [gameboy-rom-parser](https://github.com/MarkMcCaskey/gameboy-rom-parser) - Rust parser for (Super) Game Boy (Color) ROM headers.
- [gba_lib_func_sig](https://github.com/laqieer/gba_lib_func_sig) - Game Boy Advance library function signature database for reverse engineering, used to identify known compiler/SDK library functions embedded in GBA ROMs.
- [gba-disasm-decomp-tools](https://github.com/laqieer/gba-disasm-decomp-tools) - Bootstraps a disassembly or decompilation project for a Game Boy Advance game, scaffolding the toolchain and directory structure.
- [ida_gba_stuff](https://github.com/laqieer/ida_gba_stuff) - IDA Pro scripts and loaders useful when reverse engineering GBA games.
- [gba_opening_movie](https://github.com/laqieer/gba_opening_movie) - Guide and reference implementation for inserting a custom AVI-converted opening movie into a Fire Emblem GBA ROM.
- [bnGB](https://github.com/icecr4ck/bnGB) - Binary Ninja loader and architecture plugin for Game Boy ROMs, enabling GB/GBC disassembly and analysis directly within Binary Ninja.
- [Un-GameBoy](https://github.com/xvillaneau/python-ungameboy) - Interactive terminal-based tool for reverse-engineering Game Boy and Game Boy Color ROMs, with disassembly, labeling, and navigation features.
- [GBRE](https://github.com/native-gb/gbre) - Research and interoperability toolkit for analyzing user-supplied Game Boy ROMs and building native reimplementations, providing ROM-range data modeling, source-map generation, HTML coverage maps, and emulator-trace/evidence tooling.
- [gba-reversing-notes](https://github.com/Dhole/gba-reversing-notes) - Notes on reverse engineering GBA ROMs.
- [GBA-IDA-Pseudo-Terminal](https://github.com/LanHikari22/GBA-IDA-Pseudo-Terminal) - IDAPython tools aiding analysis, disassembly, and data extraction, tailored for the GBA architecture.
- [gba-recomp](https://github.com/JRickey/gba-recomp) - Static recompilation tool and runtime for Game Boy Advance ROMs.
- [gba-mapper](https://github.com/JRickey/gba-mapper) - LLM-driven automated disassembly and mapping toolkit for GBA ROM images.
- [SLaDe-AGBCC](https://github.com/JRickey/SLaDe-AGBCC) - Neural GBA decompiler experiment targeting AGBCC-compiled code.
- [super-game-boy-border-converter](https://github.com/marcrobledo/super-game-boy-border-converter) - Converts a 256x224 PNG image into Super Game Boy border SNES tile data.
- [super-game-boy-border-injector](https://github.com/marcrobledo/super-game-boy-border-injector) - Injects a custom Super Game Boy border into (almost) any Game Boy ROM, complementing the border-converter above.
- [ezgba](https://github.com/langest/ezgba) - Applies SRAM, IPS, and EZ4 patches to Game Boy Advance ROMs.
- [ungoomba](https://github.com/R-YaTian/ungoomba) - Unpacks the Game Boy ROM bundled inside a Goomba Front multi-game menu image for GBA flash carts, scanning for the emulator's embedded-ROM header. See also [unpnesmmw](https://github.com/R-YaTian/unpnesmmw), which does the same for NES ROMs bundled by PocketNES Menu Maker.
- [BadBoy](https://github.com/daid/BadBoy) - Game Boy ROM disassembler and emulator with a companion tool suite: BPS/IPS patcher, ROM-to-PNG tile dumper, and ROM diffing/text search.

###### Hardware & Die-Level Reverse Engineering

- [metroboy](https://github.com/aappleby/metroboy) - Repository of gate-level simulators and reverse-engineering tools for the original Game Boy hardware.
- [gbrom-tutorial](https://github.com/travisgoodspeed/gbrom-tutorial) - Tutorial for extracting the Game Boy boot ROM from die photographs.
- [maskromtool](https://github.com/travisgoodspeed/maskromtool) - CAD tool for extracting bits from mask ROM die photographs, used to recover boot ROM and other on-die data.
- [ninmonitorroms](https://github.com/0xabad1dea/ninmonitorroms) - Recovered Game Boy debug monitor ROMs, partial ROM images pulled from an official Nintendo Game Boy emulator.
- [dmg-schematics](https://github.com/msinger/dmg-schematics) - Reverse engineered schematics of the Game Boy's DMG-CPU B chip, including the SM83 CPU core. Successor to the archived DMG-CPU-Inside project.
- [gb-schematics](https://github.com/Gekkio/gb-schematics) - Reverse engineered Game Boy-related hardware schematics.
- [nds-slot2](https://github.com/IvanVeloz/nds-slot2) - Nintendo DS slot-2 (GBA slot) reverse engineering documentation.
- [gba-cartridge](https://github.com/jojolebarjos/gba-cartridge) - Experiments documenting how Game Boy Advance cartridges work.
- [gba-cartridge (repro RE)](https://github.com/tolik518/gba-cartridge) - Reverse engineering attempt of a Chinese repro Game Boy Advance cartridge.
- [gameboy-audio-dumper](https://github.com/FIX94/gameboy-audio-dumper) - Dumps Game Boy ROMs and save files over an analog audio connection.
- [FlashGBX](https://github.com/Lesserkuma/FlashGBX) - Cross-platform (Windows/Linux/macOS) tool to read and write Game Boy and Game Boy Advance cartridge ROM and save data, including RTC registers, via GBxCart RW, GBFlash, Joey Jr, and Game Bub hardware.
  - Features: Wide support for cartridge memory mappers and reproduction/flash cartridges, flash chip identification, decoding and extraction of Game Boy Camera photos from save data, and ROM dump report generation for game preservation.
- [ems-qart](https://github.com/rbino/ems-qart) - Cross-platform Qt application to read and write ROM and SRAM save data on EMS 64M USB Game Boy flash cartridges. See also [ems-flasher](https://github.com/mikeryan/ems-flasher), the original command-line flasher for the same hardware.
- [GBA_MultiMenu](https://github.com/Lesserkuma/GBA_MultiMenu) - Menu program and ROM-compilation builder for Game Boy Advance bootleg cartridges equipped with a multi-game mapper, supporting several common mapper chips and per-game save slot configuration. Compatible with cartridges dumped/flashed via FlashGBX above.
- [gba-auto-batteryless-patcher](https://github.com/metroid-maniac/gba-auto-batteryless-patcher) - Patches a GBA ROM for batteryless saving on bootleg cartridges containing SRAM but no battery, flushing save data a few seconds after an in-game save or on a button-trigger.
- [libsavgba](https://github.com/laqieer/libsavgba) - Library to access various backup media (SRAM, flash, EEPROM) in GBA cartridges. Successor to the archived [libgbabackup](https://github.com/laqieer/libgbabackup).
- [ags_aging (decomp)](https://github.com/Normmatt/ags_aging) - Decompilation of the AGS Aging Cartridge 7.0, a Nintendo diagnostic/burn-in test cartridge for Game Boy Advance hardware.
  - See also [AGSTests](https://github.com/DenSinH/AGSTests), a (semi-)decompilation consolidating the AGS test programs in one central place.
- [GB-SMART-multiboot-rom-manager](https://github.com/Raphael-Boichot/GB-SMART-multiboot-rom-manager) - GNU Octave/MATLAB tool that builds multiboot ROM images for EMS GB SMART 16M/32M flash cartridges, handling the proprietary mapper's ROM offset-alignment and boot-logo-scan format.
- [gb-save-manager](https://github.com/Gronis/gb-save-manager) - Backs up and restores Game Boy cartridge SAVE (SRAM) files over a Link Cable, no special flash hardware needed.
- [gb-save-states](https://github.com/mattcurrie/gb-save-states) - bsdiff patches adding save-state support to Game Boy/GBC games on original hardware via flash-cart SRAM.

###### Game Boy Camera & Printer

- [gbcam-rev-engineer](https://github.com/AntonioND/gbcam-rev-engineer) - Tools used to reverse engineer the Game Boy Camera's sensor and communication protocol using an Arduino UNO.
- [gbp-decode](https://github.com/HerrZatacke/gbp-decode) - Set of functions to decode Game Boy Printer print job data.
- [gbcamextract](https://github.com/jkbenaim/gbcamextract) - Extracts photos from Game Boy Camera / Pocket Camera save files, including the Hello Kitty camera variant.
- [gb-photo](https://github.com/untoxa/gb-photo) - Toolkit and library for reading, writing, and converting Game Boy Camera save data, including frame/border resources. Credits [cristofercruz](https://github.com/cristofercruz) as a contributor.
  - See also [Inject-pictures-in-your-Game-Boy-Camera-saves](https://github.com/Raphael-Boichot/Inject-pictures-in-your-Game-Boy-Camera-saves), a MATLAB/Python tool converting arbitrary images into the Game Boy Camera's native save format for injection via flash cart or emulator.
  - See also [gb-camera-frames](https://github.com/cristofercruz/gb-camera-frames), a community-sourced collection of decoded Game Boy Camera decoration frame data extracted from various cartridge ROM dumps.
- [game-boy-camera-manager](https://github.com/marcrobledo/game-boy-camera-manager) - Tool for managing Game Boy Camera data, including both save (SRAM) photos and ROM contents.
- [arduino-gameboy-printer-emulator](https://github.com/mofosyne/arduino-gameboy-printer-emulator) - Arduino-based Game Boy Printer emulator that captures the raw serial protocol between a Game Boy/GBC/GBA and the printer, decoding print jobs into images. See also [GameboyPrinterSniffer](https://github.com/mofosyne/GameboyPrinterSniffer), a standalone packet sniffer for the same protocol.
- [NeoGB-Printer](https://github.com/zenaror/NeoGB-Printer) - Open-source, standalone ESP32-based Game Boy Printer emulator 100% compatible with all 110 officially released compatible games, saving printed images as BMP. Co-developed with the author of arduino-gameboy-printer-emulator above.
- [The TinyGB Printer](https://github.com/Raphael-Boichot/The-TinyGB-Printer) - Raspberry Pi Pico-based Game Boy Printer emulator storing decoded print jobs directly as PNG images on an SD card, battery powered for portability.
  - Built on mofosyne's arduino-gameboy-printer-emulator protocol parser above; described by its author as a Pico "demake" of NeoGB-Printer above.
  - See also the same author's earlier [GameboyPrinterPaperSimulation](https://github.com/Raphael-Boichot/GameboyPrinterPaperSimulation) (simulates physical/e-paper printout look from the decoded data) and [PC-to-Game-Boy-Printer-interface](https://github.com/Raphael-Boichot/PC-to-Game-Boy-Printer-interface) (bridges a PC to a real Game Boy Printer, encoding images into Game Boy tile format), both since folded into this project.
- [wifi-gbp-emulator](https://github.com/HerrZatacke/wifi-gbp-emulator) - ESP8266-based Game Boy Printer emulator that exposes received print job data over a WiFi connection instead of local storage.
- [gb-link-printer](https://github.com/stacksmashing/gb-link-printer) - Firmware turning a GB-Link-Adapter into a Game Boy Printer emulator, allowing photos to be downloaded straight from the browser.
- [gbpxl](https://github.com/xx0x/gbpxl) - Game Boy Printer XL: transparent interface bridging the Game Boy Camera/Printer protocol to ESC/POS-compatible thermal receipt printers. See also [cristofercruz's fork](https://github.com/cristofercruz/gbpxl) with multi-tone printing support.
- [gameboycameralib](https://github.com/KodeMunkie/gameboycameralib) - Java library encoding, decoding, injecting, and extracting Game Boy Camera 2BPP images as PNGs or BufferedImages to/from Game Boy Camera save files.
- [GameBEye](https://github.com/mtouzot/GameBEye) - Python library for processing Game Boy Camera images.
- [gbpinter_dump2image_py](https://github.com/lennartba/gbpinter_dump2image_py) - Python script batch-converting raw Game Boy Camera image dumps into PNG files.
- [gb-printer-web](https://github.com/HerrZatacke/gb-printer-web) - Web app for organizing, editing, and sharing Game Boy Camera photos.
- [GBCamera-Android-Manager](https://github.com/Mraulio/GBCamera-Android-Manager) - Android app to manage a Game Boy Camera photo gallery, communicating over USB serial with an Arduino Printer Emulator or GBxCart RW to pull images.
- [gbcam2png](https://github.com/raphnet/gbcam2png) - Command-line tool converting Game Boy Camera save RAM photo dumps to PNG.
- [game-boy-camera-format-converter](https://github.com/thriftymeerkat/game-boy-camera-format-converter) - Converts Game Boy Camera BMP dumps, as produced by the BennVenn Joey Jr cart dumper, into upscaled, social-media-friendly PNGs.
- [gbcam-hdr-utils](https://github.com/seb-tourneux/gbcam-hdr-utils) - GUI/CLI utilities converting Game Boy Camera `.sav` dumps (single-photo, full-RAM, or multi-RAM/PHOTO! concatenated) to PNG and assembling HDR image stacks from AEB (auto-exposure-bracket) photo sequences.
- [dmg-darkroom](https://github.com/clickysteve/dmg-darkroom) - Browser-based tool that loads `.sav`/`.srm` Game Boy Camera dumps, browses photos, and applies 100+ palettes (with `.pal`/`.gbp` import/export) and effects before exporting images.
- [game-boy-camera-picture-extractor](https://github.com/tjcouch1/game-boy-camera-picture-extractor) - TypeScript/PWA that recovers a clean 128x112 4-color Game Boy Camera image from a photograph of the camera's LCD screen (or video capture), correcting for perspective and lighting.
- [dither-pattern-gen](https://github.com/HerrZatacke/dither-pattern-gen) - Documents and reproduces the Game Boy Camera's original dithering patterns (4 groups of 16 patterns) used to convert analog sensor data to the console's native 2bpp greyscale format; also generates alternative patterns.
- [Game-Boy-Camera-Faker](https://github.com/Raphael-Boichot/Game-Boy-Camera-Faker) - GNU Octave tool that converts arbitrary photos into synthetic Game Boy Camera images by modeling the Mitsubishi M64282FP sensor's artifacts and dithering algorithm.
- [direct-serial-to-gif-converter](https://github.com/HerrZatacke/direct-serial-to-gif-converter) - Converts a raw Game Boy Printer serial capture directly to an animated GIF.
- [GBP-Downloader](https://github.com/HexLions/GBP-Downloader) - Browser-based Game Boy Printer receiver using the Web Serial API, no install required.
- [Game-Boy-Camera-Fast-Wifi-Adapter](https://github.com/NatGrayYes/Game-Boy-Camera-Fast-Wifi-Adapter) - Wifi/USB-serial hardware adapter that extracts Game Boy Camera photos to a phone or PC in under 2 minutes.
- [pico-gb-printer](https://github.com/untoxa/pico-gb-printer) - Raspberry Pi Pico-based Game Boy Printer emulator exposing a web interface to browse and download received print-job photos.
- [A-Game-Boy-Printer-emulator-in-1998](https://github.com/Raphael-Boichot/A-Game-Boy-Printer-emulator-in-1998) - Preserved 1998 DOS/LPT-port Game Boy Printer emulator source, the earliest known one, decoding the same print-job protocol as later tools.

###### Mobile Adapter GB

- [libmobile](https://github.com/REONTeam/libmobile) - Reimplementation of the Mobile Adapter GB protocol used by Pokémon Crystal, Mario Golf, Mario Tennis, and other Game Boy/GBC games for early-2000s online connectivity, enabling connections to custom replacement game servers. See also [ArduinoAdapterGB](https://github.com/REONTeam/ArduinoAdapterGB) for a real-hardware emulation of the same physical adapter.
- [reon](https://github.com/REONTeam/reon) - Service replacement for the Mobile Adapter GB, targeting all officially released games as well as homebrew; includes a mail server, web-facing per-game scripts, and non-web applications such as a Pokémon Crystal Trade Corner program.
- [libmobile-bgb](https://github.com/REONTeam/libmobile-bgb) - Mobile Adapter GB emulator plugin for the BGB Game Boy emulator, built on libmobile above.
- [libmobile-atmega](https://github.com/REONTeam/libmobile-atmega) - libmobile implementation for Atmega-based devices (e.g. the Arduino UNO's atmega328p), for real-hardware Mobile Adapter GB emulation.
- [PCBridge](https://github.com/REONTeam/PCBridge) - Interprets Arduino Adapter GB commands over a serial connection and relays them to a remote server; companion to ArduinoAdapterGB above.
- [mobile-relay](https://github.com/REONTeam/mobile-relay) - Relay server for Mobile Adapter GB direct call (game-to-game) connections.
- [trade-corner](https://github.com/REONTeam/trade-corner) - Script facilitating Pokémon Crystal's online Trade Corner over the Mobile Adapter GB service.

##### Cross-Platform Formats & Archives

###### Archive & Container Formats

- [Nintendo-File-Formats](https://github.com/kinnay/Nintendo-File-Formats) - Documentation for Wii U and Switch file formats.
- [sarc](https://github.com/jam1garner/sarc) - Rust library for reading and writing Nintendo SARC and SZS (yaz0 compressed SARC) archive formats.
- [sarc-extract](https://github.com/RenolY2/sarc-extract) - Extractor for SARC archive format.
- [GARC-Unpack](https://github.com/vgmoose/GARC-Unpack) - Unpacker for Nintendo GARC archive format.
- [lzarc](https://github.com/jam1garner/lzarc) - Rust library and CLI for working with LZARC compressed archives used in Paper Mario Color Splash.
- [Lzarc-Tool](https://github.com/Fuzzy2319/Lzarc-Tool) - Tool for LZARC compressed archive format.
- [darctool](https://github.com/dnasdw/darctool) - Tool for extracting and creating DARC archive files used in Nintendo games.
- [ninfs](https://github.com/ihaveamac/ninfs) - FUSE filesystem tool to mount Nintendo 3DS and Switch container/filesystem formats (CCI, CDN, CIA, NAND, NCA, RomFS, SD, etc.) for direct file browsing.
- [sarctool](https://github.com/jam1garner/sarctool) - Command-line tool for working with Nintendo SARC archive files.
- [rust_lzss](https://github.com/silentdragonz/rust_lzss) - Rust library implementing Nintendo's LZSS decompression, used across many Nintendo game formats.
- [3DSkit](https://github.com/Tyulis/3DSkit) - Tool to extract and repack many file formats found on Nintendo DS, DSi, 3DS, Wii U, and Switch.
- [Jungle](https://github.com/kinnay/Jungle) - Accurate parser/encoder for various Nintendo file formats.
- [zbic](https://github.com/kinnay/zbic) - Python package implementing the ZBIC compression algorithm used on Nintendo Switch.
- [Nintendo-File-Samples](https://github.com/kinnay/Nintendo-File-Samples) - Test set of Nintendo file format samples covering various edge cases, for validating tools against.
- [oead](https://github.com/zeldamods/oead) - Library for recent Nintendo EAD first-party formats (BOTW/TOTK-era SARC, Yaz0, AAMP, BYML, and more), with Rust core and Python bindings. See also [cs-oead](https://github.com/EPD-Libraries/cs-oead) for a C# wrapper.
- [byml-v2](https://github.com/zeldamods/byml-v2) - Python BYML/BYAML parser, writer, and BYML-to-YAML converter supporting v2, v3, and v4 files (Breath of the Wild and Super Mario Odyssey, including 64-bit node types and both endiannesses).
  - Sibling Python libraries: [aamp](https://github.com/zeldamods/aamp) (AAMP parameter archive reader/converter, targeting Breath of the Wild), [sarc](https://github.com/zeldamods/sarc) (SARC archive reader/writer and CLI), [evfl](https://github.com/zeldamods/evfl) (EventFlow .bfevfl flowchart and .bfevtm timeline parser/writer, able to rewrite every event flow in Breath of the Wild), [tmpk](https://github.com/zeldamods/tmpk) (library and CLI for Nintendo's TMPK archive format).
- [SarcLibrary](https://github.com/EPD-Libraries/SarcLibrary) - Modern C# reader/writer for Nintendo SEAD/SEPD SARC archives.
- [SARC-Tool](https://github.com/aboood40091/SARC-Tool) - Tool for extracting and packing SARC/SZS archives from Nintendo EAD games, using SarcLib and libyaz0.
- [sarc_archiver](https://github.com/Torphedo/sarc_archiver) - C plugin for the PhysicsFS virtual filesystem library that mounts Nintendo SARC archives, with a zstd-compressed I/O wrapper (optional dictionary).
- [GARCTool](https://github.com/kwsch/GARCTool) - Nintendo 3DS GARC (un)packing tool with support for repacking compressed files, complementing GARC-Unpack above.
- [mizuna](https://github.com/tetraxile/mizuna) - C++ library for Nintendo file formats, including Yaz0, SARC/SZS, BYML, and MSBP.

###### Text, Message & Localization (MSBT/LMS)

- [msbt2sheets](https://github.com/CaXaPeK/msbt2sheets) - Converter for MSBT files to spreadsheet format.
- [MSBTEditor](https://github.com/efimandreev0/MSBTEditor) - MSBT text extractor/replacer for .msbt and .umsbt LE-files.
- [umsbt_cmd_extractor](https://github.com/efimandreev0/umsbt_cmd_extractor) - Command extractor for UMSBT files.
- [PyMsyt](https://github.com/NiceneNerd/PyMsyt) - Python library wrapping MSYT for editing Nintendo MSBT text files, used across Breath of the Wild and other Nintendo games.
- [MSBTConverter](https://github.com/KillzXGaming/MSBTConverter) - Tool to convert Nintendo MSBT text files to YAML and back.
- [CLMS](https://github.com/Trippixyz/CLMS) - C# library for Nintendo LMS (Message Studio) text format files (MSBT, MSBP, MSBF).
- [MessageStudio](https://github.com/EPD-Libraries/MessageStudio) - Modern C# implementation of Nintendo MessageStudio (LMS) text file formats.
- [MsbtToYaml](https://github.com/ArchLeaders/MsbtToYaml) - Command-line tool that converts MSBT files to and from YAML.
- [OatmealDome.NinLib.MessageStudio](https://github.com/OatmealDome/OatmealDome.NinLib.MessageStudio) - .NET library for reading MSBT files generated by Nintendo's MessageStudio suite (read-only).
- [MSBT Editor Reloaded](https://github.com/IcySon55/3DLandMSBTeditor) - Windows editor for Nintendo MSBT message files with support for sections such as LBL1 and NLI1.

###### Models, Textures, Fonts & Rendering

- [Syroot.NintenTools.Bfres](https://gitlab.com/Syroot/NintenTools) - Library for reading/writing Nintendo BFRES model format (Wii U).
- [BFRES-Viewer](https://github.com/KillzXGaming/BFRES-Viewer) - Viewer for Nintendo BFRES model format files.
- [BFRES-Tool](https://github.com/aboood40091/BFRES-Tool) - Tool for working with Nintendo BFRES files.
- [BFRES-Extractor](https://github.com/LordNed/BFRES-Extractor) - Extractor for Nintendo BFRES format files.
- [TSCBReader](https://github.com/Sage-of-Mirrors/TSCBReader) - Reader for TSCB format files.
- [3dsfont](https://github.com/dnasdw/3dsfont) - Toolkit for Nintendo BCFNT and BFFNT font files (3DS, Wii U, Switch).
- [bffnt-tools](https://github.com/rashevskyv/bffnt-tools) - Python CLI that unpacks BFFNT/BCFNT/BRFNT fonts into PNG sheets plus `font.json` and packs them back, with a Qt/OpenGL viewer for editing glyph widths and character mapping (README in Ukrainian).
- [NintyFont](https://github.com/hadashisora/NintyFont) - Nintendo binary font editor
- [img2nutexb](https://github.com/jam1garner/img2nutexb) - Converts standard images (PNG, JPG, GIF, DDS, TGA, TIFF, ICO, BMP) to Nutexb, the Namco texture format used in Smash Ultimate and other Switch games.
- [nutexb](https://github.com/jam1garner/nutexb) - Rust library for working with Namco Nutexb textures, found in Smash Ultimate and other Switch games.
- [bntx](https://github.com/jam1garner/bntx) - Rust library for working with Nintendo BNTX textures.
- [img2bntx](https://github.com/jam1garner/img2bntx) - Converts standard images to Nintendo BNTX texture format.
- [BFRES-to-FBX-Converter](https://github.com/jdperos/BFRES-to-FBX-Converter) - Windows tool to convert Nintendo BFRES model files to FBX, built on the FBX SDK.
- [BfresToCast](https://github.com/CosmicDreamsOfCode/BfresToCast) - Console tool to extract models and textures from Nintendo BFRES container files to the Cast format.
- [BFRES-Model-Importer](https://github.com/KillzXGaming/BFRES-Model-Importer) - Script for injecting and replacing models in Nintendo BFRES files (Switch and Wii U), maintaining and extending smb123w64gb's original work.
- [BFRES-Shader-Maker](https://github.com/KillzXGaming/BFRES-Shader-Maker) - Tool for building BFSHA/BNSH shader binaries from scratch using a given BFRES and GLSL code.
- [KCollisionLibrary](https://github.com/KillzXGaming/KCollisionLibrary) - Library for reading and editing Nintendo KCL collision file binaries used by various games.
- [SSBHLib](https://github.com/Ploaj/SSBHLib) - Library for reading and writing Nintendo SSBH rendering format files (used by Super Smash Bros. Ultimate and other Switch games).
- [IONET](https://github.com/Ploaj/IONET) - .NET library for reading and writing several 3D model formats into a common object model.
- [BntxLibrary](https://github.com/EPD-Libraries/BntxLibrary) - Simple C# IO library for the Nintendo BNTX texture format.
- [ssbh_lib](https://github.com/ultimate-research/ssbh_lib) - Rust library for reading and writing Nintendo SSBH rendering format files (used by Super Smash Bros. Ultimate and other Switch games).
- [NintenTools.Bfres (smb123w64gb)](https://github.com/smb123w64gb/NintenTools.Bfres) - .NET library for reading, writing, and modifying the Nintendo BFRES graphics archive format (Wii U); the original work later extended by KillzXGaming's BFRES-Model-Importer above. See also the author's [BFRES_Injector_CMD](https://github.com/smb123w64gb/BFRES_Injector_CMD), a command-line tool built on the library that injects OBJ/SMD meshes into a BFRES model, and [BFRES_IO](https://github.com/smb123w64gb/BFRES_IO), early Python scripts and classes for parsing BFRES vertex data, string tables, models, and textures.
- [hermite-editor](https://github.com/tetraxile/hermite-editor) - GUI editor for the Hermite animation curves found in Nintendo BFLAN layout animation files, exporting keyframe data in the XML format used by KillzXGaming's LayoutLibrary.
- [bfres_importer](https://github.com/RenaKunisaki/bfres_importer) - Blender importer for Nintendo BFRES/SBFRES models (Switch format), including skeletons and textures; used with Breath of the Wild and other Switch titles.
- [BfresPlatformConverter](https://github.com/KillzXGaming/BfresPlatformConverter) - Automatic converter between Wii U and Switch Nintendo BFRES binaries, handling the significant material and shader differences between the two platforms.
- [ImageLibrary](https://github.com/KillzXGaming/ImageLibrary) - Image processing library for decoding and encoding the texture pixel formats shared across KillzXGaming's BNTX, BFRES, and other Nintendo texture tooling.
- [LayoutLibrary](https://github.com/KillzXGaming/LayoutLibrary) - UI library for reading and writing Nintendo BFLYT layout and BFLAN layout-animation file binaries; its animation-curve export format is consumed by hermite-editor above.
- [bflyt-rs](https://github.com/ultimate-research/bflyt-rs) - Rust library and `bflyt-tool` command-line utility that converts Nintendo BFLYT layout files to and from JSON.
- [SwitchLayoutEditor](https://github.com/FuryBaguette/SwitchLayoutEditor) - Editor and renderer for the BFLYT and BFLAN layout files used in Nintendo Switch interfaces and games. Opens SZS archives.
- [ShaderLibrary](https://github.com/KillzXGaming/ShaderLibrary) - Library for loading and saving Nintendo BFSHA and BNSH shader binaries used across Wii U and Switch titles.
- [BntxLibrary (KillzXGaming)](https://github.com/KillzXGaming/BntxLibrary) - C# library for reading and writing the Nintendo BNTX texture format, built on ImageLibrary below for pixel-format processing.
- [BfresLibrary](https://github.com/KillzXGaming/BfresLibrary) - Reworked continuation of smb123w64gb's NintenTools.Bfres above, unifying Wii U and Switch BFRES support with shader-parameter access, in-library texture deswizzling, and near-complete cross-platform material conversion (see BfresPlatformConverter below).

###### Scripting, Parameters & Game Data

- [KMP-Expander](https://github.com/Ermelber/KMP-Expander) - Expander for KMP format files.
- [pymsc](https://github.com/jam1garner/pymsc) - Python library for MSC format files.
- [msc-debugger](https://github.com/jam1garner/msc-debugger) - Debugger for MSC bytecode files, the scripting format used in Super Smash Bros. for Wii U character logic.
- [msclang](https://github.com/jam1garner/msclang) - Custom C-to-MSC-bytecode compiler; MSC is the bytecode format used by Super Smash Bros. for Wii U for character logic.
- [mscdec](https://github.com/jam1garner/mscdec) - Decompiler that converts MSC bytecode (Super Smash Bros. for Wii U) back to C.
- [aamp2xml](https://github.com/jam1garner/aamp2xml) - Converter for Nintendo AAMP parameter archive files (used across Breath of the Wild and other Nintendo EAD games) to/from XML.
- [aamptoyaml](https://github.com/fruityloops1/aamptoyaml) - Converts Nintendo AAMP parameter archive files to readable YAML using a user-supplied list of key strings.
- [AampLibrary](https://github.com/KillzXGaming/AampLibrary) - Library for editing v1 and v2 Nintendo AAMP parameter archive files.
- [PTCLTool](https://github.com/ExplosBlue/PTCLTool) - Editor for Nintendo PTCL particle effect files, used across many first-party Wii U and Switch titles.
- [BymlLibrary](https://github.com/EPD-Libraries/BymlLibrary) - Modern C# library for reading/writing Nintendo BYML (Binary YAML) files, versions 2-7, including Tears of the Kingdom's v7 nodes.
- [AinbLibrary](https://github.com/EPD-Libraries/AinbLibrary) - C# library for Nintendo AINB (AI Node Binary) files.
- [ainby](https://github.com/RootCubed/ainby) - Viewer for Nintendo AINB (AI Node Binary) files.
- [asb](https://github.com/EPD-Libraries/asb) - Base library for parsing and recompiling Nintendo ASB (Animation State Binary) and AINB files.
- [txtg](https://github.com/EPD-Libraries/txtg) - Experimental parser for the Nintendo TexToGo (TXTG) file format.
- [RstbLibrary](https://github.com/EPD-Libraries/RstbLibrary) - C# IO library for Nintendo Resource Size Table (RSTB/RESTBL) files.
- [EvflToJson](https://github.com/ArchLeaders/EvflToJson) - Command-line tool that converts Binary Cafe Event Flow (BFEV) files to JSON and back.
- [BYAMLSharp](https://github.com/Jenrikku/BYAMLSharp) - C# library for reading and writing BYAML versions 1 to 4, including Mario Kart BYAML, with handling of recursion and circular references.

###### Audio

- [AalSharp](https://github.com/EPD-Libraries/AalSharp) - C# IO library for BARS and other Nintendo AAL audio resource file formats.
- [AudioToolkit](https://github.com/EPD-Libraries/AudioToolkit) - IO library for file formats in Nintendo's nw::snd/nn::atk (NintendoWare) audio namespace.
- [Citric Composer](https://github.com/Hengle/Citric_Composer) - Extractor, player, and converter for Nintendo 3DS/Wii U NintendoWare (nw::snd) waveform and streaming audio, with byte-level documentation of the BNK, WAR, SEQ, GRP, and WAV file formats.
- [BCSAR-View](https://github.com/thane98/BCSAR-View) - WIP editor for Nintendo 3DS sound archives (`.bcsar`), dumping and inserting wave sounds, sound sets, and archives, and dumping sequences, banks, and groups.
- [BARSReaderGUI](https://github.com/natv1337/BARSReaderGUI) - GUI for reading Nintendo BARS files and exporting their sound and metadata. Tested with Super Mario Bros. Wonder, The Legend of Zelda: Tears of the Kingdom, Splatoon 3, Animal Crossing: New Horizons and Splatoon 2.
- [BarsTool](https://github.com/NanobotZ/BarsTool) - GUI BARS file editor for extracting or replacing the embedded sound files, made with The Legend of Zelda: Breath of the Wild in mind.
  - [TOTK_BARS_Tool](https://github.com/MediaMoots/TOTK_BARS_Tool) - Patches and adds BWAV files to Tears of the Kingdom BARS files.
  - [bars_py](https://github.com/Nitr4m12/bars_py) - Python module for reading and manipulating BARS files, tested only with Breath of the Wild files.
  - [automatic-bars-patcher](https://github.com/ic-scm/automatic-bars-patcher) - Patches BARS files automatically from whole directories of BWAV files when modding in custom music.
  - [bars-to-bwav](https://github.com/jackz314/bars-to-bwav) - Extracts BWAV files from BARS containers, such as those in Animal Crossing: New Horizons.
- [NW4ArchiveTools](https://github.com/soneek/NW4ArchiveTools) - Libraries for working with SDAT, BRSAR, BCSAR and BFSAR sound archives.
  - [3DSUSoundArchiveTool](https://github.com/soneek/3DSUSoundArchiveTool) - Extracts sequences and banks from BCSAR and BFSAR sound archives.
  - [BFSAR_Split](https://github.com/switch-stuff/BFSAR_Split) - Splits out bfwav, bfstp and bfseq files from a little-endian BFSAR or similar container.
- [BCFSTM-BCFWAV-Converter](https://github.com/aboood40091/BCFSTM-BCFWAV-Converter) - Converts between the BFSTM, BCSTM, BFSTP, BFWAV and BCWAV formats.
- [brsar-patcher](https://github.com/yoshakami/brsar-patcher) - Script that patches BRSAR files, available in Python and C.

###### amiibo (NFC Tag Data)

- [amiitool](https://github.com/socram8888/amiitool) - Reverse-engineered amiibo NFC tag cryptography; decrypts/encrypts and copies Nintendo amiibo dumps. See also [amiitool.net](https://github.com/ca1e/amiitool.net), a C# port.
- [AmiiboAPI](https://github.com/N3evin/AmiiboAPI) - RESTful API and database of amiibo NFC tag data.
- [Amiibo](https://github.com/AmiiboDB/Amiibo) - Database of amiibo `.bin`/`.nfc` NFC tag dumps.
- [emuiibo](https://github.com/XorTroll/emuiibo) - Virtual amiibo (amiibo emulation) system for Nintendo Switch, evolved from ogniK5377's switch-nfp-mitm.
- [GameCubeToolkit](https://github.com/Vertridge/GameCubeToolkit) - Toolkit for reading and editing GameCube-related files.

#### Sharp X68000 SDKs & Hardware

- [mdxtools](https://github.com/vampirefrog/mdxtools) - Collection of tools for handling the MDX music format used on the Sharp X68000.
- [fathuman](https://github.com/vampirefrog/fathuman) - Lists and extracts files from Human68k (Sharp X68000) FAT12/FAT16 floppy disk images in XDF and DIM formats; also usable as a Midnight Commander extfs plugin.
- [wav2adpcm](https://github.com/tantanGH/wav2adpcm) - Converts WAV PCM audio into the Sharp X68000's native ADPCM sound format.
  - [a44enc](https://github.com/tantanGH/a44enc) - Same author's encoder (Linux/macOS) from S44/WAV 16-bit PCM to A44 (YM2608) ADPCM, the format used with the X68000 Mercury-Unit PCM expansion board.
- [mdxvv](https://github.com/tantanGH/mdxvv) - MDX voice viewer for Human68k/X680x0: MDX selector and player that displays and extracts FM voice data from MDX music files (requires MXDRV).
  - [mdxvcat](https://github.com/tantanGH/mdxvcat) - Same author's command-line extractor that writes the voice definitions of an MDX file out as MDX MML, ZMUSIC MML, XC, or X-BASIC definition data.
- [png2sp](https://github.com/tantanGH/png2sp) - Converts RGB/RGBA PNG images into X68000 sprite pattern data (or a 65536-color GVRAM bitmap array).
  - [png2grm](https://github.com/tantanGH/png2grm) - Same author's PNG to 16-bit X68000 GVRAM format converter.
  - [pymag](https://github.com/tantanGH/pymag) - Same author's Python encoder/library that writes images as MAG (.mag) files, a lightweight image format widely used on the X68000 and PC-98.
- [dim2xdf](https://github.com/tantanGH/dim2xdf) - Converts DIM floppy disk images to XDF images, as a Python tool or native Human68k program.
- [xmkmcs](https://github.com/tantanGH/xmkmcs) - Cross-platform bash script set that converts ordinary video files into MACS animation (MCS) data for the X68000, with palette optimization, LZE compression, and ADPCM audio.
- [png2xsp](https://github.com/Mikejmoffitt/png2xsp) - Converts PNG spritesheets into the Sharp X68000's XSP sprite library data format.
- [x68k2amiga](https://github.com/hitchhikr/x68k2amiga) - Amiga program to convert Sharp X68000 executable files (and various X68000 data formats) to Amiga executables for subsequent reversing.
- [x68000_converters](https://github.com/hitchhikr/x68000_converters) - Set of Python scripts to convert various Sharp X68000 file formats (including ADPCM audio samples) to more usable states.
- [furnace_z68](https://github.com/hitchhikr/furnace_z68) - Modification of the Furnace chiptune tracker adding X68000 .z68 music export and an ASM replay routine.

#### FM Towns SDKs & Hardware

*Formats and tools generic to the FM Towns/FM Towns Marty platform, not tied to a specific game.*

- [FM-Squared](https://github.com/DerekPascarella/FM-Squared) - SD card management tool for the FM Towns/FM Towns Marty optical drive emulators Wizard and DocBrown.
- [TIFF Town](https://github.com/DerekPascarella/TIFF-Town) - Cross-platform image converter that turns modern image formats into TIFF files readable by TownsOS on the FM Towns/FM Towns Marty, previewing exactly what the console will display before conversion.
- [FM Towns Self-Boot Kit](https://github.com/DerekPascarella/FM-Towns-Self-Boot-Kit) - Builds self-booting ISOs for the FM Towns/FM Towns Marty from a set of files (including IO.SYS), for use via burned CD-R or ODE.

#### PlayStation SDKs & Hardware

*Formats and tools generic to PlayStation consoles/SDKs, not tied to a specific game.*

- [LibOrbisPkg](https://github.com/maxton/LibOrbisPkg) - Library, GUI, and CLI for creating, inspecting, and modifying PS4 PKG, SFO, PFS, and related package/filesystem formats.
- [shadPKG](https://github.com/seregonwar/ShadPKG) - C++ tool that derives encryption keys for, analyses, decrypts, and extracts PS4 PKG files (games, updates, patches, DLC, and homebrew).
- [psvpfstools](https://github.com/motoharu-gosuto/psvpfstools) - Set of tools to decrypt the PFS (PlayStation File System) filesystem layer used on PS Vita.
- [psvcd](https://github.com/motoharu-gosuto/psvcd) - Documents research into hardware-dumping PS Vita game cartridges (PlayStation Vita Cartridge Dump).
- [vita2hos](https://github.com/xerpi/vita2hos) - PlayStation Vita to Horizon OS (Nintendo Switch OS) translation layer (not an emulator), parsing Vita's executable format to run titles under Switch's OS.
- [Vita3K](https://github.com/Vita3K/Vita3K) - Experimental HLE PlayStation Vita emulator for Windows, Linux, macOS, and Android, running original PS Vita game data. See also [nckstwrt's fork](https://github.com/nckstwrt/Vita3K-Plus) with extensive per-game compatibility fixes for 30+ commercial titles.
- [pkg2zip](https://github.com/lusid1/pkg2zip) - Decrypts PlayStation Vita PKG files and repackages their contents (apps, DLC, patches, themes, PSM, PSX, PSP) into zip archives.
- [unpkg_vita](https://github.com/RikuKH3/unpkg_vita) - Command-line PS Vita PKG unpacker supporting custom decryption keys.
- [VitaPKG_GetInfo](https://github.com/AnalogMan151/VitaPKG_GetInfo) - Python script that retrieves metadata (title, region, size, etc.) from a PlayStation Vita PKG URL link without downloading the full package.
- [PSY-Q SDK Version Finder](https://github.com/jdperos/psyq-version-finder) - GUI tool for PS1 decompilation projects that identifies which Sony PSY-Q SDK version(s) a binary was built with, via color-coded byte-level signature diffing across 10+ SDK releases.
- [psp-media-engine-cracking-the-unknown](https://github.com/mcidclan/psp-media-engine-cracking-the-unknown) - Research documentation on the PSP's Media Engine, covering its Virtual Mobile Engine (VME), specialized move instructions, bitstream/context handling, local DMACs, VLD unit, and H.264 decoder.
- [PsxVram-DotNet](https://github.com/romhack/PsxVram-DotNet) - PlayStation 1 VRAM viewer (.NET rewrite of PsxVram-SDL).
- [uofw](https://github.com/uofw/uofw) - The Unofficial Official FirmWare, a complete reverse engineering project for the latest PSP firmware.
- [pspdecrypt](https://github.com/John-K/pspdecrypt) - Simple tool to decrypt PSP binaries.
- [kirk](https://github.com/ProximaV/kirk) - IDA Pro processor module for the PSP's KIRK crypto engine.
- [allegrexemu](https://github.com/ProximaV/allegrexemu) - Python emulator for the PSP's MIPS Allegrex variant CPU, with an example decompressing the KL4E compression format.
- [psp-ghidra-scripts](https://github.com/pspdev/psp-ghidra-scripts) - Collection of scripts to aid in reverse engineering PSP binaries in Ghidra.
- [psp-arc-sdk](https://github.com/galaxyhaxz/psp-arc-sdk) - Tools for building and extracting the DES-CBC encrypted .arc format updates found within early PSP SDKs.
- [PSPLibDoc](https://github.com/Spenon-dev/PSPLibDoc) - Documents symbols (NIDs) of PSP modules across firmware versions, with tools to load PSPLibDoc XML, PSP export (.exp), and PPSSPP HLE source files.
- [pkgrip](https://github.com/qwikrazor87/pkgrip) - Fast Linux tool for decrypting PS3/PSP PKG files.
- [nploader](https://github.com/codestation/nploader) - PSP plugin for directly reading and loading DLC content in decrypted EDAT/PGD/SPRX form.
- [DTP-T1000-Pre-IPL-dumper](https://github.com/mathieulh/DTP-T1000-Pre-IPL-dumper) - Dumps the PSP's Pre-IPL loader segment from kbooti/bootdispi boot files.
- [qcma](https://github.com/codestation/qcma) - Cross-platform, open-source alternative to Sony's Content Manager Assistant for transferring content to/from the PS Vita.
- [VitaMTP](https://github.com/yifanlu/VitaMTP) - Library implementing the PS Vita's USB MTP-based content transfer protocol, used by qcma and similar tools. Archived.
- [mkpsxiso](https://github.com/Lameguy64/mkpsxiso) - ISO disc image maker written specifically for PlayStation homebrew development. Tool to build and extract PlayStation 1 CD images from XML. Modern cross-platform replacement for BUILDCD from PsyQ SDK. Supports mixed-mode CD-XA with audio/video streams.
- [mkps2iso](https://github.com/N4gtan/mkps2iso) - PlayStation 2 sibling of mkpsxiso, building and dumping DVD-5/9 UDF disc images from/to an XML project. Supports boot logo injection/extraction, Master Disc sector generation, and precise file LBA ordering for seek-time optimization.
- [lst2bin_iso](https://github.com/N4gtan/lst2bin_iso) - Converts CDVDGEN/CDVDREC `.lst`/`.000` disc dump files into standard PS1/PS2 `.bin`/`.iso` images, with options to regenerate or blank the EDC/ECC error-correction data.
- [XAPacker](https://github.com/N4gtan/XAPacker) - Unpacks PlayStation `.XAP` audio archives (used by Digimon Rumble Arena and other PS1 titles) into individual `.XA` audio tracks, and repacks them from a CSV manifest with configurable 2336/2352-byte sector sizes.
- [xa-interleaver](https://github.com/N4gtan/xa-interleaver) - Interleaves/deinterleaves PlayStation XA/XACD audio streams, including custom multi-file stride patterns (e.g. Mega Man X6's BGM.XA), and can replace audio streams inside STR video files; companion to XAPacker above.
- [LibOrbisPkg](https://github.com/OpenOrbis/LibOrbisPkg) - Library, GUI, and CLI tools for creating, inspecting, and modifying PlayStation 4 PKG, SFO, PFS, and related filetypes. Open-source alternative to Sony SDK tools.
- [SGXDataBuilder](https://github.com/Nenkai/SGXDataBuilder) - Creates and builds Sony SGX/SGXD Audio Banks from standard audio formats. Used in various PSP and PS3 games including Gran Turismo 5/6, LocoRoco Cocoreccho, Ape Escape Move, and more.
  - Formats: sgd/sgh/sgb (output), WAV/AC3 (input).
- [LibreFios](https://github.com/neptuwunium/LibreFios) - PSARC library in C# for working with PlayStation PSARC archive format.
- [SCEllSharp](https://github.com/InvoxiPlayGames/SCEllSharp) - Work-in-progress .NET 8.0 library for reading and writing file formats used on the PS3, PSP, and PS Vita consoles (and PS4, for PARAM.SFO).
- [memcardrex](https://github.com/ShendoXT/memcardrex) - Advanced PlayStation 1 memory card editor for managing save files with support for multiple formats.
- [mymc](https://github.com/uyjulian/mymc) - Utility for working with PlayStation 2 memory card images (PCSX2 format). Supports importing/exporting save games in MAX Drive (.max) and EMS (.psu) formats, viewing memory card contents, creating new memory card images, and adding/extracting individual files. Includes GUI and command-line interfaces.
- [EightMB](https://github.com/sevonj/eightmb) - Work-in-progress tool for examining PlayStation 2 memory card images: parses Sony's PS2 memory card file system, and displays `icon.sys` backgrounds and 3D save-icon meshes/textures alongside a dump of the card's contents.
- [ps2mc-browser](https://github.com/caol64/ps2mc-browser) - PS2 save viewer that parses the vertex and texture data of 3D save icons and renders them with OpenGL.
- [sfo](https://github.com/hippie68/sfo) - Fast C program that reads a file to print or modify its SFO parameters. Can be used for automation or to build param.sfo files from scratch. Also available as .exe file for Windows command line.
- [PARAMSFOReader](https://github.com/zyzalfors/PARAMSFOReader) - Command-line reader for PARAM.SFO files from PlayStation save files (PSP, PS3, PS4, etc.), printing the parsed data to the screen or a file.
- [ps3-ckit](https://github.com/tge-was-taken/ps3-ckit) - PS3 C code injection framework. Toolkit for running arbitrary C code in games, hooking existing functions, and inserting custom functionality.
- [ps3recomp](https://github.com/sp00nznet/ps3recomp) - Static recompilation runtime libraries for PlayStation 3 titles.
- [AteliELF](https://github.com/Hakanaou/AteliELF) - Python ELF reverse engineering and patching toolchain for PowerPC64 Big Endian binaries (Cell Broadband Engine), originally built for PS3 game text extraction/reinsertion; also has partial PS Vita and PS2 support.
  - Features: text detection (English/Japanese heuristics, CP932/Shift-JIS), pointer resolution (direct and PPC `lis`/`addic` split-pointer patterns), bin-packing string reinsertion with automatic pointer/phdr updates, EBOOT decrypt/re-encrypt integration, DeepL/Google Translate hookup, Tkinter GUI.
- [dynlib](https://github.com/aerosoul94/dynlib) - IDA Pro plugin to aid PS4 user mode ELF reverse engineering. Loads PS4-specific DYNLIBDATA segment, resolves obfuscated symbol NIDs to label imports/exports, loads symbol table, and patches relocations.
- [PS4-Package-Assessor-Java](https://github.com/Cryptogenic/PS4-Package-Assessor-Java) - Java tool that evaluates PS3/PS4 .PKG files and displays information about them in a clean manner.
- [PSN PKG Validator](https://github.com/13xforever/psn-pkg-validator) - Checks whether a (pre-PS4) PKG file was signed by Sony and whether it is corrupted, validating the header/metadata security values and a full file content hash.
- [create-fself](https://github.com/OpenOrbis/create-fself) - Takes PC-compatible ELFs and generates fake SELF files that run on the PlayStation 4.
- [pkgrename](https://github.com/hippie68/pkgrename) - Renames PS4 PKG files based on param.sfo information, online search, and predefined patterns.
- [ps4-pkg-manager](https://github.com/hippie68/ps4-pkg-manager) - Light-weight, cross-platform desktop application to manage large collections of PS4 PKG files.
- [ps4-pkg-compatibility-checker](https://github.com/hippie68/ps4-pkg-compatibility-checker) - GUI tool with drag-and-drop that checks PKG checksums to determine whether PS4 game and update PKG files are compatible ("married").
- [psxavenc](https://github.com/WonderfulToolchain/psxavenc) - PS1 audio/video encoding tool; converts standard audio/video into the PlayStation 1's native STR/SPU/XA formats.
- [ps4-pup_unpack](https://github.com/idc/ps4-pup_unpack) - PS4 PUP (firmware/system update package) unpacking tool.
- [PlayStation 1 VST Instruments](https://github.com/BodbDearg/PlayStation1Vsts) - VST instruments replicating the PS1 SPU sound chip for music production: an ADPCM sampler that plays back original PS1 .VAG samples with authentic ADSR/interpolation behavior, plus a matching SPU reverb module. Built from the SPU emulation code in the same author's PsyDoom.
- [PSn00bSDK](https://github.com/Lameguy64/PSn00bSDK) - Open source SDK for PS1 homebrew development, defining the toolchain and native formats used by the author's TIMedit, img2tim, and smxtool below.
- [TIMedit](https://github.com/Lameguy64/TIMedit) - Graphical converter and management tool for PlayStation 1 TIM texture files.
- [img2tim](https://github.com/Lameguy64/img2tim) - Converts standard images to the PlayStation 1 TIM texture format.
- [smxtool](https://github.com/Lameguy64/smxtool) - Editing tool for PlayStation RSD and SMX model data formats. See also [Blender-RSD-Plugin](https://github.com/Lameguy64/Blender-RSD-Plugin), a Blender plugin for exporting models in the PlayStation SDK RSD format.
- [psx_psyq_signatures](https://github.com/lab313ru/psx_psyq_signatures) - Signatures for PlayStation 1 PsyQ SDK LIB/OBJ files in JSON form, for identifying statically-linked SDK code in PS1 binaries. See also [psx_psyq_flair](https://github.com/lab313ru/psx_psyq_flair), the same signatures in IDA FLAIR format.
- [ps2-tim2-tool](https://github.com/PS2HomeDeveloper/ps2-tim2-tool) - Tool for working with the PS2 TIM2 texture format, used across many PS2 titles.
- [ps1-tim-tool](https://github.com/PS2HomeDeveloper/ps1-tim-tool) - Command-line converter between PNG/JPG/BMP/TGA/WebP and Sony's official TIM texture format for the original PlayStation. Supports all 4 real TIM pixel formats (4/8/16/24-bit), VRAM/TPAGE/CLUT ID placement, multi-palette recoloring, dithering, batch conversion, and TIM verification/diffing.
- [mipsasm (cakehonolulu fork)](https://github.com/cakehonolulu/mipsasm) - MIPS assembler targeting the PS2 Emotion Engine and IOP; fork of [imaandrew/mipsasm](https://github.com/imaandrew/mipsasm) (originally targeting the N64) retargeted for PS2.
- [psvimgtools](https://github.com/yifanlu/psvimgtools) - Decrypts PlayStation Vita CMA backup images.
- [psximager](https://github.com/cebix/psximager) - Tools for dumping and mastering PlayStation 1 ("PSX") CD-ROM images.
- [PicoMemcard](https://github.com/dangiu/PicoMemcard) - Emulates a PlayStation 1 memory card (or controller) using a Raspberry Pi Pico, reading/writing real memory card data over the console's controller port. See also [MrPalloncini's fork](https://github.com/MrPalloncini/PicoMemcard) with GameID support, and [alex-free's fork](https://github.com/alex-free/PicoMemcard) adding compatibility with the Tonyhax/FreePSXBoot soft-mod exploit.
- [vita-mcr2vmp](https://github.com/dots-tb/vita-mcr2vmp) - Signs PlayStation 1 MCR memory card image files for use with the PS Vita's PSP emulator VMP format, and exports MCR files back out of existing VMPs.
- [MemCardPro-ASM](https://github.com/Cybdyn-Systems/MemCardPro-ASM) - 8BitMods MemCard Pro firmware library/object source, written in MIPS R3000 assembly, for the PS1 hardware memory-card-emulation device.
- [Memory Card Annihilator](https://github.com/ffgriever-pl/Memory-Card-Annihilator) - PS2 memory card management tool with native exFAT filesystem support, covering ProtoKernel PS2 consoles (SCPH-10000/15000) and separate builds for Arcade, Developer, and Prototype memory card hardware variants.
- [PS2-ECC-Memory-Card-Converter](https://github.com/ffgriever-pl/PS2-ECC-Memory-Card-Converter) - Converts PS2 memory card images between ECC and non-ECC binary formats, including images created by Memory Card Annihilator, for use with PCSX2 and vice versa.
- [libcrypt-patcher](https://github.com/alex-free/libcrypt-patcher) - All-in-one patcher for PS1 disc images protected by Sony's LibCrypt anti-piracy scheme, removing the protection directly from the CD image.
- [ECCScan](https://github.com/Terraonion-dev/ECCScan) - PS1 EDC/ECC scanner and fixer for raw CD dumps (mode 2, 2352 bytes/sector); checks and repairs Error Detection/Correction Code mismatches, complementing the check-only edccchk tool.
- [edcre](https://github.com/alex-free/edcre) - Regenerates EDC/ECC data for PS1/PS2 CD images (BIN+CUE) after the image has been edited, so patched discs still pass integrity checks.
- [aprip](https://github.com/alex-free/aprip) - Generator for PS1 Anti-Piracy Protection bypass patches, analyzing a disc image's specific protection implementation to produce a working bypass.
- [psx-undither](https://github.com/alex-free/psx-undither) - Disables the dithering effect in PS1 games, either by patching the CD image directly or by generating GameShark codes from a DuckStation RAM dump.
- [psexe2rom](https://github.com/alex-free/psexe2rom) - Converts PS1 executables (PS-EXE) into flashable GameShark-compatible ROM files.
- [lib-enigma](https://github.com/alex-free/lib-enigma) - C library for patching and identifying PS1/PS2 CD images; spiritual successor to (and supersedes) the author's earlier lib-ppf and lib-ps-cd-id libraries.
- [pops2cue](https://github.com/bucanero/pops2cue) - Reverse-engineered (via Ghidra disassembly) reconstruction of POPS2CUE and CUE2POPS, Sony's original tools for converting PS2/PS3 "POPS" PS-one Classics packages to and from CUE+BIN disc images.
- [Ps2IsoTools](https://github.com/Finzenku/Ps2IsoTools) - Tools to read, build, and edit PS2 ISO images that use the UDF filesystem.
- [KELFBinder](https://github.com/israpps/KELFBinder) - DVD Player and System Updates manager for the PS2, building and patching the console's signed KELF (kernel-ELF) files.
- [MkPFS](https://github.com/PSBrew/MkPFS) - Command-line tool and Python library (PyPI-packaged, with GUI) for building, verifying, inspecting, browsing, and extracting PlayStation FileSystem (PFS) disk images (.ffpfs, .ffpfsc, .pfs, .dat, .exfat, .bin), including PKG/FPKG inner-PFS generation for PS4/PS5.
- [DirectPackageInstaller](https://github.com/marcussacana/DirectPackageInstaller) - Tool to preview and send PKG files directly to a PS4 or PS5 over the network, supporting three different transfer methods.
- [PS5-SELF-Decrypter](https://github.com/EchoStretch/PS5-SELF-Decrypter) - PS5 payload that uses kernel arbitrary read/write to decrypt Signed ELF (SELF) binaries from the filesystem and dump the plaintext ELFs to a USB drive.
- [psio-helper](https://github.com/ncirocco/psio-helper) - Cross-platform Go tool that prepares PS1 CUE/BIN disc images for use with the PSIO optical drive emulator cartridge.
- [xStationMenuRefiner](https://github.com/DerekPascarella/xStationMenuRefiner) - Utility for customizing how the xStation PS1 optical drive emulator displays game titles, by reading an SD card and showing the game list exactly as xStation will render it in both of its menu views, subfolders included.
- [pkg_pfs_tool](https://github.com/flatz/pkg_pfs_tool) - PKG/PFS unpacker for PS4, extracting package and filesystem contents.
- [ps5-pup-decrypt](https://github.com/zecoxao/ps5-pup-decrypt) - Decrypts PS5 PUP (firmware update package) files by directing an exploited PS5 console to decrypt them itself.
  - [ps5-pup-unpacker](https://github.com/zecoxao/ps5-pup-unpacker) - C++ unpacker for the decrypted PS5 update blobs, based on idc's ps4-pup_unpack; runs on Linux, macOS, and Windows and does not unpack the nested FAT32/exFAT filesystem images inside updates.
- [ps4-cfw-toolkit](https://github.com/Al-Azif/ps4-cfw-toolkit) - Decrypts and encrypts various PlayStation 4 firmware files.
- [Playstation-4-Save-Mounter](https://github.com/ChendoChap/Playstation-4-Save-Mounter) - Mounts PS4 save data with read/write access via ps4debug, for decrypting, replacing, sharing, and exporting save files. See also [n0llptr's fork](https://github.com/n0llptr/Playstation-5-Save-Mounter), which adds PS5 save mounting support.
- [Save-Transfer-Wizard](https://github.com/rajeshca911/Save-Transfer-Wizard) - Windows GUI tool for transferring, decrypting, and browsing PS5 save data over FTP.
- [ps5-app-dumper](https://github.com/EchoStretch/ps5-app-dumper) - PS5 payload that dumps installed application files from the console's mounted `pfsmnt` filesystem to a USB drive.
- [make_npdata](https://github.com/aniruddh22/make_npdata) - Encrypts, decrypts, and bruteforces dev_klic keys for PS3 EDAT/SDAT (NP DRM) files. Originally written by Hykem.
- [ps3xport](https://github.com/kakaroto/ps3xport) - Utility for manipulating PS3 backup archives created via the console's System Settings Backup Utility. Can create a fully working backup from scratch, or extract, rename, delete, and add files within an existing backup.
- [RCOMage](https://github.com/kakaroto/RCOMage) - General-purpose RCO resource file creation and manipulation tool, dumping RCOs to an editable XML/resource structure and compiling them back. RCOs are used in the PSP's flash0 resource directory (icons, etc.) and on UMD Video/Audio discs for menu resources. Originally written by ZiNgA BuRgA.
- [MFSUtil](https://github.com/kakaroto/MFSUtil) - Utility for manipulating an MFS (ME File System) partition, the PS3's flash filesystem, as well as the CFG files stored within it.
- [ps4-re-utilities](https://github.com/Al-Azif/ps4-re-utilities) - Dependency-free Python utilities for PS4 reverse engineering: extracting Secure Kernel/Secure Module/SELF keys from decrypted firmware binaries, splitting the AMD μBIOS from the appended FreeBSD kernel in a decrypted kernel ELF, and extracting embedded SELF files (mini-syscore.elf, safemode.elf, etc.) from it.
- [PAKerUtility](https://github.com/israpps/PAKerUtility) - Command-line tool to (un)pack `.PAK` files used by the Sony Utility Discs for PS2 and PSX.
- [romman](https://github.com/israpps/romman) - Image manager for creating, extracting, and inspecting PlayStation 2 ROM and IOPRP images.
- [ps3mca_tool](https://github.com/israpps/ps3mca_tool) - CLI tool for the PS3 CECHZM1 Memory Card adapter, adding arcade MagicGate support and KELF card unbinding on top of the original PS3MCA-TOOL.
- [Open-PS2-Loader](https://github.com/ps2homebrew/Open-PS2-Loader) - Open-source PS2 game/app loader that boots games and homebrew ELFs from USB mass storage, internal/USB hard drives (HDD), memory cards, and network shares (SMB), reading PS2 ISO9660/UDF disc images and IOPRP modules directly.
- [HDL-Batch-installer](https://github.com/israpps/HDL-Batch-installer) - GUI front-end for HDL Dump, featuring batch installation and management of PS2 games on internal/USB hard drives.
- [ps2vmc-tool](https://github.com/bucanero/ps2vmc-tool) - PS1/PS2 VMC (virtual memory card) manager tools.
- [pfsshell](https://github.com/ps2homebrew/pfsshell) - Browses and edits PFS filesystems on APA-formatted PlayStation 2 hard drives.
- [ps2mcfs](https://github.com/FranciscoDA/ps2mcfs) - FUSE driver that mounts PlayStation 2 memory card images, from emulators or real hardware, as a Linux filesystem.
- [psyz](https://github.com/Xeeynamo/psyz) - PlayStation 1 porting SDK, providing PSY-Q-compatible headers and libraries for building native ports of decompiled PS1 games.
- [PsyCross](https://github.com/OpenDriver2/PsyCross) - Compatibility framework for building and running Psy-Q SDK-based PlayStation games across other platforms, from the OpenDriver2 team.
- [IDAPy-PS2](https://github.com/grimdoomer/IDAPy-PS2) - IDA Pro Python scripts for reverse engineering PlayStation 2 Emotion Engine (EE) and IOP executables.
- [PSV-PUP-Extractor](https://github.com/Princess-of-Sleeping/PSV-PUP-Extractor) - PS Vita homebrew app that extracts PSP2UPDAT PUP firmware update package files.
- [OrbisGL](https://github.com/marcussacana/OrbisGL) - Open-source graphical UI framework for PS4 homebrew development, using C# and OpenGL for shape/text rendering, audio playback, and input handling.
- [PS4-OpenOrbis-Mono](https://github.com/marcussacana/PS4-OpenOrbis-Mono) - Sample Mono entry point for PS4 homebrews built on OrbisGL.
- [ps4_remote_pkg_installer](https://github.com/flatz/ps4_remote_pkg_installer) - Remote PKG installer for jailbroken PS4 consoles, pushing package files over the network for installation.
- [ps4_payload_ldr](https://github.com/flatz/ps4_payload_ldr) - Loads fake SELF (fPKG) applications on a jailbroken PS4 via a server, for running homebrew ELFs signed as fake SELF binaries.
- [ps4_stub_lib_maker_v2](https://github.com/flatz/ps4_stub_lib_maker_v2) - Generates stub libraries for linking PS4 homebrew against system PRX/SPRX modules. Second version of the author's original [ps4_stub_lib_maker](https://github.com/flatz/ps4_stub_lib_maker). See also [StubMaker](https://github.com/OSM-Made/StubMaker), an independent alternative for creating custom library stubs for PS4 Official SDK projects.
- [LibProsperoPKG](https://github.com/SvenGDK/LibProsperoPKG) - .NET library for creating, inspecting, and modifying PS5 PKG, GP5, and PFS package/filesystem files. PS5 counterpart to LibOrbisPkg.
- [ps4-wee-tools](https://github.com/andy-man/ps4-wee-tools) - GUI app for working with PS4 SPI/NOR flash and Syscon firmware dumps.
- [ps5-wee-tools](https://github.com/andy-man/ps5-wee-tools) - Tools for working with PS5 SPI/NOR flash dumps.
- [PlayStation-5-NOR-ErrorLog](https://github.com/apewalkers/PlayStation-5-NOR-ErrorLog) - Decodes the Error DBI crash log embedded in PS5 NOR flash dumps.
- [ps4-pup-decrypt](https://github.com/andy-man/ps4-pup-decrypt) - Payload to decrypt the contents of a PS4 firmware update file (PUP).
- [Ps4-Syscon-Read-Write-Helper](https://github.com/egycnq/Ps4-Syscon-Read-Write-Helper) - Script using SYSGLITCH to dump and validate a PS4 Syscon's RL78 firmware, converting the extracted 512KB image to Motorola S28 format and writing it back with rl78flash.
- [PS4_Nor](https://github.com/apewalkers/PS4_Nor) - Script to check and patch the UART debug flag in PS4 NOR flash dumps.
- [PS5 NOR/UART toolkit (apewalkers)](https://github.com/apewalkers/PS5-NOR_Fw_Snoop) - Small utilities for working with PS5 NOR flash dumps and UART error logs, companion to PlayStation-5-NOR-ErrorLog above.
  - Tools: [PS5-NOR_Fw_Snoop](https://github.com/apewalkers/PS5-NOR_Fw_Snoop) (extracts EMC/Southbridge firmware details from NOR `.BIN` dumps), [Ps5_Nor_Validator](https://github.com/apewalkers/Ps5_Nor_Validator) (validates dumps via header checks and entropy analysis), [Play-Station-5-Southbridge-Swap-Script](https://github.com/apewalkers/Play-Station-5-Southbridge-Swap-Script) (patches NOR dumps to swap EMC/Southbridge firmware for an exploitable auth state), [Playstation-5-UART-Reader](https://github.com/apewalkers/Playstation-5-UART-Reader) (UART terminal/decoder for PS5 error logs), [PS5-Software-ErrorLookup](https://github.com/apewalkers/PS5-Software-ErrorLookup) (GUI lookup for PS5 software error codes).
- [ShadowMountPlus](https://github.com/drakmor/ShadowMountPlus) - Automated background auto-mounter payload for jailbroken PS5 consoles that detects, mounts, and installs game backups from internal or external storage, supporting UFS, exFAT, PFS, and nested compressed PFS containers. Actively maintained, substantially expanded fork of RDX-Sci01's ShadowMount1.3GBT.
- [PS4pkg_to_ffpfsc](https://github.com/SadykovIV/PS4pkg_to_ffpfsc) - Converts a PS4 PKG (or an already-unpacked PS4 game) into `.ffpfsc` (compressed) or `.exfat` (raw) disk images for ShadowMountPlus above, merging base game and update PKGs without modifying the source files.
- [UFS2Tool](https://github.com/SvenGDK/UFS2Tool) - Cross-platform (Windows/macOS/Linux) manager for FreeBSD UFS1/UFS2 filesystem images, the filesystem used by PS4/PS5 game dumps.
- [ps5-bar-tool](https://github.com/c0w-ar/ps5-bar-tool) - PS5 payload that parses PS5 Backup and Restore (BAR) `archive.dat` files and dumps the embedded filesystem, using the console itself as an oracle.
- [ps5-uart](https://github.com/symbrkrs/ps5-uart) - Toolkit for interfacing with a PS5 mainboard's service processors over UART and decoding NAND dumps from its Titania storage controller.
  - Components: `uart`/`tool.py` (Raspberry Pi Pico bridge for live EMC/EFC/EAP access), `titania` (standalone Python library/CLI decoding a NAND capture through the scrambler, LDPC, FTL, and namespace layers to plaintext, no hardware needed).
- [selfutil](https://github.com/dmiller423/selfutil) - Converts a PS4/PS5 SELF (fake-signed ELF) executable to a plain ELF and back. See also [xSpecialFoodx's fork](https://github.com/xSpecialFoodx/SelfUtil-Patched), which cleans repetitive segment padding, adds a version segment, and adds more conversion options.
- [dump2ufs](https://github.com/raptorjeesus/dump2ufs) - Converts PS4/PS5 game dump folders or archives (RAR, 7z, etc.) directly into optimized UFS2 filesystem images compatible with ShadowMountPlus above, auto-detecting block size and the game root without an intermediate extraction step.
- [PSFFPKG](https://github.com/sinajet/PSFFPKG) - GUI wrapper for UFS2Tool above, automating the creation of `.ffpkg` (UFS2) images from PS5 game dump directories for installation via the ShadowMount payload.
- [ps5-dlc-toolchain](https://github.com/Gudui/ps5-dlc-toolchain) - Merges any number of PS5 DLC F-PKGs into the latest PATCH PKG: unpacks with orbis-pub-cmd, converts `eboot.bin` from SELF to ELF via SelfUtil, patches in entitlement stubs, regenerates a GP4 project, and repacks a new PATCH PKG.
- [ps4-eboot-dlc-patcher](https://github.com/idlesauce/ps4-eboot-dlc-patcher) - Patches a PS4/PS5 eboot (or other executable) to replace calls into `libSceAppContent`/`libSceNpEntitlementAccess` with a custom PRX, so DLC loads from the base F-PKG when the DLC F-PKGs themselves don't work.
- [PS5PKGReader](https://github.com/SvenGDK/PS5PKGReader) - Reads PS5 PKG files and extracts (some) content. Archived/no longer maintained.
- [PS Multi Tools](https://github.com/SvenGDK/PS-Multi-Tools) - Cross-platform desktop toolkit for PlayStation modders covering PS1-PS5: BIN/CUE to ISO conversion, PS2 STAR and PAK extraction, PS3 ISO tools, PKG extraction/info, PUP unpacking, RCO dumping and SELF reading, PARAM.SFO and PS5 param.json editors, and AT9/WAV conversion.
  - Companions: [PS Mac Tools](https://github.com/SvenGDK/PS-Mac-Tools) (the macOS version, adding ISO to CSO conversion, PS3 ISO make/extract/split/patch and PKG merging), [PSX XMB Manager](https://github.com/SvenGDK/PSX-XMB-Manager) (PSX DVR installer and manager that also edits XMB `.xml`/`.dic` files, converts CUE to POPS VCD, extracts STAR/PAK files, decrypts KELF/REL files and unpacks PS2/PSX BIOS files), [PS Classics fPKG Builder](https://github.com/SvenGDK/PS-Classics-fPKG-Builder) (builds PS1/PS2/PSP fake packages for PS4/PS5 from `.BIN`/`.ISO` files, with automatic TOC generation for PS1 games using CDDA music).
- [garlic-savemgr](https://github.com/earthonion/garlic-savemgr) - PS5 payload that decrypts, encrypts, and browses PS5 save data through an embedded web UI.
- [pkgdec5](https://github.com/zecoxao/pkgdec5) - Decrypts and extracts the "meta" files inside a PS5 PKG that are encrypted with entry-3 keys; port of RedEyeX32's original pkgdec for the PS5.
- [PSPModBase](https://github.com/xan1242/PSPModBase) - Plugin base and collection of basic libraries for PSP game modding and code injection.
- [SN-Systems-ProDG_for_PS2_2.0](https://github.com/AngheloAlf/SN-Systems-ProDG_for_PS2_2.0) - Preserved copy of the SN Systems ProDG PS2 toolchain (GCC 2.95.2, SN BUILD v2.73a), an official third-party compiler suite used to build commercial PS2 games; useful for matching/decompilation work requiring the exact original toolchain.
- [psxtract-2](https://github.com/has207/psxtract-2) - Decrypts and converts PSOne Classics from PSP/PS3 into standard PS1 BIN/CUE images. Actively maintained fork of DeadlySystem's psxtract-2 (itself based on Hykem's original psxtract).
- [binutils-mips-ps2-decompals](https://github.com/decompals/binutils-mips-ps2-decompals) - Fork of GNU binutils patched for PlayStation 2 (MIPS R5900) decompilation projects, providing an assembler/linker toolchain for byte-matching rebuilds.
- [Ps2BiosDecompressor](https://github.com/MarkusMaal/Ps2BiosDecompressor) - Extracts and decompresses all files from a dumped PlayStation 2 BIOS ROM (also works on DVD player ROM images); C# port of balika011's original decompression algorithm.
- [psx-serial-number](https://github.com/ncirocco/psx-serial-number) - Small Go library that extracts and normalizes a PS1 disc's serial number (e.g. `SLUS_015.52`) directly from a `.bin` image; tested against the full NTSC-U library.
- [PSBBN-Definitive-Project](https://github.com/CosmicScale/PSBBN-Definitive-Project) - Complete setup toolkit for the PlayStation 2's internal hard drive (PSBBN), covering disc/game installation, artwork, and menu management.
- [TM2Toolkit](https://github.com/CosmicScale/TM2Toolkit) / [PSMToolkit](https://github.com/CosmicScale/PSMToolkit) / [HDD-OSD-Icon-Generator](https://github.com/CosmicScale/HDD-OSD-Icon-Generator) - Companion utilities to PSBBN-Definitive-Project (above), by the same author.
  - TM2Toolkit: extracts and creates PlayStation 2 TIM2 (`.tm2`) textures.
  - PSMToolkit: extracts/builds PlayStation 2 BB Navigator `.psm` video containers (bundling a `.pss` video with a `.tm2` thumbnail) and pulls the embedded `.tm2` textures back out.
  - HDD-OSD-Icon-Generator: generates PS2 HDD-OSD icons for the HDD-OSD Icon Database.
- [maspsx](https://github.com/mkst/maspsx) - "Modern ASPSX": post-processes GCC-generated MIPS assembly so it can be assembled with GNU `as` into byte-identical ELF objects, replacing the original PSYQ `ASPSX.EXE` + psyq-obj-parser toolchain in PS1 decompilation projects.
- [oscetool](https://github.com/spacemanspiff/oscetool) - Open-source clone of Sony's scetool for PS3 SELF/PKG (de)signing and decryption.

#### WonderSwan SDKs & Hardware

*Formats and tools generic to the WonderSwan platform/SDKs, not tied to a specific game.*

- [ws-ieepview](https://github.com/asiekierka/ws-ieepview) - Viewer/editor for the WonderSwan's internal EEPROM data.
- [wonderswan-tools](https://github.com/dekadencedemo/wonderswan-tools) - Various tools for working with WonderSwan cartridge data, by Dekadence.
- [splashbuilder](https://github.com/Godzil/splashbuilder) - Builds custom boot splash images for the WonderSwan.
- [WonBe](https://github.com/Godzil/WonBe) - WonderWitch BASIC development environment for the WonderSwan.
- [WonX](https://github.com/Godzil/WonX) - WonderWitch on X, a WonderWitch compatibility layer for Unix/X11.
- [swancc](https://github.com/Godzil/swancc) - Tentative WonderSwan C compiler based on BCC.
- [MiracleMage](https://github.com/Godzil/MiracleMage) - WonderWitch emulator for Win32, for running WonderSwan homebrew built with the WonderWitch development kit.

#### Xbox SDKs & Hardware

*Formats and tools generic to the Xbox platform/OS, not tied to a specific game.*

- [SlimEra](https://github.com/XWine1/SlimEra) - Slim Win32 reference implementations of select DLLs from the Xbox ERA operating system (e.g. D3DCompiler_46.dll, xg_x.dll), intended for research/analysis tooling rather than running full games.
- [XDL Compiler](https://github.com/XWine1/XDLCompiler) - Compiler for XDL, an IDL-like interface definition language (with versioning support) used to generate headers for reversing Xbox ERA OS components.
- [XboxAudio2](https://github.com/XWine1/XboxAudio2) - XAudio2 wrapper providing XMA2 audio format support for Xbox TitleOS applications.
- [xma2-rs](https://github.com/echo000/xma2-rs) - Pure-Rust XMA2 and xWMA audio decoder, ported from FFmpeg (no FFmpeg/C toolchain dependency).
- [dump-xbox-dvd](https://github.com/JayFoxRox/dump-xbox-dvd) - Dumps original Xbox game discs (XGD) to redump preservation standard using Kreon-firmware optical drives.
- [xbox-dvd-compress](https://github.com/JayFoxRox/xbox-dvd-compress) - Proof-of-concept tools to inspect redump-format Xbox DVD images: extracts embedded authoring-tool version tags and traces the RNG seed used to generate sector padding, as groundwork for compression.
- [UnXiP](https://github.com/JayFoxRox/UnXiP) - Extracts XIP archive files from the original Xbox dashboard, based on Voltaic's PIXIT research.
- [WinDurango](https://github.com/WinDurango/WinDurango) - Xbox One compatibility layer for Windows, allowing Xbox One executables to run natively on PC.
- [iso2god-rs](https://github.com/iliazeus/iso2god-rs) - Actively maintained, cross-platform (Windows/Linux/macOS) Rust CLI that converts Xbox and Xbox 360 ISOs into the Xbox 360 "Games on Demand" (GoD) container format. See also [r4dius/Iso2God](https://github.com/r4dius/Iso2God), a decompiled C# rewrite of the original tool with quality-of-life improvements.
- [Xbox360BadUpdate](https://github.com/grimdoomer/Xbox360BadUpdate) - Non-persistent, software-only hypervisor exploit for Xbox 360 working on the latest (17559) dashboard/kernel version. See also [bibarub's fork](https://github.com/bibarub/Xbox360BadUpdate).
- [PiPROM](https://github.com/grimdoomer/PiPROM) - Reads, writes, and erases original Xbox EEPROM chips using a Raspberry Pi.
- [XboxImageGrabber](https://github.com/grimdoomer/XboxImageGrabber) - Research tool that generates images visualizing the memory profile/layout of an Xbox console, originally built to aid development of the Halo 2 Vista/HD patch.
- [GoD2NXE](https://github.com/InvoxiPlayGames/GoD2NXE) - Converts GoD-format downloaded Xbox 360 games into NXE installed-game format, useful for building NXE "installed games" out of ISO files.
- [XDVDForenSic](https://github.com/InvoxiPlayGames/XDVDForenSic) - Data recovery tool for damaged/messed-up XDVDFS (Xbox/XGD/"XISO") disc image filesystems.
- [CikExtractor](https://github.com/LukeFZ/CikExtractor) - Dumps stored packed CIK (Content Integrity Key) data for MSIXVC packages from the registry, and leverages emulation to derive the device encryption key needed to decrypt the CIKs for normal usage. See also [InvoxiPlayGames's fork](https://github.com/InvoxiPlayGames/CikExtractor).

#### Tamagotchi (Bandai) Hardware

*Formats and tools generic to the original Tamagotchi handheld toy hardware, not tied to a specific software release.*

- [tamalib](https://github.com/jcrona/tamalib) - Hardware-agnostic emulation library for the first-generation Tamagotchi, reverse-engineering its E0C6S46 CPU and ROM dump format.
- [mcugotchi](https://github.com/jcrona/mcugotchi) - First-generation Tamagotchi (P1) emulator for microcontrollers, built on tamalib. See also [pebblegotchi](https://github.com/jcrona/pebblegotchi), a port for Pebble smartwatches.

##### Tamagotchi Paradise

- [tama-para-research](https://github.com/GMMan/tama-para-research) - Reverse-engineering notes on the Tamagotchi Paradise handheld, documenting its sprite and archive file formats, CJK text/charset handling, and ghost/save data structures.

#### Digimon Color (Bandai) Hardware

*Formats and tools for Bandai's Digimon Color handheld toy line.*

- [DigimonColorSpriteTool](https://github.com/GMMan/DigimonColorSpriteTool) - Sprite import/export tool for the Digimon Color handheld, decoding and re-encoding its BMP-based sprite data format.

#### Sega SDKs & Hardware

- [sega2asm](https://github.com/hansbonini/sega2asm) - Sega Genesis/Mega Drive disassembler and splitter written in Golang, producing reassemblable, annotated source from ROM images.
- [PscdPack](https://github.com/GMMan/PscdPack) - ROM packer for the SEGA Genesis Classics compilation's packaged ROM format.
- [libdreamroq](https://github.com/dreamcastdevs/libdreamroq) - Library version of the DreamROQ video codec used by many Sega Dreamcast games, based on Mike Melanson's original DreamROQ playback engine.
- [SampleToWav](https://github.com/maxim-zhao/SampleToWav) - Converts sampled audio data inside ROM files to WAV, originally targeting Sega 8-bit home video game systems. Supports 4-bit SN76489 volume-control data, 8-bit unsigned PCM, and 1-bit PDM extraction with configurable output bit depth and sample rate.
- [GEMSPlay](https://github.com/ValleyBell/GEMSPlay) - Player for data of GEMS, the sound driver the author describes as the most common on the Sega Mega Drive/Genesis: loads the instrument, envelope, sequence, and sample files or reads them from a ROM via pointers, handles the GEMS 2.8 pointer format, and can log to VGM; includes disassembled Z80 driver sources for several GEMS versions.

#### Soviet PDP-11 Clone SDKs & Hardware (BK-0010/BK-0011M, UKNC)

- [bkdecmd](https://github.com/nzeemin/bkdecmd) - Cross-platform command-line utility for reading/writing BK-0010/BK-0011M floppy disk images, based on gid's BKDE; auto-detects the image's file system.
- [ukncbtl-utils](https://github.com/nzeemin/ukncbtl-utils) - Collection of format conversion utilities for the UKNC (Elektronika MS 0511) computer.
  - Tools: BkBin2Sav/Sav2BkBin (BK-0010 BIN <-> RT-11 SAV conversion), rt11dsk (RT-11 disk image utility), Sav2Cart (RT-11 SAV to UKNCBTL cartridge images), sav2wav (RT-11 SAV to WAV), SavDisasm (SAV file disassembler), UkncArcMan (unarchiver for UKNC's LZS/LZA/FCU archive formats).

### Runtimes, Services & Toolkits
#### RAD Game Tools

*Middleware provider (Bink video, Granny 3D, Miles Sound System) used in hundreds of games across all platforms.*

- [Knit](https://github.com/neptuwunium/Knit) - Fully managed C# reader for Granny 2 files used in many games.
- [GR2Toolkit](https://github.com/REDxEYE/GR2Toolkit) - Toolkit for working with Granny 3D (GR2) model format files.
- [Granny Converter Library](https://github.com/Anohros/GrannyConverterLibrary) - C++ library for converting Granny2 (.gr2) models and animations to FBX format.
- [opengr2](https://github.com/arves100/opengr2) - Open source Granny2 (.gr2) input/output library and tools, with accompanying file format documentation.
- [opengr2-rs](https://github.com/NoFr1ends/opengr2-rs) - Open source Rust parser for Granny2 (.gr2) files.
- [opengr2-bevy](https://github.com/NoFr1ends/opengr2-bevy) - Bevy engine file loader for Granny2 (.gr2) files, built on opengr2-rs.
- [bonkdec](https://github.com/Helco/bonkdec) - Permissive Bink video decoder library in C#.

#### Virtools

- [VirtoolsUnpacker](https://github.com/Hiro420/VirtoolsUnpacker) - C# rewrite of Luigi Auriemma's Virtools file unpacker, for extracting Virtools-packed game files.
- [CK2](https://github.com/doyaGu/CK2) - Actively maintained, clean-room reimplementation of the Virtools Behavioral Engine (CK2) and the VxMath math/utility library, with modern CMake tooling and `.cmo`/`.nmo` file I/O.
  - See also [NeMo2](https://github.com/doyaGu/NeMo2), an earlier reimplementation effort covering the same CK2/VxMath libraries.
- [libnmo](https://github.com/doyaGu/libnmo) - Modern C library for reading and writing Virtools' `.nmo`/`.cmo`/`.vmo` file formats directly, without the full CK2 engine.
- [Virtools-SDK-2.1](https://github.com/doyaGu/Virtools-SDK-2.1) - Reconstructed headers for the original Virtools SDK 2.1.0.14, used as a reference/dependency by other Virtools reimplementation projects.
- [CKRenderEngine](https://github.com/doyaGu/CKRenderEngine) - Standalone reimplementation of Virtools' render engine.
  - See also [Swung0x48/CKRasterizer](https://github.com/Swung0x48/CKRasterizer) and [CKRasterizerLib](https://github.com/doyaGu/CKRasterizerLib) for custom rasterizer backends.
- [CKAngelScript](https://github.com/doyaGu/CKAngelScript) - Integrates the AngelScript scripting language into the Virtools/CK2 runtime as a building block, providing script bindings for the CK/Vx SDK.
- [CKParameterOperations](https://github.com/doyaGu/CKParameterOperations) - Reimplements Virtools' built-in Parameter Operations plugin.
- [CKPlugins](https://github.com/doyaGu/CKPlugins) - Collection of Virtools plugins extending file format support (image formats including BMP, TGA).

##### Ballance

- [Ballanced](https://github.com/doyaGu/Ballanced) - Reversed code of Ballance, the Virtools-engine game used as the reference implementation for reverse-engineering the Virtools/CK2 engine format.
- [BallancePlayer](https://github.com/doyaGu/BallancePlayer) - Modern, enhanced player for Ballance, built by decompiling and improving the original game executable while keeping compatibility with the original game data.
- [BallanceModLoaderPlus](https://github.com/doyaGu/BallanceModLoaderPlus) - Renovated mod loader for Ballance, based on [Gamepiaynmo/BallanceModLoader](https://github.com/Gamepiaynmo/BallanceModLoader).
- [BallanceTAS](https://github.com/doyaGu/BallanceTAS) - Tool-assisted speedrun (TAS) framework for Ballance, with a Lua scripting system for recording, generating, and debugging routes.
- [physics_RT](https://github.com/doyaGu/physics_RT) - Reimplementation of Ballance's physics building blocks.
- [BallanceMMO](https://github.com/Swung0x48/BallanceMMO) - Adds massively-multiplayer online play to Ballance by hooking into the Virtools runtime.
- [BallanceMapPreviewer](https://github.com/Gamepiaynmo/BallanceMapPreviewer) - Tool for previewing Ballance custom maps.

#### Games for Windows Live (GFWL)

*Formats and tools generic to the Games for Windows Live (GFWL) middleware, not tied to a specific game.*

- [xlive-research](https://github.com/widberg/xlive-research) - Research pertaining to Games for Windows Live (GFWL) xlive.dll internals.
- [gfwl-stripper](https://github.com/pallando/gfwl-stripper) - Removes the GFWL header from `.sgd` savegames (Batman: Arkham Asylum and Arkham City) and copies the patched saves to a Steam account.

#### Steam (Valve) Platform Tools

*Libraries for interacting with Valve's Steam network/platform protocols, not tied to a specific game.*

- [SteamKit](https://github.com/SteamRE/SteamKit) - .NET library implementing Valve's Steam network protocol, providing programmatic access to Steam services (CDN/depot downloads, game coordinator messages, etc.).
- [steam](https://github.com/ValvePython/steam) - Python package for interacting with the Steam network, including a CDNClient for depot/manifest access. See also [ValvePython/csgo](https://github.com/ValvePython/csgo) for the CS:GO Game Coordinator protocol.
- [steam-shortcut-editor](https://github.com/tirish/steam-shortcut-editor) - Node.js library to read and write Steam's binary `shortcuts.vdf` file (the non-Steam game shortcuts database), parsing it to a JSON object and back to the original binary format.
- [SteamAppInfo](https://github.com/xPaw/SteamAppInfo) - Reader/example for the Steam client's `appinfo.vdf` and `packageinfo.vdf` files that documents their binary layout across versions.

#### Acrodea VIVID Runtime (G-Gee)

- [acrodea-vivid-runtime-drm](https://github.com/ComoEstaisAmigos/acrodea-vivid-runtime-drm) - Reverse-engineering notes and format documentation for Acrodea's VIVID Runtime, the portable-binary game platform behind the Japanese G-Gee (Gゲー) mobile store (GMO Internet/Acrodea, ~2010-2017); covers the platform's container formats and rights-object key model.
