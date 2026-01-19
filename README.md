# 🎮 Awesome Game File Format Reversing

[Awesome](https://github.com/sindresorhus/awesome)
[License: CC0-1.0](LICENSE)

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
    - [Platform \& SDK Documentation](#platform--sdk-documentation)
    - [Game-Specific Wikis](#game-specific-wikis)
    - [📚 Learning Resources \& Tutorials](#-learning-resources--tutorials)
      - [🎥 Video Tutorials](#-video-tutorials)
    - [Asset Databases](#asset-databases)
  - [🛠️ General Tools](#️-general-tools)
    - [🎨 Asset Viewers \& Converters](#-asset-viewers--converters)
    - [📦 Archive Extractors](#-archive-extractors)
    - [🔊 Audio Tools](#-audio-tools)
    - [🌐 Translation \& Localization](#-translation--localization)
    - [🔍 Hex Editors](#-hex-editors)
    - [🔬 Format Analysis \& Reverse Engineering](#-format-analysis--reverse-engineering)
    - [💻 Development Libraries](#-development-libraries)
    - [📂 Script Collections \& Multi-Game Tools](#-script-collections--multi-game-tools)
  - [⚙️ Engines](#️-engines)
    - [GameMaker](#gamemaker)
    - [Source (Valve)](#source-valve)
    - [Unity](#unity)
    - [Unreal Engine](#unreal-engine)
    - [CryEngine](#cryengine)
    - [Hedgehog Engine](#hedgehog-engine)
    - [Northlight Engine](#northlight-engine)
    - [Pragma Engine](#pragma-engine)
    - [Build Engine](#build-engine)
    - [3DSTATE](#3dstate)
    - [AtiSushi Engine](#atisushi-engine)
    - [Genie Engine](#genie-engine)
    - [RPG Maker](#rpg-maker)
    - [Ren'Py](#renpy)
    - [Rawthrills G7 Engine](#rawthrills-g7-engine)
    - [OpenSpace](#openspace)
    - [Raven Software](#raven-software)
      - [Heretic II](#heretic-ii)
      - [Soldier of Fortune](#soldier-of-fortune)
  - [🔧 Middleware \& SDKs](#-middleware--sdks)
    - [Fast3d/F3dex (N64)](#fast3df3dex-n64)
    - [Havok](#havok)
    - [JSYSTEM (GameCube/Wii)](#jsystem-gamecubewii)
    - [MikuMikuDance](#mikumikudance)
    - [RenderWare](#renderware)
    - [CRI](#cri)
    - [XNA](#xna)
    - [Sappy (GBA Audio)](#sappy-gba-audio)
  - [Game \& Studio Tools](#game--studio-tools)
    - [Activision / Infinity Ward / Treyarch](#activision--infinity-ward--treyarch)
      - [Call of Duty](#call-of-duty)
      - [Tony Hawk's Pro Skater](#tony-hawks-pro-skater)
      - [Ghostbusters](#ghostbusters)
      - [A Series of Unfortunate Events](#a-series-of-unfortunate-events)
    - [Angel Matrix](#angel-matrix)
    - [Angel Studios / Rockstar San Diego](#angel-studios--rockstar-san-diego)
    - [Anthony Bongers](#anthony-bongers)
    - [Ape, Inc](#ape-inc)
    - [Arrowhead Game Studios](#arrowhead-game-studios)
    - [11 bit studios](#11-bit-studios)
    - [Avalanche Studios](#avalanche-studios)
    - [Remedy Entertainment](#remedy-entertainment)
      - [Max Payne](#max-payne)
    - [Argonaut Games](#argonaut-games)
    - [Arkane Studios](#arkane-studios)
    - [Atlus](#atlus)
    - [Asobo Studio](#asobo-studio)
    - [Black Element Software](#black-element-software)
    - [Bandai Namco](#bandai-namco)
    - [Electronic Arts](#electronic-arts)
      - [SSX](#ssx)
    - [EA DICE](#ea-dice)
      - [Battlefield Series](#battlefield-series)
      - [Star Wars: Battlefront](#star-wars-battlefront)
    - [EgoSoft](#egosoft)
    - [Capcom](#capcom)
      - [RE Engine](#re-engine)
      - [Resident Evil](#resident-evil)
      - [Monster Hunter](#monster-hunter)
      - [Devil May Cry](#devil-may-cry)
      - [Street Fighter](#street-fighter)
      - [Ultimate Marvel vs Capcom 3](#ultimate-marvel-vs-capcom-3)
      - [Mega Man](#mega-man)
      - [Gregory Horror Show](#gregory-horror-show)
      - [Gotcha Force](#gotcha-force)
      - [Phoenix Wright: Ace Attorney](#phoenix-wright-ace-attorney)
    - [CCR](#ccr)
    - [CCP Games](#ccp-games)
    - [CR-Space](#cr-space)
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
    - [DOKA Studios](#doka-studios)
    - [EA Black Box](#ea-black-box)
      - [Need for Speed Series](#need-for-speed-series)
    - [FromSoftware](#fromsoftware)
    - [Frictional Games](#frictional-games)
    - [Gearbox Software](#gearbox-software)
      - [MechWarrior 4](#mechwarrior-4)
    - [Game Freak](#game-freak)
      - [Gen I \& II](#gen-i--ii)
      - [Gen III](#gen-iii)
      - [Gen VI](#gen-vi)
      - [Gen V](#gen-v)
    - [Gameloft](#gameloft)
    - [Genius Sonority](#genius-sonority)
    - [Genki](#genki)
    - [Grezzo](#grezzo)
    - [Human Head Studios](#human-head-studios)
    - [id Software](#id-software)
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
    - [Innerloop Studios](#innerloop-studios)
    - [iNiS](#inis)
    - [Jupiter](#jupiter)
    - [Jagex](#jagex)
    - [Konami](#konami)
      - [Metal Gear Solid](#metal-gear-solid)
      - [Silent Hill](#silent-hill)
      - [Fatal Frame](#fatal-frame)
      - [Castlevania](#castlevania)
    - [Kuju London](#kuju-london)
    - [Larian Studios](#larian-studios)
      - [Baldur's Gate 3](#baldurs-gate-3)
      - [Divinity: Original Sin 2](#divinity-original-sin-2)
    - [Level-5](#level-5)
    - [Lionhead Studios](#lionhead-studios)
    - [Metropolis Software](#metropolis-software)
      - [Gorky 17](#gorky-17)
    - [Microsoft Studios / Bungie / Turn 10](#microsoft-studios--bungie--turn-10)
      - [Halo](#halo)
      - [Destiny](#destiny)
      - [Gears of War](#gears-of-war)
      - [Forza](#forza)
      - [Age of Empires](#age-of-empires)
    - [Mobius Digital](#mobius-digital)
    - [Midway](#midway)
      - [Area 51](#area-51)
      - [Gauntlet](#gauntlet)
      - [NFL Blitz](#nfl-blitz)
    - [Monolith Productions](#monolith-productions)
      - [F.E.A.R](#fear)
      - [Trespasser](#trespasser)
      - [Blood](#blood)
      - [Blood 2: The Chosen](#blood-2-the-chosen)
      - [No One Lives Forever](#no-one-lives-forever)
      - [Shogo: Mobile Armor Division](#shogo-mobile-armor-division)
      - [Serious Sam](#serious-sam)
    - [Monolith Soft](#monolith-soft)
      - [Xenoblade Chronicles](#xenoblade-chronicles)
    - [Oddworld Inhabitants](#oddworld-inhabitants)
    - [Naughty Dog](#naughty-dog)
      - [Crash Bandicoot 1-3 \& CTR](#crash-bandicoot-1-3--ctr)
      - [Spyro the Dragon](#spyro-the-dragon)
      - [Jak and Daxter](#jak-and-daxter)
    - [NanaOn-Sha](#nanaon-sha)
    - [Nintendo EAD](#nintendo-ead)
      - [Animal Crossing](#animal-crossing)
      - [AST](#ast)
      - [Luigi's Mansion](#luigis-mansion)
      - [Pikmin](#pikmin)
      - [Pikmin 2](#pikmin-2)
      - [Mario Artist](#mario-artist)
      - [Mario Kart: Double Dash](#mario-kart-double-dash)
      - [Super Mario 64](#super-mario-64)
      - [Super Mario 64 DS](#super-mario-64-ds)
      - [Super Mario (Other)](#super-mario-other)
      - [New Super Mario Bros Wii](#new-super-mario-bros-wii)
      - [Zelda](#zelda)
      - [Wii Sports](#wii-sports)
      - [Star Fox Adventures](#star-fox-adventures)
      - [Star Fox 64](#star-fox-64)
      - [Star Fox 64 3D](#star-fox-64-3d)
      - [Super Monkey Ball](#super-monkey-ball)
      - [F-Zero](#f-zero)
      - [Chibi-Robo](#chibi-robo)
      - [Snowboard Kids](#snowboard-kids)
      - [Wave Race 64](#wave-race-64)
      - [The New Tetris](#the-new-tetris)
      - [New Super Mario Bros DS](#new-super-mario-bros-ds)
      - [Metroid Prime](#metroid-prime)
      - [Pokemon](#pokemon)
    - [Nintendo SDKs \& Hardware](#nintendo-sdks--hardware)
    - [Ntreev Soft](#ntreev-soft)
    - [BioWare](#bioware)
      - [Mass Effect](#mass-effect)
      - [Dragon Age: Origins](#dragon-age-origins)
      - [Knights of the Old Republic](#knights-of-the-old-republic)
    - [Obsidian Entertainment](#obsidian-entertainment)
      - [Neverwinter Nights 2](#neverwinter-nights-2)
    - [Panic](#panic)
    - [Paradox Interactive](#paradox-interactive)
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
      - [Dreamkiller](#dreamkiller)
    - [Piranha Bytes](#piranha-bytes)
    - [Polyphony Digital](#polyphony-digital)
    - [RAD Game Tools](#rad-game-tools)
    - [Rebel Act](#rebel-act)
    - [Rebellion Developments](#rebellion-developments)
      - [Aliens vs. Predator 2](#aliens-vs-predator-2)
      - [Aliens vs. Predator (2010)](#aliens-vs-predator-2010)
    - [Rare](#rare)
      - [Banjo-Kazooie](#banjo-kazooie)
      - [Banjo-Tooie](#banjo-tooie)
      - [Donkey Kong 64](#donkey-kong-64)
      - [Diddy Kong Racing](#diddy-kong-racing)
      - [GoldenEye 007](#goldeneye-007)
    - [Runic Games](#runic-games)
      - [Torchlight](#torchlight)
      - [Torchlight II](#torchlight-ii)
    - [Runecraft](#runecraft)
    - [1C Company / Best Way](#1c-company--best-way)
      - [Men of War](#men-of-war)
      - [Royal Quest Online](#royal-quest-online)
    - [Ironclad Games / Stardock](#ironclad-games--stardock)
      - [Sins of a Solar Empire](#sins-of-a-solar-empire)
    - [Radical Entertainment](#radical-entertainment)
    - [Reflections Interactive](#reflections-interactive)
    - [Riot Games](#riot-games)
    - [Santa Monica Studio](#santa-monica-studio)
    - [SCS Software](#scs-software)
    - [Sega](#sega)
      - [Creative Assembly](#creative-assembly)
        - [Alien: Isolation](#alien-isolation)
        - [Total War Series](#total-war-series)
    - [Sonic Team](#sonic-team)
      - [Sonic Adventure](#sonic-adventure)
      - [Sonic Heroes / Shadow](#sonic-heroes--shadow)
      - [Other Sonic Games](#other-sonic-games)
    - [Snowblind Studios](#snowblind-studios)
      - [Baldur's Gate: Dark Alliance](#baldurs-gate-dark-alliance)
    - [Sony (First Party)](#sony-first-party)
    - [Square Enix](#square-enix)
      - [Final Fantasy](#final-fantasy)
      - [Chrono Cross](#chrono-cross)
      - [Xenogears](#xenogears)
      - [Xenosaga](#xenosaga)
      - [Vagrant Story](#vagrant-story)
      - [Soul Blazer](#soul-blazer)
      - [The World Ends With You](#the-world-ends-with-you)
      - [Babylon's Fall](#babylons-fall)
      - [Hitman](#hitman)
    - [Sucker Punch](#sucker-punch)
      - [Sly Cooper](#sly-cooper)
    - [Supercell](#supercell)
    - [SuperTuxKart](#supertuxkart)
    - [Telltale Games](#telltale-games)
    - [GSC Game World](#gsc-game-world)
      - [S.T.A.L.K.E.R](#stalker)
    - [Troika Games](#troika-games)
    - [Terminal Reality](#terminal-reality)
      - [BloodRayne](#bloodrayne)
    - [THQ / Rainbow Studios](#thq--rainbow-studios)
      - [Cars](#cars)
      - [MX vs ATV](#mx-vs-atv)
      - [Twisted Metal](#twisted-metal)
    - [3D Realms](#3d-realms)
      - [Duke Nukem 3D](#duke-nukem-3d)
      - [Duke Nukem: Manhattan Project](#duke-nukem-manhattan-project)
      - [Duke Nukem Forever (2001)](#duke-nukem-forever-2001)
      - [Duke Nukem Forever (2011)](#duke-nukem-forever-2011)
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
    - [2K Czech / Illusion Softworks](#2k-czech--illusion-softworks)
    - [Natsume](#natsume)
    - [Falcom](#falcom)
    - [Working Designs](#working-designs)
    - [Toby Fox](#toby-fox)
    - [Terry Cavanagh](#terry-cavanagh)
      - [VVVVVV](#vvvvvv)
    - [Studio MDHR](#studio-mdhr)
    - [TaleWorlds Entertainment](#taleworlds-entertainment)
      - [Mount\&Blade](#mountblade)
    - [TT Games](#tt-games)
    - [Acclaim Entertainment](#acclaim-entertainment)
    - [Whoopee Camp](#whoopee-camp)
    - [Team Shanghai Alice](#team-shanghai-alice)
    - [5th Cell](#5th-cell)
    - [Asmik Ace Entertainment](#asmik-ace-entertainment)
    - [Stainless Games](#stainless-games)
    - [Gumi](#gumi)
    - [Ninja Kiwi](#ninja-kiwi)
    - [Eutechnyx](#eutechnyx)
    - [Eurocom](#eurocom)
    - [Hasbro Interactive](#hasbro-interactive)
    - [H2O Entertainment](#h2o-entertainment)
    - [Bohemia Interactive](#bohemia-interactive)
    - [Bugbear Entertainment](#bugbear-entertainment)
    - [Blizzard Entertainment](#blizzard-entertainment)
    - [Westwood Studios / EA Los Angeles](#westwood-studios--ea-los-angeles)
    - [Mojang Studios](#mojang-studios)
    - [Grasshopper Manufacture](#grasshopper-manufacture)
    - [Free Radical Design](#free-radical-design)
    - [Enhance Games](#enhance-games)
    - [Gravity / Ragnarok Online](#gravity--ragnarok-online)
    - [Stencyl](#stencyl)
    - [Her Interactive](#her-interactive)
    - [HeroForge](#heroforge)
    - [Yostar / Revived Witch](#yostar--revived-witch)
    - [CyberStep](#cyberstep)
    - [Mobile Games](#mobile-games)
    - [Bandai Namco (Dragon Ball)](#bandai-namco-dragon-ball)
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

### Platform & SDK Documentation

- [Psy-Q SDK Documentation](https://psx.arthus.net/sdk/Psy-Q/DOCS/) - Official PlayStation SDK documentation archive. Includes file format references, development guides, and API documentation.
  - [File Format Reference](https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Filefrmt.pdf) - Official Psy-Q SDK file format documentation.
- [PSX-SPX Console Dev](https://psx-spx.consoledev.net/) - Comprehensive PlayStation technical documentation and reference. Covers CD-ROM file formats, hardware specifications, BIOS functions, and development resources.
  - [CD-ROM File Formats](https://psx-spx.consoledev.net/cdromfileformats/) - Detailed documentation on PlayStation CD-ROM file formats and structures.

### Game-Specific Wikis

- [The Cutting Room Floor](https://tcrf.net/Help:Contents/Finding_Content) - Community for discovering and documenting unused and debug game content.
- [Nintendo File Formats](https://nintendo-formats.com/) - Documentation for Wii U and Switch games.
- [Custom Mario Kart Wiiki](https://wiki.tockdom.com/wiki/List_of_File_Formats) - Formats used in Mario Kart Wii and related games.
- [Mario Kart 8 Wiki](https://mk8.tockdom.com/wiki/Main_Page) - Documentation for Mario Kart 8 formats and modding.
- [Luma's Workshop](https://www.lumasworkshop.com/wiki/Category:File_formats) - Nintendo modding wiki.
- [Splatoon Technical Wiki](https://wiki.oatmealdome.me/index.php/Special:AllPages) - Technical documentation for Splatoon game formats.
- [Souls Modding Wiki](https://www.soulsmodding.com/doku.php?id=start) - Documentation for FromSoftware formats.

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

*Multi-format tools that support a wide variety of unrelated games.*

### 🎨 Asset Viewers & Converters

- [Noesis](https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91) - Popular all-in-one tool for previewing and converting 500+ model, texture, and animation formats. Supports batch conversion, has a rich plugin ecosystem, and can handle most common game formats out of the box.
  - [Noesis Plugins (Rich Whitehouse)](https://richwhitehouse.com/index.php?content=inc_projects.php#prjmp91) - Official plugin collection by the creator of Noesis.
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
- [swizzleinator](https://github.com/v4nguard/swizzleinator) - Library for detiling/deswizzling various image formats. `no_std`-friendly. Supports PS3, PS4, and X360 texture swizzling/unswizzling.
- [RAW pixels viewer](https://www.kernellabs.com/rawpixels/) - Web-based tool for analyzing raw image data. Displays memory dumps of frame buffers, video buffers, and uncompressed video files. Allows interactive exploration of color formats and image parameters (width, height, offset, flip, invert, zoom) to help identify unknown pixel formats.
- [DDS.Tools](https://github.com/BoBoBaSs84/DDS.Tools) - Simple DDS and PNG tool set that converts DDS images to PNG images and vice versa on a large scale. Has options for duplicate detection and sorting.
- [Sprite Sheet Addon for Blender](https://www.moddb.com/engines/blender-game-engine/downloads/sprite-sheet-addon-for-blender) - Sprite sheet script for Blender VSE. (video squence editor) Convert image sequences to sprite sheet.
- [Sprite Sheet Addon for Blender VSE](https://www.moddb.com/groups/blender-game-engine/downloads/sprite-sheet-addon-for-blender-vse) - Sprite sheet script for Blender VSE. (video squence editor) Convert image sequences to sprite sheet.
- [blender-tooling](https://github.com/bigianb/blender-tooling) - Scripts to import files into Blender.
- [Blender_ioEDM](https://github.com/ndevenish/Blender_ioEDM) - Experimental Blender importer/exporter for .EDM model files used in DCS World flight simulator. Supports basic geometry, textures, animations, and connectors.
- [3ds-Max-Scripts](https://github.com/tge-was-taken/3ds-Max-Scripts) - Archive of 3ds Max scripts including model importing scripts for various game formats and utility scripts.
- [blender_magicavoxel](https://github.com/AstrorEnales/blender_magicavoxel) - MagicaVoxel `.vox` importer for Blender with hierarchy/greedy meshing, voxel hull reduction, and UV-aware material modes.
- [MagicaVoxel-Importer](https://github.com/scayze/MagicaVoxel-Importer) - Godot Engine plugin for importing MagicaVoxel `.vox` format files as meshes. Supports Godot 3.0+ with import scaling and centering based on voxel resolution.
  - Options: multiple meshing modes (voxel-as-model, simple cubes/quads, greedy), UV unwrapping, vertex colors, texture baking, and voxel hull pruning.
  - Material modes: ignore, vertex colors, per-color materials, palette textures, and UV-unwrapped textured models.
- [mviewer](https://github.com/majimboo/mviewer) - Reverse engineering tool for viewing and analyzing MView 3D file format.
- [psx-modding-toolchain](https://github.com/mateusfavarin/psx-modding-toolchain) - Toolchain for PlayStation 1 modding including model and texture tools.
- [detex](https://github.com/hglm/detex) - Low-level library for decompression and manipulation of texture blocks compressed using formats such as BC1/DXT1/S3TC, BC2-BC3, BC4/RGTC1, BC5/RGTC2, BC6 (BPTC_FLOAT), BC7 (BPTC), ETC1 and the ETC2 family, loading of KTX and DDS files, and conversion between pixel formats.
- [heightmap-viewer](https://github.com/impiaaa/heightmap-viewer) - Simple 3D viewer for loading regular heightmaps and special format heightmap files.
- [io_mesh_ninjaripper](https://github.com/REDxEYE/io_mesh_ninjaripper) - Blender addon for importing NinjaRipper .rip files. Supports Blender 2.78-2.79.

### 📦 Archive Extractors

- [QuickBMS](https://aluigi.altervista.org/quickbms.htm) - Universal archive extractor and reimporter with extensive script database covering thousands of games. Uses BMS scripting language to describe archive formats.
- [RTB-QuickBMS-Scripts](https://github.com/RandomTBush/RTB-QuickBMS-Scripts) - Collection of QuickBMS scripts for various games.
- [isodump](https://github.com/Lameguy64/isodump) - PlayStation ISO content extraction tool. Extracts files from PSX ISO/BIN images, supports ISO9660 filesystem, XA and STR files. Generates MKPSXISO-compatible XML project files for rebuilding ISOs.
- [UnkrawerterGBA](https://github.com/MCJack123/UnkrawerterGBA) - Game Boy Advance ROM extractor and converter for games using the Krawall sound engine. Exports audio as XM or S3M module files. Supports automatic detection of instrument/sample lists and modules, direct rip mode for lossless extraction, and can be used as a library.
- [PKGTool](https://github.com/thesupersonic16/PKGTool) - Tool for extracting and repacking PKG files from The Legend of Heroes: Trails of Cold Steel.
- [wad-tools](https://github.com/libertyernie/wad-tools) - Tools for WAD archive format (Wii/GameCube). Fork of BFGR WadTools with enhanced command-line options for wadpacker and wadunpacker, including custom output directories and common-key.bin path specification. Supports C++and C++/CLI compilation.
- [mymc](https://github.com/uyjulian/mymc) - Utility for working with PlayStation 2 memory card images (PCSX2 format). Supports importing/exporting save games in MAX Drive (.max) and EMS (.psu) formats, viewing memory card contents, creating new memory card images, and adding/extracting individual files. Includes GUI and command-line interfaces.
- [archives](https://github.com/mholt/archives) - Cross-platform archive library for Go supporting many formats. Provides unified API and virtual file systems compatible with `io/fs`.
  - Formats: .zip, .tar (including compressed variants), .rar (read-only), .7z (read-only), brotli, bzip2, gzip, lz4, lzip, minlz, snappy/S2, xz, zlib, zstandard.
  - Features: Stream-oriented APIs, automatic format identification, password-protected 7-Zip/RAR support, insert into .tar/.zip without recreating, multithreaded Gzip, DeepFS for traversing archives transparently.
- [GARbro](https://github.com/morkt/GARbro) - Visual novels resource browser and extractor supporting many formats.
  - Engines: KiriKiri (KAG3/TJS2), Nitro+, NScripter, Ren'Py, CatSystem2, AliceSoft, BGI/Ethornell, Liar-soft, Unity, Wolf RPG Editor, RealLive (Key/Visual Arts), Majiro, Nekoneko Soft, Active Soft, DRS, NeXAS, and many others.
  - Formats: `.xp3` (KiriKiri), `.npa` (Nitro+), `.nsa`, `.sar`, `.dat` (NScripter), `.rpa` (Ren'Py), `.int`, `.hg3` (CatSystem2), `.ald`, `.afa`, `.alk` (AliceSoft), `.arc`, `.bsa` (BGI/Ethornell), `.xfl` (Liar-soft), UnityFS, `.assets` (Unity), `.wolf`, `.data` (Wolf RPG Editor), and 200+ other archive formats.
  - Notable Games: *Fate/stay night*, *Fate/hollow ataraxia*, *Steins;Gate*, *Chaos;Head*, *Tsukihime*, *Umineko*, *Katawa Shoujo*, *Doki Doki Literature Club!*, *Grisaia no Kajitsu*, *Rance* series, *Clannad*, *Little Busters!*, *Muv-Luv* series, and many others.

### 🔊 Audio Tools

- [vgmstream](https://github.com/vgmstream/vgmstream) - Audio playback library supporting 1000+ game audio formats including looping, multi-channel streams, and console-specific codecs. Works as a standalone player or Winamp/foobar2000 plugin. If a game audio file exists, vgmstream probably plays it.
- [jpsxdec](https://github.com/m35/jpsxdec) - Cross-platform PlayStation 1 audio and video converter.
- [VGAudio](https://github.com/Thealexbarney/VGAudio) - .NET library for encoding, decoding, and manipulating audio files from video games. Supports many Nintendo formats (BRSTM, BCSTM, BFSTM, IDSP, HPS, DSP, etc.).
- [vgm_ripping](https://github.com/hcs64/vgm_ripping) - Sources for game music ripping tools.
- [wwiseutil](https://github.com/hpxro7/wwiseutil) - Tool for manipulating Wwise SoundBank (.bnk, .nbnk) and File Package (.pck, .npck) files. Supports unpacking WEM audio files, replacing audio with automatic metadata updates, and editing loop points. Works with any game using Wwise audio middleware.
- [soundbank-editor](https://github.com/t1f7/soundbank-editor) - Python-based editor for Wwise soundbank files (.bnk). List, extract, and replace WEM sounds while preserving headers, events, and metadata. Works with any game using Wwise audio middleware.
- [Wwise-Unpacker](https://github.com/Vextil/Wwise-Unpacker) - Windows tool for extracting audio from Wwise PCK and BNK containers to OGG or MP3 format. Works with any game using Wwise audio middleware.
- [Wwise-BNKExtract](https://github.com/rickvg/Wwise-BNKExtract) - Extraction utility for Wwise soundbank files (BNK format, file version 113 and earlier). Extracts WEM audio files for conversion to OGG Vorbis format.
- [wwiser](https://github.com/bnnm/wwiser) - Wwise .bnk explorer and audio simulator. Python tool for parsing Wwise soundbank files, viewing HIRC audio scripting data, generating TXTP files for vgmstream playback, and dumping bank contents. Works with any game using Wwise audio middleware.
- [WwiseParser](https://github.com/xyx0826/WwiseParser) - C# library for parsing Wwise 2016.1 SoundBank object formats. Supports deserializing Wwise objects, rebuilding hierarchies (Master-Mixer and Actor-Mixer), and dumping SoundBank files to JSON. Works with any game using Wwise audio middleware.
- [wwise-audio-tools](https://github.com/WolvenKit/wwise-audio-tools) - Static and dynamic library plus command-line tool for converting Wwise WEM files to OGG format. Modern replacement for ww2ogg and revorb with easier integration.
- [ww2ogg](https://github.com/hcs64/ww2ogg) - Converts Wwise RIFF/RIFX Vorbis audio (.wem files) to standard Ogg Vorbis format. Command-line tool with packed codebook support for various encoding variants. Note: vgmstream is recommended for playback, but ww2ogg is useful when Ogg Vorbis output is specifically required.
- [atrac9j](https://github.com/ShadelessFox/atrac9j) - Java port of the LibAtrac9 library for decoding ATRAC9 audio format used in PlayStation games.
- [BassoonTracker](https://github.com/steffest/BassoonTracker) - Web-based old-school Amiga music tracker in plain JavaScript. Plays and edits Amiga Mod files and FastTracker XM files.
- [DSP2BRSTM](https://github.com/onepiecefreak3/DSP2BRSTM) - Converter and multichannel creator for DSP to BRSTM. Merges multiple DSP files into one multichannel BRSTM. Also supports DSP to WAV conversion.
- [fsb5_split](https://github.com/CyberBotX/fsb5_split) - Tool to split a multi-stream FSB5 into multiple single-stream FSB5s.
- [MCAConverter](https://github.com/onepiecefreak3/MCAConverter) - Converter for Capcom's MCA format. Converts MCA to WAVs and vice versa.
- [HIRCDump](https://github.com/neptuwunium/HIRCDump) - Dump soundbank samples via event IDs.
- [vgmstream-funkify](https://github.com/gheskett/vgmstream-funkify) - vgmstream library for playback of various streamed audio formats used in video games.
- [ray2get](https://github.com/Synthesis/ray2get) - Convert the .apm music files from Rayman 2 (PC) to .wav.
- [libnus3audio](https://github.com/jam1garner/libnus3audio) - Rust library for working with nus3audio files.
- [ntrWavTool](https://github.com/turtleisaac/ntrWavTool) - Converts WAV to IMA ADPCM SWAV for use in DS games.
- [es-ps2-vag-tool](https://github.com/eurotools/es-ps2-vag-tool) - Tool to convert Sony PS2 VAG files to WAV PCM 16-bit encoding and vice versa.
- [es-xbox-adpcm-tool](https://github.com/eurotools/es-xbox-adpcm-tool) - Tool to convert Xbox ADPCM files to WAV PCM 16-bit encoding and vice versa.
- [es-dsp-adpcm-tool](https://github.com/eurotools/es-dsp-adpcm-tool) - Nintendo GameCube DSP audio data encoder. Converts GameCube DSP ADPCM to WAV PCM 16-bit encoding and vice versa.
- [es-ima-adpcm-encoder-decoder](https://github.com/eurotools/es-ima-adpcm-encoder-decoder) - Tool to convert IMA ADPCM files to WAV PCM 16-bit encoding and vice versa.
- [es-eurocom-adpcm-encoder-decoder](https://github.com/eurotools/es-eurocom-adpcm-encoder-decoder) - Tool to convert custom Eurocom ADPCM files to WAV PCM 16-bit encoding and vice versa.
- [Citric-Composer](https://github.com/gota7/Citric-Composer) - Editor for 3DS, Wii U, and Switch sound files. See also [Tiniifan's fork](https://github.com/Tiniifan/Citric-Composer).

### 🌐 Translation & Localization

- [Kuriimu](https://github.com/IcySon55/Kuriimu) - General purpose game translation toolkit.
- [Kuriimu2](https://github.com/FanTranslatorsInternational/Kuriimu2) - Next-gen version of Kuriimu.

### 🔍 Hex Editors

- [010 Editor](https://www.sweetscape.com/010editor/) - Professional hex editor with powerful template system for analyzing binary file structures (paid).
- [ImHex](https://github.com/WerWolv/ImHex) - Modern, open-source hex editor with pattern language for reverse engineering file formats (free).
- [hexerator](https://github.com/crumblingstatue/hexerator) - Versatile GUI hex editor focused on binary file exploration and aiding pattern recognition. Written in Rust.
- [hexyl](https://github.com/sharkdp/hexyl) - Command-line hex viewer with colored output.
- [hex](https://github.com/cosarara/hex) - Simple hexadecimal editor with vi-like modal interface.
- [hxd-plugin-framework](https://github.com/maelh/hxd-plugin-framework) - Plugin framework for HxD hex editor to support custom file formats.

### 🔬 Format Analysis & Reverse Engineering

- [Kaitai Struct](https://kaitai.io/) - Declarative language for describing binary data structures with code generation for multiple programming languages.
- [Veles](https://codisec.com/veles/) - Binary analysis and visualization tool for reverse engineering (open-source).
- [atlas](https://github.com/nblockbuster/atlas) - Hashing tool for reverse engineering work. Plugin-based system supporting FNV (0, 1, 1a), MD2/MD4/MD5, Murmur2/3, SipHash, SHA1/SHA2/SHA3, XXHash/XXHash3. Useful for analyzing hashed values in game file formats.
- [010 Templates / ImHex Patterns](https://github.com/neptuwunium/bt) - Templates for binary analysis.
- [010GameTemplates](https://github.com/Nenkai/010GameTemplates) - Collection of 010 Editor templates for various games including Gran Turismo, Forza, Project Cars, Ridge Racer 7, Tales of Vesperia, Xenoblade Chronicles, Granblue Fantasy: Relink, Driveclub, WWE 2K, and many others.
- [010-Editor-Templates](https://github.com/tge-was-taken/010-Editor-Templates) - Collection of 010 Editor binary templates for game file format analysis.
- [mafia-formats](https://github.com/pudingus/mafia-formats) - 010 Editor templates for Mafia: The City of Lost Heaven file formats.
- [chtdb](https://github.com/tge-was-taken/chtdb) - Cheats and patches database for PSX games, primarily intended for use with DuckStation emulator. Contains GameShark codes and patches for various games.
- [XenonRecomp](https://github.com/hedge-dev/XenonRecomp) - Tool for recompiling Xbox 360 games to native executables. Converts Xbox 360 executables into C++ code that can be recompiled for any platform.
- [DataExplorer](https://github.com/x64dbg/DataExplorer) - Data explorer plugin for x64dbg debugger that integrates the pattern language from ImHex.
- [HexForge](https://github.com/elastic/HexForge) - IDA plugin that extends the functionality of the assembly and hex view, allowing you to decode/decrypt/alter data directly from the IDA Pro interface.
- [FakePDB](https://github.com/Mixaill/FakePDB) - Tool for PDB generation from IDA Pro database. Supports IDA >= 7.0. Can generate PDB files, export IDA database to JSON, find binary signatures, and import function names from JSON.
- [HexRaysCodeXplorer](https://github.com/REhints/HexRaysCodeXplorer) - Hex-Rays Decompiler plugin for better code navigation in reverse engineering. Automates code reconstruction of C++ applications and modern malware. Features include automatic type reconstruction, virtual function table detection, and RTTI analysis.
- [microavx](https://github.com/gaasedelen/microavx) - AVX lifter for the Hex-Rays Decompiler. Extends IDA Pro decompiler with partial support for Intel Advanced Vector Extensions (AVX) instructions. Demonstrates how Hex-Rays microcode can be used to lift and decompile new or previously unsupported instructions.
- [Ouroboros](https://github.com/Hexorg/Ouroboros) - Symbolic-execution decompiler written in Rust. Recovers high-level structure from binaries using symbolic execution and constraint tracking. Features CFG recovery, structural reconstruction (if/else, loops), calling convention inference, and beautiful UI with egui.
- [qiling](https://github.com/qilingframework/qiling) - Advanced binary emulation framework. Emulates multi-platforms (Windows, macOS, Linux, Android, BSD, UEFI, DOS) and multi-architectures (x86, ARM, MIPS, RISC-V, PowerPC). Supports PE, Mach-O, ELF formats with fine-grain instrumentation, cross-architecture debugging, and dynamic hot patching.
- [Pattern16](https://github.com/Dasaav-dsv/Pattern16) - Fastest x86-64 signature matching library. Optimized for reverse engineering with speeds up to 25 GB/s. Uses AVX1, SSE4.1, SSE2, CMOVE, BMI2, and BMI1. Header-only C++ library for pattern scanning in memory regions.
- [Recaf](https://github.com/Col-E/Recaf) - Modern Java bytecode editor. Easy-to-use interface for editing Java bytecode with decompiler integration, built-in compiler, bytecode assembler, and support for standard Java and Android applications.
- [iced](https://github.com/icedland/iced) - Blazing fast and correct x86/x64 disassembler, assembler, decoder, and encoder. Available for Rust, .NET, Java, Python, and Lua. Useful for reverse engineering game binaries.
- [IDArling](https://github.com/IDArlingTeam/IDArling) - Collaborative reverse engineering plugin for IDA Pro and Hex-Rays. Enables multiple users to work on the same IDA database simultaneously.
- [Reloaded.Hooks](https://github.com/Reloaded-Project/Reloaded.Hooks) - Advanced native function hooks for x86 and x64. High-performance hooking library for .NET with support for unit testing hooks. Used in Reloaded modding framework.
- [Reloaded-II](https://github.com/Reloaded-Project/Reloaded-II) - Universal .NET Core powered modding framework for any native game (x86, x64). DLL injection based mod loader with mod management system, optional mod SDK, and extensive plugin support.
- [ExeGag](https://github.com/efimandreev0/ExeGag) - Tool to edit game strings into compiled ELF files.
- [binviz](https://github.com/VelocityRa/binviz) - Binary visualization tool for identifying patterns and structure in unknown files. Creates visual representations showing potential compression/encryption, structured data and padding at a glance. Helpful for spotting where assets begin/end in unstructured archives.
- [JSC-PyDecrypt-Tool](https://github.com/bartlomiejduda/JSC-PyDecrypt-Tool) - Decrypts JSC (JavaScript Compiled) files from Cocos2d games. Requires valid encryption key extracted via Frida from running game instances.
- [pics](https://github.com/corkami/pics) - File formats dissections and visualizations for reverse engineering.
- [psxrev](https://github.com/emu-russia/psxrev) - Sony PlayStation PCB/chips reverse engineering documentation and resources.
- [Ghidra-GameCube-Loader](https://github.com/Cuyler36/Ghidra-GameCube-Loader) - Nintendo GameCube binary loader for Ghidra reverse engineering framework.
- [NTRGhidra](https://github.com/onepiecefreak3/NTRGhidra) - Nintendo DS binary loader for Ghidra reverse engineering framework.
- [Ghidra-RSP](https://github.com/Random06457/Ghidra-RSP) - Nintendo 64 RSP processor module and loader for Ghidra.
- [dwarf2cpp](https://github.com/seilc/dwarf2cpp) - Converts DWARF v1 debug data from ELF files into C/C++ definitions including structs, enums, unions, and function definitions. Useful for reverse engineering games with DWARF debug information.
- [BinaryX](https://github.com/Cuyler36/BinaryX) - BinaryReader capable of reading both BigEndian and LittleEndian schemes.
- [research](https://github.com/ProjectDreamland/research) - Research on game engine and decompiled game code.
- [gsaxml](https://github.com/Candoran2/gsaxml) - XML description of the binary format of compiled GSA (Game Script Archive) files.
- [decomp-toolkit](https://github.com/encounter/decomp-toolkit) - GameCube & Wii decompilation toolkit.
- [splat](https://github.com/ethteck/splat) - Binary splitting tool to assist with decompilation and modding projects.
- [objdiff](https://github.com/encounter/objdiff) - Local diffing tool for decompilation projects.
- [decomp-permuter](https://github.com/simonlindholm/decomp-permuter) - Randomly permute C files to better match a target binary.
- [m2c](https://github.com/matt-kempster/m2c) - MIPS and PowerPC decompiler.
- [vutrace](https://github.com/chaoticgd/vutrace) - PlayStation 2 vector unit tracing debugger.
- [hlsldecompiler-rs](https://github.com/cohaereo/hlsldecompiler-rs) - Statically linked 3dmigoto Rust wrapper for HLSL shader decompilation.

### 💻 Development Libraries

- [assert-offset](https://github.com/cohaereo/assert-offset) - Rust derive macro for asserting the memory offset of fields in a struct. Useful for low-level FFI and embedded development.
- [ReverseBox](https://github.com/bartlomiejduda/ReverseBox) - Python library for reverse engineering with utilities for checksums (Adler32, CRC variants, Fletcher, XOR), compression (BZIP2, LZ4, LZMA, MIO0, PackBits, RLE variants), encryption (ROT13, XOR cipher), hashing (FNV, DJB2, MD5, SHA, Murmur3), and image processing (100+ pixel formats including DXT, PVRTC, ETC, ASTC, BC formats, swizzling for multiple platforms).
- [binread](https://github.com/jam1garner/binread) - Rust library for reading binary file formats with derive macros.
- [DragonLib](https://github.com/neptuwunium/DragonLib) - Common library for file format research.
- [GL Editor Framework](https://github.com/jupahe64/GL_EditorFramework) - OpenGL-based framework for creating 3D game editors with hardware-accelerated graphics.
- [SFGraphics](https://github.com/ScanMountGoat/SFGraphics) - OpenGL graphics library for rendering game formats, used in various format viewers.
- [MeshSharp](https://github.com/MinshuG/MeshSharp) - 3D library in pure C# for reading and writing multiple formats (FBX, STL, PLY).
- [Assimp.Net](https://github.com/StirlingLabs/Assimp.Net) - C# .NET Core wrapper for the Open Asset Import Library (Assimp) for importing 3D models.
- [ooz](https://github.com/powzix/ooz) - Open-source decompressor for Oodle compression formats (Kraken, Mermaid, Selkie, Leviathan, LZNA, Bitknit) used in many modern games including Warframe and other titles using RAD Game Tools compression.
- [Syroot.BinaryData](https://gitlab.com/Syroot/BinaryData) - .NET library for easy binary data reading/writing with support for various endianness and encodings.
- [Amicitia.IO](https://github.com/tge-was-taken/Amicitia.IO) - High performance File IO library with full support for big endian and offsets.
- [SharpRiff](https://github.com/gigaherz/SharpRiff) - .NET library for reading and writing RIFF format files, such as .wav, .avi, or WebP.
- [XeNTaXTools-Legacy](https://github.com/XeNTaXTools/XeNTaXTools-Legacy) - Legacy tools scraped from the XeNTaX forums.
- [formast](https://github.com/amorilia/formast) - FormAST exposes file format descriptions through a simple API.
- [vmf](https://github.com/Galaco/vmf) - Go library for parsing Valve's Hammer Editor .vmf map files.
- [GameFormatReader](https://github.com/lioncash/GameFormatReader) - Library for reading various game formats (mostly Nintendo ones).
- [CTLib](https://github.com/narahiero/CTLib) - Utility library to create and convert various file formats used in Mario Kart Wii custom tracks.
- [Byaml-Tool](https://github.com/KillzXGaming/Byaml-Tool) - Simple BYAML tool which currently just converts endianness using Syroot's Byaml library.
- [tinybcdec](https://github.com/jandk/tinybcdec) - Small block compression decoder library in pure Java. Decodes BC1-DXT1, BC2-DXT3, BC3-DXT5, BC4-ATI1, BC5-ATI2, BC6H, and BC7 texture formats. Zero dependencies, focus on speed and accuracy with support for partial decodes.
- [Console-Swizzler](https://github.com/matyamod/Console-Swizzler) - C library to swizzle DDS textures for console games. Supports PS4 and Switch texture swizzling/unswizzling with configurable GOB block heights. Includes CLI tool for batch processing.
- [prs.net](https://github.com/FraGag/prs.net) - PRS compression/decompression library and GUI front-end for the .NET Framework. PRS is based on LZ77 with run-length encoding and is used in numerous games since the SEGA Saturn, including Phantasy Star Universe.
- [NKZIPLib](https://github.com/pixeldesu/NKZIPLib) - C# library for parsing NKZIP archive files used in MMO games from the early 2000s. Simple format with no compression - files stored sequentially with header containing magic, version, raw data bytes, and file count.

### 📂 Script Collections & Multi-Game Tools

- [noclip.website](https://github.com/magcius/noclip.website) - In-browser 3D viewer for 60+ games across multiple platforms and studios.
  - Games: Source Engine games (17 titles including Half-Life 2, Portal 1 & 2, Team Fortress 2, CS:GO, L4D2),
  Nintendo games (Mario 64, Mario Kart series, Zelda series, Pikmin, Luigi's Mansion, Super Mario Galaxy 1 & 2, Paper Mario series, Kirby, Smash Bros Melee/Brawl), Rare games (Banjo-Kazooie, DKC), GTA series (III, Vice City, San Andreas), Crash Bandicoot, Dark Souls, Katamari Damacy, Okami, Psychonauts, Need for Speed: Most Wanted, SpongeBob games, Outer Wilds, Halo CE, and more.
- [GameArchives](https://github.com/PikminGuts92/GameArchives) - C# library for reading 14+ video game archive formats.
  - Games: Harmonix titles (Frequency, Amplitude, Guitar Hero series, Rock Band series 1-4, Beatles, Green Day, Lego, VR, Karaoke Revolution, Disney Fantasia),
  Konami rhythm games (DDR Universe 1-3, DDR 2010, Dance Masters), FreeStyleGames (DJ Hero series, Guitar Hero Live, Sing Party), Psychonauts, Power Gig.
  - Formats: Ark, PSARC, PACKAGE, PFS, STFS, XDVDFS, U8. See also [maxton's fork](https://github.com/maxton/GameArchives) with FSAR support for Sing Party.
- [psarc](https://github.com/ShadelessFox/psarc) - Viewer for PlayStation Archive (PSARC) archives. Supports listing and extracting files from PSARC archives with GUI and CLI interfaces.
- [MeltyTool](https://github.com/MeltyPlayer/MeltyTool) - Multitool for viewing/extracting assets from various N64/GCN/3DS/PC games.
  - Games: Super Mario 64, Mario Artist (Polygon Studio, Talent Studio), Paper Mario TTYD, Super Paper Mario, Mario Kart Double Dash, Pikmin 1 & 2, Super Mario Sunshine, Chibi-Robo, Super Smash Bros. Melee, Battalion Wars 1 & 2, Super Mario 64 DS, Luigi's Mansion 3D, Majora's Mask 3D, Ocarina of Time 3D, Professor Layton vs. Phoenix Wright, Dead Space, Glover, Halo Wars, Celeste 64, Pokemon Colosseum, and more.
- [Noesis Plugins](https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91) - Community plugin collections extending Noesis support to hundreds more games.
  - See [6 major plugin collections](https://richwhitehouse.com/index.php?content=inc_projects.php#prjmp91) including Tales series, Midnight Club 2, Visceral Games titles, and many more formats.
- [EdnessP/scripts](https://github.com/EdnessP/scripts) - Collection of scripts for various game file formats.
  - Games: Bully series, Burnout series (1, 2, 3, Legends, CRASH!), Call of Duty: Finest Hour, Jak & Daxter series (1, II, 3, X), Midnight Club series (2, 3), Saints Row series (2, Undercover), The Sims series (Bustin' Out, Urbz, 2, Pets, Castaway), The Simpsons Game, Tomb Raider (Wii), Need for Speed: Shift (PSP), Activision/Atari Anthology, Adventure Time, Bomberman Act:Zero, Big Rigs, Castle Strike, Driver: San Francisco, Epic Mickey, Exit, Freaky Flyers, Ready 2 Rumble Boxing, SpongeBob's Surf & Skate Roadtrip, Strike Suit Zero/Infinity, Yakuza 1 & 2 (PS2), and more.
- [bartlomiejduda/Tools](https://github.com/bartlomiejduda/Tools) - Collection of tools to manage and modify files from many various games. Includes archive tools, binary templates, and format-specific utilities.
  - Games: 150+ titles including Harry Potter series, Bully, Crash Bandicoot series, Tony Hawk's Underground, Sonic 2006/Unleashed, Resident Evil 7, Silent Hill series, Just Cause, Splinter Cell, SimCity 3000, LEGO games, The Sims series, Super Mario Sunshine, Star Wars Jedi Academy, Tekken 5, Transformers, Beyond Good & Evil, and many more.
- [Murugo/Misc-Game-Research](https://github.com/Murugo/Misc-Game-Research) - Research artifacts and tools for various games.
  - Games: Vib-Ribbon (PS1), Gitaroo Man (PS2), Silent Hill 2 & 3 (PS2), Kingdom Hearts series (PS2), Rule of Rose (PS2), Musashi: Samurai Legend (PS2).
- [game-extraction-toolbox](https://github.com/shawngmc/game-extraction-toolbox) - Python CLI tools for extracting ROMs from game rereleases and investigating game files.
  - Supports extracting ROMs from collections like Capcom Arcade Stadium, Street Fighter 30th Anniversary Collection, Mega Man Legacy Collections, SNK 40th Anniversary Collection, and many more.
- [save-decrypters](https://github.com/bucanero/save-decrypters) - Collection of custom save-game decrypters and checksum fixers for PS3, PSP, and PS4.
  - Games: GTA5, The Last of Us, Uncharted series, Metal Gear Solid series, Resident Evil series, Final Fantasy XIII series, and many more.
- [HyoutaTools](https://github.com/AdmiralCurtiss/HyoutaTools) - .NET CLI collection of tools for packing and unpacking video game archives. Includes functions for extracting data from and reinserting data into various games.
- [vgm-disasm](https://github.com/loveemu/vgm-disasm) - Disassembly collection of classic video game music drivers. Disassembles VGM (Video Game Music) files for educational and preservation purposes.
- [RTB-3DSMax-Scripts](https://github.com/RandomTBush/RTB-3DSMax-Scripts) - Comprehensive collection of 3ds Max scripts for importing models from dozens of games and engines.
  - Games: Pokémon (Switch/3DS), Zelda (BOTW/TOTK/Wind Waker HD), Mario (Odyssey/Kart 8/3D World), Splatoon (1-3), Hyperdimension Neptunia series, Crash Bandicoot N. Sane Trilogy, Sonic (Unleashed/Riders), Telltale Games (Walking Dead/Batman), and many more.
  - Highlights: Support for ISM2, IGZ, MDL, D3DMesh, and Nintendo BFRES/BCH formats across PS1, PS3, Wii, Wii U, and Switch.

## ⚙️ Engines

*Tools specific to widespread third-party game engines.*

### GameMaker

- [UndertaleModTool](https://github.com/UnderminersTeam/UndertaleModTool) - Tool for modding/decompiling GameMaker games.
- [GMS-Explorer](https://github.com/puggsoy/GMS-Explorer) - Game Maker Studio `data.win` explorer.
- [GMSD](https://github.com/lynn/GMSD) - GameMaker Studio decompiler in F#.
- [UndertaleTools](https://github.com/fjay69/UndertaleTools) - GameMaker data.win unpacker/packer.
- [pugIFF](https://github.com/nkrapivin/pugIFF) - GameMaker IFF gamefile reader in GML.
- [YYTextureView](https://github.com/YAL-GameMaker-Tools/YYTextureView) - Tool for exploring textures in GameMaker games.
- [libaltar](https://github.com/Prashant-Jonny/libaltar) - Library for processing GameMaker: Studio binary file formats (decompiler).
- [gamemaker2-data-research](https://github.com/jam1garner/gamemaker2-data-research) - Tools/Documentation for GameMaker 2 data files.
- [LojRipper](https://github.com/nkrapivin/LojRipper) - Tool to dump .win files from GameMaker YYC-compiled executables for game modding purposes.

### Source (Valve)

- [valve-bsp-parser](https://github.com/ReactiioN1337/valve-bsp-parser) - Parser for Valve BSP (Binary Space Partition) map files.
- [Blender Source Tools](https://github.com/Artfunkel/BlenderSourceTools) - Blender addon for importing and exporting Source Engine model and animation formats. Enables 3D asset creation and modification for all Source Engine games in Blender.
- [noclip.website (Source Engine)](https://github.com/magcius/noclip.website/tree/main/src/SourceEngine) - In-browser Source engine map viewer supporting Counter-Strike: Source, Half-Life 2, Half-Life 2: Deathmatch, Half-Life 2: Lost Coast, Half-Life 2: Episode 1, Half-Life 2: Episode 2, Team Fortress 2, Portal, Portal 2, Counter-Strike: Global Offensive, Left 4 Dead 2, The Stanley Parable, Infra, Neo Tokyo, and Estranged: Act I.
- [noclip.website (GoldSrc)](https://github.com/magcius/noclip.website/tree/main/src/GoldSrc) - In-browser Half-Life (GoldSrc) viewer.
- [srctools](https://github.com/TeamSpen210/srctools) - Python modules for working with Source Engine file formats (VMF, BSP, VPK, etc).
- [vdf-parser](https://github.com/lukezbihlyj/vdf-parser) - Parser for Valve Data Format (VDF) files used in Source games.
- [go-valve](https://github.com/handsomematt/go-valve) - Go library for querying A2S server information from Source servers.
- [valve-vrm](https://github.com/UnBeatWaterGH/valve-vrm) - Documentation and converter for Valve's experimental VRM model format.
- [sledge-formats](https://github.com/LogicAndTrick/sledge-formats) - C# parsers and formats for Half-Life 1 and related engines.
- [corvid](https://github.com/KILLTUBE/corvid) - Source Engine level converter for Call of Duty.
- [Plumber](https://github.com/lasa01/Plumber) - Blender add-on for importing Source 1 engine maps, models, materials and textures from CS:GO, TF2, CS:S, and other titles.
  - Features: full map import (brushes, overlays, lights, props, skyboxes), MDL/material/texture import with color options, and embedded file browser.
- [powerjack](https://github.com/cohaereo/powerjack) - Team Fortress 2 asset viewer and demo player. Features improved rendering with direct lightmap sampling from BSP data.
- [SourceOps](https://github.com/bonjorno7/SourceOps) - Blender addon for exporting models to Source 1. More convenient alternative to Blender Source Tools. Features export objects as SMD or FBX, export actions as SMD, generate QC based on UI settings, buttons to compile and view models, and experimental export for brushes and displacements to VMF. Requires Blender 2.83 or newer.
- [io_mesh_SourceBSP](https://github.com/REDxEYE/io_mesh_SourceBSP) - Blender addon for importing and exporting Source Engine BSP map files.
- [io_texture_VTF](https://github.com/REDxEYE/io_texture_VTF) - Blender addon for importing and exporting Source Engine VTF texture files. (Archived)
- [AutoMDL](https://github.com/NvC-DmN-CH/AutoMDL) - Blender 4+ addon for Source engine MDL compilation workflow. Automatically compiles .blend files to .mdl format when saved in a models folder, with Hammer++ hotloading support. Features automatic material path detection, collision model support, and studiomdl.exe integration.
- [AutoVTF](https://github.com/NvC-DmN-CH/AutoVTF) - C# WinForms tool for working with VTF files. Monitors materials folder and automatically converts updated images (PNG, BMP, TGA, JPG, PSD) to VTF format, preserving VTF settings. Features drag-and-drop conversion, advanced VTF options panel, and Hammer++ hotloading support.
- [StdPatch](https://github.com/kohtep/StdPatch) - StudioMDL Compiler Patcher that removes limitations of the Source Engine models compiler. Allows compiling high-poly models by expanding vertex arrays, weight arrays, and flexcontroller arrays. Includes StdInjector for DLL injection into studiomdl process.
- [3D Studio Max SMD Import Plugin](https://www.moddb.com/games/half-life/downloads/3d-studio-max-smd-import-plug-in-import-smd-mode) - Plugin for 3DS Max 9, 2008, and 2009 to import SMD files from Valve games. Inspired by Cannonfodder's work for 3DS Max 5-7.
- [3D Studio Max SMD Export Plug-in](https://www.moddb.com/games/half-life/downloads/3d-studio-max-smd-export-plug-in) - Plugin for 3DS Max 9, 2008, and 2009 to export Source reference and animation sequence SMD files. Supports Standard and Multi/Sub-Object materials, Editable Mesh and Editable Poly geometry, Skin and Physique modifiers, and helper nodes.
- [Dvondrake's SMD exporter for Blender](https://www.moddb.com/groups/source-developers/downloads/dvondrake-smd-blender) - The first fully-functional Source engine SMD exporter for Blender. Supports reference, physics and animation, and has an accompanying video tutorial.
- [Autodesk Softimage Mod Tool 7.5 (Source Developers)](https://www.moddb.com/groups/source-developers/downloads/autodesk-softimage-mod-tool-75) - (Formerly the XSI Mod Tool) A completely free version of the Autodesk Softimage modelling package. Plugins for Source, CryEngine 2, Unreal Engine 3, XNA, Unity, and more are available.
- [Blender3D SMD Exporter (Half-Life 2)](https://www.moddb.com/games/half-life-2/downloads/blender3d-smd-exporter) - Provides support for Blender3D to export models to the Half-Life 2 SMD format. Supports rigged meshes as well as animations.
- [ValveResourceFormat](https://github.com/ValveResourceFormat/ValveResourceFormat) - Source 2 Viewer is a powerful tool that allows you to browse VPK archives, view, extract, and decompile Source 2 assets, including maps, models, materials, textures, sounds, and more. Also includes C# library for reading and writing Valve Source engine resource files.
- [studiomodel](https://github.com/Galaco/studiomodel) - Go library for loading Valve studiomodel formats (.mdl, .vtx, .vvd).
- [VTFLib](https://github.com/NeilJed/VTFLib) - C/C++ library for reading/writing VTF and VMT texture/material files.
- [source-engine](https://github.com/nillerusr/source-engine) - Modified Source engine (2017) developed by Valve and leaked in 2020. Not for commercial purposes.
- [GtkRadiant](https://github.com/TTimo/GtkRadiant) - Open source, cross-platform level editor for id Tech and Source engine games.
- [Goldsrc Model Viewer (V 0.3a Beta2)](https://www.moddb.com/games/half-life/downloads/goldsrc-model-viewer-v-03a-beta2-archived-for-other-use) - Simple model viewer for GoldSrc engine (Half-Life 1) models. Supports MDL format (v0.3a Beta2, archived). Note: MDL v4 support not yet added.
- [Half Life 2 MDL (v37) Importer V 0.9 Beta for 3DS](https://www.moddb.com/games/half-life-2/downloads/half-life-2-mdl-v37-importer-v-0-9-beta-for-3ds)
- [Jed's Half-Life Model Viewer 1.36](https://www.moddb.com/games/half-life/downloads/jeds-half-life-model-viewer-136) - Modified version of Mete Ciragan's Half-Life Model Viewer 1.25 with support for new Half-Life engine texture features (v1.36).
- [Source Model Viewer [Build: 2019-04-23] (Half-Life 2)](https://www.moddb.com/games/half-life-2/downloads/source-model-viewer-build-2019-04-23)
- [VTF-2-TGA Convertor Utility (Half-Life 2)](https://www.moddb.com/games/half-life-2/downloads/vtf-2-tga-convertor-utility) - Batch converter for VTF files to TGA format.
- [Texture Tool v1.2.1 (Half-Life)](https://www.moddb.com/mods/half-life-episode-two/downloads/texture-tool) - Tool for auto-generating texture flag scripts for the external loader feature in Trinity\Abyss. Useful for flagging hundreds of external high-resolution textures for in-game usage.
- [BSP Decompiler by 005 (Half-Life)](https://www.moddb.com/games/half-life/downloads/bsp-decompiler-by-005) - 005 (created by 005) is a decompiler for most BSP formats. Support may vary between engines. Also supports outputing to many different map editor file formats.
- [Bloody Knife + Addon DB Skin Tutorial (Counter-Strike: Source)](https://www.moddb.com/games/counter-strike-source/downloads/bloody-knife-addon-db-skin-tutorial) - Official tutorial addon with full narrated video tutorial (20+ minutes) on how to modify skins for Source-based games.
- [Bloodlines Character Search Tool v1.0 (Vampire: The Masquerade – Bloodlines)](https://www.moddb.com/games/vampire-the-masquerade-bloodlines/downloads/bloodlines-character-search-tool-v10)
- [Detail Tool v1.0 (Half-Life)](https://www.moddb.com/mods/half-life-episode-two/downloads/detail-tool-v10) - Tool for auto-generating "detailtextures.txt" for the detail file generator used by the Trinity\Abyss engine.
- [Game Server Browser & Admin Tool 1.2.1 (Half-Life 2)](https://www.moddb.com/games/half-life-2/downloads/game-server-browser-admin-tool-1-2-1) - A versatile tool that benefits both gamers and administrators alike.
- [GMad Extractor (Garry's Mod)](https://www.moddb.com/mods/garrys-mod-11-half-life-rebuilt/downloads/gmad-extractor) - A noice, custom, GUI that allows extracting Garry's Mod addon files (.GMA)
- [Half Life 1 Modding Kit Addon 2](https://www.moddb.com/mods/half-life-modding-kit/downloads/half-life-1-modding-kit-addon-2) - Map files and prefabs for Half-Life 1 modding. Includes: M60, Barrett 50 cal, Black Mesa Van, military tanks/trucks, vending machines, computers, and more. Not all tested.
- [Half-Life Asset Manager V3.0.0](https://www.moddb.com/games/half-life/downloads/half-life-asset-manager-v300) - Modeling tool based on Half-Life Model Viewer 2 with many improvements. Best model viewer for Half-Life 1. Note: Only supports Half-Life 1/GoldSource, not Half-Life 2/Source and Source 2 (v3.0.0).
- [Half-Life DLL Decompiler](https://www.moddb.com/games/half-life/downloads/half-life-dll-decompiler) - DLL decompiling tool for pre-Steam CD-retail versions of Half-Life. Source code provided for programmers and developers.
- [Half-Life: Insecure - Mapping Tools and Source Code v1.3](https://www.moddb.com/mods/half-life-insecure/downloads/half-life-insecure-mapping-tools-and-source-code-version-13) - Mapping tools and source code for Half-Life: Insecure mod. Made specifically for the Steam version of Half-Life (v1.3).
- [Half-Life Quick Mod Creation tool](https://www.moddb.com/games/half-life/downloads/half-life-quick-mod-creation-tool) - Quick tool for creating Half-Life mods from scratch. Generates custom liblist.gam and folder structure.
- [Half-Life to Quake 3 .MAP converter](https://www.moddb.com/games/half-life/downloads/half-life-to-quake-3-map-converter) - A small utility for mappers to convert .map output from worldcraft 3.3 to quake3 format, and back.
- [Half-Life Unified SDK Map Decompiler (Counter-Strike)](https://www.moddb.com/games/counter-strike/downloads/half-life-unified-sdk-map-decompiler) - Powerful tool by SamVanheer for decompiling Half-Life 1 BSP version 29 and 30 files. Written in C# for better maintainability and source code accessibility. Also supports original Half-Life and Half-Life Alpha 0.52 BSP files. Features two decompilation strategies (tree-based and face-to-brush) and applies Nodraw texture.
- [Keybinder Source Tool (Counter-Strike: Source)](https://www.moddb.com/games/counter-strike-source/downloads/keybinder-source-tool) - Bilingual (English/German) tool for configuring Counter-Strike: Source. Create or customize config files, bind keys for faster buying, and adjust 30+ graphic settings via simple mouse clicks. Features expert mode and backup functionality.
- [Jed's Half-Life Model Viewer 1.36 (Counter-Strike)](https://www.moddb.com/games/counter-strike/downloads/jeds-half-life-model-viewer-1361) - Model viewer with skin editor and pack viewer functionality for Half-Life models (v1.36).
- [Xash studioMDL Goldsrc Large Model Compiler (Counter-Strike)](https://www.moddb.com/games/counter-strike/downloads/xash-studiomdl-goldsrc-large-model-compiler) - Large model compiler for Half-Life mods supporting models up to 16MB, 9x blending, $texrendermode command, and textures up to 1024x1023.
- [Half-Life Studio Model Decompiler v1.2.1 (Win32, Linux, Mac)](https://www.moddb.com/games/half-life/downloads/half-life-studio-model-decompilerwin32-linux-mac) - Cross-platform Half-Life Studio Model decompiler (Windows, Linux, macOS). Similar to Kratisto's mdldec with improvements: detects texrendermodes, custom activities, Paranoia 2/PrimeXT features, fixed UV-coords and animations, Crowbar-like .qc output.
- [Valve Batch Compile Tool](https://www.moddb.com/engines/source/downloads/valve-batch-compile-tool) - A map compiling manager bringing a breeze to mappers.
- [XSI Valve Source Tools](https://www.moddb.com/downloads/valve-source-tools) - Source engine plugin for Mod Tool 7.5/6 and 32-bit Softimage. Features SMD import/export for models/animations, VMF import/export for Hammer maps, weightmap import/export, skeleton tools, and sample rigs (Valve Biped).
- [Wedge MDL Compiler (QC Generator) 1.0.1](https://www.moddb.com/company/wedge/downloads/wedge-mdl-compiler-qc-generator-1-0-1) - QC Generator and MDL Compiler for quickly creating QC files for model compilation. Russian language only (v1.0.1, registered version only).
- [Windows Vista/7 Phoneme Extractor 1.3](https://www.moddb.com/groups/source-developers/downloads/windows-vista7-phoneme-extractor-13) - A Faceposer phoneme extractor that functions on Windows Vista and 7 (and provides better results than under XP) for Source 2007 and 2009.
- [XSI Mod Tool 6.01](https://www.moddb.com/groups/source-developers/downloads/xsi-mod-tool-601) - A completely free version of the professional Softimage|XSI modelling package. Supports Source, CryEngine 2, Unreal Engine 3, XNA, Unity, and more.

### Unity

- [UABEANext](https://github.com/nesrak1/UABEANext) - Research and modding tool for SerializedFiles and Asset Bundles.
- [AssetStudio (Perfare)](https://github.com/Perfare/AssetStudio) - Tool for exploring, extracting, and exporting assets and assetbundles (original version).
- [AssetStudio (aelurum fork)](https://github.com/aelurum/AssetStudio) - Actively maintained fork with UI optimization and enhancements.
- [AssetStudio (zhangjiequan fork)](https://github.com/zhangjiequan/AssetStudio) - Continuation of Perfare's AssetStudio with support for new Unity versions and additional improvements.
- [UABEA (Unity Asset Bundle Extractor Avalonia)](https://github.com/nesrak1/UABEA) - C# UABE for newer versions of Unity. Cross-platform Unity asset bundle and serialized file editor/extractor built with Avalonia.
- [UnityExplorer](https://github.com/sinai-dev/UnityExplorer) - In-game UI for exploring, debugging, and modifying IL2CPP and Mono Unity games.
- [Unity Asset Editor v0.2 (7 Days To Die)](https://www.moddb.com/games/7-days-to-die/downloads/unity-asset-editor) - Plugin-based asset editor, exporter, and importer for Unity Engine games. Can import and export assets in raw data format and be extended through plugins to support additional asset types (v0.2).
- [Il2CppDumper](https://github.com/Perfare/Il2CppDumper) - Unity IL2CPP reverse engineer tool for extracting IL2CPP metadata and converting IL2CPP binaries.
- [Il2CppInspector](https://github.com/djkaty/Il2CppInspector) - Powerful automated tool for reverse engineering Unity IL2CPP binaries. Outputs IL2CPP type definitions, metadata and method pointers as C# stub code, creates .NET assembly shim DLLs, and generates C++ scaffolding for all types, methods, function pointers and API functions.
- [UnityPy](https://github.com/K0lb3/UnityPy) - Python module that makes it possible to extract/unpack and edit Unity assets.
- [AssetsTools.NET](https://github.com/nesrak1/AssetsTools.NET) - Read and write Unity assets/bundle files, based on UABE.
- [CC3Decrypt](https://github.com/tge-was-taken/CC3Decrypt) - Decrypts Unity asset bundle headers used by Chain Chronicle 3.
- [Unity3DCompressor](https://gitgoon.dev/IllusionMods/Unity3DCompressor) - Utility for compressing Unity asset bundles using LZ4 to reduce file size and improve load times.
- [XUnity.AutoTranslator](https://github.com/bbepis/XUnity.AutoTranslator) - Universal translation framework for Unity games. Supports automatic text translation with various translator backends and IL2CPP support.
- [il2cpp-modder](https://github.com/juanmjacobs/il2cpp-modder) - Generate DLL injection templates for reverse engineering and modding Unity IL2CPP games. Automatically generates code for method hooks, field modifications, and implementation replacements without requiring manual pointer arithmetic.

### Unreal Engine

- [pyUE4Parse](https://github.com/MinshuG/pyUE4Parse) - UE4 asset parser/reader in Python.
- [Unreal-Mappings-Archive](https://github.com/TheNaeem/Unreal-Mappings-Archive) - Archive of Unreal Engine mapping files.
- [io_scene_psk_psa](https://github.com/DarklightGames/io_scene_psk_psa) - Blender addon for importing and exporting PSK (skeletal mesh) and PSA (animation) formats used in Unreal Engine. Supports PSK/PSKX mesh import with vertex normals, extra UV channels, vertex colors, and shape keys.
- [io_scene_ase](https://github.com/DarklightGames/io_scene_ase) - Blender exporter for the legacy ASE (ASCII Scene Export) format used by Unreal Engine 1 & 2 games (e.g., Unreal Tournament 2004).
- [UEViewer (UModel)](https://github.com/gildor2/UEViewer) - Viewer and exporter for Unreal Engine 1-4 assets (UE Viewer).
  - [Compatibility Table](https://www.gildor.org/projects/umodel/compat) - Official compatibility list.
- [UE4Dumper](https://github.com/kp7742/UE4Dumper) - Tool for dumping Unreal Engine 4 assets and structures.
- [UAssetGUI](https://github.com/atenfyr/UAssetGUI) - GUI tool for viewing and editing Unreal Engine UAsset files.
- [blender3d_import_psk_psa](https://github.com/Befzz/blender3d_import_psk_psa) - Blender addon for importing PSK (skeletal mesh) and PSA (animation) formats from Unreal Engine.
- [repak](https://github.com/trumank/repak) - Unreal Engine .pak file library and CLI in Rust.
- [Unreal-Library](https://github.com/EliotVU/Unreal-Library) - Library for reading and writing Unreal Engine file formats.
- [UE4-AES-Key-Extracting-Guide](https://github.com/Cracko298/UE4-AES-Key-Extracting-Guide) - Guide for extracting AES encryption keys from Unreal Engine 4 games.
- [uesave-rs](https://github.com/trumank/uesave-rs) - Rust library for reading and writing Unreal Engine save files.
- [UAssetAPI](https://github.com/atenfyr/UAssetAPI) - Low-level .NET library for reading and writing Unreal Engine game assets.
- [UEFormat](https://github.com/h4lfheart/UEFormat) - Library for working with Unreal Engine file formats.
- [UEAssetToolkit](https://github.com/Archengius/UEAssetToolkit) - Toolkit for extracting and modifying Unreal Engine assets.
- [FModel](https://fmodel.app/) - Open-source software for data-mining UE4-5 games.
- [CUE4Parse](https://github.com/FabianFG/CUE4Parse) - C# Parser for UE archives.
- [UnrealExporter](https://github.com/luk-gg/UnrealExporter) - Batch file exporter.
- [UE-Modding-Tools](https://github.com/Buckminsterfullerene02/UE-Modding-Tools) - Databank of generic UE modding tools.
- [Snooper](https://github.com/FModel/Snooper/tree/opengl) - OpenGL based 3D viewer for cooked UE packages.
- [ActorX Tools](https://www.moddb.com/groups/unreal-tournament-3-mod-developers/downloads/actorx-tools-for-maya-85-3dsmax-9) - The ActorX Tool is a plugin for various 3d creation packages allowing you to import skeletal meshes and animations in Unreal Engine games.
- [ActorX Softimage Exporter](https://www.moddb.com/downloads/actorx-softimage-exporter) - ActorX plugin for Softimage to export skeletal meshes and animations to binary formats (.psk and .psa) for Unreal Editor import. Also exports static meshes to .ase format. Install by extracting to \Application\Plugins.
- [kismet-analyzer](https://github.com/trumank/kismet-analyzer) - Tools for analyzing and manipulating kismet bytecode in cooked Unreal Engine assets. Generates CFG graphs and class hierarchies from blueprint/kismet scripts.
- [BPPseudoCodeGen](https://github.com/Archengius/BPPseudoCodeGen) - Generate C++ pseudo-code from parsed blueprint code.
- [unhood](https://github.com/yole/unhood) - Decompiler for the UnrealEngine 3 version of UnrealScript. Tested with Unreal Tournament 3 and compatible with other UE3 games (Gears of War, Mass Effect, Mirror's Edge, etc.).
- [U3D](https://www.moddb.com/games/unreal-tournament/downloads/u3d-v10-unreal-model-conversion-tool) - Presently there are at least four other unreal model converters out there but as you may know, each one has it's own set of limitations that either make the conversion process a pain in the rear, or plug in to a specific version of 3D StudioMAX.
- [Unreal to Deus Ex mesh converter](https://www.moddb.com/games/deus-ex/downloads/unreal-to-deus-ex-mesh-converter) - Converts Unreal/Unreal Tournament meshes to Deus Ex format. Enables use of Unreal export utilities (MilkShape 3D, 3ds2unr, etc.).
- [DUT TOOL-2.0.2.0 (Unreal Tournament 3)](https://www.moddb.com/mods/defend-unreal-territories/downloads/dut-tool-2020) - C# tool for creating Unreal Tournament 3 mods (v2.0.2.0).
- [UEd Style Tools for Maya (Unreal Tournament)](https://www.moddb.com/games/unreal-tournament/downloads/ued-style-tools-for-maya) - Tool window for Maya providing UEd-style CSG tools and addressing common issues when building meshes/brushes for Unreal Editor maps. Handles size differences between Maya and UEd with fast controls.
- [UShock - Unreal level viewer (Unreal Tournament)](https://www.moddb.com/games/unreal-tournament/downloads/ushock-unreal-level-viewer) - Experimental Unreal level viewer for Unreal Engine games from Unreal 1 to UT2004 (tested: Unreal 1, UT99, WOT, Unreal 2, UT2003, UT2004). Loads dependent packages (textures, static meshes, etc.) and displays using OpenGL renderer.
- [Unreal Unit Converter](https://www.moddb.com/downloads/unreal-unit-converter1)
- [PS3 Mod Tools version 2.1 (Unreal Tournament 3)](https://www.moddb.com/games/unreal-tournament-3/downloads/ps3-mod-tools-version-21) - Tools for publishing Unreal Tournament 3 modifications with PS3 support (v2.1).
- [WOTgreal Package Exporter (Unreal Tournament)](https://www.moddb.com/games/unreal-tournament/downloads/wotgreal-package-exporter) - Tool for viewing and exporting static (non-animated) textures, models, and sounds from Unreal Engine 1/2 games. Also decompiles UC scripts. Created by Dean Harmon.
- [Advanced Model Support SDK (Unreal Tournament)](https://www.moddb.com/mods/ut-skins-voices-mods-fixes/downloads/advanced-model-support-sdk) - Documentation for Unreal Tournament modellers creating plugin player models with Advanced Model Support v102 or v110. Also for modellers and programmers working on larger mods using skeletal models and/or Advanced Model Support code.
- [Blender 2.49 Scripts for UT2004](https://www.moddb.com/games/unreal-tournament-2004/downloads/blender-249-scripts-for-ut2004) - Scripts with all PSA / PSK converters available IQM converter for use with noesis ASE export And other useful stuff
- [February 2015 Unreal Development Kit (UDK)](https://www.moddb.com/engines/unreal-development-kit/downloads/february-2015-unreal-development-kit-udk) - Final version of the UDK by Epic (February 2015 release). Unreal Development Kit is the free edition of Unreal Engine 3.

### CryEngine

- [Far Cry 1 Noesis import plugin](https://www.moddb.com/games/far-cry/downloads/far-cry-1-noesis-import-plugin) - Noesis plugin for importing Far Cry 1 models. Export from Noesis to CryEngine is not supported.
- [Far Cry 1 3dsmax 9 plugin](https://www.moddb.com/games/far-cry/downloads/far-cry-1-3dsmax-9-plugin) - 3DS Max 9 plugin for exporting Far Cry 1 models.
- [CryEngine 2 3d archive](https://www.moddb.com/games/crysis/downloads/cryengine-2-3d-archive) - Archive of CryEngine 2 resources and files useful for creating modifications for Crysis and Crysis Wars.
- [CryENGINE 2 Resources (Crysis)](https://www.moddb.com/games/crysis/downloads/cryengine-2-resources1) - Archive of CryEngine 2 resources and files useful for creating modifications for Crysis and Crysis Wars.
- [CryEngine2 Archive (Crysis)](https://www.moddb.com/games/crysis/downloads/cryengine2-archive) - Archive of CryEngine 2 tutorials in browser-readable format for Crysis modding.
- [Crysis Benchmarking Tool 1.05](https://www.moddb.com/games/crysis/downloads/crysis-benchmarking-tool-1-05) - Robust front-end tool for benchmarking Crysis (v1.05).
- [Cryengine Mod SDK 1.4 (Far Cry)](https://www.moddb.com/games/far-cry/downloads/cryengine-mod-sdk-14) - Official Far Cry 1 SDK released by Crytek (v1.4).
- [Enhanced Gibbed Tools with Hash Decoder (Far Cry 2)](https://www.moddb.com/games/far-cry-2/downloads/enhanced-gibbed-tools-with-hash-decoder) - Modified version of Gibbed's Far Cry 2 tools by Wobatt with hash decoder functionality. Based on original tools by Rick (Gibbed) with additional enhancements. Not officially endorsed by original author.
- [Far Cry 2 Mod Tools](https://www.moddb.com/mods/far-cry-2-redux/downloads/far-cry-2-mod-tools) - Updated version of Far Cry 2 mod tools with additional features and improved compatibility.
- [Far Cry 3 Mod Tools](https://www.moddb.com/mods/far-cry-3-redux/downloads/far-cry-3-mod-tools) - Updated modding tools for Far Cry 3.
- [FCMAP Tool v0.3B-0.5B (Far Cry)](https://www.moddb.com/mods/fcmap-tool/downloads/fcmap-tool-v03b-05b) - 💙 FCMAP is the first automated tool in the world of Far Cry 1 mapping and modding, written by me in Python 3.
- [FCMAP Tool v1.0 (Far Cry)](https://www.moddb.com/mods/fcmap-tool/downloads/fcmap-tool-v05-10) - 💙 FCMAP is the first automated tool in the world of Far Cry 1 mapping and modding, written by me in Python 3.

### Hedgehog Engine

- [HedgeLib](https://github.com/Radfordhound/HedgeLib) - C++ library and collection of tools that aims to make modding games in the Sonic the Hedgehog franchise easier.
- [Hedgehog Engine Blender I/O](https://github.com/hedge-dev/HedgehogEngineBlenderIO) - WIP Blender add-on for Hedgehog Engine I/O including import/export and animation editing.
- [RflTemplates](https://github.com/blueskythlikesclouds/RflTemplates) - 010 Editor binary templates for Hedgehog Engine 2 RFL files.
- [surfboard-templates](https://github.com/DeaTh-G/surfboard-templates) - Templates for various versions of the SWIF file format used primarily in Hedgehog Engine games.
- [HedgehogEngineReversing](https://github.com/WistfulHopes/HedgehogEngineReversing) - BinSync project for Hedgehog Engine reversing.
- [Shadow-the-Hedgehog-.BON-MTN-import-export-tool](https://github.com/Shadowth117/Shadow-the-Hedgehog-.BON-MTN-import-export-tool) - Script for applying external properties from Shadow the Hedgehog .BON files to their respective bones in .DFF model files after importing with AAP's RWIO plugin for 3ds Max.
- [SonicHeroesUTXEditor](https://github.com/Heroes-Hacking-Central/SonicHeroesUTXEditor) - UTX editor for Sonic Heroes.

### Northlight Engine

- [BlenderNorthlight](https://github.com/OpenAWE-Project/BlenderNorthlight) - Blender plugin for loading binmsh/binfbx files from Northlight Engine games (Control, Alan Wake 2, Quantum Break).

### Pragma Engine

- [io_pragma_engine](https://github.com/REDxEYE/io_pragma_engine) - Blender plugin for importing and exporting Pragma Engine models.

### Build Engine

- [BUILD Map Importer](https://github.com/jensnt/io_import_build_map) - Blender add-on for importing BUILD maps (Blood, Duke Nukem 3D, etc.) that can auto-extract textures from `.ART`, `.GRP`, and `.RFF` files.
  - Import options: split sectors/walls/sky, preserve sprite offsets, reuse materials, shade to vertex colors, and store original map data in custom properties.
- [Build palette editing tools (Duke Nukem 3D)](https://www.moddb.com/mods/black-shadow/downloads/build-palette-editing-tools) - Tools for manipulating and creating palettes for BUILD Engine games including Duke Nukem 3D. Work in progress.

### 3DSTATE

- [3DS MAX 5 and 3DS MAX 6 converter](https://www.moddb.com/engines/3dstate/downloads/3ds-max-5-and-3ds-max-6-converter) - Converts 3DS Max scenes to 3DSTATE WLD format, preserving lighting, shadows, and effects. Includes script for rendering to texture and converting to binary 3dstate format.

### AtiSushi Engine

- [AtiSushi](https://github.com/REDxEYE/AtiSushi) - UniLoader plugin for importing AtiSushi engine files.

### Genie Engine

- [geniedoc](https://github.com/aap/geniedoc) - Documentation of Age of Empires II .dat files (Genie Engine formats).

### RPG Maker

- [rgssad](https://github.com/luxrck/rgssad) - Extract rgssad/rgss2a/rgss3a files from RPG Maker games.
- [rpga](https://github.com/elizagamedev/rpga) - RPG archive extraction and creation utility. Can extract and create RPG Maker XP+ archives and Wolf RPG archives (though Wolf archive creation does not work yet).

### Ren'Py

*Visual novel engine used in many indie and commercial visual novels.*

- [unrpa](https://github.com/Lattyware/unrpa) - Program to extract files from the RPA archive format used in Ren'Py visual novels.

### Rawthrills G7 Engine

- [G7Reader](https://github.com/Surasia/G7Reader) - Small utility to read Rawthrills G7 Engine archive files.

### OpenSpace

- [openspace-ps2-extractor](https://github.com/byvar/openspace-ps2-extractor) - Extractor for OpenSpace PS2 archive files.
- [BinarySerializer.OpenSpace](https://github.com/BinarySerializer/BinarySerializer.OpenSpace) - BinarySerializer extension library for serializing OpenSpace game formats.

### Raven Software

#### Heretic II

- [Quake Model to FlexModel Converter](https://www.moddb.com/games/heretic-ii/downloads/quake-model-to-flexmodel-converter-aka-convert) - Converts Quake models to FlexModel format. Preserves vertex placement only (no skeletal structure), suitable for static models, not animated player models.
- [FlexModel to Wavefront Object Converter (FM2OBJ)](https://www.moddb.com/games/heretic-ii/downloads/flexmodel-to-wavefront-object-converter-aka-fm2obj) - Exports Heretic II animation frames (e.g., conjure11, draw5) as 3D meshes in Alias/Wavefront OBJ format. Can export Corvus or Kiera in specific poses, with option to export each mesh node (head, arm, etc.) as separate meshes.
- [Heretic II Toolkit v1.06](https://www.moddb.com/games/heretic-ii/downloads/heretic-ii-toolkit-v106) - Official Heretic II modding toolkit. Usually included with the Heretic II CD, but available for download here (v1.06).

#### Soldier of Fortune

- [Official 3dsmax 3x plugin (Soldier of Fortune)](https://www.moddb.com/games/soldier-of-fortune/downloads/official-3dsmax-3x-plugin) - Official GHOUL exporter for 3DS Max 3.x. Includes Controller for 3D Studio Max (avg_ctrl.dlc), Softimage|3D import plugin, and GHOUL prep program.
- [.m32 to .tga/.adp to .wav file converters (Soldier of Fortune)](https://www.moddb.com/games/soldier-of-fortune/downloads/m32-to-tga-file-converter) - Convert your .m32 (SoF) texture files to manageable .tga texture files with an easy to use GUI. Also includes .adp to .wav for audio conversion. Also includes source code.
- [.m32 tool (Soldier of Fortune)](https://www.moddb.com/games/soldier-of-fortune/downloads/m32-tool) - .m32 tool is a texture conversion utility for Soldier of Fortune. Allows batch conversion of .tga files to .m32.
- [.os script decompiler v2.0 (Soldier of Fortune)](https://www.moddb.com/games/soldier-of-fortune/downloads/os-script-decompiler-v20) - Command line program that tries to convert .os files back into .ds file form.

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

- [Havok IO (Blender)](https://github.com/NewSkyLine-dev/havokmax-blender) - Havok tool for Blender (replaces legacy HavokMax 3ds Max plugin). Blender add-on that imports `.hkx`, `.hkt`, `.hka`, `.igz`, and `.pak` files from Havok XML and binary archives.
  - Capabilities: builds armatures and keyframed actions from animation data, constructs static meshes from geometry blocks, and unwraps PAK/IGZ containers.
- [HavokNoesis](https://github.com/PredatorCZ/HavokNoesis) - Noesis plugin for Havok format.
- [MapEditor](https://github.com/BF3RM/MapEditor) - Realtime map editor mod for Venice Unleashed (Battlefield 3).
- [HavokPreviewToolsBatch2018](https://github.com/asasasasasbc/HavokPreviewToolsBatch2018) - Batch conversion script for Havok Preview Tool 2018 that can automatically convert Havok HKX/HKT files' format.
- [hkxlib](https://github.com/aerisarn/hkxlib) - JAXB parser for editing TAGXML formatted Havok files.
- [hkxEdit](https://github.com/aerisarn/hkxEdit) - Visual editor for Havok 2010.2 files based on hkxlib, written in Java.
- [TagTools](https://github.com/blueskythlikesclouds/TagTools) - Tools for editing Havok 2015/2016 binary tag files. Includes TagTools converter and CollisionConverter for converting rigid bodies to static compound shapes with type and flag tags.
- [FF16-Model-Importer](https://github.com/Nenkai/FF16-Model-Importer) - Tool to export and import Final Fantasy XVI .mdl file binaries as .gltf or .dae.
- [SSE-Fallout-4-Animation-Converter](https://github.com/Backporter/SSE-Fallout-4-Animation-Converter) - Tool to convert animations to PS4 format for Skyrim Special Edition and Fallout 4.

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
- [ARCTool](https://github.com/tpwrules/ARCTool) - Python script to extract RARC, Yaz0, and U8 archives.
- [atirut.bdl](https://github.com/atirut-w/atirut.bdl) - JSYSTEM BMD/BDL model importer for Godot Engine.
- [wsystool](https://github.com/XAYRGA/wsystool) - WAVESYSTEM modification toolkit for JSYSTEM games.
- [jampacked](https://github.com/XAYRGA/jampacked) - BAA unpacker for JSYSTEM games.

### MikuMikuDance

*Freeware animation program and its associated model and motion formats (.pmx, .pmd, .vmd).*

- [MikuMikuLibrary](https://github.com/blueskythlikesclouds/MikuMikuLibrary) - Library for working with MikuMikuDance formats.
- [MMD Tools](https://github.com/MMD-Blender/blender_mmd_tools) - Blender add-on for importing/exporting MikuMikuDance assets. Supports physics, bone constraints, and motion/pose data.
- [MMD Tools Append](https://github.com/MMD-Blender/blender_mmd_tools_append) - Companion extension for MMD Tools that provides material/scene controls, lighting presets, and Rigify helpers.

### RenderWare

*Cross-platform 3D engine and middleware developed by Criterion Games. Powering the Grand Theft Auto trilogy (III, Vice City, San San Andreas), Burnout series, and many other titles.*

- [librw](https://github.com/aap/librw) - Re-implementation of the RenderWare Graphics engine.
- [DragonFF](https://github.com/Parik27/DragonFF) - Blender add-on for RenderWare `.dff` models, `.txd` textures, `.col` collisions, and `.ipl` map data.
- [Blender-3D-RW-Anm-plugin](https://github.com/Psycrow101/Blender-3D-RW-Anm-plugin) - Import and export RenderWare animations (.anm) into Blender 3D.
- [rwio](https://github.com/aap/rwio) - RenderWare import/export plugin for 3ds Max.
- [rwd3d9](https://github.com/aap/rwd3d9) - D3D9 extension of RenderWare for GTA III and Vice City.
- [RenderWareFile](https://github.com/igorseabra4/RenderWareFile) - Library for working with RenderWare binary files.
- [RenderWareNET](https://github.com/Venomalia/RenderWareNET) - Library to work with RenderWare 3 formats.
- [RWIDE2YTYP](https://github.com/Hancapo/RWIDE2YTYP) - RenderWare .IDE to Five .YTYP and NY .IDE converter.

### CRI

*CRI Middleware formats (CPK archives, ADX audio, etc.) used in many Japanese games across multiple platforms.*

- [CriPakTools](https://github.com/esperknight/CriPakTools) - Tools for extracting and repacking CRI CPK archives used in many Japanese games.
- [CriPakTools (GUI)](https://github.com/wmltogether/CriPakTools) - GUI version of CriPakTools with additional features including Shift-JIS support, 2GB+ CPK support for PS3, batch mode, compression support, and improved CPK header handling.
- [Universal-CPK-Mod-Installer](https://github.com/PTKay/Universal-CPK-Mod-Installer) - Universal installer for CPK mod files.
- [CriFsV2Lib](https://github.com/Sewer56/CriFsV2Lib) - Library for working with CRI FileSystem V2 archives.
- [AfsLib](https://github.com/Sewer56/AfsLib) - Simple, relatively fast library for reading and writing CRIWare AFS archives.
- [AfsBatch](https://github.com/tge-was-taken/AfsBatch) - Batch AFS packer. Packs each subdirectory in a given directory into an AFS file of the same name.
- [PyCriCodecs](https://github.com/Youjose/PyCriCodecs) - Python frontend for CRI codec tools.

### XNA

*Microsoft XNA Framework model format used in various Xbox 360 and PC games.*

- [blender_xna](https://github.com/REDxEYE/blender_xna) - Blender import plugin for XNA model formats.

### Sappy (GBA Audio)

*SDK-provided formats for the Game Boy Advance sound engine. Used in [Pokémon Gen III](#gen-iii) and many other GBA titles.*

- [gba-mus-ripper](https://github.com/berg8793/gba-mus-ripper) - GBA music ripper.
- [SapPy](https://github.com/mayhaps-perchance/SapPy) - Python-based GBA sound tool.
- [agbplay](https://github.com/ipatix/agbplay) - Music player and music ripper for GBA.
- [sappy](https://github.com/maddievision/sappy) - GBA sound tool.
- [Sappy (Touched)](https://github.com/Touched/Sappy) - Fork with additional features.
- [shinen-gax-python](https://github.com/beanieaxolotl/shinen-gax-python) - Python tools for Shin'en Multimedia's GAX Sound Engine used in Game Boy Advance games. Includes conversion, unpacking, waveform dumping, and song rendering tools. Also supports NAX Sound Engine format.
- [gsfopt](https://github.com/loveemu/gsfopt) - GSF (GBA Sound Format) optimizer tool. Optimizes GSF sets by removing unused code/data, converts minigsfs/gsflibs to single GSF files, and includes timing functionality for auto-tagging.
- [saptapper](https://github.com/loveemu/saptapper) - Automated GSF ripper for Game Boy Advance games using the Sappy driver. Extracts music from GBA ROMs automatically.
- [deadbeef_GSFdecoder](https://github.com/joshbarrass/deadbeef_GSFdecoder) - GSF decoder plugin for DeaDBeeF media player. Enables playback of GSF (GBA Sound Format) files in DeaDBeeF, based on viogsf/VBA-M.

## Game & Studio Tools

### Activision / Infinity Ward / Treyarch

#### Call of Duty

- [Tyrant](https://github.com/Scobalula/Tyrant) - RE Engine asset extractor for Call of Duty file formats.
- [ShibaInu](https://github.com/Scobalula/ShibaInu) - Weapon file converter for Call of Duty Mod Tools.
- [iwd-tool](https://github.com/ZoneTool/iwd-tool) - Command-line tool for generating IWD files for Call of Duty.
- [lui-tool](https://github.com/xensik/lui-tool) - Utility to assemble and disassemble IW engine UI scripts. Supports Call of Duty: Ghosts (IW6).
- [blender-cod](https://github.com/CoDEmanX/blender-cod) - Blender add-on for Call of Duty modding.
- [WraithXArchon](https://github.com/dtzxporter/WraithXArchon/) - Legendary Call of Duty asset extraction tool.
- [Cordycep](https://github.com/Scobalula/Cordycep) - Tool that utilizes modified game executables to load fast files for Call of Duty.
- [zonebuilder](https://github.com/RagdollPhysics/zonebuilder) - Fastfile generator for IW4 (Modern Warfare 2).
- [IWI DDS Fast Converter V1.40 (Call of Duty 2)](https://www.moddb.com/games/call-of-duty-2/downloads/iwi-dds-fast-converter-v140)
- [x to xmodel_export converter 1.6 cod5 Version (Call of Duty: World at War)](https://www.moddb.com/games/call-of-duty-world-at-war/downloads/x-to-xmodel-exporter-converter-16-cod5-version) - Converter for DirectX (*.x) and Wavefront Object (*.obj) files to Call of Duty: World at War xmodel_export format. Converted files can then be converted to xmodel using the Asset Manager. Place xconv.exe in CoD5 directory and run (v1.6).
- [iw4-open-formats](https://github.com/iw4x/iw4-open-formats/blob/main/src/iw4-of/assets/assets.cpp) - Asset conversion system for MW2 formats.
- [BSP Decompiler (Call of Duty)](https://www.moddb.com/games/call-of-duty/downloads/bsp-decompiler) - Hereby we release our decompiler and the sources. May it prove to be useful for you or your team.
- [gsc-asm](https://github.com/ZoneTool/gsc-asm) - GSC assembler/disassembler for IW5 (Call of Duty: Modern Warfare 3).
- [Call of Duty 1 Milkshape plugins](https://www.moddb.com/games/call-of-duty/downloads/call-of-duty-1-milkshape-plugins) - Series of Milkshape plugins for Call of Duty 1. Created by scorpiomidget.
- [Call of Duty 1 Mod Tools No Installer Version](https://www.moddb.com/games/call-of-duty/downloads/call-of-duty-1-mod-tools-no-installer-version) - Alternative version for users experiencing installation issues with the official installer, typically caused by missing or corrupt game registry entries.
- [Call of Duty 2 Mod Tools](https://www.moddb.com/games/call-of-duty-2/downloads/call-of-duty-2-mod-tools) - Official modding tools for Call of Duty 2.
- [Call of Duty 2 Mod Tools No Installer](https://www.moddb.com/games/call-of-duty-2/downloads/call-of-duty-2-mod-tools-no-installer) - Alternative version for users experiencing installation issues with the official installer, typically caused by missing or corrupt game registry entries.
- [Call of Duty 4 Mod Tools (SDK)](https://www.moddb.com/games/call-of-duty-4-modern-warfare/downloads/call-of-duty-4-mod-tools-sdk) - The official SDK from Infinity Ward. Now the real mod'ing will begin.
- [Iwi Converter (Call of Duty 2)](https://www.moddb.com/games/call-of-duty-2/downloads/iwi-converter) - IWI converter with multi-file selection support for Call of Duty 2. Created to address lack of multi-select support in other IWI converters.
- [KV Map Converter v2 Beta2 (Call of Duty 4: Modern Warfare)](https://www.moddb.com/games/call-of-duty-4-modern-warfare/downloads/kv-map-converter-v2-beta2) - Utility by KillerVirus for converting Source Engine maps to Call of Duty 4: Modern Warfare format (v2 Beta2).

#### Tony Hawk's Pro Skater

- [WAD Tool v1.0 (Tony Hawk's Pro Skater)](https://www.moddb.com/games/tony-hawks-pro-skater/downloads/wad-tool-v10) - A small tool to build and extract WAD files from early thps-engine based games.
- [C2M](https://github.com/sheilan102/C2M) - Tool to export maps from Call of Duty games.
- [TOXEC (The Obj to Xmodel Export Converter)](https://www.moddb.com/games/call-of-duty-world-at-war/downloads/toxec-the-obj-to-xmodel-export-converter) - Converter for OBJ files to Xmodel format. For use with Call of Duty 4 and Call of Duty: World at War mapping.
- [DDS/IWI Converter 1.5 (Call of Duty 2)](https://www.moddb.com/games/call-of-duty-2/downloads/dds-iwi-converter-1-5)

#### Ghostbusters

- [Gibbed.Ghostbusters](https://github.com/gibbed/Gibbed.Ghostbusters) - Tools and code for use with Ghostbusters: The Video Game (2009).

#### A Series of Unfortunate Events

- [resPack](https://github.com/XAYRGA/resPack) - Extractor for Xbox A Series of Unfortunate Events archive files.

### Angel Matrix

- [noclip.website (Neon White)](https://github.com/magcius/noclip.website/tree/main/src/NeonWhite) - In-browser Neon White viewer.

### Angel Studios / Rockstar San Diego

- [GTAVHandlingEditor](https://github.com/ikt32/GTAVHandlingEditor) - Real-time handling editor for Grand Theft Auto V.

### Anthony Bongers

- [GhostsAndGraves (decomp)](https://github.com/AnthonyBongers/GhostsAndGraves) - Matching decompilation of Ghosts And Graves (NES, 100%).
- [gta5-nativedb-data](https://github.com/alloc8or/gta5-nativedb-data) - Native function database for Grand Theft Auto V.
- [AngelStudiosBlenderAddon](https://github.com/Dummiesman/AngelStudiosBlenderAddon) - Blender add-on that handles several formats used in Angel Studios/Rockstar San Diego games from ~1999-2006. Supports multiple formats (BMS, DLP, MOD/XMOD, BND, SKEL, GEO) used in Midnight Club 2, Midtown Madness 1, and other titles.
- [MidnightClub2 (Noesis)](https://himeworks.com/noesis-plugins/) - Noesis plugin for Midnight Club 2 model formats.
- [Sollumz](https://github.com/Hancapo/Sollumz) - Blender plugin to import CodeWalker converter XML files from GTA V. GTA V modding suite for Blender (RAGE engine formats). [Documentation here](https://docs.sollumz.org).
- [pyrpfiv](https://github.com/gmroder/pyrpfiv) - Python library for parsing and manipulating GTA IV's RPF (Resource Package Format) archives. Supports file extraction, modification, and encrypted TOC handling.
- [noclip.website (Grand Theft Auto III)](https://github.com/magcius/noclip.website/tree/main/src/GrandTheftAuto3) - In-browser Grand Theft Auto III viewer.
- [openrw](https://github.com/rwengine/openrw) - Open source recreation of the classic Grand Theft Auto III game executable (Open ReWrite).
- [noclip.website (Grand Theft Auto: Vice City)](https://github.com/magcius/noclip.website/tree/main/src/GrandTheftAuto3) - In-browser Grand Theft Auto: Vice City viewer.
- [noclip.website (Grand Theft Auto: San Andreas)](https://github.com/magcius/noclip.website/tree/main/src/GrandTheftAuto3) - In-browser Grand Theft Auto: San Andreas viewer.
- [MidtownExtractor](https://github.com/0x1F9F1/MidtownExtractor) - Midtown Madness 1/2 and Midnight Club 2 file extractor.
- [RGLExtractor](https://github.com/Disquse/RGLExtractor) - Tool for extracting content from Rockstar Games Launcher RAGE packfiles (currently just Launcher.rpf). Uses RPF7 format with different AES encryption key.
- [MeltyTool](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/AngelStudios) - Multitool for viewing/extracting assets from various N64/GCN/3DS/PC games en-masse.
- [CLEO library v2.0.0.5 by Seemann (Grand Theft Auto III)](https://www.moddb.com/games/grand-theft-auto-3/downloads/cleo-library-by-seemann-for-gta-iii) - Welcome to the CLEO library (or simply CLEO) - a hugely popular extensible plugin for the Grand Theft Auto games series by Rockstar Games, allowing the use of thousands of unique mods which change or expand the gameplay. There are different versions of CLEO made for GTA III, GTA Vice City and GTA...
- [CLEO library v2.0.0.5 by Seemann (Grand Theft Auto: Vice City)](https://www.moddb.com/games/grand-theft-auto-vice-city/downloads/cleo-library-v2005-by-seemann-for-gta-vc) - Welcome to the CLEO library (or simply CLEO) - a hugely popular extensible plugin for the Grand Theft Auto games series by Rockstar Games, allowing the use of thousands of unique mods which change or expand the gameplay. There are different versions of CLEO made for GTA III, GTA Vice City and GTA...
- [CLEO library v4.3.22 by Seemann (Grand Theft Auto: San Andreas)](https://www.moddb.com/games/grand-theft-auto-san-andreas/downloads/cleo-library-v4322-by-seemann-for-gta-sa) - Welcome to the CLEO library (or simply CLEO) - a hugely popular extensible plugin for the Grand Theft Auto games series by Rockstar Games, allowing the use of thousands of unique mods which change or expand the gameplay. There are different versions of CLEO made for GTA III, GTA Vice City and GTA...
- [Epic GTA2 Script Decompiler Source Code (Grand Theft Auto 2)](https://www.moddb.com/games/grand-theft-auto-2/downloads/epic-gta2-script-decompiler-source-code) - Source code for the Epic GTA2 Script Decompiler included with Epic's level editor. Created by T.M.
- [GMP/STY file format descriptions (Grand Theft Auto 2)](https://www.moddb.com/games/grand-theft-auto-2/downloads/gmpsty-file-format-descriptions) - Official file format documentation for GMP and STY files in Grand Theft Auto 2. Created by DMA Design.
- [GTA Font compiler (Grand Theft Auto)](https://www.moddb.com/games/grand-theft-auto/downloads/gta-font-compiler) - Tool for viewing, creating, and editing Grand Theft Auto 1 font files. Can also view other hidden game content.
- [GTA V Suspend Resume tool (Grand Theft Auto V)](https://www.moddb.com/games/grand-theft-auto-v/downloads/gta-v-suspend-resume-tool)
- [IMG Tool v1.3 (Grand Theft Auto III)](https://www.moddb.com/games/grand-theft-auto-3/downloads/iii-img-tool-v13)
- [IMG Tool 2.0 (Grand Theft Auto: San Andreas)](https://www.moddb.com/games/grand-theft-auto-san-andreas/downloads/img-tool-20) - Tool for working with GTA3.img archive files from Grand Theft Auto 3, Vice City, and San Andreas. Required for installing modifications such as cars, skins, weapons, and other game assets (v2.0).

### Ape, Inc

- [earthbound-script-dumper](https://github.com/CataLatas/earthbound-script-dumper) - EarthBound text script dumper.
- [ebtexted](https://github.com/PKHackers/ebtexted) - Tomato's EarthBound text editor.
- [EBME](https://github.com/Supremekirb/EBME) - GUI editor for EarthBound's overworld areas.
- [ebbinex](https://github.com/Herringway/ebbinex) - Simple utility for extracting data from Earthbound ROM files.

### Arrowhead Game Studios

- [helldivers2-rs](https://github.com/nblockbuster/helldivers2-rs) - Work-in-progress tool to extract files from Helldivers 2.

### 11 bit studios

- [Frostract - Frostpunk idx and dat unpacker](https://www.moddb.com/games/frostpunk/downloads/frostract-frostpunk-idx-and-dat-unpacker)

### Avalanche Studios

- [ApexPredator](https://github.com/REDxEYE/ApexPredator) - Tool/library for reading Apex Engine assets. Currently supports Generation Zero. Written in C++.

### Remedy Entertainment

#### Max Payne

- [Game Levels Importing plugin for Maya (Max Payne)](https://www.moddb.com/games/max-payne/downloads/game-levels-importing-plugin-for-maya)
- [MAX-FX Tools (Max Payne)](https://www.moddb.com/games/max-payne/downloads/max-fx-tools) - Official modding package for Max Payne 1. Tools are not included with the Steam version, so they are provided here.
- [Max Payne 1-2 Packer](https://www.moddb.com/games/max-payne-2/downloads/max-payne-1-2-packer) - For guys who don't wanna write bat-file for RasMaker
- [MaxPayne Toolset](https://www.moddb.com/games/max-payne/downloads/maxpayne-toolset) - Max Payne Toolset to pack/extract Mod/RAS Files for Max Payne 1/2. And extracting Textures from LDB Files.
- [Mod Tools (Max Payne 2)](https://www.moddb.com/games/max-payne-2/downloads/mod-tools) - Official toolset for creating mods, levels, and custom content for Max Payne 2.

### Argonaut Games

- [croc (decomp)](https://github.com/xeeynamo/croc) - Matching decompilation of Croc: Legend of the Gobbos.
- [PS1-BRender-Reverse](https://github.com/OverSurge/PS1-Argonaut-Reverse) - Reverse engineering tools for PlayStation 1 BRender engine games like Harry Potter and Croc 2.
- [Stratigise](https://github.com/Argonaut-PS1-Reverse/Stratigise) - WIP tool for disassembling and (re)assembling ASL binaries for Croc 1.
- [CrocUtils](https://github.com/Rexhunter99/CrocUtils) - Utilities for Croc game file formats.

### Arkane Studios

- [Arx Fatalis .PAK unpacker](https://www.moddb.com/games/arx-fatalis/downloads/arx-fatalis-pak-unpacker-v13) - Tool for unpacking PAK files from Arx Fatalis. Includes source code. Created by CTPAX-X Team (v1.3).
- [disrev](https://github.com/chipolux/disrev) - Python tools for extracting and modifying Dishonored 2 assets.
- [dishonored2_scripts](https://github.com/usernametoolo/dishonored2_scripts/blob/master/tools/scripts/unpack_resources.py) - Resource extraction script for unpacking .pak archives.
- [Obscura](https://github.com/Mikompilation/Obscura) - Modding toolkit for Dishonored games.
- [Field Editor 0.5.1 Tautologist tool (Dishonored)](https://www.moddb.com/games/dishonored/downloads/field-editor-051-tautologist-tool) - Field editor for Dishonored with improved menu system, keyboard shortcuts, auto-completing text boxes, additional grouping and fields, live filtering/searching, settings persistence, and XML file browsing (v0.5.1).

### Atlus

- [Amicitia](https://github.com/tge-was-taken/Amicitia) - Tool for working with Persona 3/4/5 file formats.
- [yafe](https://github.com/tge-was-taken/yafe) - Field editor for Persona 5 allowing import of FBN and HBN files into 3ds Max for visual editing.
- [P5X_vFileContentExtract](https://github.com/DeathChaos25/P5X_vFileContentExtract) - Content extractor for Persona 5 X vFile archives.
- [DDS3-Model-Studio](https://github.com/tge-was-taken/DDS3-Model-Studio) - WIP Model editing tools for DDS3 engine based SMT games (SMT: Nocturne, DDS 1 & 2, Raidou 1 & 2).
- [AtlusFileSystemLibrary](https://github.com/tge-was-taken/AtlusFileSystemLibrary) - Library containing utilities for working with file systems used in Atlus games.
- [Atlus-Script-Tools](https://github.com/tge-was-taken/Atlus-Script-Tools) - Set of tools for working with Atlus script formats including flow script files (.bf) and message script files (.bmd, .bm2). Supports Persona series, SMT series, Catherine, Trauma Center, and more.
- [AtlusPM1MessageScriptEditor](https://github.com/tge-was-taken/AtlusPM1MessageScriptEditor) - Message script editor for Persona 1.
- [GFD-Studio](https://github.com/tge-was-taken/GFD-Studio) - Model editor for viewing, editing and converting models in GMD/GFS format used in P3D, P4D, P5D, and Persona 5.
- [EvtTool](https://github.com/tge-was-taken/EvtTool) - Persona 5 (Royal) EVT file editor. Converts EVT/ECS/LSD files to JSON and vice versa.
- [SMT1L1ON](https://github.com/tge-was-taken/SMT1L1ON) - Translation tools for Shin Megami Tensei 1.
- [P5RFieldTexUtility](https://github.com/ShrineFox/P5RFieldTexUtility) - Utility for quickly extracting field textures and duplicating edits in Persona 5 Royal. Supports batch extraction and repacking of .BIN files with DDS texture support.
- [EPLGen](https://github.com/ShrineFox/EPLGen) - GUI for quickly generating EPL leafs featuring animated sprites for Persona 5 Royal. Supports particle effect creation with DDS textures and GMD file integration.
- [p5s-txteditor](https://github.com/samudebug/p5s-txteditor) - Text editor for editing text files found in Persona 5 Strikers.
- [smt1dasm](https://github.com/spannerisms/smt1dasm) - Disassembly of Shin Megami Tensei J1.0 for the SNES.
- [p4u2modtools](https://github.com/zarroboogs/p4u2modtools) - Modding tools for Persona 4 Arena Ultimax, Persona 4 Arena, etc. Includes bddata.bin extraction tools and custom game update creation.
- [P5CharacterSwapper](https://github.com/ShrineFox/P5CharacterSwapper) - Batch-replaces P5 character models/animations by ID. Can retarget models and animations if specified.
- [PersonaRandomizer](https://github.com/ShrineFox/PersonaRandomizer) - Program for quickly randomizing files in Persona 3 FES, Persona 4, and Persona 5. Supports randomizing various TBL files including PERSONA, UNIT, SKILL, ITEM, NAME, and ENCOUNT tables.
- [AemulusModManager](https://github.com/TekkaGB/AemulusModManager) - Mod package manager for Persona 4 Golden (PC), Persona 3 FES, Persona 5, and Persona 5 Strikers. Automatically merges conflicting bin, bmd, pm1, bf, and tbl files from different mods.
- [p4g-saveconv](https://github.com/zarroboogs/p4g-saveconv) - Persona 4 Golden save converter. Converts PS Vita saves to PC format and vice versa, including data00XX.bin, system.bin, and sdslot.dat files.
- [p5-rte](https://github.com/TheHiddenHour/p5-rte) - Real-time editing tool for Persona 5 on jailbroken PS3. Allows editing of persona slots, stats, and skills using PS3Lib.
- [GMDTool](https://github.com/lemoncove/GMDTool) - Command-line utility to convert Persona .GMD model files to Collada .DAE format. Uses GFDLibrary for GMD loading.

### Asobo Studio

- [fmtk](https://github.com/widberg/fmtk) - FUEL Modding Toolkit.
- [ImZouna](https://github.com/widberg/ImZouna) - ImHex patterns for Zouna data structures used in Asobo Studio games (FUEL, WALL-E, Ratatouille, Toy Story 3, A Plague Tale series, Microsoft Flight Simulator, and more).

### Black Element Software

- [Alpha Prime RES Unpacker](https://www.moddb.com/mods/alpha-prime-dominus-prime/downloads/alpha-prime-res-unpacker-modding-tool) - Modding Tool for opening the .RES files for the "data00.res" and "data01.res" in Alpha Prime.

### Bandai Namco

- [kl2_lv_decomp (decomp)](https://github.com/entriphy/kl2_lv_decomp) - Matching decompilation of Klonoa 2: Lunatea's Veil (PS2).
- [Dragon-Ball-Legends (decomp)](https://github.com/GodkuHacking/Dragon-Ball-Legends) - Matching decompilation of Dragon Ball Legends (Android APK).
- [SoulCalibur2-game-unpacker](https://github.com/PS2Homebrew-arcade/SoulCalibur2-game-unpacker) - Unpacker for Soul Calibur 2 game files.
- [BinarySerializer.Klonoa](https://github.com/BinarySerializer/BinarySerializer.Klonoa) - Serializer for Klonoa games.
- [TalesOfFantasy (Noesis)](https://himeworks.com/noesis-plugins/) - Noesis plugins for Tales series.
- [ARC](https://github.com/Bigchillghost/ARC) - Animation Recipe Cracker for Bandai Namco games.
- [MBTL.BIN.Tool](https://github.com/Ekey/MBTL.BIN.Tool) - Tool for extracting BIN archives from MELTY BLOOD: TYPE LUMINA.
- [RRUnpacker](https://github.com/Nenkai/RRUnpacker) - Unpacker for Ridge Racer PSP/6/7/PS Vita and Go Vacation .DAT files. Supports extraction of all files including custom compressed ones.
- [BBFSUnpacker](https://github.com/Nenkai/BBFSUnpacker) - Extraction tool for Ridge Racer Drifttopia files.
- [ggst_collision_editor_rs](https://github.com/WistfulHopes/ggst_collision_editor_rs) - Collision editor for Guilty Gear Strive.
- [noclip.website (Klonoa)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Klonoa viewer.
- [noclip.website (Katamari Damacy)](https://github.com/magcius/noclip.website/tree/main/src/KatamariDamacy) - In-browser Katamari Damacy viewer.

### Electronic Arts

- [EA-Graphics-Manager](https://github.com/bartlomiejduda/EA-Graphics-Manager) - Handles FSH, SSH, XSH, PSH, GSH, ASH, QFS and MSH files from EA games. Parse, preview, and export/import graphics as DDS/PNG/BMP.
  - Games: FIFA series (97, 2000, 06, 09, 14, Street, UEFA Euro 2004), Need For Speed series (1994, II, High Stakes, Hot Pursuit 2, Porsche Unleashed, Carbon, Undercover), Medal of Honor series (Frontline, Rising Sun, Vanguard, European Assault), Madden NFL (06, 08), NHL series (2001, 2002, 2005, 07), NBA Live 97, MVP Baseball/NCAA Baseball (2005, 2007), SSX series, Cricket (2005, 2007), Harry Potter (Chamber of Secrets, Quidditch World Cup), Def Jam: Fight For New York, Fight Night Round 3, GoldenEye, SimCity 4 Deluxe, Triple Play 2000, ReBoot, F.A. Premier League Football Manager 2000, EA Playground (Wii), and more across PS1, PS2, PSP, PC, Xbox, Wii, and Zeebo platforms.
- [EA-Font-Manager](https://github.com/bartlomiejduda/EA-Font-Manager) - Handles EA font files (FFN, PFN, XFN, MFN, SFN formats). Preview, decode flags, edit character tables, and convert font images.
  - Games: FIFA 97, Need for Speed series (2, High Stakes, Hot Pursuit, Undercover), NBA Live 06-07, SSX series, MVP Baseball 2005, Medal of Honor: European Assault,
  NHL series, Def Jam: Fight for NY, Harry Potter and the Chamber of Secrets, The Sims, and more.
- [EA-Loc-Manager](https://github.com/bartlomiejduda/EA-Loc-Manager) - Extract and import localization files (LOC format) from EA games. Supports UTF-8, UTF-16, and Latin-1 encodings.
  - Games: Harry Potter and the Chamber of Secrets (PS2), Medal of Honor: European Assault (Xbox), SSX On Tour, SSX Tricky (PS2), NHL 07 (PSP), and more.

#### SSX

- [ssx (decomp)](https://github.com/ssxdecomp/ssx) - Matching decompilation of SSX (2000).
- [ssx3 (decomp)](https://github.com/ssxdecomp/ssx3) - Matching decompilation of SSX 3 (2003).
- [ssxdvd (decomp)](https://github.com/ssxdecomp/ssxdvd) - Matching decompilation of SSX Tricky (2001).

### EA DICE

- [Frostbite-Scripts](https://github.com/NicknineTheEagle/Frostbite-Scripts) - Scripts and tools for Frostbite engine games.
- [libbndl](https://github.com/Bo98/libbndl) - Library for reading BUNDLE archives used in Burnout Paradise.

#### Battlefield Series

- [BF1942 3dsmax 8 plugin](https://www.moddb.com/games/battlefield-1942/downloads/bf1942-3dsmax-8-plugin) - Plugin for 3DS Max 8 to import/export Battlefield 1942 meshes and animations. Extracted from the Battlefield Mod Development Toolkit 1.0B by DICE.
- [BF2 Maya 4-6 Tools](https://www.moddb.com/games/battlefield-2/downloads/bf2-maya-4-6-tools) - Official Battlefield 2 tools for Maya 4-6 for exporting and importing game assets. Also included with the BF2 Editor but provided separately here.
- [BF42 3dsMax plugins 2.762](https://www.moddb.com/mods/battlefield-2-play-for-free-mod/downloads/bf42-3dsmax-plugins-2762) - 3DS Max plugins for Battlefield 2/1942 for Max 9 and higher (v2.762).
- [BGF Heightmap Converter](https://www.moddb.com/games/battlefield-2/downloads/bgf-heightmap-converter-utility) - Utility for viewing and resizing heightmap (.RAW) files. Primarily intended for converting maps from Battlefield 1942 or Battlefield Vietnam to Battlefield 2, but can also be used to change a BF2 map to a different size.
- [DDS Viewer Plugin (Battlefield Vietnam)](https://www.moddb.com/games/battlefield-vietnam/downloads/dds-viewer-plugin) - Plugin for previewing DDS files in folder preview window before conversion. Useful for mappers and modders.
- [NVIDIA DDS Utilities (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/nvidia-dds-utilities) - Collection of utilities for manipulating DDS image files: nvDXT (command-line binary), detach (extracts MIP levels), stitch (recombines MIP levels), and readDXT (reads compressed images).
- [NVIDIA Texture Atlas Tool (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/nvidia-texture-atlas-tool) - A collection of tools for creating texture atlases, which can help to increase batch sizes.
- [POE2 3DS Max 6-8 BF2 Tools (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/poe2-3ds-max-6-8-tools) - POE2's advanced rendition of the 3DS Max BF2 tools (for Max 6-8).
- [POE2 3DS Max 9 BF2 Tools (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/poe2-3ds-max-9-bf2-tools) - POE2's advanced rendition of the 3DS Max BF2 tools (for Max 9).
- [Windows Texture Viewer v089b (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/windows-texture-viewer-v089b) - Tool for viewing .dds texture files. Shows resolution, DDS format, mipmap count, and alpha channel used by HUD.
- [Texture Tool 0.2 (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/texture-tool-0-2) - Ecomap that automates the texturing of BF2 maps.
- [Clan Tool (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/clan-tool) - Advanced Tactical Center for Battlefield 2. Connect team members to online sessions, create detailed tactics together in real time. Includes zoom, text tools, export tactics, and Custom Map Wizard.
- [Dragon UnPACKer (Battlefield 2)](https://www.moddb.com/games/battlefield-2/downloads/dragon-unpacker) - Tool for viewing and extracting files from game archive formats (e.g., Quake 2 PAK files). Includes HyperRipper for scanning files for known formats (MP3, OGG, WAV, AVI, TGA, BMP, etc.).

#### Star Wars: Battlefront

- [StarWars Battlefront unpacker / decoder](https://www.moddb.com/games/star-wars-battlefront/downloads/starwars-battlefront-unpacker-decoder) - Custom toolset for unpacking and extracting Star Wars: Battlefront archives.
- [Star Wars: Battlefront Modification Tools](https://www.moddb.com/games/star-wars-battlefront/downloads/star-wars-battlefront-modification-tools) - Official modding tools for creating levels in Star Wars: Battlefront. Originally from Game Front. Download subject to End User License Agreement terms.
- [3D Object Converter (Star Wars Battlefront II)](https://www.moddb.com/games/star-wars-battlefront-ii/downloads/3d-object-converter) - Polygon-based 3D object file format converter supporting 440 file formats.

### EgoSoft

- [X4Tools](https://github.com/REDxEYE/X4Tools) - Standalone plugin for importing and exporting assets from X4 game.

### Capcom

#### RE Engine

- [REE.PAK.Tool](https://github.com/Ekey/REE.PAK.Tool) - Tools for extracting and repacking PAK archives from games based on RE ENGINE.
- [RE-Engine-VSDF-Template](https://github.com/Silvris/RE-Engine-VSDF-Template) - Template for RE Engine VSDF files.

#### Resident Evil

- [BioHazard File Archive Tool (Resident Evil 4)](https://www.moddb.com/games/resident-evil-4/downloads/biohazard-file-archive-tool) - File archive tool for Resident Evil 4. Two versions available: one designed for Windows XP, another ported for Windows 7. Both are 32-bit but work on 64-bit systems. Windows 7 version is backwards compatible with XP.

#### Monster Hunter

- [mh1j (decomp)](https://github.com/2Tie/mh1j) - Matching decompilation of Monster Hunter (PS2, Japanese release).
- [mhst2-arc-tool](https://github.com/Fexty12573/mhst2-arc-tool) - Archive tool for Monster Hunter Stories 2.
- [MHW-Research](https://github.com/TheCrazyT/MHW-Research) - Research and tools for Monster Hunter: World file formats.
- [MHST2-Save-Tools](https://github.com/AsteriskAmpersand/MHST2-Save-Tools) - Save file tools for Monster Hunter Stories 2.
- [Mod3-MHW-Importer](https://github.com/AsteriskAmpersand/Mod3-MHW-Importer) - Blender Import-Exporter for Monster Hunter World Mod3 model format.
- [RingingBloom](https://github.com/Silvris/RingingBloom) - WWise audio editing toolkit for Monster Hunter: World and other Capcom titles.
- [GFDConverter](https://github.com/onepiecefreak3/GFDConverter) - Converts GFD (v1) to GFD (v2) from Capcom's MT Framework.
- [GMDConverter](https://github.com/onepiecefreak3/GMDConverter) - Converter for the GMD file format from Capcom's MT Framework. Supports Version 1 and Version 2.
  - Features: BNK Editor (soundbanks), PCK Editor (packages), Loop Calculator, WEM Creator, WWCT/WWBK/WWPK/EPVSP editors.
  - Formats: .nbnk/.bnk, .npck/.pck, .wwct, .wwbk/.wwpk, .epvsp, .wem.

#### Devil May Cry

- [dmc_hd_tools](https://github.com/Kerilk/dmc_hd_tools) - Toolkit for Devil May Cry HD Collection including Noesis plugins and binary templates.

#### Street Fighter

- [3s-decomp (decomp)](https://github.com/crowded-street/3s-decomp) - Matching decompilation of Street Fighter III: 3rd Strike (PS2).

#### Ultimate Marvel vs Capcom 3

- [umvc3-tools](https://github.com/tge-was-taken/umvc3-tools) - Ultimate Marvel vs Capcom 3 tools and research. Includes MT Framework Model (MOD) import/export plugin for 3ds Max, Texture (TEX) converter, Material (MTL) converter, and binary templates.
- [ThreeWorkTool](https://github.com/EternalYoshi/ThreeWorkTool) - GUI tool for managing MT .arc files in Ultimate Marvel vs Capcom 3. Supports DDS texture imports, character animation keyframe import/exports, and archive file management.

#### Mega Man

- [mmx4 (decomp)](https://github.com/sozud/mmx4) - Matching decompilation of Mega Man X4 (PS1).
- [MegaManPoweredUpTool](https://github.com/efimandreev0/MegaManPoweredUpTool) - Tool to extract main archive from Mega Man Powered Up.
- [MegaManLINKExtract](https://github.com/efimandreev0/MegaManLINKExtract) - Tool to work with Mega Man Powered Up .link archive files.
- [ARC Unpacker & Repacker](https://www.moddb.com/games/devil-may-cry-4/downloads/arc-unpacker-repacker-v09428) - Modding tool letting you extract and repack ARC file containers in MT Framework games (Resident Evil 5, Resident Evil 6, Dragon’s Dogma, Devil May Cry 4, and other Capcom titles) which can also convert many of the file formats in the archives.

#### Gregory Horror Show

- [GregoryHorrorShow-Blender-IO](https://github.com/boringhexi/GregoryHorrorShow-Blender-IO) - Imports PS2 Gregory Horror Show assets (`.ghs`, `.map-pm2`, `.pm2`) into Blender.

#### Gotcha Force

- [gotcha-afs-tool](https://github.com/RenolY2/gotcha-afs-tool) - Unpacker and repacker for Gotcha Force's AFS format (tested on GameCube version).

#### Phoenix Wright: Ace Attorney

- [pwaa1 (decomp)](https://github.com/atasro2/pwaa1) - Matching decompilation of Phoenix Wright: Ace Attorney (Gyakuten Saiban, Japan).
- [recv-dc-decomp (decomp)](https://github.com/fmil95/recv-dc-decomp) - Matching decompilation of Resident Evil - Code: Veronica (Dreamcast).
- [recvx-decomp (decomp)](https://github.com/fmil95/recvx-decomp) - Matching decompilation of Resident Evil - Code: Veronica X (PS2).

### CCR

- [RF Online Addon](https://github.com/Cardboard-box-a/cbb-rf-online-addon) - Blender 4.3 importer/exporter for RF Online `.msh`, `.bn`, `.ani`, and `.bsp` formats.

### CCP Games

- [yretenai/Jackdaw](https://github.com/neptuwunium/Jackdaw) - Research project for Carbon Engine file formats used in EVE Online.

### CR-Space

- [Diamond](https://github.com/tge-was-taken/Diamond) - Reverse engineering and enhancement project for Martial Heroes. Provides tooling, parsers, and client-side improvements including binary parsers, VFS archive tools, and 010 Editor templates.

### CD Projekt Red

#### The Witcher 3 / REDEngine 3

- [WolvenManager](https://github.com/rfuzzo/WolvenManager) - Manager for Witcher game file formats.
- [WolvenKit (legacy)](https://github.com/WolvenKit/WolvenKit-7) - REDEngine 3 file editor designed to simplify and accelerate modding workflow for The Witcher 3.

#### The Witcher

- [Blender 2.49 exporter for The Witcher](https://www.moddb.com/games/the-witcher/downloads/blender-exporter-for-the-witcher) - Blender 2.49 script for exporting static models to The Witcher 1 MDL format.
- [twMax v1.2.3.2 -- mdb Importer for 3DSMax (The Witcher)](https://www.moddb.com/games/the-witcher/downloads/twmax-v1232-mdb-importer-for-3dsmax) - Model importer for The Witcher's binary model format (MDB) that imports compiled models into 3DS Max 9 (v1.2.3.2).
- [Extra tools (The Witcher)](https://www.moddb.com/games/the-witcher/downloads/extra-tools) - Tools for working with The Witcher file formats: DLG (dialogue), QST (quest), BIF, MDB, GFF, and NSS files.

#### Cyberpunk 2077 / REDEngine 4

- [WolvenKit](https://github.com/WolvenKit/WolvenKit) - REDEngine 4 file editor designed to simplify and accelerate modding workflow for Cyberpunk 2077.
- [Cyber Engine Tweaks](https://github.com/maximegmd/CyberEngineTweaks) - Framework to script mods using Lua with access to all the internal scripting features.
- [inl-cpp-parser-mangler](https://github.com/Mozz3d/inl-cpp-parser-mangler) - Standalone inline C++ parser, mangler, and hasher script intended for reversing and deriving Cyberpunk 2077 hashed linker names.
- [CR2WTools](https://github.com/rfuzzo/CR2WTools) - WIP library for reading CR2W files (Witcher/Cyberpunk format).
- [Gibbed.RED4](https://github.com/gibbed/Gibbed.RED4) - Tools for Cyberpunk 2077 file formats.

### Clover Studio

- [noclip.website (Okami)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Okami viewer.

### Cygames

- [GBFRBlenderTools](https://github.com/WistfulHopes/GBFRBlenderTools) - Blender addon for importing Granblue Fantasy Relink mesh models.
- [GBFR2Blender2GBFR](https://github.com/WistfulHopes/GBFR2Blender2GBFR) - Tools for importing/exporting animations and collision data for Granblue Fantasy Relink.

### Disney Interactive

#### Toontown Online

- [omUlette](https://github.com/lifelandman/omUlette) - Lightweight exporter for Panda3D `.egg` files (used in Toontown) that works without Panda3D installed.

### Double Fine

- [CostumeQuest-Decomp (decomp)](https://github.com/Costume-Quest-Modding/CostumeQuest-Decomp) - Matching decompilation of Costume Quest (PC).
- [noclip.website (Psychonauts)](https://github.com/magcius/noclip.website/tree/main/src/psychonauts) - In-browser Psychonauts viewer.

### 8monkey Labs

- [Translation Tool (Darkest of Days)](https://www.moddb.com/games/darkest-of-days/downloads/darkest-of-days-translation-tool)

### Crystal Dynamics / Eidos Interactive

- [soul-re (decomp)](https://github.com/fmil95/soul-re) - Matching decompilation of Legacy of Kain: Soul Reaver (PS1).
- [gex64decomp (decomp)](https://github.com/matbourgon/gex64decomp) - Matching decompilation of Gex 64: Enter the Gecko (N64).
- [Blood Omen 2 3D Rip Tools](https://www.moddb.com/games/blood-omen-2/downloads/blood-omen-2-3d-rip-tools) - A group of cli to export and manipulate blood omen 2 raw 3d model into wavefront and dds textures
- [trview](https://github.com/chreden/trview) - Level visualizer for Tomb Raider 1-5 with speedrunning in mind. View room layouts, triggers, and analyze route possibilities.
  - Formats: .TR2, .TR4, .TRC, .PHD

### Ion Storm

#### Anachronox

- [Anachronox Modding Tools](https://www.moddb.com/games/anachronox/downloads/anachronox-modding-tools) - Mapping and modding tools for Anachronox, includes documentation.

#### Deus Ex

- [cdcEngineDXHR (decomp)](https://github.com/rrika/cdcEngineDXHR) - Matching decompilation of Deus Ex: Human Revolution.
- [Gibbed's Deus Ex HR tools](https://www.moddb.com/games/deus-ex-3/downloads/gibbeds-deus-ex-hr-tools) - A set of tools for compiling and decompiling the Crystal Dynamics engine's data files. Requires the .NET Framework 4 Client Profile.

### Massive Entertainment

#### AquaNox

- [aquanox-tools](https://github.com/Swyter/aquanox-tools) - Reverse engineering tools for the first AquaNox's file formats. Includes 010 Editor binary template (`.bt`) to decrypt and open `.pak` files and their filenames/sizes, and extractor script (`.1sc`). Documents internal formats: `.dds`, `.tga` textures, `.sco` Lua bytecode, `.des` configuration files, `.fog` volumetric fog tables, and `.msb` mesh files.
- [AquaNox 1-2 modding tools](https://www.moddb.com/games/aquanox/downloads/aquanox-1-2-modding-tools) - Modding tools for AquaNox 1-2 including: save editor, file unpacker (for PAK files containing models, scripts, materials, etc.), model converter (MSB to X format), and modding guides. Tools and guides by GodGell and ProjectAqua.

#### World in Conflict

- [Broadcast Tool v6 (World in Conflict)](https://www.moddb.com/games/world-in-conflict/downloads/broadcast-tool-v6) - Allows DX10 users to broadcast a game T.V.-like. Good for LAN or other multi-player matches for spectators. Just a way for someone to watch a match without having to crowd around the two players' screens.
- [Broadcast Tool v7 (World in Conflict)](https://www.moddb.com/games/world-in-conflict/downloads/broadcast-tool-v7) - Allows DX10 users to broadcast a game T.V.-like. Good for LAN or other multi-player matches for spectators. Just a way for someone to watch a match without having to crowd around the two players' screens.
- [Broadcast Tool v8 (World in Conflict)](https://www.moddb.com/games/world-in-conflict/downloads/broadcast-tool-v8) - Allows DX10 users to broadcast a game T.V.-like. Good for LAN or other multi-player matches for spectators. Just a way for someone to watch a match without having to crowd around the two players' screens.

### Surreal Software

- [Drakan Editing Tools v1.2](https://www.moddb.com/games/drakan-order-of-the-flame/downloads/drakan-editing-tools-v12) - Surreal Softwares, Level and model Editor for "Drakan Edition"
- [reo converter to obj (Drakan: Order of the Flame)](https://www.moddb.com/games/drakan-order-of-the-flame/downloads/reo-converter-to-obj) - by Roosen5 – useful for level editors and game mods. For developers only! - See more at: arokhslair

### Dynamix / Sierra

#### Tribes Series

- [Tribes 2 3D Studio MAX Export Plug-in](https://www.moddb.com/games/tribes-2/downloads/tribes-2-3d-studio-max-export-plug-in) - Export plugin for 3D Studio MAX v2.5 for creating and modifying objects in Tribes 2. Requires 3D Studio MAX (professional 3D modeling suite, recommended for advanced users).
- [Tribes: Vengeance Editing Tools](https://www.moddb.com/games/tribes-vengeance/downloads/tribes-vengeance-editing-tools) - Beta release of TribesEd for creating Tribes: Vengeance maps.
- [Tribes 1.40 LoDFix plugin](https://www.moddb.com/games/tribes/downloads/tribes-140-lodfix-plugin) - Plugin that fixes a known level of detail (LOD) issue with certain weapons in Tribes. Affects users with field of view (FOV) higher than default. Place LoDFix.dll in plugins folder. Created by Groove (v1.40).

### DOKA Studios

- [reSL (decomp)](https://github.com/konovalov-aleks/reSL) - Matching decompilation of ShortLine v1.1.

### EA Black Box

- [Castaway (decomp)](https://github.com/HaydnTrigg/Castaway) - Matching decompilation of The Sims 2: Castaway.

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

- [UXM](https://github.com/JKAnderson/UXM) - Unpacker for Dark Souls III and Sekiro archives.
- [DarkSoulsIII.FileFormats](https://github.com/Atvaark/DarkSoulsIII.FileFormats) - Library for reading Dark Souls III file formats.
- [dstools](https://github.com/katalash/dstools) - Tools for Dark Souls file formats.
- [ds3-open-re](https://github.com/garyttierney/ds3-open-re) - Open reverse engineering resources for Dark Souls 3.
- [ParamCrypt](https://github.com/Grimrukh/ParamCrypt) - Encryption tool for Dark Souls param files.
- [Souls Modding Wiki](https://www.soulsmodding.com/doku.php?id=start) - Documentation for FromSoftware formats.
- [libER](https://github.com/Dasaav-dsv/libER) - ELDEN RING API library with focus on binary compatibility and safety. Written in modern C++20 with byte-perfect documentation of ELDEN RING type layouts, type safety, thread safety, and non-invasive modifications. Supports symbol definition files separated by game version.
- [Awesome Elden Ring](https://github.com/sovietspaceship/awesome-elden-ring) - Curated list of resources and tools for Elden Ring.
- [Sekiro Modding Wiki](https://github.com/SekiroResurrection/modding-wiki) - Documentation for Sekiro modding.
- [DSMapStudio](https://github.com/soulsmods/DSMapStudio) - Map/level editor for Souls/Bloodborne/Elden Ring.
- [DSMSPortable](https://github.com/mountlover/DSMSPortable/tree/main) - Portable version of DSMapStudio.
- [FLVER_Editor](https://github.com/asasasasasbc/FLVER_Editor) - Multifunctional editor to edit and view FromSoftware game's FLVER files (Sekiro, Dark Souls, Bloodborne, etc.).
- [elden-ring-open-re](https://github.com/garyttierney/elden-ring-open-re) - Public knowledge on reverse engineering Elden Ring.
- [BinderTool](https://github.com/Atvaark/BinderTool) - Tool for extracting and repacking BND/BHD archives.
- [dark-souls-map-viewer](https://github.com/colevk/dark-souls-map-viewer) - Web-based Dark Souls map viewer.
- [blender-flver](https://github.com/elizagamedev/blender-flver) - Blender addon for importing/exporting FLVER models from FromSoftware games. Supports Dark Souls, Dark Souls: Remastered, Bloodborne, and Sekiro.
- [Coremats](https://github.com/JKAnderson/Coremats) - .NET library for FromSoftware formats.
- [soulsformats-rs](https://github.com/garyttierney/soulsformats-rs) - Rust library that can read/write file formats from FromSoftware's recent games.
- [FromSoftware-Blender-Importer](https://github.com/FelixBenter/FromSoftware-Blender-Importer) - Blender importer for FromSoftware FLVER formats. Supports Dark Souls 1, 2, 3, and Sekiro: Shadows Die Twice (characters, partsbnds, and maps for DS1/DS3).
- [soulstruct](https://github.com/Grimrukh/soulstruct) - Python library for Dark Souls file formats and modding.
- [soulstruct-blender](https://github.com/Grimrukh/soulstruct-blender) - Blender plugin for soulstruct.
- [SoulsTemplates](https://github.com/JKAnderson/SoulsTemplates) - 010 Editor templates for Souls formats.
- [noclip.website (DarkSouls)](https://github.com/magcius/noclip.website/tree/main/src/DarkSouls) - In-browser Dark Souls map viewer.
- [DSAnimStudio](https://github.com/Meowmaritus/DSAnimStudio) - Animation and cutscene editor for Souls games.
- [dark_souls_hkx](https://github.com/Danilodum/dark_souls_hkx) - Noesis plugins for Dark Souls HKX (Havok animation) format with extra root bone and root motion support.
- [ESDLang](https://github.com/thefifthmatt/ESDLang) - Decompiler for ESD event script format.
- [Zeditor](https://github.com/AinTunez/Zeditor) - Editor for FromSoftware's ESD (Event Script Data) files used in Souls games.
- [Gibbed.DarkSouls](https://github.com/gibbed/Gibbed.DarkSouls) - Tools & code for use with Dark Souls.
- [DS2Template](https://github.com/LordRadai/DS2Template) - Collection of 010 .bt templates specifically made for Dark Souls II
- [ER.DATA.Tool](https://github.com/Ekey/ER.DATA.Tool) - Tool for extracting data archives from mobile game Earth Revival (Project Arrival).

### Frictional Games

- [AmnesiaLoader](https://github.com/REDxEYE/AmnesiaLoader) - UniLoader addon for most Frictional Games titles (Amnesia series, Soma, etc).

### Gearbox Software

- [Gibbed.Borderlands3.Datamining](https://github.com/gibbed/Gibbed.Borderlands3.Datamining) - Datamining tools for Borderlands 3.
- [Borderlands 2 Texture Modding Tool for PC](https://www.moddb.com/games/borderlands-2/downloads/borderlands-2-texture-modding-tool-for-pc) - PC-only guide and tool (TexMod) for extracting, editing, and using textures in Borderlands 2. TexMod is a popular texture tool also used for Arkham City, Tomb Raider, and other games.

#### MechWarrior 4

- [MW4 Sound Extractor (MechWarrior 4: Mercenaries)](https://www.moddb.com/games/mechwarrior-4-mercenaries/downloads/mw4-sound-extractor) - Sound extractor for MechWarrior 4: Mercenaries. Created by mektek, one of the first tools created for the game.

### Game Freak

*Pokémon games across various generations.*

#### Gen I & II

- [map-editor](https://github.com/KernelEquinox/map-editor) - Map editor for Generation I/II Pokémon games.
- [polished-map](https://github.com/Rangi42/polished-map) - Polished map editor for Gen II.
- [puzzleleague64 (decomp)](https://github.com/angheloalf/puzzleleague64) - Matching decompilation of Pokémon Puzzle League.
- [xd-decomp (decomp)](https://github.com/TeamOrre/xd-decomp) - Matching decompilation of Pokémon XD: Gale of Darkness (GameCube).
- [pokeheartgold (decomp)](https://github.com/pret/pokeheartgold) - Matching decompilation of Pokémon HeartGold (100%).
- [pokefirered (decomp)](https://github.com/pret/pokefirered) - Matching decompilation of Pokémon FireRed (100%).
- [pokecrystal (decomp)](https://github.com/pret/pokecrystal) - Matching decompilation of Pokémon Crystal (100%).
- [pokegold (decomp)](https://github.com/pret/pokegold) - Matching decompilation of Pokémon Gold (100%).
- [pokegold-spaceworld (decomp)](https://github.com/pret/pokegold-spaceworld) - Matching decompilation of Pokémon Gold (SpaceWorld Demo) (100%).
- [pokeyellow (decomp)](https://github.com/pret/pokeyellow) - Matching decompilation of Pokémon Yellow (100%).
- [pokered (decomp)](https://github.com/pret/pokered) - Matching decompilation of Pokémon Red (100%).

#### Gen III

*See also [Sappy (GBA Audio)](#sappy-gba-audio) for audio tools used in these games.*

- [SaveStadium](https://github.com/Ploaj/SaveStadium) - Save file editor for Pokémon Stadium games.
- [Wargrave-Pokemon-Gen2-Editors](https://github.com/sandbPublic/Wargrave-Pokemon-Gen2-Editors) - Editors for Pokémon Gen 2 games.
- [Pokemon-Shuffle-Unpacker](https://github.com/SciresM/Pokemon-Shuffle-Unpacker) - Unpacker for Pokémon Shuffle archive files.
- [JPoke-Export](https://github.com/vgmoose/JPoke-Export) - Pokémon save file exporter.
- [blue-spider](https://github.com/cosarara/blue-spider) - Map editor for Pokémon Ruby/Sapphire/Emerald.
- [porymap](https://github.com/huderlem/porymap) - Modern map editor for Gen III Pokémon games.
- [MEH](https://github.com/shinyquagsire23/MEH) - Map editor for Gen III.
- [pokeemerald-jp (decomp)](https://github.com/pret/pokeemerald-jp) - Matching decompilation of Pokémon Emerald (JP) (100%).
- [pokeemerald (decomp)](https://github.com/pret/pokeemerald) - Matching decompilation of Pokémon Emerald (100%).
- [AwesomeMapEditor](https://github.com/Sierraffinity/AwesomeMapEditor) - Alternative map editor for Gen III.
- [pokeruby (decomp)](https://github.com/pret/pokeruby) - Matching decompilation of Pokémon Ruby (100%).
- [gomons](https://github.com/huderlem/gomons) - Go library that can read and modify Pokémon Emerald save files.
- [Bulbapedia (Gen I)](https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_I)) - Save data structure documentation for Generation I.
- [Bulbapedia (Gen II)](https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_II)) - Save data structure documentation for Generation II.
- [Bulbapedia (Gen III)](https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_(Generation_III)) - Save data structure documentation for Generation III.

#### Gen VI

- [pokediamond (decomp)](https://github.com/pret/pokediamond) - Matching decompilation of Pokémon Diamond (100%).
- [pokeplatinum (decomp)](https://github.com/pret/pokeplatinum) - Matching decompilation of Pokémon Platinum (100%).
- [Personal-Editor](https://github.com/SciresM/Personal-Editor) - Editor for Generation 6 Pokémon games (Pokémon X/Y and Pokémon OR/AS). Use on extracted files from Personal.GARC.

#### Gen V

- [SwissArmyKnife](https://github.com/PlatinumMaster/SwissArmyKnife) - Cross-platform ROM editor for Generation V Pokémon games (Black, White, Black 2, White 2). Supports editing map containers, text, events, zone headers, entities, and encounters.
- [pbr-dtk (decomp)](https://github.com/bgsamm/pbr-dtk) - Matching decompilation of Pokémon Battle Revolution.
- [pokestadium (decomp)](https://github.com/pret/pokestadium) - Matching decompilation of Pokémon Stadium (100%).
- [pokestadiumgs (decomp)](https://github.com/pret/pokestadiumgs) - Matching decompilation of Pokémon Stadium 2 (100%).
- [pmd-red (decomp)](https://github.com/pret/pmd-red) - Matching decompilation of Pokémon Mystery Dungeon: Red Rescue Team (100%).
- [pmd-sky (decomp)](https://github.com/pret/pmd-sky) - Matching decompilation of Pokémon Mystery Dungeon: Explorers of Sky (100%).
- [pokepinballrs (decomp)](https://github.com/pret/pokepinballrs) - Matching decompilation of Pokémon Pinball: Ruby & Sapphire (100%).
- [pokepinball (decomp)](https://github.com/pret/pokepinball) - Matching decompilation of Pokémon Pinball (100%).
- [poketcg (decomp)](https://github.com/pret/poketcg) - Matching decompilation of Pokémon TCG (100%).
- [poketcg2 (decomp)](https://github.com/pret/poketcg2) - Matching decompilation of Pokémon TCG 2 (100%).
- [pokeblack (decomp)](https://github.com/pokemodding/pokeblack) - Matching decompilation of Pokémon Black.

### Gameloft

- [GameloftEngineLoader](https://github.com/REDxEYE/GameloftEngineLoader) - UniLoader addon for importing Gameloft engine PIG files. Supports meshes, textures, transforms, nodes, and compression (LZ4, ZSTD).
- [Greenier-Farm-3-Decomp (decomp)](https://github.com/SmithGoll/Greenier-Farm-3-Decomp) - Matching decompilation of Green Farm 3.

### Genius Sonority

*Pokémon Colosseum, Pokémon XD: Gale of Darkness.*

- [pokemon_fsys_tool](https://github.com/gamemasterplc/pokemon_fsys_tool) - Tool for FSYS archive format used in Pokémon Colosseum/XD.
- [PokemonFSYSConverter](https://github.com/vgmoose/PokemonFSYSConverter) - Program to extract .obm and textures out of .fsys files found in some GameCube/Wii titles.
- [tdmextractor](https://github.com/NerduMiner/tdmextractor) - Archive extractor and repacker for "The Denpa Men" series (TDM1/TDM2/TDM3/TDMF archives). Can replace the usage of the existing quickbms script for The Denpa Men 3.

### Genki

*Jade Cocoon: Story of the Tamamayu, Jade Cocoon 2.*

- [Jade-Cocoon-Unpacker-Repacker](https://github.com/Meos4/Jade-Cocoon-Unpacker-Repacker) - Tool to unpack and repack DATA.001 archive files from Jade Cocoon (PS1).
- [Jade-Cocoon-2-Unpacker-Repacker](https://github.com/Meos4/Jade-Cocoon-2-Unpacker-Repacker) - Tool to unpack and repack archive files from Jade Cocoon 2 (PS2).
- [Tamamayu-Monogatari-Dennou-Bijutsukan-Unpacker](https://github.com/Meos4/Tamamayu-Monogatari-Dennou-Bijutsukan-Unpacker) - Unpacker for DATA.001 archives from Tamamayu Monogatari Dennou Bijutsukan demo (PS1).
- [GUTArchiveTools](https://github.com/igorciz777/GUTArchiveTools) - Archive tools for GUT (Genki Utility) archive format used in Genki's PS2 racing games (Tokyo Xtreme Racer series, Kaido Racer, Shutokou Battle, etc.).

### Grezzo

*Ocarina of Time 3D, Majora's Mask 3D, Luigi's Mansion remake, Ever Oasis.*

- [io_scene_cmb](https://github.com/M-1-RLG/io_scene_cmb) - Blender add-on for Grezzo's "Ctr Model Binary" (CMB) format.
- [noclip.website (OoT3D)](https://github.com/magcius/noclip.website/tree/main/src/OcarinaOfTime3D) - In-browser Ocarina of Time 3D viewer.
- [MeltyTool (Grezzo)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/Grezzo) - Grezzo format viewer/exporter.
- [N3DSCmbViewer](https://github.com/xdanieldzd/N3DSCmbViewer) - Viewer for 3DS CMB models.
- [Scarlet](https://github.com/xdanieldzd/Scarlet) - General purpose 3DS/Vita game tool.
- [Gar/Zar UnPacker](https://gbatemp.net/threads/release-gar-zar-unpacker-v0-1.385264/) - Archive unpacker for Ocarina of Time 3D and Majora's Mask 3D.
- [Switch-Toolbox](https://github.com/KillzXGaming/Switch-Toolbox/tree/master/File_Format_Library/FileFormats/Grezzo) - A tool to edit many video game file formats
- [GARTool](https://github.com/efimandreev0/GARTool) - Tool tested with Ever Oasis and Luigi's Mansion.
- [irarc_unpacker](https://github.com/efimandreev0/irarc_unpacker) - Unpacker for IRARC archive format from Blaster Master Zero and Azure Striker Gunvolt (3DS).

### Human Head Studios

- [Gwynhala's Model Exporter (Rune)](https://www.moddb.com/games/rune/downloads/gwynhalas-model-exporter) - Rune SuperCoolModel Exporter for Milkshape 3D by Gwynhala

### id Software

- [DOOM64-RE (decomp)](https://github.com/Erick194/DOOM64-RE) - Matching decompilation of Doom 64.
- [PSXDOOM-RE (decomp)](https://github.com/Erick194/PSXDOOM-RE) - Matching decompilation of Doom (PlayStation).
- [valen](https://github.com/jandk/valen) - Multi-game resource extractor with GUI. Supports DOOM Eternal, Dark Ages, Great Circle, and other id Software games. Features file browser, bulk export, texture/model/material/skeleton/animation extraction, and preview capabilities. Exports to DDS, PNG, GLTF formats.
- [blender_io_mesh_bsp](https://github.com/andyp123/blender_io_mesh_bsp) - Blender addon for importing Quake BSP (Binary Space Partition) map files.
- [wadext](https://github.com/ZDoom/wadext) - Simple WAD extraction command-line tool for Doom engine (id Tech 1) mods. Extracts and converts Doom format patches/flats to PNG and sounds to WAV. Supports Doom, Heretic, Hexen, and Strife palettes.
- [DOOMP](https://github.com/Ret-HZ/DOOMP) - Doom file format parser and extractor.
- [DoomRPG-RE-3DS](https://github.com/efimandreev0/DoomRPG-RE-3DS) - Nintendo 3DS port of the reverse engineered Doom RPG.
- [rtcw-wet-blender-model-tools](https://github.com/mino-git/rtcw-wet-blender-model-tools) - Blender model tools for Return to Castle Wolfenstein: Enemy Territory.
- [ExtractDoomDisk](https://github.com/gibbed/ExtractDoomDisk) - Extractor for Doom disk image files.
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

### Guerrilla Games

- [ProjectZeroDawn](https://github.com/neptuwunium/ProjectZeroDawn) - File format research and tools for Horizon Zero Dawn.
- [decima](https://github.com/ShadelessFox/decima) - GUI application for viewing and editing resources found in games powered by Decima Engine. Supports browsing and editing core objects, previewing models/textures/shaders, exporting assets, and repacking archives. Works with Horizon Zero Dawn, Death Stranding, and other Decima Engine games.
- [decima-native](https://github.com/ShadelessFox/decima-native) - Native library components for Decima Engine tools.
- [decima-rpcs3-dumper](https://github.com/ShadelessFox/decima-rpcs3-dumper) - Tool for dumping Decima Engine resources from RPCS3 emulator.
- [odradek](https://github.com/ShadelessFox/odradek) - Horizon Forbidden West asset viewer and extractor. Reincarnation of Decima Workshop specifically targeting Horizon Forbidden West for modding purposes.
- [forbidden-west-localizer](https://github.com/ShadelessFox/forbidden-west-localizer) - Modification that allows changing any localized text in Horizon Forbidden West. Supports text replacement via JSON configuration files.
- [cauldron](https://github.com/cauldronloader/cauldron) - Mod loader for Decima engine games (Horizon Zero Dawn/Forbidden West, Death Stranding, etc). Rust-based modding framework with game detection, DLL proxy loading, and RTTI symbol dumping capabilities.
- [stormbird](https://github.com/neptuwunium/stormbird) - Interop library for Horizon Zero Dawn. Provides interfaces for working with Horizon Zero Dawn file formats and game data.
- [decima-dmf](https://github.com/REDxEYE/decima-dmf) - Blender addon for importing DMF files produced by Decima Workshop. Supplementary addon for working with Decima Engine models in Blender.
- [ProjectDecima](https://github.com/spammydavis/ProjectDecima) - GUI application for previewing, exporting and modifying game resources in Decima Engine games. Archive explorer with texture preview and export capabilities. (Fork)

### LucasArts

- [rogue_squadron64 (decomp)](https://github.com/Tmcg2/rogue_squadron64) - Matching decompilation of Star Wars: Rogue Squadron (N64).
- [SW_RACER_RE (decomp)](https://github.com/tim-tim707/SW_RACER_RE) - Matching decompilation of Star Wars Episode 1: Racer.
- [scummtools](https://github.com/UnBeatWaterGH/scummtools) - Tools for SCUMM (Script Creation Utility For Maniac Mansion).
- [Grim Fandango model viewer](https://www.moddb.com/games/grim-fandango/downloads/grim-fandango-model-viewer)
- [Easy Saber Editing Script 2.0 (Star Wars: Jedi Academy)](https://www.moddb.com/games/star-wars-jedi-academy/downloads/easy-saber-editing-script-2-0) - Script for skipping the saber menu and receiving a default saber in Star Wars: Jedi Academy (v2.0).
- [JK editing manuals (Star Wars Jedi Knight: Dark Forces II)](https://www.moddb.com/games/star-wars-jedi-knight-dark-forces-ii/downloads/jk-editing-manuals) - Offline archive of notable JED level editor tutorials for Star Wars Jedi Knight: Dark Forces II.
- [JKVersions Tool 3.0 by The_MAZZTer (Star Wars Jedi Knight: Dark Forces II)](https://www.moddb.com/mods/todoa/downloads/jkversions-tool-by-the-mazzter) - Tool for extracting JK 1.01 binary from patch EXE and applying patches to downgrade to JK 1.00 or upgrade to JKUP. Created by The_MAZZTer (v3.0).

### Gust (Koei Tecmo)

- [slpm86183 (decomp)](https://github.com/Erizur/slpm86183) - Matching decompilation of Pop'N Music CS1 (PS1).
- [gust_stuff](https://github.com/eArmada8/gust_stuff) - Modding toolkit for G1M model files used in Gust games (Atelier series).
- [Project-G1M](https://github.com/Joschuka/Project-G1M) - Noesis plugin for importing G1M 3D model format used in Gust and Bandai Namco games.
- [Cethleann](https://github.com/neptuwunium/Cethleann) - KTGL (Soft Engine) data exploration and research tool for Koei Tecmo games.

### Harmonix

*Rock Band, Guitar Hero, Amplitude, Dance Dance Revolution Universe, Frequency, Karaoke Revolution.*

- [rb3ds (decomp)](https://github.com/ieee802dot11ac/rb3ds) - Matching decompilation of Rock Band 3 (Nintendo DS).
- [LibForge](https://github.com/maxton/LibForge) - Library for reading, writing, and converting Forge engine formats (Rock Band 4, Rock Band VR, FUSER). Handles MIDI, textures (PNG, BMP), models (FBX, OBJ), DTA/DTB, RBmid, RBsong, lipsync, and package files (CON, GP4, PKG). See also [PikminGuts92's fork](https://github.com/PikminGuts92/LibForge) with v2 RB MIDI support, MAGMA v1 milos support, and AMP/RBVR .mid_* file support.
- [pikaxe](https://github.com/PikminGuts92/pikaxe) - Milo engine modding tool for Harmonix games. Supports Guitar Hero 1-2, Guitar Hero Encore: Rocks the 80s, Rock Band series, Dance Central, and other Milo engine titles. Handles DTA, GLTF, and ARK formats across Xbox, Wii, and PS3. Evolution of Mackiloha.
- [DtxCS](https://github.com/maxton/DtxCS) - C# library for parsing and interpreting DTA/DTB scripting format used in Rock Band and Guitar Hero games.
- [CON-Tools](https://github.com/PikminGuts92/CON-Tools) - Create, modify, and combine Rock Band CON files. Convert to Phase Shift, Wii, and PS3 formats.
- [PyMilo](https://github.com/PikminGuts92/PyMilo) - Python library for managing milo files from Harmonix games. Includes GUI and archive extraction utilities. (Archived)
- [BFForever](https://github.com/PikminGuts92/BFForever) - Library for managing and creating game files for BandFuse (PS3, Xbox 360). Handles RIFF files, CELT audio encoding/decoding.
- [Beatles Rock Band Blender plugin](https://www.moddb.com/games/rock-band/downloads/beatles-rock-band-blender-plugin) - Blender plugin for The Beatles: Rock Band. Created by Turk645.
- [amplitools](https://github.com/PikminGuts92/amplitools) - Tools for Amplitude '03.
- [offbeat](https://github.com/PikminGuts92/offbeat) - Rust library for Dance Dance Revolution Universe. Includes DDM to glTF converter.
- [praise-mod](https://github.com/PikminGuts92/praise-mod) - Toolkit for creating Guitar Praise custom content. Converts Clone Hero songs to GP format. Supports ogg vorbis audio.
- [WorshipTools](https://github.com/PikminGuts92/WorshipTools) - Converts Jam Band songs to Clone Hero format. (Archived)
- [ghlcrypt](https://github.com/maxton/ghlcrypt) - C# tool for Guitar Hero Live.
- [re-notes](https://github.com/PikminGuts92/re-notes) - Reverse engineering notes and templates for Harmonix games (Dance Dance Revolution Universe, DJ Hero, Karaoke Revolution) and other titles. Includes 010 Editor templates, Python scripts, and data dumps for BlitzTech, Forge, and Milo engines.

### HAL Laboratory

*Kirby, Super Smash Bros series.*

- [slippi-ssbm-asm](https://github.com/project-slippi/slippi-ssbm-asm) - Assembly tools for Super Smash Bros. Melee Slippi format.
- [rdb_tool](https://github.com/Raytwo/rdb_tool) - Tool for patching RDB files in Super Smash Bros. Ultimate. Allows patching files into RDB archives using file hash-based syntax.
- [ARCropolis](https://github.com/Raytwo/ARCropolis) - Modding framework for loading and managing community-made mods and plugins for Super Smash Bros. Ultimate. Powered by Skyline for Switch homebrew.
- [skyline](https://github.com/skyline-dev/skyline) - Environment for runtime hooking and code patching within Super Smash Bros. Ultimate. Provides linking, runtime hooking, and code patching capabilities for Switch homebrew modding.
- [StudioSB](https://github.com/Ploaj/StudioSB) - Model application for Super Smash Bros. Ultimate. Work-in-progress tool for viewing and working with SSBU model files.
- [GekkoAssembler](https://github.com/CryZe/GekkoAssembler) - Assembles Gekko Assembly to Action Replay or Gecko Cheat Code format. Used for GameCube and Wii game modding.
- [KirbyAirRideTools](https://github.com/LuigiBlood/KirbyAirRideTools) - Tools for Kirby Air Ride file formats.
- [k64cs-project](https://github.com/shygoo/k64cs-project) - Hacking tools and notes for Kirby 64: The Crystal Shards. Includes web-based model viewer, Collada DAE to Kirby64 geometry converter, ROM/RAM structure notes, and debugger scripts.
- [Sm4shExplorer](https://github.com/jam1garner/Sm4shExplorer) - Tool for managing the file-system of Super Smash Bros. for Wii U.
- [smash-arc](https://github.com/jam1garner/smash-arc) - Library for working with Super Smash Bros. Ultimate's ARC format.
- [BrawlLib](https://github.com/libertyernie/brawltools) - Library for reading/writing file formats from Super Smash Bros. Brawl and other Wii games.
- [Smash-Forge](https://github.com/jam1garner/Smash-Forge) - Open source editor for Super Smash Bros. 4 file formats.
- [smash-fnv](https://github.com/jam1garner/smash-fnv) - Rust library for reading and writing sound_volume_fighter_num_table.fnv files from Super Smash Bros. for Nintendo 3DS and Wii U and Super Smash Bros. Ultimate.
- [smash-sli](https://github.com/jam1garner/smash-sli) - Rust library for reading and writing soundlabelinfo.sli files from Super Smash Bros. Ultimate.
- [smash-csb](https://github.com/jam1garner/smash-csb) - Rust library for reading and writing commonsoundtable.csb files from Super Smash Bros. Ultimate.
- [BrawlStageManager](https://github.com/libertyernie/BrawlStageManager) - Stage (.pac/.rel) and song (.brstm) managers for Brawl mods.
- [BrawlStageManager](https://github.com/libertyernie/BrawlStageManager) - Stage (.pac/.rel) and song (.brstm) managers for Brawl mods.
- [smash-fnv](https://github.com/jam1garner/smash-fnv) - Rust library for reading and writing sound_volume_fighter_num_table.fnv files from Super Smash Bros. for Nintendo 3DS and Wii U and Super Smash Bros. Ultimate.
- [smash-sli](https://github.com/jam1garner/smash-sli) - Rust library for reading and writing soundlabelinfo.sli files from Super Smash Bros. Ultimate.
- [smash-csb](https://github.com/jam1garner/smash-csb) - Rust library for reading and writing commonsoundtable.csb files from Super Smash Bros. Ultimate.
- [smash-bgm-property](https://github.com/jam1garner/smash-bgm-property) - Rust library for reading and writing bgm_property.bin files from Super Smash Bros. Ultimate.
- [ArcExplorer](https://github.com/ScanMountGoat/ArcExplorer) - File browser and extractor for Super Smash Bros. Ultimate's data.arc file. Supports Windows, macOS, and Linux with network connection support.
- [ArcCross](https://github.com/Ploaj/ArcCross) - File extractor for Super Smash Bros. Ultimate's ARC file. Replaced by ArcExplorer but useful for data.arc files prior to game version 5.0.
- [arc-fuse](https://github.com/jam1garner/arc-fuse) - FUSE wrapper for Super Smash Bros. Ultimate's ARC filetype.
- [HSDLib](https://github.com/Ploaj/HSDLib) - Library for HAL's HSD format (used in Super Smash Bros Melee).
- [MeleeMedia](https://github.com/Ploaj/MeleeMedia) - Media extractor for Super Smash Bros Melee.
- [noclip.website (Melee)](https://github.com/magcius/noclip.website/tree/main/src/SuperSmashBrosMelee) - In-browser Melee stage viewer.
- [noclip.website (Super Smash Bros Brawl)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Super Smash Bros Brawl viewer.
- [noclip.website (SYSDOLPHIN)](https://github.com/magcius/noclip.website/tree/main/src/SYSDOLPHIN) - In-browser SYSDOLPHIN format viewer.
- [noclip.website (Kirby Air Ride)](https://github.com/magcius/noclip.website/tree/main/src/KirbyAirRide) - In-browser Kirby Air Ride viewer.
- [noclip.website (Kirby's Return to Dream Land)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Kirby's Return to Dream Land viewer.
- [RDLMINT](https://github.com/firubii/RDLMINT) - Disassembler and assembler for Kirby's Return to Dream Land's MINT bytecode. Can unpack and disassemble MINT Archives, and recompile and repack MINT XBIN scripts.
- [MeltyTool (Sysdolphin)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/Sysdolphin) - Sysdolphin format viewer/exporter.
- [Melee DAT format](https://smashboards.com/threads/melee-dat-format.292603/) - Documentation for Melee's DAT format.
- [DATReaderC](https://github.com/EstevanBR/DATReaderC) - A C program that reads a .dat file (Super Smash Bros. Melee)
- [ssb-decomp-re (decomp)](https://github.com/vetritheretri/ssb-decomp-re) - Matching decompilation of Super Smash Bros. (N64).
- [melee (decomp)](https://github.com/doldecomp/melee) - Matching decompilation of Super Smash Bros. Melee.
- [brawl (decomp)](https://github.com/doldecomp/brawl) - Matching decompilation of Super Smash Bros. Brawl.

### Heavy Iron Studios

- [bfbb (decomp)](https://github.com/bfbbdecomp/bfbb) - Matching decompilation of SpongeBob SquarePants: Battle for Bikini Bottom.
- [SBMI-Decomp (decomp)](https://github.com/Juanen100/SBMI-Decomp) - Matching decompilation of SpongeBob Moves In! (Android).
- [BFBBJSPTool](https://github.com/igorseabra4/BFBBJSPTool) - JSP tool for SpongeBob SquarePants: Battle for Bikini Bottom.
- [SpyroETDChunkTool](https://github.com/igorseabra4/SpyroETDChunkTool) - Chunk tool for Spyro: Enter the Dragonfly.
- [IndustrialPark](https://github.com/igorseabra4/IndustrialPark) - Viewer and editor for SpongeBob SquarePants: Battle for Bikini Bottom and Scooby-Doo games.
- [noclip.website (SpongeBob Battle for Bikini Bottom)](https://github.com/magcius/noclip.website/tree/main/src/HeavyIron) - In-browser SpongeBob BFBB viewer.
- [noclip.website (SpongeBob The Movie)](https://github.com/magcius/noclip.website/tree/main/src/HeavyIron) - In-browser SpongeBob The Movie viewer.
- [noclip.website (SpongeBob Revenge of the Flying Dutchman)](https://github.com/magcius/noclip.website/tree/main/src/SpongebobRevengeOfTheFlyingDutchman) - In-browser SpongeBob ROTFD viewer.

### Hudson Soft

*Mario Party series (Nintendo 64).*

- [bm642romtool](https://github.com/gamemasterplc/bm642romtool) - Bomberman 64 The Second Attack ROM compression tool.
- [bland2digtool](https://github.com/gamemasterplc/bland2digtool) - Bomberman Land 2 (GameCube) DIG file extractor and rebuilder.
- [PartyPlanner64](https://github.com/PartyPlanner64/PartyPlanner64) - Full-featured board editor and modding tool for Mario Party (N64) games.
- [symbols](https://github.com/PartyPlanner64/symbols) - Debug symbol maps for reverse engineering Mario Party games.
- [mpdsarchivetool](https://github.com/gamemasterplc/mpdsarchivetool) - Mario Party DS archive (.bin) extraction tool.
- [mpromtool](https://github.com/gamemasterplc/mpromtool) - Mario Party 1-3 (N64) ROM extractor and rebuilder tool.
- [hsfview](https://github.com/Muzzarino/hsfview) - Model viewer for Mario Party (Wii).

### Insomniac Games

- [RatchetLevelEditor](https://github.com/badger41/RatchetLevelEditor) - Level editor for Ratchet & Clank games.
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

- [fe11-us (decomp)](https://github.com/Eebit/fe11-us) - Matching decompilation of Fire Emblem: Shadow Dragon (NDS, USA).
- [Kid-Icarus-JSON-Parser](https://github.com/onepiecefreak3/Kid-Icarus-JSON-Parser) - JSON parser for Kid Icarus file formats.
- [FEAT](https://github.com/SciresM/FEAT) - Fire Emblem Archive Tool for automatically extracting data from 3DS Fire Emblem archives.
- [FEIF_ARC](https://github.com/GovanifY/FEIF_ARC) - Fire Emblem If ARC re/unpacker.

#### Paper Mario 64

*See also [Fast3d/F3dex (N64)](#fast3df3dex-n64) for graphics format tools used in this game.*

- [papermario (decomp)](https://github.com/pmret/papermario) - Matching decompilation of Paper Mario (Nintendo 64).
- [leaflitter (decomp)](https://github.com/darxoon/leaflitter) - Work-in-progress decompilation of Paper Mario: Sticker Star.
- [noclip.website (PM64)](https://github.com/magcius/noclip.website/tree/main/src/PaperMario64) - In-browser Paper Mario 64 map viewer.
- [star-rod](https://github.com/z64a/star-rod) - Modding tool for Paper Mario 64 including map editor and script tools.
- [Hack64 Paper Mario](https://hack64.net/wiki/doku.php?id=paper_mario) - Documentation for Paper Mario 64 file formats and data structures.

#### Paper Mario: TTYD / Super Paper Mario

*See also [JSYSTEM](#jsystem-gamecubewii) for additional format tools used in these games.*

- [ttyd (decomp)](https://github.com/doldecomp/ttyd) - Matching decompilation of Paper Mario: The Thousand-Year Door.
- [spm-decomp (decomp)](https://github.com/seekyct/spm-decomp) - Matching decompilation of Super Paper Mario.
- [SpmViewer](https://github.com/follyfoxe/SpmViewer) - Tool for viewing Super Paper Mario model files.
- [ttyd-utils](https://github.com/jdaster64/ttyd-utils) - Utilities for modding Paper Mario: TTYD.
- [noclip.website (TTYD)](https://github.com/magcius/noclip.website/tree/main/src/PaperMarioTTYD) - In-browser TTYD map viewer.
- [MeltyTool (TTYD)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/PaperMarioTheThousandYearDoor) - Model viewer/exporter.
- [PistonMiner/ttyd-tools](https://github.com/PistonMiner/ttyd-tools) - Development tools including Blender exporter, disassembler, and REL linker.
- [PaperMarioModelViewer](https://github.com/uyjulian/PaperMarioModelViewer) - Model viewer for Paper Mario games.
- [lzarc](https://github.com/jam1garner/lzarc) - Rust library and CLI for extracting and packing LZARC compressed archives used in Paper Mario Color Splash.
- [CollisionSceneBinary](https://github.com/KillzXGaming/CollisionSceneBinary) - A library and tool for handling csb and ctb collision files found in paper mario games.

### Interactive Studios

#### Glover

- [noclip.website (Glover)](https://github.com/magcius/noclip.website/tree/main/src/Glover) - In-browser Glover level viewer.
- [libgarib](https://github.com/naclomi/libgarib) - Glover reverse engineering tools and information library.

### Illusion

*Koikatsu, Koikatsu Sunshine, Honey Select, AI Girl, PlayHome.*

- [KK-Blender-Porter-Pack](https://archive.org/details/kkbp-importer-8.0.2) - Exporter/importer pack for Koikatsu characters in Blender with near-perfect mesh and texture replication, facial shapekeys, Rigify armature, and FBX export.
  - Games: Koikatsu, Koikatsu Sunshine.
  - See also [gitgoon mirror](https://gitgoon.dev/kkbp-dev/KKBP_Importer).
- [KKBP_Exporter](https://gitgoon.dev/kkbp-dev/KKBP_Exporter) - In-game BepInEx plugin that exports Koikatsu character cards as PMX models with textures and skeletal data for use with KKBP Importer or MMD tools.
- [KoikatsuModdingTools](https://gitgoon.dev/IllusionMods/KoikatsuModdingTools) - Unity Editor toolkit for creating Koikatsu mods including clothing, accessories, hair, maps, and custom shaders. Supports asset bundle building, FBX import with bone optimization, and uTinyRipper integration.
- [ZipStudio](https://gitgoon.dev/IllusionMods/ZipStudio) - Utility for converting Koikatsu hard-mods to sideloader format with automatic list conversion to CSV and manifest editing.

### Innerloop Studios

- [IGI2ModTool](https://github.com/REDxEYE/IGI2ModTool) - Modding tools for I.G.I.-2: Covert Strike file formats.

### iNiS

- [Murugo/Misc-Game-Research (Gitaroo Man)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Gitaroo%20Man) - Reverse engineering notes for Gitaroo Man (PS2).
- [blender3d_xeios](https://github.com/boringhexi/blender3d_xeios) - Blender importer for Xeios engine games including Gitaroo Man (PS2) and まげる つける はしーる.

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
- [libgcl](https://github.com/Jayveer/libgcl) - Attempt at reversing the libgcl library used in Metal Gear Solid 4. Expected to be compiled on Big Endian architecture as per the original.
- [MGS-KMD-Noesis](https://github.com/Jayveer/MGS-KMD-Noesis) - Noesis Plugin for Metal Gear Solid PS1 Model (KMD) and Animation (OAR) files
- [MGS2 HZX Format](https://github.com/GirianSeed/mgs2/blob/trunk/source/include/fmt_hzx.h) - Documentation for Metal Gear Solid 2 HZX (Hazard) map navigation format including patrol routes, navmesh, triggers, cameras, and spatial zones.
- [MGS-MDL-Noesis](https://github.com/Jayveer/MGS-MDL-Noesis) - Noesis plugin for importing Metal Gear Solid 3 MDL models and MTAR animations.
- [DAR Archive Editor (Metal Gear Solid 2: Sons of Liberty)](https://www.moddb.com/games/metal-gear-solid-2-sons-of-liberty/downloads/dar-archive-editor)

#### Silent Hill

- [silent-hill-decomp (decomp)](https://github.com/Vatuu/silent-hill-decomp) - Matching decompilation of Silent Hill (PS1, US 1.1).
- [sh2SaveTools](https://github.com/TheMachineAmbassador/sh2SaveTools) - Save file tools for Silent Hill 2.

#### Fatal Frame

- [himuro (decomp)](https://github.com/mikompilation/himuro) - Matching decompilation of Fatal Frame (PS2).
- [minakami (decomp)](https://github.com/mikompilation/minakami) - Matching decompilation of Fatal Frame 2 (PS2).
- [SH2Unpack](https://github.com/SamusAranX/SH2Unpack) - Unpacker for Silent Hill 2 archive files.
- [SilentHillOrigins_PS2_AudioExtractor](https://github.com/iluny1/SilentHillOrigins_PS2_AudioExtractor) - Audio extractor for Silent Hill Origins (PS2).
- [sh3redux](https://github.com/Palm-Studios/sh3redux) - Silent Hill 3 archive extraction and modification tools.
- [Castlevania](https://github.com/Sparagas/Castlevania) - Castlevania reverse engineering file formats documentation and tools.
- [Sparagas/Silent-Hill](https://github.com/Sparagas/Silent-Hill) - Reverse engineering research and documentation for Silent Hill file formats.
- [Murugo/Misc-Game-Research (Silent Hill 2)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Silent%20Hill%202%2B3) - Reverse engineering notes for Silent Hill 2 & 3 (PS2).
- [Silent Hill Museum](https://silenthillmuseum.org/) - Website dedicated to Silent Hill series with file format documentation.
- [dreamingmoths/silent-hill-museum](https://github.com/dreamingmoths/silent-hill-museum) - Repository for Silent Hill Museum website with technical documentation.
- [Silent-Hill-2-Enhancements](https://github.com/elishacloud/Silent-Hill-2-Enhancements) - Project to enhance Silent Hill 2 (PC) graphics and audio, includes scripts to build or modify SH2 audio files (SFX, BGM, Dialog).
- [mgs_reversing (decomp)](https://github.com/FoxdieTeam/mgs_reversing) - Matching decompilation of Metal Gear Solid (PSX).

#### Castlevania

- [cv64 (decomp)](https://github.com/k64ret/cv64) - Matching decompilation of Castlevania (N64).
- [cvaos (decomp)](https://github.com/testyourmine/cvaos) - Matching decompilation of Castlevania: Aria of Sorrow.
- [sotn-decomp (decomp)](https://github.com/xeeynamo/sotn-decomp) - Matching decompilation of Castlevania: Symphony of the Night (PSX, PSP, Saturn).

### Kuju London

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

### Larian Studios

#### Baldur's Gate 3

- [Norbyte's Baldur's Gate 3 Script Extender](https://github.com/Norbyte/bg3se) - Baldur's Gate 3 Script Extender.
- [Native Mod Loader](https://www.nexusmods.com/baldursgate3/mods/944) - Native DLL plugin loader for Baldur's Gate 3.
- [BG3-DialogsBinary-Node-Editor](https://github.com/kitmods/BG3-DialogsBinary-Node-Editor) - Node-based editor for Baldur's Gate 3 dialog binary files.

#### Divinity: Original Sin 2

- [DoS-2-Savegame-Editor](https://github.com/NovFR/DoS-2-Savegame-Editor) - Save game editor for Divinity: Original Sin 2.
- [LSLib](https://github.com/Norbyte/lslib) - Tools for manipulating Divinity Original Sin and Baldur's Gate 3 files including archive extraction.
- [Norbyte's Divinity Script Extender](https://github.com/Norbyte/ositools) - Divinity: Original Sin 2 script extender toolkit adding features to the scripting language of the game.

### Level-5

- [dcdecomp (decomp)](https://github.com/adubbz/dcdecomp) - Matching decompilation of Dark Cloud (PS2).
- [Inazuma-Eleven-Toolbox](https://github.com/SwareJonge/Inazuma-Eleven-Toolbox) - Toolbox for Inazuma Eleven game files.
- [Metanoia](https://github.com/Ploaj/Metanoia) - Model viewer and research tool for Level-5 games.
- [MeltyTool (Level5)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/Level5) - Level-5 format viewer/exporter for games like Dark Cloud and Professor Layton.
- [Albatross](https://github.com/Tiniifan/Albatross) - Game editor for Yo-Kai Watch series. Modifies game data files (yokai tribe, attacks, soultimates) for Yo-Kai Watch, Yo-Kai Watch 2 (BF/FS/PS), Yo-kai Watch 3, and Yo-kai Watch Blasters.
- [blender-ymd-io](https://github.com/hinadevi/blender-ymd-io) - Blender addon for decompiling .ez files and converting .ymd files to Blender. Supports Level-5 YMD model format.
- [CfgBinEditor](https://github.com/Tiniifan/CfgBinEditor) - Level 5 Bin Editor
- [EnumaLimunada](https://github.com/Tiniifan/EnumaLimunada) - Converter for Inazuma Eleven GO models. Converts IEGO CS/Galaxy model formats to IEGO format.
- [Fougere](https://github.com/Tiniifan/Fougere) - Level-5 games tool.
- [GetNPCPos](https://github.com/Tiniifan/GetNPCPos) - Converting minimap coordinates to real NPC positions in Level-5 games
- [IEGOFormationEditor](https://github.com/Tiniifan/IEGOFormationEditor) - Formation editor for Inazuma Eleven GO series. Edit formations and strategies for Inazuma Eleven GO, Chrono Stone, and Galaxy.
- [InazumaElevenGoMapenv](https://github.com/Tiniifan/InazumaElevenGoMapenv) - Compiler and decompiler for mapenv files used in Inazuma Eleven GO games.
- [InazumaElevenGoScript](https://github.com/Tiniifan/InazumaElevenGoScript) - Documentation and research on Squirrel scripts used in Inazuma Eleven GO games. Covers script format, event system, and reverse engineering notes.
- [InazumaElevenMapEventEditor](https://github.com/Tiniifan/InazumaElevenMapEventEditor) - Map event editor for Inazuma Eleven GO games.
- [InazumaElevenSaveEditor](https://github.com/Tiniifan/InazumaElevenSaveEditor) - Save editor for Inazuma Eleven GO series. Supports Inazuma Eleven GO, Chrono Stone, and Galaxy.
- [InazumaDSEditor](https://github.com/NielsHotweels/InazumaDSEditor) - ROM editor for Inazuma Eleven 1 and 2 (NDS). Edit player data from unitbase.dat, unitbase.STR, and unitstat.dat directly in ROM.
- [inz_cond](https://github.com/Tiniifan/inz_cond) - Condition compiler and decompiler for Level-5 3DS games. Converts Base64-encoded condition data to human-readable C/Squirrel code and back. Supports Inazuma Eleven GO condition system.
- [level5_material](https://github.com/Tiniifan/level5_material) - Convert .mtr to .json and back
- [Level5Outline](https://github.com/Tiniifan/Level5Outline) - Converter for Level-5 outline files. Converts .sil (XCSL) format to JSON and back for easier editing.
- [Level5ResourceEditor](https://github.com/Tiniifan/Level5ResourceEditor) - Level-5 Resource Editor (RES.bin)
- [Lynx](https://github.com/Tiniifan/Lynx) - Comprehensive game editor for Inazuma Eleven GO Light and Shadow. Includes charabase editor, charaparam editor, shop editor, skill editor, script editor, map viewer, and save editor.
- [mini_map_converter](https://github.com/Tiniifan/mini_map_converter) - Mini map converter for Inazuma Eleven GO series. Converts mini map formats between IEGO and CS/Galaxy versions.
- [MyTagsIE](https://github.com/Tiniifan/MyTagsIE) - Enhanced tag definitions for CfgBinEditor. Provides labeled field names for editing .cfg.bin files from Inazuma Eleven GO games.
- [Nyanko](https://github.com/Tiniifan/Nyanko) - Level 5 Text Editor
- [Ocelot](https://github.com/Tiniifan/Ocelot) - Map event editor for Inazuma Eleven GO Light & Shadow. Edit map information, events, NPCs, and heal points with visual interface.
- [Pingouin](https://github.com/Tiniifan/Pingouin) - Level 5 Archive File Manager
- [projectz](https://github.com/Tiniifan/projectz) - Modding template and toolkit for Inazuma Eleven GO Light/Shadow. Provides template for modifying code.bin, enhancement patches, and game documentation. Includes Squirrel scripting engine integration.
- [Strikers2013Editor](https://github.com/obluda3/Strikers2013Editor) - Modding tool and save editor for Inazuma Eleven GO Strikers 2013. Edit moves and player information.
- [studio_eleven](https://github.com/Tiniifan/studio_eleven) - Blender addon for Level-5 3DS file formats. Supports XPRM (3D mesh), XPCK (archives), XMTN (bone animation), XIMA (UV animation), XMTM (material animation), and XCMA (camera) formats. Games: Inazuma Eleven GO series, Yo-Kai Watch series, Professor Layton vs. Phoenix Wright.
- [StudioElevenLib](https://github.com/Tiniifan/StudioElevenLib) - Additional C# library for files supported by the Studio Eleven Blender Addon
- [UltimateGalaxyRandomizer](https://github.com/Tiniifan/UltimateGalaxyRandomizer) - Randomizer for Inazuma Eleven GO Galaxy. Randomizes player elements, positions, move power, and other game elements.
- [ie3ogres (decomp)](https://github.com/CacaBueno64/ie3ogres) - Matching decompilation of Inazuma Eleven 3 - Sekai e no Chousen: The Ogre!! (NDS).
- [yw-cond](https://github.com/n123git/yw-cond) - Web-based UI and toolkit for parsing, decompiling, analyzing and generating Yo-kai Watch Conds (CExpressions). Supports Yo-kai Watch franchise condition system with more complex features than Inazuma Eleven GO.
- [XtractQuery](https://github.com/onepiecefreak3/XtractQuery) - Command-line tool to decompile and recompile script files (.xq, .xs) from Level-5 3DS games and (.cq, .lb, .gds) from Level-5 NDS games.

### Lionhead Studios

- [bw2-unstuff](https://github.com/openblack/bw2-unstuff) - Unpacker for Black & White 2 archive files.

### Metropolis Software

#### Gorky 17

- [Gorky 17 *.dat and *.kdt extractor tool](https://www.moddb.com/games/gorky-17/downloads/gorky-17-dat-and-kdt-extractor-tool) - Extractor tool for *.dat and*/.kdtr files. You can now extract the contents of these data containers. I'm started to working on the gui version of the program that will supports more filetypes and will include a scripter, updated extractor - builder, you will be able to pl...

### Microsoft Studios / Bungie / Turn 10

- [XbTool](https://github.com/Thealexbarney/XbTool) - Tool for working with Xbox file formats.
- [XbxDeTool](https://github.com/Nenkai/XbxDeTool) - Xbox file format tool.

#### Halo

- [KSoft](https://github.com/KornnerStudios/KSoft) - Toolkit for working with Halo engine file formats.
- [ekur](https://github.com/TheHaloArchive/ekur) - Blam! engine (Halo) format library and research tools.
- [Reclaimer](https://github.com/Gravemind2401/Reclaimer) - Halo asset extraction and analysis tool supporting Halo 1, 2, 3, 4, Reach, and Online.
- [IndexV2](https://github.com/Wildenhaus/IndexV2) - Tool for Halo: Combat Evolved Anniversary and Halo 2 Anniversary that extracts textures, models, and more.
- [h5_dumper](https://github.com/Surasia/h5_dumper) - Simple tag dumper for Halo 5 and Halo 5 Forge written in Rust. Recursively goes through each .module file in directory and writes tags to specified path.
- [HaloWarsDocs](https://github.com/HaloMods/HaloWarsDocs) - Documentation and 010 Editor templates for modding Halo Wars 1 and 2.
- [XTraction - Halo 3/ODST texture extractor](https://www.moddb.com/games/halo-3/downloads/xtraction-halo-3-odst-texture-extractor-tool) - Versatile texture extractor for Halo 3 and ODST. Extracts textures from MAP files as TIFF images, enabling editing and replacement of Halo 3 era textures. Originally created for WMClan members.
- [Stream Ripping Tools - Halo 3/4/ODST/CEA/HR Game Asset Extractors Converters Kit](https://www.moddb.com/games/halo-2/downloads/stream-ripping-tools-game-asset-extractors-converters-kit) - Large collection of tools for extracting, modding, and converting game assets from up to 2100 games. Includes Halo 3/2/4/ODST/Reach tools. Contains help instructions, documentation, and links to sources.
- [Halo2 Gravemind Tool Extractor v1.6B](https://www.moddb.com/games/halo-2/downloads/halo2-gravemind-tool-extractor) - Extractor tool for Halo 2 assets including models, sounds, textures, and maps (v1.6B).
- [Bonobo [Version 1.0.0.3] Halo2/3/ODST/Reach Animation Extractor](https://www.moddb.com/games/halo-2/downloads/bonobo-version-1003) - Animation extractor for Halo 2, 3, ODST, and Reach (v1.0.0.3).
- [Composer Halo 4 Audio Extractor](https://www.moddb.com/games/halo-4/downloads/composer-halo-4-audio-extractor) - Tool used with QuickBMS to extract and convert Halo 4's .XMA audio files to WAV format. Includes all necessary tools and documentation.
- [3ds Max GBX Importer (Halo CE)](https://www.moddb.com/downloads/3ds-max-gbx-importer-halo-ce) - 3DS Max plugin for importing Halo: Combat Evolved GBX model formats.
- [noclip.website (Halo: Combat Evolved)](https://github.com/magcius/noclip.website/tree/main/src/Halo1) - In-browser Halo: Combat Evolved viewer.
- [Halo 2 Xbox Modding Tools](https://www.moddb.com/games/halo-2/downloads/halo-2-xbox-modding-tools) - Collection of 5 tools for modding Xbox Halo 2 maps.
- [Halo CE Batch Bitmap Extractor](https://www.moddb.com/downloads/halo-ce-batch-bitmap-extractor)

#### Destiny

- [alkahest](https://github.com/cohaereo/alkahest) - Multi-tool for viewing Destiny 2 assets, with a focus on an accurate recreation of the renderer. Supports Tiger engine formats.
- [tiger-pkg](https://github.com/v4nguard/tiger-pkg) - Destiny 1/2 package library and tools (unpacker, verification). Supports Destiny 1 (Internal Alpha, The Taken King, Rise of Iron), Destiny 2 (Beta through Edge of Fate), and Marathon. Handles PKG files across PS3, PS4, X360, XONE, and Windows platforms.
- [quicktag](https://github.com/v4nguard/quicktag) - Destiny 1/2 package file data structure explorer. Scans and analyzes Tiger engine structure files (8080 files) to discover structures, patterns, strings, and more. Features tag viewer, localized/raw strings browser, and asset preview for textures and Wwise audio streams.
- [Charm](https://github.com/cohaereo/Charm) - Destiny 2 reverse engineering tool for extracting assets from game files. Supports multiple Tiger engine versions and Destiny 2 game versions (Shadowkeep through Lightfall). Focuses on providing access to information in game files for artists and content preservation.
- [d2-map-importer-addon](https://github.com/DeltaDesigns/d2-map-importer-addon) - Blender 4.0+ addon for importing Destiny 2 rips from Charm. Assembles maps (statics, dynamics, lights, terrain), auto-assigns gear shaders and textures to player gear, compatible with DARE/DCG skeletons and IK Player Skeleton.
- [Destiny-Collada-Generator](https://github.com/DeltaDesigns/Destiny-Collada-Generator) - Tool to generate Collada files of items from Destiny 2 via web/mobile API. Exports geometry, mesh weights, UV coordinates, normals, tangents, vertex colors, and dye slots. Generates textures in PNG format and shader parameter lists.
- [SBox-Destiny-2-Map-Importer](https://github.com/DeltaDesigns/SBox-Destiny-2-Map-Importer) - Tool for importing ripped Destiny 2 maps from Charm into S&Box Hammer. Imports maps with materials, shaders, and models into S&Box scenes.
- [MIDA](https://github.com/DeltaDesigns/MIDA) - Fork of Charm designed for Marathon. Tool for extracting assets from Marathon game files, focused on artists and content preservation. Supports Marathon Closed Alpha. Note: Most features currently non-functional, development status uncertain.
- [destinydocs](https://github.com/cohaereo/destinydocs) - Documentation for Destiny 1/2 internals.
- [DestinyDocs](https://github.com/MontagueM/DestinyDocs) - Documentation on Destiny game files, particularly for recent versions of Destiny 2. Includes Charm wiki, engine overview, and tag format explanations.
- [D2StaticDocs](https://github.com/nblockbuster/D2StaticDocs) - Documentation on the Destiny 2 Beyond Light static model format. Covers main model files, subfiles, material tables, and loadzone structures.
- [destinypkgtool](https://github.com/v4nguard/destinypkgtool) - Rust library and tools for working with Destiny 1 pkg files (unpacker, verification).
- [ddkf](https://github.com/v4nguard/ddkf) - Destiny Decryption Key Finder.
- [DestinyUnpackerCPP](https://github.com/nblockbuster/DestinyUnpackerCPP) - C++ unpacker for Destiny 1 (PS4/PS3/X360) and Destiny 2 PC packages. Supports WEM conversion, TXTP generation, hex ID naming, and music-only extraction. See also [MontagueM/DestinyUnpackerCPP](https://github.com/MontagueM/DestinyUnpackerCPP) for the original version.
- [destiny-unpacker-rs](https://github.com/nblockbuster/destiny-unpacker-rs) - Rust implementation of Destiny unpacker (archived).
- [D2StaticExtractor](https://github.com/nblockbuster/D2StaticExtractor) - Static model extraction tool that converts Destiny 2 static models into FBX files. Supports Beyond Light and later versions. Note: Superseded by Charm, but still useful for specific use cases (archived).
- [D2TextureRipper](https://github.com/nblockbuster/D2TextureRipper) - Batch texture and image ripper for Destiny 2. Supports versions 1.0.0.1 through 4.0.0.1 (The Witch Queen). Extracts textures from package files with batch processing support.
- [MontevenDynamicExtractor](https://github.com/nblockbuster/MontevenDynamicExtractor) - Fork of MDE for extracting Destiny 2 dynamic models to FBX. Supports textures, skeletons, weighted models, and batch extraction. See also [MontagueM/MontevenDynamicExtractor](https://github.com/MontagueM/MontevenDynamicExtractor) for the original version.
- [Destiny-API-Ripper-Extension](https://github.com/nblockbuster/Destiny-API-Ripper-Extension) - Extension and GUI for Destiny Collada Generator and Monteven Dynamic Extractor. Provides automated workflow for extracting Destiny 2 assets via API.
- [Destiny-Collada-Generator](https://github.com/nblockbuster/Destiny-Collada-Generator) - Fork of tool to generate Collada files of items from Destiny 2 via web/mobile API. Exports geometry, mesh weights, UV coordinates, normals, tangents, vertex colors, and dye slots. See also [DeltaDesigns/Destiny-Collada-Generator](https://github.com/DeltaDesigns/Destiny-Collada-Generator) for the maintained version.
- [DestinyOSTListGen](https://github.com/nblockbuster/DestinyOSTListGen) - Tool to generate a list (OSTs.db) of all GinsorIDs of music from Destiny. Uses WwiseParser to parse soundbanks. Supports comparison with previous lists and SFX filtering.
- [DestinyWwiseParserScript](https://github.com/nblockbuster/DestinyWwiseParserScript) - Python script to create and parse JSON files created by WwiseParser, specialized for Destiny and Destiny 2. Supports automatic WAV export and version switching (D1/pre-BL).
- [bungie-lua-decompiler](https://github.com/nblockbuster/bungie-lua-decompiler) - Tool to decompile Bungie's Lua scripts found in the Destiny 1 Alpha with format 14.

#### Gears of War

- [Gears of War Map Cooker Tool for Newbies](https://www.moddb.com/mods/gears-multiplayer-enhancement-mod/downloads/gears-of-war-map-cooker-tool-for-newbies) - .NET application for simplifying map cooking for H.I.V.E Mode and Multiplayer Enhancement Mod.

#### Forza

- [ForzaTech-extraction-tools](https://github.com/Doliman100/ForzaTech-extraction-tools) - Documentation and tools for ForzaTech .carbin and .modelbin file structures.

#### Age of Empires

- [Audio Modding Guide (AoE2DE)](https://steamcommunity.com/sharedfiles/filedetails/?id=1915891079) - Comprehensive tutorial for audio modding in Age of Empires II: Definitive Edition.
  - Topics: Scenario triggers, SFX replacement, music, voice-overs, taunts, data file editing with Wwise audio system.
  - Tools: Ravioli Tools, vgmstream, Advanced Genie Editor.
- [halo (decomp)](https://github.com/halo-re/halo) - Matching decompilation of Halo: Combat Evolved (Xbox).

### Mobius Digital

- [noclip.website (Outer Wilds)](https://github.com/magcius/noclip.website/tree/main/src/OuterWilds) - In-browser Outer Wilds viewer.

### Midway

- [revenge (decomp)](https://github.com/svinsmoke212/revenge) - Matching decompilation of WCW/nWo Revenge (N64).

#### Area 51

- [engine-51](https://github.com/bigianb/engine-51) - Experimental tools for Area 51 (2005) engine.

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

#### F.E.A.R

- [F.E.A.R. 3dsmax 7 model import plugin](https://www.moddb.com/games/fear/downloads/3dsmax-7-model-import-plugin)
- [F.E.A.R. 2 unofficial extraction tools](https://www.moddb.com/games/fear-2/downloads/fear-2-unofficial-extraction-tools) - Unofficial tools for extracting F.E.A.R. 2 archives, textures, and sounds.
- [FEAR Online 3dsmax script (F.E.A.R. 2)](https://www.moddb.com/games/fear-2/downloads/fear-online-3dsmax-script)
- [Video Tutorial: 3DSMax Plugin (F.E.A.R.)](https://www.moddb.com/games/fear/downloads/video-tutorial-3dsmax-plugin)
- [FEAR Database Extractor](https://www.moddb.com/games/fear/downloads/fear-database-extractor)
- [FEAR Public Tools v2](https://www.moddb.com/games/fear/downloads/fear-public-tools-v2) - FEAR sdk v2, allows making singleplayer levels on the Steam version
- [FEAR Tweaking Tool and Guide](https://www.moddb.com/games/fear/downloads/fear-tweaking-tool-and-guide) - Designed to squeeze more FPS from the game without doing any drastic changes.
- [ltar](https://github.com/cmbasnett/ltar) - Python CLI for I/O on LTAR archive files found in games using the Lithtech Jupiter engine.
- [Lithtech Jupiter Ex FX Decompiler (F.E.A.R.)](https://www.moddb.com/games/fear/downloads/lithtech-jupiter-ex-fx-decompiler)

#### Trespasser

- [Blender 2.6 Trespasser Exporter](https://www.moddb.com/games/trespasser/downloads/blender-26-trespasser-exporter-10) - Rewrite of the exporter to work with Blender 2.6 . This script exports models into trespasser formats. Supports writting TPM files as well as values.txt files. Also adds UI elements to configurate the export easily. For the individual types of meshes a basic set of values is exported. For meshes,...
- [Blender3D Trespasser Exporter 1.0](https://www.moddb.com/games/trespasser/downloads/blender3d-trespasser-exporter-10) - Blender script for exporting models to Trespasser formats. Exports TPM files and values.txt files with mesh type filtering (v1.0).

#### Blood

- [BLOOD ULTIMATE BUNDLE TOOLS KIT](https://www.moddb.com/mods/blood-modern-voxels-pak-for-mappers-and-moders/downloads/blood-ultimate-bundle-tools-kit) - A complete collection of editors for creating your own mod or even a full-fledged Total Conversion.
- [BLOOD UNOFFICIAL TOOLS](https://www.moddb.com/games/blood/downloads/blood-unofficial-tools) - Unofficial toolkit for Blood with documentation for DOS tools (Mapedit, EditArt, ArEdit). Includes professional-style documentation for users of DOS tools or those seeking nostalgia.
- [Spill Some: The Blood Tool](https://www.moddb.com/games/blood/downloads/spill-some-the-blood-tool) - Launcher and demo utility for Blood/Cryptic Passage running under DOS/DOSBox. Enables playback of user-recorded demo files by automatically renaming default demos.

#### Blood 2: The Chosen

- [Updated 3dsmax plugin (Blood 2: The Chosen)](https://www.moddb.com/games/blood-2-the-chosen/downloads/updated-3dsmax-plugin) - Updated 3dsmax plugin for Blood 2 and Shogo. Obtained from Monolith's old FTP server
- [Blood 2 Modding tools](https://www.moddb.com/games/blood-2-the-chosen/downloads/blood-2-modding-tools) - Complete modding toolkit for Blood 2: The Chosen, including ABC exporter and other essential tools.
- [Blood 2 Toolset 64 bit fix](https://www.moddb.com/games/blood-2-the-chosen/downloads/blood-2-toolset-64-bit-fix) - 64-bit compatible version of Blood 2 toolset. The default installer doesn't work on 64-bit Windows, so these are the extracted files.
- [Milkshape ABC Plugin (Blood 2: The Chosen)](https://www.moddb.com/games/blood-2-the-chosen/downloads/milkshape-abc-plugin) - Milkshape ABC plugin for Blood 2. Includes import/export plugins

#### No One Lives Forever

- [Lithtech Jupiter Maya/3dsmax plugins (No One Lives Forever 2)](https://www.moddb.com/games/no-one-lives-forever-2-a-spy-in-harm/downloads/lithtech-jupiter-maya3dsmax-plugins) - Collection of Lithtech Jupiter model and level import/export plugins for 3DS Max 3-7 and Maya 4-7.
- [Lithtech 2.2 toolset (No One Lives Forever)](https://www.moddb.com/games/no-one-lives-forever/downloads/lithtech-22-toolset) - Updated version of the Lithtech 2.0 tools with enhancements including .lta support and rebinding buttons (v2.2).
- [NOLF Tools (No One Lives Forever)](https://www.moddb.com/games/no-one-lives-forever/downloads/nolf-tools) - Official modding tools for No One Lives Forever.
- [No One Lives Forever 2 Toolkit](https://www.moddb.com/games/no-one-lives-forever-2-a-spy-in-harm/downloads/no-one-lives-forever-2-toolkit) - Complete toolkit for No One Lives Forever 2 including editing tools and source code. Provided as-is without official support.

#### Shogo: Mobile Armor Division

- [Shogo Mobile Armor Division Modding Tools](https://www.moddb.com/games/shogo-mobile-armor-division/downloads/shogo-mobile-armor-division-modding-tools) - Modding tools for Shogo Mobile Armor Division. Includes help for Shogo API:s used in the Source Code.
- [Shogo tools 64 bit](https://www.moddb.com/games/shogo-mobile-armor-division/downloads/shogo-tools-64-bit) - 64-bit compatible SDK files for Shogo: Mobile Armor Division. The official SDK installer only works on 16-bit and 32-bit systems, so these are the extracted files for 64-bit systems.

#### Serious Sam

- [SeriousSaveEditor](https://github.com/widberg/SeriousSaveEditor) - Save editor for Serious Sam games.

### Monolith Soft

*Japanese studio (distinct from Monolith Productions, USA).*

#### Xenoblade Chronicles

- [xenoblade (decomp)](https://github.com/xbret/xenoblade) - Matching decompilation of Xenoblade Chronicles (Wii, JP).
- [XenoTools](https://github.com/Nenkai/XenoTools) - Tools for Xenoblade Chronicles file formats.
- [bdat-rs](https://github.com/roccodev/bdat-rs) - Rust library for reading and writing BDAT format used in Xenoblade Chronicles games for data tables.
- [xcnx-file-loader](https://github.com/roccodev/xcnx-file-loader) - File replacement mod for Switch Xenoblade games allowing custom files to be loaded from RomFS instead of ARD archives.
- [ard-tools](https://github.com/roccodev/ard-tools) - Tools for working with ARD/ARH archive files from Switch Xenoblade Chronicles games. Includes ardain library, ard-tools CLI, and fuse-ard FUSE driver.

### Oddworld Inhabitants

- [Asset Tool (Oddworld: Abe's Exoddus)](https://www.moddb.com/games/oddworld-abes-exoddus/downloads/asset-tool) - Tool for converting Oddworld: Abe's Exoddus cutscenes to MP4 and previewing/exporting sprites from both Abe's Oddysee and Abe's Exoddus. Requires level files from both games, the tool, and ffmpeg.exe.
- [Sprite / CAM Extractor (Oddworld: Abe's Exoddus)](https://www.moddb.com/games/oddworld-abes-exoddus/downloads/sprite-cam-extractor) - Application for converting "cam" files from the PC versions of Oddworld: Abe's Exoddus and Oddworld: Abe's Oddysee.

### Naughty Dog

#### Crash Bandicoot 1-3 & CTR

- [ReBandicoot](https://github.com/kohtep/ReBandicoot) - Reverse engineering tools for Crash Bandicoot.
- [Crash-Bandicoot-Resources](https://github.com/Helias/Crash-Bandicoot-Resources) - Comprehensive collection of resources for Crash Bandicoot file formats and reverse engineering. Covers N. Sane Trilogy, Twinsanity, Crash Team Racing, Crash Bash, and original PS1 trilogy. Includes documentation for extracting/modifying PAK archives, IGZ models, NSD/NSF files, plus links to 30+ specialized tools, character mods, decompilation projects, and modding frameworks.
- [CTR-tools](https://github.com/CTR-tools/CTR-tools) - Toolkit for Crash Team Racing (PlayStation 1) file formats.
- [CrashEdit](https://github.com/cbhacks/CrashEdit) - Level and graphics editor for PlayStation 1 Crash Bandicoot games.
- [drnsf](https://github.com/cbhacks/drnsf) - Format research tool for Naughty Dog games including Crash.
- [crash-bandicoot-nsf](https://github.com/dehodson/crash-bandicoot-nsf) - NSF (Naughty Dog Streaming File) format tools for Crash Bandicoot.
- [Crash-Bandicoot-2-Modelexport](https://github.com/warenhuis/Crash-Bandicoot-2-Modelexport) - Model exporter for Crash Bandicoot 2.
- [crashutils](https://github.com/wurlyfox/crashutils) - Collection of utilities for Crash Bandicoot file formats.
- [noclip.website (Crash Bandicoot: Warped)](https://github.com/magcius/noclip.website/tree/main/src/CrashWarped) - In-browser Crash Bandicoot: Warped viewer.
- [c2c (decomp)](https://github.com/ughman/c2c) - Matching decompilation of Crash Bandicoot 2: Cortex Strikes Back.
- [crash-ps2 (decomp)](https://github.com/calmsacibis995/crash-ps2) - Matching decompilation of Crash Bandicoot: The Wrath of Cortex (PS2).

#### Spyro the Dragon

- [spyroedit](https://github.com/LXShades/spyroedit) - Emulator plugin for modifying Spyro the Dragon games on PlayStation 1. Compatible with Windows emulators such as ePSXe and PCSX. Features include editing level textures and colors, replacing level skies, modifying object properties, and editing scenery positions.
- [spyro-1 (decomp)](https://github.com/TheMobyCollective/spyro-1) - Matching decompilation of Spyro the Dragon.

#### Jak and Daxter

- [jak1-vag-splitter](https://github.com/blahpy/jak1-vag-splitter) - Tool for splitting VAG audio files from Jak and Daxter 1.
- [JakAndDaxter1Sound](https://github.com/efimandreev0/JakAndDaxter1Sound) - Sound extraction and playback tool for Jak and Daxter 1.
- [Blender-Script-JaD-Actors](https://github.com/innocentmiau/Blender-Script-JaD-Actors) - Blender script for importing Jak and Daxter actor models.
- [JakAudioTools](https://github.com/jwetzell/JakAudioTools) - Audio extraction and conversion tools for Jak and Daxter series.
- [JakAudioTool](https://github.com/LuminarLight/JakAudioTool) - GUI tool for working with Jak and Daxter audio files.
- [CTR-ModSDK (decomp)](https://github.com/CTR-tools/CTR-ModSDK) - Matching decompilation of Crash Team Racing (PS1).

### NanaOn-Sha

- [parappa2 (decomp)](https://github.com/parappadev/parappa2) - Matching decompilation of PaRappa the Rapper 2 (PS2).
- [open-ribbon (decomp)](https://github.com/open-ribbon/open-ribbon) - Matching decompilation of VIB Ribbon (PS1, PAL).
- [Murugo/Misc-Game-Research (Vib-Ribbon)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS1/Vib-Ribbon) - Reverse engineering notes for Vib-Ribbon (PS1).

### Nintendo EAD

*First-party Nintendo titles. Many GameCube/Wii games use [JSYSTEM](#jsystem-gamecubewii) middleware.*

#### Animal Crossing

*See also [JSYSTEM](#jsystem-gamecubewii) for additional format tools used in this game.*

- [010Editor-AnimalCrossing-Templates](https://github.com/Cuyler36/010Editor-AnimalCrossing-Templates) - Binary templates for analyzing Animal Crossing file formats in 010 Editor.
- [AC-Audiobank-Dumper](https://github.com/Cuyler36/AC-Audiobank-Dumper/tree/main/AC%20Audiobank%20Dumper) - Tool for extracting audio from Animal Crossing audio banks.
- [ACNESCreator](https://github.com/Cuyler36/ACNESCreator) - NES ROM editor for Animal Crossing.
- [LibACNH](https://github.com/Slattz/LibACNH) - C++ library for parsing file formats and algorithms used by Animal Crossing: New Horizons.
- [ACSE](https://github.com/Cuyler36/ACSE) - Animal Crossing Save Editor for GameCube.
- [Animal-Crossing-Model-Editor](https://github.com/Cuyler36/Animal-Crossing-Model-Editor) - 3D model editor for Animal Crossing.
- [Animal-Crossing-Texture-Editor](https://github.com/Cuyler36/Animal-Crossing-Texture-Editor) - Texture editing tool for Animal Crossing.
- [Cross-View](https://github.com/Cuyler36/Cross-View) - Model viewer for Animal Crossing.
- [RELDumper](https://github.com/Cuyler36/RELDumper) - Tool for dumping REL files from Animal Crossing.
- [af (decomp)](https://github.com/zeldaret/af) - Matching decompilation of Animal Forest.
- [ac-decomp (decomp)](https://github.com/acreteam/ac-decomp) - Matching decompilation of Animal Crossing (GameCube).
- [afe-decomp (decomp)](https://github.com/acreteam/afe-decomp) - Matching decompilation of Animal Forest e+ (JP).

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
- [LuigisMansion_Ghidra_NTSC](https://github.com/Sage-of-Mirrors/LuigisMansion_Ghidra_NTSC) - Ghidra project for the NTSC-U version of Luigi's Mansion for the Nintendo GameCube.
- [SuperLM](https://github.com/Sage-of-Mirrors/SuperLM) - Library for working with the BIN and MP formats found in Luigi's Mansion.
- [noclip.website (Luigi's Mansion)](https://github.com/magcius/noclip.website/tree/main/src/LuigisMansion) - In-browser Luigi's Mansion viewer.

#### Pikmin

*See also [JSYSTEM](#jsystem-gamecubewii) for additional format tools used in this game.*

- [pikmin (decomp)](https://github.com/projectPiki/pikmin) - Matching decompilation of Pikmin.
- [pik2wii (decomp)](https://github.com/projectPiki/pik2wii) - Matching decompilation of New Play Control! Pikmin 2 (Wii, USA).
- [pikmin2 (decomp)](https://github.com/projectPiki/pikmin2) - Matching decompilation of Pikmin 2 (GameCube, USA).
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

#### Mario Artist

*Mario Artist series (Nintendo 64DD Disk Drive).*

- [leotools](https://github.com/jkbenaim/leotools) - Toolkit for extracting and working with 64DD disk images.
- [leo64dd_python](https://github.com/LuigiBlood/leo64dd_python) - Python-based tools for 64DD disk manipulation.
- [mfs_manager](https://github.com/LuigiBlood/mfs_manager) - Manager for MFS (Multi File System) used on 64DD disks.
- [MeltyTool (MarioArtist)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/MarioArtist) - Format viewer and exporter for Mario Artist series.
- [ma3d1toOBJ](https://github.com/LuigiBlood/ma3d1toOBJ) - Mario Artist Polygon Studio Model File to OBJ

#### Mario Kart: Double Dash

*See also [JSYSTEM](#jsystem-gamecubewii).*

- [MeltyTool (MarioKartDoubleDash)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/MarioKartDoubleDash) - Format viewer/exporter for Mario Kart Double Dash.
- [mkdd-collision](https://github.com/RenolY2/mkdd-collision) - Tool for viewing and editing collision data in Mario Kart Double Dash.
- [mkdd-track-editor](https://github.com/RenolY2/mkdd-track-editor) - Full-featured track editor for Mario Kart Double Dash.
- [DouBOL-Dash](https://github.com/shibbo/DouBOL-Dash) - BOL file format tool for editing race course layouts in Mario Kart Double Dash.
- [noclip.website (Mario Kart: Double Dash)](https://github.com/magcius/noclip.website/tree/main/src/j3d) - In-browser Mario Kart Double Dash viewer.
- [mkdd (decomp)](https://github.com/doldecomp/mkdd) - Matching decompilation of Mario Kart: Double Dash!!.

#### Super Mario 64

*See also [Fast3d/F3dex](#fast3df3dex-n64).*

- [Quad64](https://github.com/DavidSM64/Quad64) - Level editor for Super Mario 64.
- [MeltyTool (SuperMario64)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/SuperMario64) - Super Mario 64 format viewer/exporter.
- [SM64Paint](https://github.com/Trenavix/SM64Paint) - Texture editor for Super Mario 64.
- [Hack64 Super Mario 64](https://hack64.net/wiki/doku.php?id=super_mario_64) - Documentation for Super Mario 64 formats.
- [sm64 (decomp)](https://github.com/n64decomp/sm64) - Matching decompilation of Super Mario 64.

#### Super Mario 64 DS

- [SM64DSe](https://github.com/Arisotura/SM64DSe) - Level editor for Super Mario 64 DS.
- [SM64DSe-Ultimate](https://github.com/Gota7/SM64DSe-Ultimate) - Enhanced version of SM64DSe.
- [noclip.website (SM64DS)](https://github.com/magcius/noclip.website/tree/main/src/SuperMario64DS) - In-browser Super Mario 64 DS viewer.
- [MeltyTool (SuperMario64Ds)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Games/SuperMario64Ds) - Super Mario 64 DS format viewer/exporter.

#### Super Mario (Other)

*See also [JSYSTEM](#jsystem-gamecubewii) for Super Mario Sunshine and Galaxy.*

- [bba-wd (decomp)](https://github.com/vabold/bba-wd) - Matching decompilation of Big Brain Academy: Wii Degree.
- [bodyharvestdecomp (decomp)](https://github.com/deltaniumindustries/bodyharvestdecomp) - Matching decompilation of Body Harvest (N64).
- [chameleontwistv1.0-jp (decomp)](https://github.com/chameleontwistret/chameleontwistv1.0-jp) - Matching decompilation of Chameleon Twist (N64, JP).
- [doshin-gc (decomp)](https://github.com/break-core/doshin-gc) - Matching decompilation of Doshin the Giant (GameCube).
- [pcopter_wii (decomp)](https://github.com/Bsquo/pcopter_wii) - Matching decompilation of Radio Helicopter (Wii).
- [KinokoDecomp-S (decomp)](https://github.com/Moddimation/KinokoDecomp-S) - Matching decompilation of Captain Toad: Treasure Tracker for Nintendo Switch.
- [drmario64 (decomp)](https://github.com/angheloalf/drmario64) - Matching decompilation of Dr. Mario 64.
- [mariogolf64 (decomp)](https://github.com/monde-lointain/mariogolf64) - Matching decompilation of Mario Golf (N64).
- [mk64 (decomp)](https://github.com/n64decomp/mk64) - Matching decompilation of Mario Kart 64.
- [mkds-re (decomp)](https://github.com/XorTroll/mkds-re) - Reverse engineering work for Mario Kart DS (EU).
- [mkw (decomp)](https://github.com/snailspeed3/mkw) - Matching decompilation of Mario Kart Wii.
- [marioparty (decomp)](https://github.com/mariopartyrd/marioparty) - Matching decompilation of Mario Party.
- [marioparty2 (decomp)](https://github.com/mariopartyrd/marioparty2) - Matching decompilation of Mario Party 2.
- [marioparty3 (decomp)](https://github.com/mariopartyrd/marioparty3) - Matching decompilation of Mario Party 3.
- [marioparty4 (decomp)](https://github.com/mariopartyrd/marioparty4) - Matching decompilation of Mario Party 4.
- [red-pro2 (decomp)](https://github.com/aboood40091/red-pro2) - Matching decompilation of New Super Mario Bros. U v1.3.0 (US).
- [OdysseyDecomp (decomp)](https://github.com/MonsterDruide1/OdysseyDecomp) - Matching decompilation of Super Mario Odyssey for all versions.
- [smstrikers-decomp (decomp)](https://github.com/yannicksuter/smstrikers-decomp) - Matching decompilation of Super Mario Strikers.
- [sms (decomp)](https://github.com/doldecomp/sms) - Matching decompilation of Super Mario Sunshine.
- [smb-tools](https://github.com/PistonMiner/smb-tools) - Tools for Super Mario Bros. file formats.
- [smstools](https://github.com/impiaaa/smstools) - Toolkit for decoding and working with Super Mario Sunshine data files.
- [Bin-editor-improvements](https://github.com/Muzzarino/Bin-editor-improvements) - Enhanced version of miluaces' bin editor for Super Mario Sunshine with fixed orthogonal mode, duplicate/translate/subdivide buttons, improved UI, and Camera Intro editor (WIP).
- [Corona](https://github.com/shibbo/Corona) - Toolkit designed for custom C++ code injection in Super Mario Sunshine. Can be used to create new enemies, objects, bosses, items, and more.
- [flaaffy](https://github.com/arookas/flaaffy) - Audio toolchain for Super Mario Sunshine. Runtime library for loading, utilizing, and playing various audio-related formats with tools and utilities to convert and create these formats.
- [Track-Studio](https://github.com/MapStudioProject/Track-Studio) - Full-featured track and course editor for Mario Kart 8.
- [CTR-Studio](https://github.com/MapStudioProject/CTR-Studio) - Editor for 3DS BCH/BCRES formats used in Mario Kart 7 and other 3DS games.
- [noclip.website (Super Mario Sunshine)](https://github.com/magcius/noclip.website/tree/main/src/j3d) - In-browser Super Mario Sunshine viewer.
- [noclip.website (Super Mario Galaxy)](https://github.com/magcius/noclip.website/tree/main/src/SuperMarioGalaxy) - In-browser Super Mario Galaxy viewer.
- [noclip.website (Super Mario Galaxy 2)](https://github.com/magcius/noclip.website/tree/main/src/SuperMarioGalaxy) - In-browser Super Mario Galaxy 2 viewer.
- [noclip.website (Mario Kart 64)](https://github.com/magcius/noclip.website/tree/main/src/MarioKart64) - In-browser Mario Kart 64 viewer.
- [noclip.website (Mario Kart DS)](https://github.com/magcius/noclip.website/tree/main/src/nns_g3d) - In-browser Mario Kart DS viewer.
- [noclip.website (Mario Kart Wii)](https://github.com/magcius/noclip.website/tree/main/src/MarioKartWii) - In-browser Mario Kart Wii viewer.
- [noclip.website (Mario Kart 8 Deluxe)](https://github.com/magcius/noclip.website/tree/main/src/MarioKart8Deluxe) - In-browser Mario Kart 8 Deluxe viewer.
- [ToadsTool](https://github.com/huderlem/ToadsTool) - Tool for editing Mario Golf: Toadstool Tour files including map containers, text, events, zone headers, entities, and encounters.
- [GSTExtract](https://github.com/shibbo/GSTExtract) - Extracts the data out of .gst files found in Super Mario Galaxy 1 and 2.
- [bea-extract](https://github.com/shibbo/bea-extract) - Extracts BEA files from Super Mario Party.
- [M-LTool](https://github.com/efimandreev0/M-LTool) - Tool to extract archives from Mario & Luigi: Partner's in Time and Mario & Luigi: Bowser's Inside Story (NDS).

#### New Super Mario Bros Wii

- [NSMBW-Decomp (decomp)](https://github.com/NSMBW-Community/NSMBW-Decomp) - Matching decompilation of New Super Mario Bros. Wii.
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
- [EventWaker](https://github.com/Sage-of-Mirrors/EventWaker) - Editor for the map events in The Legend of Zelda: The Wind Waker.
- [Event_List_Editor](https://github.com/Sage-of-Mirrors/Event_List_Editor) - Editor for the event_list.dat files found in The Legend of Zelda: The Wind Waker.

#### Wii Sports

- [wii-ipl (decomp)](https://github.com/koopthekoopa/wii-ipl) - Matching decompilation of Wii Menu.
- [ogws (decomp)](https://github.com/doldecomp/ogws) - Matching decompilation of Wii Sports.
- [noclip.website (Wii Sports)](https://github.com/magcius/noclip.website/tree/main/src/WiiSports) - In-browser Wii Sports viewer.
- [noclip.website (Wii Sports Resort)](https://github.com/magcius/noclip.website/tree/main/src/WiiSports) - In-browser Wii Sports Resort viewer.

#### Star Fox Adventures

- [noclip.website (Star Fox Adventures)](https://github.com/magcius/noclip.website/tree/main/src/StarFoxAdventures) - In-browser Star Fox Adventures viewer.

#### Star Fox 64

- [sf64 (decomp)](https://github.com/sonicdcer/sf64) - Matching decompilation of Star Fox 64.
- [sf64ex](https://github.com/jkbenaim/sf64ex) - Extractor for extracting files from Star Fox 64 ROMs.

#### Star Fox 64 3D

- [SF643D_Tools](https://github.com/thtrandomlurker/SF643D_Tools) - Collection of tools for viewing and potentially modifying data from Star Fox 64 3D.

#### Super Monkey Ball

- [noclip.website (Super Monkey Ball)](https://github.com/magcius/noclip.website/tree/main/src/SuperMonkeyBall) - In-browser Super Monkey Ball viewer.

#### F-Zero

- [fzerox (decomp)](https://github.com/inspectredc/fzerox) - Matching decompilation of F-Zero X.
- [fzerox-expansion-kit (decomp)](https://github.com/inspectredc/fzerox-expansion-kit) - Matching decompilation of F-Zero X Expansion Kit.

#### Chibi-Robo

- [cbr_decomp (decomp)](https://github.com/eavpsp/cbr_decomp) - Matching decompilation of Chibi-Robo! (GameCube).

#### Snowboard Kids

- [sk (decomp)](https://github.com/sonicdcer/sk) - Matching decompilation of Snowboard Kids (N64).
- [snowboardkids2-decomp (decomp)](https://github.com/cdlewis/snowboardkids2-decomp) - Matching decompilation of Snowboard Kids 2 (N64).

#### Wave Race 64

- [wave-race-64 (decomp)](https://github.com/llonsit/wave-race-64) - Matching decompilation of Wave Race 64.

#### The New Tetris

- [tnt (decomp)](https://github.com/kiritodv/tnt) - Matching decompilation of The New Tetris (N64).

#### New Super Mario Bros DS

- [nsmb (decomp)](https://github.com/NSMB-Decomp/nsmb) - Matching decompilation of New Super Mario Bros.
- [noclip.website (New Super Mario Bros DS)](https://github.com/magcius/noclip.website/tree/main/src/nns_g3d) - In-browser New Super Mario Bros DS viewer.

#### Metroid Prime

- [noclip.website (Metroid Prime)](https://github.com/magcius/noclip.website/tree/main/src/MetroidPrime) - In-browser Metroid Prime viewer.
- [DreadGhidraPlugin](https://github.com/duncathan/DreadGhidraPlugin) - Ghidra plugin to assist with reverse engineering Metroid Dread.
- [noclip.website (Metroid Prime 2)](https://github.com/magcius/noclip.website/tree/main/src/MetroidPrime) - In-browser Metroid Prime 2: Echoes viewer.
- [noclip.website (Metroid Prime 3)](https://github.com/magcius/noclip.website/tree/main/src/MetroidPrime) - In-browser Metroid Prime 3: Corruption viewer.
- [noclip.website (Metroid Prime Hunters)](https://github.com/magcius/noclip.website/tree/main/src/MetroidPrimeHunters) - In-browser Metroid Prime Hunters viewer.
- [mzm (decomp)](https://github.com/metroidret/mzm) - Matching decompilation of Metroid: Zero Mission.
- [mf (decomp)](https://github.com/metroidret/mf) - Matching decompilation of Metroid Fusion.
- [prime (decomp)](https://github.com/primedecomp/prime) - Matching decompilation of Metroid Prime.
- [echoes (decomp)](https://github.com/primedecomp/echoes) - Matching decompilation of Metroid Prime 2: Echoes.

#### Pokemon

- [noclip.website (Pokemon Snap)](https://github.com/magcius/noclip.website/tree/main/src/PokemonSnap) - In-browser Pokemon Snap viewer.
- [noclip.website (Pokemon Platinum)](https://github.com/magcius/noclip.website/tree/main/src/nns_g3d) - In-browser Pokemon Platinum viewer.
- [noclip.website (Pokemon HeartGold/SoulSilver)](https://github.com/magcius/noclip.website/tree/main/src/nns_g3d) - In-browser Pokemon HeartGold/SoulSilver viewer.
- [camelotgcdatatool](https://github.com/gamemasterplc/camelotgcdatatool) - Camelot GameCube games (Mario Golf: Toadstool Tour and Mario Power Tennis) data decoder/encoder.
- [amnoid.de/gc](http://amnoid.de/gc/) - GameCube file format documentation and tools.
- [BMS-Analyzer](https://github.com/3e2j/BMS-Analyzer) - Nintendo Wii/Gamecube BMS to MIDI converter
- [CaveGenerator](https://github.com/Fizz14/CaveGenerator) - A tool to generate caves for Pikmin 2.
- [NintyFont](https://github.com/hadashisora/NintyFont) - Nintendo binary font editor
- [MarioKartToolbox](https://github.com/HaroohiePals/MarioKartToolbox) - New version of Mario Kart Toolbox, a fully fledged Mario Kart DS editor.
- [GRPEdit](https://github.com/Garhoogin/GRPEdit) - Editor for Mario Kart DS grpconf.tbl file.
- [picori](https://github.com/Julgodis/picori) - Picori (ピッコル) is a library for decompilation, modding, and rom-hacking with focus on GameCube and Wii games.
- [MasterOcarina](https://github.com/mzxrules/MasterOcarina) - Collection of Zelda 64 programs
- [zelda-internal-file-extractor](https://github.com/politerust/zelda-internal-file-extractor) - Command-line utility that extracts the internal files of Zelda 64 ROMs.
- [Zelda64Loader](https://github.com/Random06457/Zelda64Loader) - Ghidra loader for Zelda 64 ROMs.
- [zcamedit](https://github.com/sauraen/zcamedit) - Zelda 64 (Ocarina of Time/Majora's Mask) cutscene camera editor Blender plugin.
- [OoT-Anim-Copy](https://github.com/skawo/OoT-Anim-Copy) - Copies a Zelda Ocarina of Time animation between ZOBJ files.
- [OoT-NPC-Maker](https://github.com/skawo/OoT-NPC-Maker) - NPC creation tool for The Legend of Zelda: Ocarina of Time.
- [PyZelda64-Text-Editor](https://github.com/skawo/PyZelda64-Text-Editor) - Cross-platform Zelda 64 Text Editor
- [pycgfx](https://github.com/skyfloogle/pycgfx) - Program for converting glTF models into the Nintendo 3DS's CGFX format.
- [zev](https://github.com/wareya/zev) - ZEV, a ZElda 64 level Viewer
- [ozmav](https://github.com/xdanieldzd/ozmav) - Legacy N64 emulation and game modding tools (unmaintained, automatically exported from code.google.com/p/ozmav).
- [SceneNavi](https://github.com/xdanieldzd/SceneNavi) - Level editor for The Legend of Zelda: Ocarina of Time (N64) (unmaintained).
- [sharpocarina](https://github.com/xdanieldzd/sharpocarina) - Automatically exported from code.google.com/p/sharpocarina (unmaintained).
- [z64font](https://github.com/z64dev/z64font) - The first font editor for Zelda games on the Nintendo 64
- [z64viewer](https://github.com/z64dev/z64viewer) - HLE Zelda 64 model rendering in modern OpenGL
- [zzrtl](https://github.com/z64dev/zzrtl) - the lightweight Zelda 64 filesystem management utility
- [z64audio](https://github.com/z64tools/z64audio) - Somewhat flexible audio converter for Zelda 64 games.
- [Z64Utils](https://github.com/zeldaret/Z64Utils) - Asset viewer for the Zelda64 Engine
- [NSMBHD Wiki (BCRES)](https://nsmbhd.net/wiki/BCRES/) - BCRES format documentation for 3DS games.
- [CloudModding Wiki (OoT Animation)](https://wiki.cloudmodding.com/oot/Animation_Format) - Animation format documentation for Ocarina of Time.
- [mm (decomp)](https://github.com/zeldaret/mm) - Matching decompilation of The Legend of Zelda: Majora's Mask.
- [oot (decomp)](https://github.com/zeldaret/oot) - Matching decompilation of The Legend of Zelda: Ocarina of Time.
- [oot-vc (decomp)](https://github.com/zeldaret/oot-vc) - Matching decompilation of the Wii Virtual Console N64 emulator for Ocarina of Time (JP).
- [oot3d (decomp)](https://github.com/zeldaret/oot3d) - Matching decompilation of The Legend of Zelda: Ocarina of Time 3D.
- [tww (decomp)](https://github.com/zeldaret/tww) - Matching decompilation of The Legend of Zelda: The Wind Waker.
- [tmc (decomp)](https://github.com/zeldaret/tmc) - Matching decompilation of The Legend of Zelda: The Minish Cap.
- [ph (decomp)](https://github.com/zeldaret/ph) - Matching decompilation of The Legend of Zelda: Phantom Hourglass.
- [st (decomp)](https://github.com/yanis002/st) - Matching decompilation of The Legend of Zelda: Spirit Tracks.
- [ss (decomp)](https://github.com/zeldaret/ss) - Matching decompilation of The Legend of Zelda: Skyward Sword.
- [botw (decomp)](https://github.com/zeldaret/botw) - Matching decompilation of The Legend of Zelda: Breath of the Wild (Switch 1.5.0).
- [las-decomp (decomp)](https://github.com/Owen-Splat/las-decomp) - Matching decompilation of Link's Awakening Switch (2019 remake).
- [tp (decomp)](https://github.com/zeldaret/tp) - Matching decompilation of The Legend of Zelda: Twilight Princess.

### Nintendo SDKs & Hardware

*Formats and tools generic to Nintendo consoles or SDKs.*

- [Nintendo-File-Formats](https://github.com/kinnay/Nintendo-File-Formats) - Documentation for Wii U and Switch file formats.
- [hactool](https://github.com/SciresM/hactool) - Tool to view information about, decrypt, and extract Nintendo Switch file formats including NCA, XCI, PFS0, HFS0, RomFS, ExeFS, save data, and more.
- [WiiUTools](https://github.com/NWPlayer123/WiiUTools) - Collection of Python utilities for working with Wii U file formats including IPK packages, RPX executables, SARC archives, and texture editing (TexHaxU/TexHaxU2).
- [Syroot.NintenTools.Bfres](https://gitlab.com/Syroot/NintenTools) - Library for reading/writing Nintendo BFRES model format (Wii U).
- [Nitro Files](https://wiki.vg-resource.com/Nitro_Files) - Documentation for Nintendo DS file formats.
- [narchive](https://github.com/nickworonekin/narchive) - Tool for extracting and creating NARC archives used in DS games.
- [RomFS-Builder](https://github.com/SciresM/RomFS-Builder) - Program to convert a folder in Windows into a 3DS RomFS binary. For use with makerom.
- [XCI-Explorer](https://github.com/StudentBlake/XCI-Explorer) - Tool for viewing contents of Nintendo Switch XCI and NSP files. Features include viewing metadata, exploring partitions, checking NCA hashes, extracting NCA, and modifying certificates.
- [gc-c-kit](https://github.com/RenolY2/gc-c-kit) - Toolkit for compiling C code using devkitppc and injecting it into a GameCube Executable (DOL). Can be adapted to different GC games.
- [WiiTools](https://github.com/Megazig/WiiTools) - Tools for Wii reverse engineering and function identification to help hacking Wii games.
- [N64Recomp](https://github.com/N64Recomp/N64Recomp) - Tool to statically recompile N64 games into native executables. Converts N64 binaries into C code that can be compiled for any platform.
- [wfslib](https://github.com/koolkdev/wfslib) - WFS (WiiU File System) library and tools.
- [ctpktool](https://github.com/dnasdw/ctpktool) - Tool for exporting/importing CTPK texture package files used in Nintendo 3DS games.
- [AudiobankToC](https://github.com/sauraen/AudiobankToC) - Scripts for converting between N64 Audiobank bank files and C code. Matches on binary -> C -> binary for banks in OoT.
- [libansnd](https://github.com/Oaisus/libansnd) - Audio library for Wii and GameCube homebrew with support for ADPCM audio decoding and arbitrary resampling. Supports up to 48 simultaneous voices with hardware ADPCM decoding.
- [LegacySwitchLibraries](https://github.com/KillzXGaming/LegacySwitchLibraries) - Switch file format libraries for Switch Toolbox and other programs.
- [exefs_patches](https://github.com/misson20000/exefs_patches) - ExeFS patching tool for Nintendo Switch.
- [otptool](https://github.com/SciresM/otptool) - Tool for Nintendo OTP (One-Time Programmable) files.
- [switch-reversing](https://github.com/SciresM/switch-reversing) - Reverse engineering resources for Nintendo Switch.
- [sarc](https://github.com/jam1garner/sarc) - Rust library for reading and writing Nintendo SARC and SZS (yaz0 compressed SARC) archive formats.
- [sarc-extract](https://github.com/RenolY2/sarc-extract) - Extractor for SARC archive format.
- [GARC-Unpack](https://github.com/vgmoose/GARC-Unpack) - Unpacker for Nintendo GARC archive format.
- [lzarc](https://github.com/jam1garner/lzarc) - Rust library and CLI for working with LZARC compressed archives used in Paper Mario Color Splash.
- [Lzarc-Tool](https://github.com/Fuzzy2319/Lzarc-Tool) - Tool for LZARC compressed archive format.
- [msbt2sheets](https://github.com/CaXaPeK/msbt2sheets) - Converter for MSBT files to spreadsheet format.
- [MSBTEditor](https://github.com/efimandreev0/MSBTEditor) - MSBT text extractor/replacer for .msbt and .umsbt LE-files.
- [umsbt_cmd_extractor](https://github.com/efimandreev0/umsbt_cmd_extractor) - Command extractor for UMSBT files.
- [BFRES-Viewer](https://github.com/KillzXGaming/BFRES-Viewer) - Viewer for Nintendo BFRES model format files.
- [BFRES-Tool](https://github.com/aboood40091/BFRES-Tool) - Tool for working with Nintendo BFRES files.
- [BFRES-Extractor](https://github.com/LordNed/BFRES-Extractor) - Extractor for Nintendo BFRES format files.
- [TinkeDSi](https://github.com/R-YaTian/TinkeDSi) - Viewer and extractor for Nintendo DS/DSi file formats.
- [ctpktool](https://github.com/dnasdw/ctpktool) - Tool for working with CTPK texture package files.
- [gc-gcm](https://github.com/jam1garner/gc-gcm) - Tool for GameCube GCM file format.
- [LibGCM](https://github.com/Sage-of-Mirrors/LibGCM) - Library for GameCube memory card formats.
- [dolreader](https://github.com/RenolY2/dolreader) - Reader for GameCube/Wii DOL executable format.
- [gci-bt](https://github.com/jam1garner/gci-bt) - GameCube GCI file tool with Bluetooth support.
- [Chihuahua](https://github.com/Sage-of-Mirrors/Chihuahua) - Tool for GameCube/Wii file formats.
- [TSCBReader](https://github.com/Sage-of-Mirrors/TSCBReader) - Reader for TSCB format files.
- [KMP-Expander](https://github.com/Ermelber/KMP-Expander) - Expander for KMP format files.
- [pymsc](https://github.com/jam1garner/pymsc) - Python library for MSC format files.
- [cgrr-gameboy](https://github.com/sopoforic/cgrr-gameboy) - Tools for Game Boy file formats.
- [cgrr-gamecube](https://github.com/sopoforic/cgrr-gamecube) - Tools for GameCube file formats.
- [HexManiacAdvance](https://github.com/haven1433/HexManiacAdvance) - Hex editor for Game Boy Advance ROMs with scripting support.
- [UnkrawerterGBA](https://github.com/MCJack123/UnkrawerterGBA) - Game Boy Advance ROM extractor and converter.
- [Hatenatools](https://github.com/pbsds/Hatenatools) - Python tools for Flipnote Studio (Nintendo DSi) file formats. Supports reading and writing .ppm (Flipnote files), .tmb (thumbnail files), .ugo (user data), and .ntft (image files). Can extract metadata, frames, and audio from Flipnote files.
- [SuperFamiconv](https://github.com/Optiroc/SuperFamiconv) - Command-line tool to convert graphics to Super Nintendo format.
- [M1TE2](https://github.com/nesdoug/M1TE2) - SNES Mode 1 Tile Editor for generating, editing, and arranging SNES tiles and tilemaps (2bpp/4bpp) with palette support. Designed for Mode 1 but works with any mode needing 2bpp or 4bpp graphics.
- [3dstool](https://github.com/dnasdw/3dstool) - All-in-one tool for extracting and creating 3DS file formats (CIA, CCI, NCCH, NCSD, etc.).
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
- [nod](https://github.com/encounter/nod) - Rust library for reading and writing Nintendo Optical Disc images (GameCube and Wii). Supports ISO (GCM), WIA/RVZ, WBFS, CISO, NFS (Wii U VC), GCZ, and TGC formats. Includes nodtool CLI for extraction, conversion, and verification.

### Ntreev Soft

- [PangLib](https://github.com/retreev/PangLib) - Series of tools to interact with Pangya PC MMO game files.
- [Pangya .iff formats](https://pixelde.su/blog/reverse-engineering-pangya-file-formats-2-iff/) - Blog post detailing the IFF file format used in Pangya.
- [Pangya .dat formats](https://desu.blog/reverse-engineering-pangya-file-formats-1-dat) - Blog post explaining the DAT file format used in Pangya.

### BioWare

#### Mass Effect

- [Gibbed.MassEffectAndromeda](https://github.com/gibbed/Gibbed.MassEffectAndromeda) - Tools for Mass Effect: Andromeda file formats.

#### Dragon Age: Origins

- [Dragon Age Origins 3dsmax Import Export script](https://www.moddb.com/games/dragon-age-origins/downloads/dragon-age-origins-3dsmax-import-export-script) - Dragon Age Origins 3dsmax import export script. Version 5.38. Reportedly works best with 3dsmax 2013

#### Knights of the Old Republic

- [StarForge](https://github.com/Astral-C/StarForge) - Tool for Star Wars: Knights of the Old Republic file formats.
- [Kotor Tool 1](https://www.moddb.com/games/star-wars-knights-of-the-old-republic/downloads/kotor-tool-1) - Tool for extracting files, changing game rules, and customizing levels in Knights of the Old Republic.

### Obsidian Entertainment

#### Neverwinter Nights 2

- [NWN2MDK](https://github.com/Arbos/nwn2mdk) - Neverwinter Nights 2 Modding & Development Kit. Includes a Blender add-on for meshes/animations and command-line converters.

### Panic

- [playdate-reverse-engineering](https://github.com/cranksters/playdate-reverse-engineering) - Reverse engineering notes and tools for Playdate handheld console.
- [noclip.website (A Short Hike)](https://github.com/magcius/noclip.website/tree/main/src/AShortHike) - In-browser A Short Hike viewer.

### Paradox Interactive

- [io_pdx_mesh](https://github.com/ross-g/io_pdx_mesh) - Blender addon for importing Paradox Interactive mesh formats.

### Petroglyph Games

- [alo/ala max importer exporter (Star Wars: Empire at War)](https://www.moddb.com/groups/starwars-empire-at-war-fan-mod-group/downloads/aloala-max-importer-exporter) - the files needed for 3ds max to make ALO/ALA files.
- [Blender-ALAMAO-Plugin for 4.2LTS (Star Wars: Empire at War: Forces of Corruption)](https://www.moddb.com/games/star-wars-empire-at-war-forces-of-corruption/downloads/blender-alamao-plugin-for-42lts) - A plugin that allow reading and writing of ALAMO-Engine model(.alo) and animation(.ala) files. Specifically designed to work with Empire at War: Forces of Corruption.
- [Grey Goo Official Asset Adding Tools](https://www.moddb.com/games/grey-goo/downloads/grey-goo-asset-adding-tools) - Official Grey Goo SDK and asset tools for importing custom assets. Includes 32-bit 3DS Max plugin and tools for handling .meg files.
- [3DS Max 7 and 8 Plugin for Map Editor (Star Wars: Empire At War)](https://www.moddb.com/games/star-wars-empire-at-war/downloads/3ds-max-7-and-8-plugin-for-map-editor) - 3DS Max 7 and 8 Plugin for Map Editor.
- [Star Wars Empire At War FOC DDS Tool](https://www.moddb.com/games/star-wars-empire-at-war-forces-of-corruption/downloads/star-wars-empire-at-war-foc-dds-tool) - DDS texture tool for Star Wars: Empire at War modding. Part of Dr. Chelli Lona Aphra's modding resource collection. Provides general assistance for modding (may not apply to all situations).
- [Star Wars Empire At War FOC DDS Viewer & Thumbplug _tga1.10](https://www.moddb.com/games/star-wars-empire-at-war-forces-of-corruption/downloads/star-wars-empire-at-war-foc-dds-viewer-thumbplug-tga110) - DDS viewer and TGA thumbnail plugin for Star Wars: Empire at War modding (v1.10). Part of Dr. Chelli Lona Aphra's modding resource collection. Provides general assistance for modding.
- [Star Wars Empire At War FOC Alamo Object Importer 1.2](https://www.moddb.com/games/star-wars-empire-at-war-forces-of-corruption/downloads/alamo-object-importer-12) - Alamo object importer for 3DS Max for Star Wars: Empire at War modding (v1.2). Part of Dr. Chelli Lona Aphra's modding resource collection. Provides general assistance for modding.
- [Star Wars Empire At War FOC Alamo Viewer 1.2](https://www.moddb.com/games/star-wars-empire-at-war-forces-of-corruption/downloads/alamo-viewer-12) - Alamo viewer for Star Wars: Empire at War modding (v1.2). Part of Dr. Chelli Lona Aphra's modding resource collection. Provides general modding assistance.

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

- [Archive files plugin for Noesis (The I of the Dragon)](https://www.moddb.com/games/the-i-of-the-dragon/downloads/archive-files-plugin-for-noesis-v001) - Basic tools to work with archive resource files (.res).

### Polytron

- [noclip.website (Fez)](https://github.com/magcius/noclip.website/tree/main/src/Fez) - In-browser Fez viewer.

### Mithis Entertainment

#### Nexus: The Jupiter Incident

- [Nexus Mesh Importer](https://www.moddb.com/games/nexus-the-jupiter-incident/downloads/nexus-mesh-importer) - A plug-in for Milkshape 3d that'll allow you to work on existing Nexus ship mesh & tex files.
- [Nexus Texture Converter](https://www.moddb.com/games/nexus-the-jupiter-incident/downloads/nexus-texture-converter) - converts Nexus' proprietary .tex file format to regular .tga images .NET Framework 3.5 required

### Punchline

- [Murugo/Misc-Game-Research (Rule of Rose)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Rule%20of%20Rose) - Reverse engineering notes for Rule of Rose (PS2).

### People Can Fly

#### Painkiller

- [Painkiller 3ds Max Plugins (Upd270522)](https://www.moddb.com/games/painkiller/downloads/painkiller-3ds-max-plugins) - 3ds Max import/export plug-ins for Painkiller assets (Upd270522) by dilettante
- [HavokXML2HKE converter for Ragdoll physics 3ds Max (Painkiller)](https://www.moddb.com/games/painkiller/downloads/havokxml2hke-converter-for-ragdoll-physics) - Converter Havok-XML to *.HKE (Havok Exporter) for ragdoll physics by dilettante. HavokPcXsContentTools_X64_2010-2-0_20101115 for 3dsmax9 x64 is also included.
- [PainFull Extractor v1.3.2 (Painkiller)](https://www.moddb.com/games/painkiller/downloads/painfull-extractor-v132) - Unpacker for Painkiller & NecroVision game resources (.pak files). This program is outdated and should be run in the WindowsXP (SP 2) compatibly mode. Use Dragon UnPACKer or QuickBMS as an alternative.
- [Painkiller converters mpk/dat to ASE and ASE to mpk/dat](https://www.moddb.com/games/painkiller/downloads/painkiller-converters-mpk-to-ase-and-ase-to-mpk) - Console utilities to convert the Painkiller mpk and dat geometry format to and from Ascii Scene (ASE): ase2mpk, mpk2ase, blend, PKBlend, dat2ase, and mpk2dat.

#### Dreamkiller

- [Dreamkiller Mapping Tools for 3ds Max](https://www.moddb.com/games/dreamkiller/downloads/dreamkiller-mapping-tools) - DKStaticMeshImp.dli - 3dsMax static mesh import plugin. UnpackTEXT.exe - texture extractor.

### Piranha Bytes

- [ZenLib](https://github.com/ataulien/ZenLib) - Loading library for proprietary formats used by the engine in Gothic and Gothic II games.

### Polyphony Digital

- [GTAllPaintEditor](https://github.com/Nenkai/GTAllPaintEditor) - Tool to edit Gran Turismo 6's allpaint.bin file for assigning custom paints to cars through GT Auto.
- [gt2-reversing](https://github.com/ginryuoku/gt2-reversing) - Reverse engineering tools for Gran Turismo 2.
- [PDTools](https://github.com/Nenkai/PDTools) - Utilities for extracting and modifying Gran Turismo game files.
- [GT4SaveEditor](https://github.com/Nenkai/GT4SaveEditor) - Save editor for Gran Turismo 4.

### RAD Game Tools

- [Knit](https://github.com/neptuwunium/Knit) - Fully managed C# reader for Granny 2 files used in many games.
- [GR2Toolkit](https://github.com/REDxEYE/GR2Toolkit) - Toolkit for working with Granny 3D (GR2) model format files.

### Rebel Act

- [3D tools for Severance v2.5](https://www.moddb.com/games/severance-blade-of-darkness/downloads/3d-tools-for-severance-v25) - Tools needed to import / export animations, obsjects and characters into the game. It's recommended to use also the TPTPT Scripts.
- [3D Tools & Scripts v1.2.1](https://www.moddb.com/games/severance-blade-of-darkness/downloads/3d-tools-scripts-v121) - Collection of 3DS Max tools and scripts for Severance: Blade of Darkness. Includes: TPBladeToolsChar for Max 2.5 (v1.2.0 Patch 1.2.1), BladeTools for Max 8 (v1.2.0 Patch 1.2.1), TPBladeCharEditorTools for Max 8 (v1.2.0 Patch 1.2.1), Python 2.4, and Py2exe for Python 2.4 (v1.2.1).
- [Blade of Darkness Mod Tools & Tutorials](https://www.moddb.com/games/severance-blade-of-darkness/downloads/blade-of-darkness-mod-tools-tutorials) - Comprehensive collection of tools, tutorials, demonstration files, textures, and maps for Severance: Blade of Darkness. Includes most resources needed to get started with making maps and characters. Collection organized by bigtruck.
- [Blade Tools English. Severance - SDK](https://www.moddb.com/games/severance-blade-of-darkness/downloads/blade-tools-english-severance-sdk) - SDK and modding tools for Severance: Blade of Darkness (English version).
- [Blade Tools Spanish. Blade SDK](https://www.moddb.com/games/severance-blade-of-darkness/downloads/blade-tools-spanish-blade-sdk) - Herramientas de edición del juego Blade: The Edge of Darkness.

### Rebellion Developments

- [AvP Editing Tools](https://www.moddb.com/games/aliens-vs-predator/downloads/avp-editing-tools) - Collection of modding tools for Aliens versus Predator including old modding programs and Rebellion's official Gold tools. Includes: AVPTweak, AVP Launcher, Fastfile Backup, Fastfile Explorer, Leadworks, Level Tweaker, nelev, Patch Editor, Patch Installer, PREtweak, Profile Tweaker, Ripley2, ScreamED, Texture Infector, and more.
- [AVP Gold Tools and Source Code (Aliens versus Predator - Classic)](https://www.moddb.com/games/aliens-vs-predator/downloads/avp-gold-tools-and-source-code) - Official editing tools by Rebellion for Aliens versus Predator Gold Edition, including game source code and complete instructions/guidelines. Essential for editing and creating new content....

#### Aliens vs. Predator 2

- [AVP2 official tools](https://www.moddb.com/games/aliens-vs-predator-2/downloads/avp2-official-tools) - AVP2's official tools created by Monolith. Mirrored here for archival purposes.

#### Aliens vs. Predator (2010)

- [Asura Engine Extractor (Aliens vs. Predator 2010)](https://www.moddb.com/games/avp2010/downloads/asura-engine-extractor) - A very experimental tool to unpack textures and repack it with live preview. The tool is open Source so anyone has the freedom to modify it. Enjoy!. Build with help of Codex

### Rare

- [sssv (decomp)](https://github.com/mkst/sssv) - Matching decompilation of Space Station Silicon Valley (N64).

#### Banjo-Kazooie

- [noclip.website (Banjo-Kazooie)](https://github.com/magcius/noclip.website/tree/main/src/BanjoKazooie) - In-browser Banjo-Kazooie viewer.
- [Banjo-Kazooie-Floor-Tool](https://github.com/oohnahleevay/Banjo-Kazooie-Floor-Tool) - Tool to modify floor collision properties in Banjo-Kazooie.
- [Banjo-s-Backpack](https://github.com/RareExports/Banjo-s-Backpack) - Level editor for Banjo-Kazooie (map and object editing).
- [Bottles_Glasses](https://github.com/RareExports/Bottles_Glasses) - Model and map renderer for Banjo-Kazooie and Banjo-Tooie.

#### Banjo-Tooie

- [conker (decomp)](https://github.com/mkst/conker) - Matching decompilation of Conker's Bad Fur Day (N64).
- [noclip.website (Banjo-Tooie)](https://github.com/magcius/noclip.website/tree/main/src/BanjoTooie) - In-browser Banjo-Tooie viewer.
- [Bottles_Glasses](https://github.com/RareExports/Bottles_Glasses) - Model and map renderer for Banjo-Kazooie and Banjo-Tooie.
- [WumbasWigwam](https://github.com/RareExports/WumbasWigwam) - Level exporter for Banjo-Tooie (Blender import support).
- [BK2BT](https://github.com/Muzzarino/BK2BT) - Fast3DEX to Fast3DEX2 microcode converter for Banjo-Kazooie model files to Banjo-Tooie format. Includes model previewer and converter.

#### Donkey Kong 64

- [noclip.website (Donkey Kong 64)](https://github.com/magcius/noclip.website/tree/main/src/DonkeyKong64) - In-browser Donkey Kong 64 viewer.
- [DK64MapGenerator](https://github.com/GloriousLiar/DK64MapGenerator) - Tool for generating Donkey Kong 64 map and floor files from 3D meshes.
- [DK64-Viewer](https://github.com/RareExports/DK64-Viewer) - Model and map viewer for Donkey Kong 64.
- [dk64_lib](https://github.com/ThomasJRyan/dk64_lib) - Library for extracting data from Donkey Kong 64 ROMs.

#### Diddy Kong Racing

- [noclip.website (Diddy Kong Racing)](https://github.com/magcius/noclip.website/tree/main/src/DiddyKongRacing) - In-browser Diddy Kong Racing viewer.

#### GoldenEye 007

- [noclip.website (GoldenEye 007)](https://github.com/magcius/noclip.website/tree/main/src/GoldenEye007) - In-browser GoldenEye 007 viewer.
- [GoldEditor](https://github.com/carnivoroussociety/GoldEditor) - Setup editor for GoldenEye 007 game configurations.
- [bk360 (decomp)](https://github.com/banjo360/bk360) - Matching decompilation of Banjo-Kazooie (Xbox 360).
- [diddy-kong-racing (decomp)](https://github.com/davidsm64/diddy-kong-racing) - Matching decompilation of Diddy Kong Racing.

### Runic Games

#### Torchlight

- [Nimet - Ogre3D Mesh Viewer (Torchlight)](https://www.moddb.com/games/torchlight/downloads/nimet-ogre3d-mesh-viewer) - Nimet is an advanced 3D model viewer for Ogre3D engine.
- [Cliffside tile set build 1.0.00 (Torchlight)](https://www.moddb.com/games/torchlight/downloads/cliffside-tile-set-build-1000) - Mod adding a new tile set and prop set called CliffSide for Torchlight. Outdoor set for creating areas based around mountains, forests, and water (v1.0.00).

#### Torchlight II

- [Modified PAK Extractor Tool](https://www.moddb.com/games/torchlight-ii/downloads/modified-pak-extractor-tool-by-jarcho) - Tool for extracting data files from Torchlight 2's DATA.PAK file. Developed by Jarcho, modified by timebomb. Enables modding by extracting game assets.
- [GUTS Tools and Assets](https://www.moddb.com/games/torchlight-ii/downloads/guts-tools-and-assets) - This .ZIP includes raw media, assets, and tools which will be useful to you when creating mods for Torchlight II. Below is a brief description of the resources you will find in this package.

### Runecraft

- [esa (decomp)](https://github.com/mkst/esa) - Matching decompilation of Evo's Space Adventures (PS1).

### 1C Company / Best Way

#### Men of War

- [Men of War 3DS Max Exporter Tools](https://www.moddb.com/games/men-of-war/downloads/men-of-war-3ds-max-exporter-tools) - 3DS Max exporter tools for Men of War. Supports 32-bit versions of 3DS Max 8, 9, 2008, and 2009 only. Mirrored here as the original Best Way download is no longer available.

#### Royal Quest Online

- [RQ.TOC.Tool](https://github.com/Ekey/RQ.TOC.Tool) - Tool for extracting archives from Royal Quest Online game files.

### Ironclad Games / Stardock

#### Sins of a Solar Empire

- [Sins 3D Max Import export](https://www.moddb.com/games/sins-of-a-solar-empire-rebellion/downloads/sins-3d-max-impotrt-export) - 3DS Max importer for Sins of a Solar Empire: Rebellion TXT mesh format. Exporter in progress. Trial alpha version.
- [sins TXT Tools with export (Sins of a Solar Empire: Rebellion)](https://www.moddb.com/games/sins-of-a-solar-empire-rebellion/downloads/sins-txt-tools-with-export) - This version with export to TXT! Alpha version...adds sins standart material with default settings
- [Forge Tools (Sins of a Solar Empire)](https://www.moddb.com/games/sins-of-a-solar-empire/downloads/forge-tools) - Official development tools for creating custom maps and modifications for Sins of a Solar Empire. Includes Galaxy Forge and Particle Forge tools used by the development team.
- [Map Conversion (Sins of a Solar Empire)](https://www.moddb.com/games/sins-of-a-solar-empire/downloads/map-conversion) - Convert maps between Sins versions with this user-created tool. Created by Ross Placing. Requires .Net 2.0; Updated for Sins 1.15/Entrenchment 1.01.

### Radical Entertainment

- [scarface-p3d](https://github.com/aap/scarface-p3d) - Code to deal with P3D files from "Scarface: The World is Yours".
- [map-data-editor](https://github.com/WeaselOnaStick/map-data-editor) - Blender 2.80+ addon for editing SHAR map data like road networks, fences, paths, locators, and level trees in The Simpsons: Hit & Run.

### Reflections Interactive

- [driver-tools](https://github.com/Fireboyd78/driver-tools) - Modding tools for DRIV3R, Driver: Parallel Lines, and Driver: San Francisco.
- [REDRIVER2](https://github.com/OpenDriver2/REDRIVER2) - Driver 2 Playstation game reverse engineering effort.
- [Driver model tools](https://www.moddb.com/games/driver-you-are-the-wheelman/downloads/driver-model-tools) - Package contains the model extractor/replacement tool, import and export plugins for Milkshape 3D

### Riot Games

- [yordle](https://github.com/neptuwunium/yordle) - League of Legends research project for file formats.
- [MindCorpViewer](https://github.com/autergame/MindCorpViewer?tab=readme-ov-file) - Model viewer for League of Legends SKN/SKL/DDS files [archived].
- [MindCorpViewer-Rust](https://github.com/autergame/MindCorpViewer-Rust) - Modern Rust rewrite of League of Legends model viewer with improved performance.

### Santa Monica Studio

- [god_of_war_browser](https://github.com/mogaika/god_of_war_browser) - WebGL-based in-browser viewer for God of War I/II (PS2/PS3/Vita) models and textures.
- [God of War 2018 PS4 Tools](https://forum.xentax.com/viewtopic.php?f=16&t=22897) - XeNTaX forum discussion and extraction tools for God of War (2018) on PlayStation 4. *(Link archived/dead)*

### SCS Software

- [ETS2.SCS.Tool](https://github.com/Ekey/ETS2.SCS.Tool) - Tool for extracting SCS archives from Euro Truck Simulator 2.

### Sega

- [ogre-decomp (decomp)](https://github.com/hamzaxx370/ogre-decomp) - Matching decompilation of Yakuza 1 (PS2).
- [tbg-decomp (decomp)](https://github.com/lhsazevedo/tbg-decomp) - Matching decompilation of Tokyo Bus Guide (Dreamcast).
- [SkiesofArcadiaLegends (decomp)](https://github.com/rainchus/SkiesofArcadiaLegends) - Matching decompilation of Skies of Arcadia Legends (GameCube).
- [puyotools](https://github.com/nickworonekin/puyotools) - Collection of tools and libraries for accessing contents of various game files. Initially built for Puyo Puyo games but can handle files from other games as well.
- [puyo-pac](https://github.com/nickworonekin/puyo-pac) - Command-line app for creating and extracting PAC archives used in Puyo Puyo Tetris 2.
- [PP20thDataExtractor](https://github.com/nickworonekin/PP20thDataExtractor) - Extracts and builds GAME.DAT in the Wii and PSP versions of Puyo Puyo!! 20th Anniversary.
- [JSRGraffitiTool](https://github.com/chrisderwahre/JSRGraffitiTool) - Tool for modding Jet Set Radio's graffiti files.
- [ParManager](https://github.com/Kaplas80/ParManager) - Tools for Yakuza series PAR archive files.
- [yk_gmd_io](https://github.com/theturboturnip/yk_gmd_io) - Import/export addon for Blender 3.2+ that allows .gmd files from the Yakuza game series to be imported/exported.
- [PSO2-Aqua-Library](https://github.com/Shadowth117/PSO2-Aqua-Library) - Library for handling Phantasy Star Online 2 Aqua formats, with a focus on models. Functional in grabbing model data from the game's format.
- [PSO2-Salon-Tool](https://github.com/Shadowth117/PSO2-Salon-Tool) - Program to edit and convert between Phantasy Star Online 2 .xxp and .cml files.
- [FpkTool](https://github.com/Shadowth117/FpkTool) - Unpacks and repacks Phantasy Star Online 2 FPK archives (pre NGS).
- [PSO2 Tools](https://github.com/dummycount/blender_pso2_tools) - Blender add-on for Phantasy Star Online 2 assets (`.aqp`, `.aqn`, ICE archives). Features model search, archive browsing, and automatic texture assignment.

#### Creative Assembly

##### Alien: Isolation

- [Alien Isolation Animation Exporter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-animation-exporter) - Exports animations and bone structures from Alien Isolation.
- [Alien Isolation Model Exporter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-model-exporter) - Exports models from Alien Isolation for re-import into Blender.
- [Alien Isolation Texture Exporter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/texture-extractor) - Extracts textures from Alien Isolation. By Cra0kalo, modified by MattFiler.
- [Alien Isolation Audio Converter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-audio-converter) - Converts audio in Alien Isolation. Includes revorb, bnkextr, ww2ogg, and instructions.
- [Alien Isolation BML Converter](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-bml-converter) - BML file converter for Alien Isolation enabling modding of behaviors, weapons, and more.
- [Alien Isolation UI Mod Tool](https://www.moddb.com/mods/alien-isolation-extractors/downloads/alien-isolation-ui-mod-tool)

##### Total War Series

- [Texture 2 DDS Converter (Medieval II: Total War)](https://www.moddb.com/games/medieval-2-total-war/downloads/texture-2-dds-converter)
- [Vercengetorix's CAS Import/Export (Medieval II: Total War)](https://www.moddb.com/games/medieval-2-total-war/downloads/vercengetorix-s-cas-import-export) - Allows you to import and export .CAS files to and from 3ds Max.
- [CAS Exporter (Medieval II: Total War)](https://www.moddb.com/games/medieval-2-total-war/downloads/cas-exporter) - Public release of model and animation exporter for Rome: Total War and Medieval II: Total War.
- [Community Modding Framework (Total War: Warhammer II)](https://www.moddb.com/games/total-war-warhammer-ii/downloads/community-modding-framework-1104) - Community Modding Framework v1.10.4, authored by Crynsos. This mod acts as a central compatibility manager for all script mods that have been registered to prevent any potential conflicts. As a secondary function, this mod also serves as a bugfix for a long standing issue with new characters and ...
- [Symphony Sound Packer (Empire: Total War)](https://www.moddb.com/mods/foothold-in-india/downloads/symphony-sound-packer) - British Line Infantry starts shouting "Revolutionary Guard!" when you click them after installing a mod with new units? This tool should help you. All credits to crux3D.
- [Aqua-Toolset](https://github.com/Shadowth117/Aqua-Toolset) - Toolkit primarily for Phantasy Star Online 2 file formats.
- [NaomiMod/games-ExtractTools](https://github.com/NaomiMod/games-ExtractTools) - QuickBMS scripts to extract NaomiLib models from Dreamcast/Naomi arcade games. Supports Dead or Alive 2, Initial D3, Mortal Kombat 4, Super Monkey Ball, Virtua Tennis, Castlevania Resurrection, Rent-A-Hero, and more.
- [NaomiLib Blender Addon](https://github.com/NaomiMod/blender-NaomiLib) - Blender addon for importing NaomiLib 3D models from SEGA Dreamcast and Naomi arcade games (Crazy Taxi, Dead or Alive 2, Marvel vs. Capcom 2, Shenmue 2, Virtua Tennis, and more).
- [PCSX2 Patches](https://github.com/PCSX2/pcsx2_patches) - Game patches for PCSX2 emulator including widescreen and interlacing fixes.
- [noclip.website (Jet Set Radio)](https://github.com/magcius/noclip.website/tree/main/src/JetSetRadio) - In-browser Jet Set Radio viewer.
- [Sonic-1-2-2013-Decompilation (decomp)](https://github.com/RSDKModding/RSDKv4-Decompilation) - Matching decompilation of Sonic 1 & 2 (2013 mobile) and Retro Engine v4.
- [Sonic-CD-11-Decompilation (decomp)](https://github.com/RSDKModding/RSDKv3-Decompilation) - Matching decompilation of Sonic CD (2011 mobile) and Retro Engine v3.
- [sa1 (decomp)](https://github.com/SAT-R/sa1) - Matching decompilation of Sonic Advance (GBA, Europe).
- [sa2 (decomp)](https://github.com/SAT-R/sa2) - Matching decompilation of Sonic Advance 2 (GBA).
- [sa3 (decomp)](https://github.com/SAT-R/sa3) - Matching decompilation of Sonic Advance 3 (GBA).
- [Sonic-Mania-Decompilation (decomp)](https://github.com/RSDKModding/Sonic-Mania-Decompilation) - Matching decompilation of Sonic Mania (2017).
- [RunnersDecomp (decomp)](https://github.com/itsmattkc/RunnersDecomp) - Matching decompilation of Sonic Runners.
- [SonicRushAdventure-Decomp (decomp)](https://github.com/RushRE/SonicRushAdventure-Decomp) - Matching decompilation of Sonic Rush Adventure.

### Sonic Team

#### Sonic Adventure

- [SCHG:Sonic_Adventure](https://info.sonicretro.org/SCHG:Sonic_Adventure) - Sonic Community Hacking Guide documentation for Sonic Adventure.
- [sadtools](https://github.com/FraGag/sadtools) - Command-line tools for Sonic Adventure file formats.
- [sa_tools](https://github.com/X-Hax/sa_tools) - Modding toolkit for Sonic Adventure series. Supports Sonic Adventure DX (SADX) and Sonic Adventure 2 PC (SA2PC).
- [SonicAdventureBlenderIO](https://github.com/X-Hax/SonicAdventureBlenderIO) - Blender 4.0+ add-on for exporting Sonic Adventure 1 & 2 3D formats (`.nj`, `.gj`, `.njm`, `.nja`).

#### Sonic Heroes / Shadow

- [HeroesPowerPlant](https://github.com/igorseabra4/HeroesPowerPlant/wiki/Level-Editor) - Full-featured level editor for Sonic Heroes and Shadow the Hedgehog.
- [Heroes.SDK](https://github.com/Muzzarino/Heroes.SDK) - Unified library for manipulating Sonic Heroes at runtime and definitions for internal data structures and functions. Includes format parsers for creating/extracting various game formats. Primarily intended for Reloaded II mods but contains structures useful for standalone tools.

#### Other Sonic Games

- [SonicMania-SaveEditor](https://github.com/Erik-JS/SonicMania-SaveEditor) - Save editor for Sonic Mania.
- [Sonic-Colors-Set-Editor](https://github.com/thesupersonic16/Sonic-Colors-Set-Editor) - Set editor for Sonic Colors.
- [HeroesCollisionTool](https://github.com/igorseabra4/HeroesCollisionTool) - Collision tool for Sonic Heroes.
- [HeroesVisibilityEditor](https://github.com/igorseabra4/HeroesVisibilityEditor) - Visibility editor for Sonic Heroes.
- [BBSonicDSTool](https://github.com/efimandreev0/BBSonicDSTool) - Tool for Sonic DS file formats.
- [blue-sphere](https://github.com/scurest/blue-sphere) - Tool for Sonic 3 & Knuckles special stage files.
- [Glitter](https://github.com/crash5band/Glitter) - Format library and editor application to open, modify, and resave GTE/GTM particle files for Sonic Generations.
- [libgens-sonicglvl](https://github.com/Muzzarino/libgens-sonicglvl) - Level editor and formats library for the PC version of Sonic Generations.
- [SonLVL-RSDK](https://github.com/Lavesiime/SonLVL-RSDK) - Level editor for RSDK v3/v4 games (Sonic CD, Sonic 1, Sonic 2).
- [RSDK-Reverse](https://github.com/Rubberduckycooly/RSDK-Reverse) - Reverse engineering tools for Retro Engine games (Sonic CD, Sonic 1, Sonic 2).
- [rsdkv6-extract](https://github.com/RSDKModding/rsdkv6-extract) - Extractor for RSDK v6 format files.
- [HedgeLib](https://github.com/Radfordhound/HedgeLib) - C++ library and collection of tools that aims to make modding games in the Sonic the Hedgehog franchise easier.
- [Marathon](https://github.com/hyperbx/Marathon) - Toolkit and library for Sonic The Hedgehog file formats.
- [Sonic-1-2-2013-Decompilation](https://github.com/RSDKModding/RSDKv4-Decompilation) - Complete decompilation of Sonic 1 & Sonic 2 (2013) & Retro Engine (v4).
- [UnleashedRecomp](https://github.com/hedge-dev/UnleashedRecomp) - Unofficial PC port of the Xbox 360 version of Sonic Unleashed created through static recompilation.
- [noclip.website (Sonic Colors)](https://github.com/magcius/noclip.website/tree/main/src/rres) - In-browser Sonic Colors viewer.
- [Sonic Retro (SA2 Hacking Guide)](https://info.sonicretro.org/SCHG:Sonic_Adventure_2) - Sonic Hacking Guide for Sonic Adventure 2.
- [AllStarsRacingTools](https://github.com/tge-was-taken/AllStarsRacingTools) - Unfinished tools for Sonic & Sega All Stars Racing. Incomplete and mostly for reference purposes.
- [Shuriken](https://github.com/crash5band/Shuriken) - XNCP/YNCP UI Editor for Sonic games.
- [Sega_NN_tools](https://github.com/Argx2121/Sega_NN_tools) - Python library for Blender with tools for games using Sega's NN libraries.
- [Sonic-Adventure-Animation-.JSON-Input-Output](https://github.com/Shadowth117/Sonic-Adventure-Animation-.JSON-Input-Output) - Imports and exports Sonic Adventure, Sonic Adventure DX, Sonic Adventure 2, and Sonic Adventure 2 Battle animations extracted with SA Tools into and out of 3ds Max.

### Snowblind Studios

#### Baldur's Gate: Dark Alliance

- [bgda-explorer](https://github.com/bigianb/bgda-explorer) - Data file explorer for Baldur's Gate: Dark Alliance (PS2).
- [jbgda](https://github.com/bigianb/jbgda) - Java-based tools for Baldur's Gate: Dark Alliance (PS2).
- [frostbite](https://github.com/bigianb/frostbite) - Experimental implementation of the Snowblind engine.

### Sony (First Party)

- [ico-decomp (decomp)](https://github.com/rossydoubleunderscore/ico-decomp) - Matching decompilation of Ico (PS2).
- [medievil-decomp (decomp)](https://github.com/medievildecompilation/medievil-decomp) - Matching decompilation of MediEvil (PS1).
- [mkpsxiso](https://github.com/Lameguy64/mkpsxiso) - ISO disc image maker written specifically for PlayStation homebrew development. Tool to build and extract PlayStation 1 CD images from XML. Modern cross-platform replacement for BUILDCD from PsyQ SDK. Supports mixed-mode CD-XA with audio/video streams.
- [LibOrbisPkg](https://github.com/OpenOrbis/LibOrbisPkg) - Library, GUI, and CLI tools for creating, inspecting, and modifying PlayStation 4 PKG, SFO, PFS, and related filetypes. Open-source alternative to Sony SDK tools.
- [SGXDataBuilder](https://github.com/Nenkai/SGXDataBuilder) - Creates and builds Sony SGX/SGXD Audio Banks (sgd/sgh/sgb) from standard audio formats (WAV/AC3). Used in various PSP and PS3 games including Gran Turismo 5/6, LocoRoco Cocoreccho, Ape Escape Move, and more.
- [LibreFios](https://github.com/neptuwunium/LibreFios) - PSARC library in C# for working with PlayStation PSARC archive format.
- [memcardrex](https://github.com/ShendoXT/memcardrex) - Advanced PlayStation 1 memory card editor for managing save files with support for multiple formats.
- [mymc](https://github.com/uyjulian/mymc) - Utility for working with PlayStation 2 memory card images.
- [sfo](https://github.com/hippie68/sfo) - Fast C program that reads a file to print or modify its SFO parameters. Can be used for automation or to build param.sfo files from scratch. Also available as .exe file for Windows command line.
- [ps3-ckit](https://github.com/tge-was-taken/ps3-ckit) - PS3 C code injection framework. Toolkit for running arbitrary C code in games, hooking existing functions, and inserting custom functionality.
- [dynlib](https://github.com/aerosoul94/dynlib) - IDA Pro plugin to aid PS4 user mode ELF reverse engineering. Loads PS4-specific DYNLIBDATA segment, resolves obfuscated symbol NIDs to label imports/exports, loads symbol table, and patches relocations.
- [PS4-Package-Assessor-Java](https://github.com/Cryptogenic/PS4-Package-Assessor-Java) - Java tool that evaluates PS3/PS4 .PKG files and displays information about them in a clean manner.
- [RORPSPTOOL](https://github.com/leeao/RORPSPTOOL) - Cars Race-O-Rama PSP/DS .mif/.rbh archive tools.
- [pysx](https://github.com/cmbasnett/pysx) - Python Final Fantasy VII (PSX) file extraction and conversion tools.
- [NLG-File-Editor-Tool](https://github.com/KillzXGaming/NLG-File-Editor-Tool) - Simple tool to extract and edit files from .dict/data archives used in LittleBigPlanet 2.

### Square Enix

#### Final Fantasy

- [FFCC-Decomp (decomp)](https://github.com/zcanann/FFCC-Decomp) - Matching decompilation of Final Fantasy Crystal Chronicles.
- [ff7tool](https://github.com/jkbenaim/ff7tool) - Tool for viewing Final Fantasy VII world maps.

#### Chrono Cross

- [chrono-cross-decomp (decomp)](https://github.com/jdperos/chrono-cross-decomp) - Matching decompilation of Chrono Cross (100%, based on Radical Dreamers version).

#### Xenogears

- [xenogears-decomp (decomp)](https://github.com/ladysilverberg/xenogears-decomp) - Matching decompilation of Xenogears.
- [Noah (decomp)](https://github.com/yaz0r/Noah) - Non-matching decompilation of Xenogears.

#### Xenosaga

- [xenosaga (decomp)](https://github.com/squareman/xenosaga) - Matching decompilation of Xenosaga Episode 1 (PS2, USA).

#### Vagrant Story

- [rood-reverse (decomp)](https://github.com/ser-pounce/rood-reverse) - Matching decompilation of Vagrant Story.

#### Soul Blazer

- [RustyBlazer (decomp)](https://github.com/hellow554/RustyBlazer) - Matching decompilation of Soul Blazer.

#### The World Ends With You

- [twewy (decomp)](https://github.com/Yotona/twewy) - Matching decompilation of The World Ends With You (NDS).

#### Babylon's Fall

- [BabylonsFallTools](https://github.com/Nenkai/BabylonsFallTools) - Extraction tools for Babylon's Fall PKZL/.pkz and DAT files.

#### Hitman

- [re47 (decomp)](https://github.com/0danny/re47) - Matching decompilation of Hitman: Codename 47 (2000).
- [HiTMAN Archive Manager](https://www.moddb.com/games/hitman-world-of-assassination/downloads/hitman-archive-manager) - Use this tool to install HiTMAN mods or extract the *.rpkg archives in which HiTMAN files are stored. Version 2: Now called Hitman Archive Manager
- [OpenKH](https://github.com/OpenKH/OpenKh) - Comprehensive reverse-engineering toolkit for Kingdom Hearts series. Handles MDLX/PMO models, PAM/ANB animations, TXA textures, map data, battle configs, and message files. Includes 50+ specialized editors and converters. Supports KH1, KH2, Birth by Sleep, Re:Coded, and Dream Drop Distance.
- [AudioMog](https://github.com/Yoraiz0r/AudioMog) - Free all-in-one audio modding tool that allows users to unpack and repack supported game's audio binary files. Created for Kingdom Hearts III modding and works on other games such as Melody of Memory, Final Fantasy XV, and more.
- [KH2-Worldpoint-Editor](https://github.com/Kite2810/KH2-Worldpoint-Editor) - Opens from Kingdom Hearts 2 00Worldpoint.bin and is able to edit the values there.
- [KH2Suite](https://github.com/Truthkey/KH2Suite) - Suite of programs made to assist the user in Kingdom Hearts 2 or 2 Final Mix modding.
- [KHBBS_EXA_Editor](https://github.com/Truthkey/KHBBS_EXA_Editor) - Editor for EXA events in Kingdom Hearts: Birth by Sleep.
- [KH1FM_Toolkit](https://github.com/GovanifY/KH1FM_Toolkit) - Tool used for modding the game Kingdom Hearts: 1 Final Mix.
- [RECOM_Toolkit](https://github.com/GovanifY/RECOM_Toolkit) - Tool used for modding the game Kingdom Hearts: Re Chain of Memories.
- [Gibbed.EFX](https://github.com/gibbed/Gibbed.EFX) - Tools and code for use with EFX files found in Final Fantasy XII and Tactics Ogre.
- [BBSPluginNoesis](https://github.com/Truthkey/BBSPluginNoesis) - Updated Noesis plugin for Kingdom Hearts Birth by Sleep working with modern versions of Visual Studio.
- [WOFFington](https://github.com/neptuwunium/WOFFington) - Library to process and manage World of Final Fantasy files.
- [heretic](https://github.com/adamrt/heretic) - Final Fantasy Tactics toolkit for modding.
- [KH-ReCOM-Tools](https://github.com/Murugo/KH-ReCOM-Tools) - Set of experimental tools for Kingdom Hearts Re:Chain of Memories (PS2).
- [Murugo/Misc-Game-Research (Kingdom Hearts II)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Kingdom%20Hearts%20II%20Final%20Mix) - Reverse engineering notes for Kingdom Hearts II Final Mix (PS2).
- [Murugo/Misc-Game-Research (Musashi: Samurai Legend)](https://github.com/Murugo/Misc-Game-Research/tree/main/PS2/Musashi%20Samurai%20Legend) - Reverse engineering notes for Musashi: Samurai Legend (PS2).
- [kh1](https://github.com/ethteck/kh1) - WIP Decompilation of Kingdom Hearts (PS2, JP).
- [noclip.website (Final Fantasy X)](https://github.com/magcius/noclip.website/tree/main/src/FinalFantasyX) - In-browser Final Fantasy X viewer.
- [Final Fantasy X HD translation tools](https://www.moddb.com/games/final-fantasy-x/downloads/final-fantasy-x-hd-translation-tools) - Tools for Final Fantasy X HD (PC) to extract and import game data for translation (texts and graphics).
- [noclip.website (Kingdom Hearts)](https://github.com/magcius/noclip.website/tree/main/src/KingdomHearts) - In-browser Kingdom Hearts viewer.
- [noclip.website (Kingdom Hearts II Final Mix)](https://github.com/magcius/noclip.website/tree/main/src/KingdomHearts2FinalMix) - In-browser Kingdom Hearts II Final Mix viewer.
- [noclip.website (Dragon Quest VIII)](https://github.com/magcius/noclip.website/tree/main/src/DragonQuest8) - In-browser Dragon Quest VIII viewer.
- [SlimeMoriMori](https://github.com/onepiecefreak3/SlimeMoriMori) - Reverse engineering tool for the custom compression format used in Slime Mori Mori (Dragon Quest spinoff) on Game Boy Advance.
- [fptTool](https://github.com/LinkOFF7/fptTool) - Dragon Quest VII FPT text converter.
- [kh2mdlx](https://github.com/GovanifY/kh2mdlx) - Tool for importing and exporting Kingdom Hearts 2 3D models.
- [kh2vif](https://github.com/GovanifY/kh2vif) - Model importer for Kingdom Hearts 2 (OBJ to VIF format converter).
- [KH2-Anm-Generator](https://github.com/Kite2810/KH2-Anm-Generator) - Automated animation cutscene generator for Kingdom Hearts 2 custom character models.
- [Hypercrown](https://github.com/Some1fromthedark/Hypercrown) - Tool for converting models from Kingdom Hearts 1 into more common model formats. Also converts back to the native format so that edited models can be patched into the game.
- [CrystalEditor](https://github.com/Cuyler36/CrystalEditor) - Savegame editor for the WiiWare title Final Fantasy Crystal Chronicles: My Life as a King.
- [ff7-decomp (decomp)](https://github.com/xeeynamo/ff7-decomp) - Matching decomp of Final Fantasy VII for PlayStation 1

### Sucker Punch

#### Sly Cooper

- [sly1 (decomp)](https://github.com/TheOnlyZac/sly1) - Matching decompilation of Sly Cooper and the Thievius Raccoonus (PS2).
- [SlyTools](https://github.com/VelocityRa/SlyTools) - Sly Cooper (PS2/PS3 games) modding tools & research
- [Sly2ModelRE](https://github.com/froggestspirit/Sly2ModelRE) - Researching the model format in Sly 2: Band of Thieves.
- [sly_dec.py](https://github.com/yukinogatari/Reverse-Engineering/blob/573fc1c20796fb40a982f11dfda4039eb480a34e/Sly%20Cooper/sly_dec.py) - Python script for decrypting Sly Cooper files.
- [PS23DFormat (Sly 2)](https://web.archive.org/web/20160205080914/http://ps23dformat.wikispaces.com/Sly+2+Band+of+Thieves) - Archived documentation for Sly 2 3D format.
- [PS23DFormat Wiki Archive](https://archive.org/details/wiki-ps23dformat.wikispaces.com) - Complete archive of PS23DFormat wiki covering PS2 3D formats.
- [SlyCineTrainer](https://github.com/slynders/SlyCineTrainer) - Trainer for creating camera animations in Sly Cooper games.

### Supercell

- [SCEditor](https://github.com/ToxicLand/SCEditor) - Create or edit Supercell (Clash of Clans, Clash Royale, Brawl Stars, Boom Beach) SC files. Add or edit an existing or custom character, building, or other game object.
- [SCP-Unpacker](https://github.com/baraklevy20/SCP-Unpacker) - Unpacker for Supercell's new packer (SCP) format.
- [Supercell-Extractor](https://github.com/baraklevy20/Supercell-Extractor) - Fastest tool to extract graphics from Supercell games (Clash of Clans, Clash Royale, etc.).
- [sc-compression](https://github.com/jeanbmar/sc-compression) - Node.js module to decompress and compress game assets from Supercell games. Supports multiple compression signatures: lzma, sc, sclz, sig, sc2, and zstd. Automatically infers compression signature when decompressing.
- [gltf-Supercell-IO](https://github.com/Daniil-SV/gltf-Supercell-IO) - glTF Blender IO plugin for import/export Supercell Odin (.glb) files. Supports Blender 5.0+ and Android/iOS games.
- [SupercellFlash](https://github.com/sc-workshop/SupercellFlash) - C++ library for loading and processing Supercell 2D (.sc) assets.
- [X-coder](https://github.com/lilmuff2/X-coder) - Tool to decode and encode SC files from Supercell games. Decodes SC to PNG and encodes PNG to SC. Supports Clash Royale, Brawl Stars, and other Supercell games. Supports Zstandard and LZMA compression, ZKTX format, and batch processing.

### SuperTuxKart

- [STK Blender Addons](https://github.com/supertuxkart/stk-blender) - Exporter/importer suite for SuperTuxKart `SPM` meshes and `Antarctica` engine assets.

### Telltale Games

- [TTG-Tools](https://github.com/zenderovpaulo95/TTG-Tools) - Translation utility for Telltale Games titles ([original version here](https://github.com/bartlomiejduda/TTG_Tools)). Supports texture conversion (d3dtx to dds/pvr), bitmap font editing/export to ttf, archive building/unpacking (ttarch/ttarch2), lua/lenc decryption/encryption, and extended game support including Sam & Max remasters and The Walking Dead: Definitive Series.
  - Games: Telltale Texas Hold'em, Bone (Out from Boneville, The Great Cow Race), Sam & Max (Save the World, Beyond Time and Space, The Devil's Playhouse), Strong Bad's Cool Game for Attractive People, Wallace & Gromit's Grand Adventures, Tales of Monkey Island, Hector: Badge of Carnage, Nelson Tethers: Puzzle Agent, Poker Night at the Inventory, Back to the Future: The Game, Puzzle Agent 2, Jurassic Park: The Game, Law & Order: Legacies, The Walking Dead (Season One, Season Two, Michonne, A New Frontier), Poker Night 2, The Wolf Among Us, Tales from the Borderlands, Game of Thrones, Minecraft: Story Mode, Batman: The Telltale Series.
- [Telltale-Texture-Tool](https://github.com/Telltale-Modding-Group/Telltale-Texture-Tool) - GUI application designed to make texture mods possible for Telltale Tool games. Converts D3DTX files to PNG, DDS, TGA, and other image formats and vice versa.
- [Telltale-Script-Editor](https://github.com/Telltale-Modding-Group/Telltale-Script-Editor) - Unofficial, open source script editor for games made by Telltale.
- [D3DMESH-Converter](https://github.com/Telltale-Modding-Group/D3DMESH-Converter) - Application designed for converting .d3dmesh models (Telltale Tool Models) to a standard model format and back (work-in-progress).
- [ttarch-docs](https://github.com/Telltale-Modding-Group/ttarch-docs) - Documentation and guide for reading Telltale Archive files programmatically.
- [IMAP-Editor](https://github.com/Telltale-Modding-Group/IMAP-Editor) - Application designed to edit .imap files that exist within Telltale games.
- [Unity_WBOX_Editor](https://github.com/Telltale-Modding-Group/Unity_WBOX_Editor) - Unity-based tool for importing and generating `.wbox` navigation mesh files.
- [TelltaleToolPaper](https://github.com/LucasSaragosa/TelltaleToolPaper) - Small informal paper which goes through Telltale file formats and game engine structure.
- [TelltaleGames_D3DMesh_Importer](https://github.com/WeaselOnaStick/TelltaleGames_D3DMesh_Importer) - Rewrite of RTB's "Telltale Games Almost-All-In-One Model Importer" for use in Blender (work-in-progress).

### GSC Game World

#### S.T.A.L.K.E.R

- [Geometry Decompiler plugin for 3dsmax](https://www.moddb.com/games/stalker/downloads/geometry-decompiler-plugin-for-3dsmax) - This plugin is designed to import into 3ds Max (works with versions 7-8, not tested on version 9) map geometry files of the game STALKER"
- [STALKER game archives unpacker](https://www.moddb.com/mods/old-good-stalker-evolution/downloads/stalker-game-archives-unpacker) - Needed for unpacking game archives - if you want to try to install russian version of mod - you'll need this.
- [STALKER Extractor](https://www.moddb.com/games/stalker/downloads/stalker-extractor) - STALKER database extractor. Compatible with all game versions. Allows choosing files to extract.
- [LtxParser](https://github.com/JKAnderson/LtxParser) - C# library for loading .ltx trees from the STALKER series.
- [S.T.A.L.K.E.R Mod Tool](https://www.moddb.com/games/stalker/downloads/stalker-mod-tool) - NOT MY ADDON! The S.T.A.L.K.E.R mod tool used to extract the files from the .db files. Place all gamedata files into a folder called old once you have extracted every .db to a folder called gamedata in stalkers main directory like. G:\program files\THQ\S.T.A.L.K.E.R. - Shadow of Chernobyl\gamedat...
- [Unpack Pack xr files Stalker (S.T.A.L.K.E.R.: Call of Pripyat)](https://www.moddb.com/games/stalker-call-of-pripyat/downloads/unpack-pack-xr-files-stalker) - Gathered most of the pearl scripts into a heap and adapted them to a single library. The archives are all taken from the AMK website, and re-uploaded here because they were on a Yandex disk
- [XRay Exporter v2.03 (S.T.A.L.K.E.R. Shadow of Chernobyl)](https://www.moddb.com/games/stalker/downloads/xray-exporter-v203) - Official SDK 0.4 export plugins for 3ds Max 7, 8, 9, 2008, 2009, 2010, 2011, LightWave 3D 7.5 and 8.0, and Maya 7, 8, 8.5, 2008, 2009, 2010. In addition, missing libraries have been added.
- [XRay Exporter v2.03 (S.T.A.L.K.E.R.: Call of Pripyat)](https://www.moddb.com/games/stalker-call-of-pripyat/downloads/xray-exporter-v2031) - Official export plugins for SDK 0.5, 0.6, 0.7 for 3ds Max 8, 9, 2008, 2009, 2010, 2011, LightWave 3D 8.0 and Maya 7, 8, 8.5, 2008, 2009, 2010. Also added missing libraries.
- [X-ray game asset tools pack FINAL](https://www.moddb.com/games/stalker/downloads/x-ray-game-asset-tools-pack-final) - Complete toolset for editing all aspects of S.T.A.L.K.E.R. games. Includes: AI Wrapper 2.2 (compiling AI levels), converter (geometry and models), ACDC pack (editing all.spawn), and Milkshape/Maya plugins....
- [Clear Sky: Game Database Unpacker](https://www.moddb.com/games/stalker/downloads/clear-sky-game-database-unpacker) - This utility allows you to unpack all the game files.
- [STALKER utilities pack](https://www.moddb.com/games/stalker/downloads/stalker-utilities-pack) - Tool for editing LTX configuration files in S.T.A.L.K.E.R. games.
- [Updated Milkshape plugin](https://www.moddb.com/games/stalker/downloads/updated-milkshape-plugin) - Updated Milkshape plugin for S.T.A.L.K.E.R. (dated 01/08/2016).
- [Database converter (S.T.A.L.K.E.R.: Call of Pripyat)](https://www.moddb.com/mods/call-of-chernobyl/downloads/cop-coc-db-converter) - COP/COC converter, which unpacks db files to gamedata files.
- [Extractor de archivos para S.T.A.L.K.E.R.: Shadow of Chernobyl](https://www.moddb.com/games/stalker/downloads/extractor-de-archivos-para-stalker-shadow-of-chernobyl) - Lightweight program for extracting all files from S.T.A.L.K.E.R.: Shadow of Chernobyl for modding purposes.
- [General X Ray SDK CS-CoP Tools (S.T.A.L.K.E.R.: Call of Pripyat)](https://www.moddb.com/games/stalker-call-of-pripyat/downloads/general-x-ray-sdk-tools) - General X Ray SDK Tools. This archive contains dds2tgaLE X-Ray game asset converter 02 june 2011 rev10192 Fake flatness CS&CoP; Compilers 2010 v3.0

### Troika Games

- [Vampire the Masquerade Bloodlines Blender 2.42 plugin](https://www.moddb.com/games/vampire-the-masquerade-bloodlines/downloads/vampire-the-masquerade-bloodlines-blender-242-plugin) - Blender 2.42 plugin for importing and exporting Vampire: The Masquerade - Bloodlines model files (MDLx format) with UV coordinate support.
- [NOD Noesis Plugin (Vampire: The Masquerade – Redemption)](https://www.moddb.com/games/vampire-the-masquerade-redemption/downloads/nod-noesis-plugin) - Noesis plugin for importing and exporting NOD and NAD model/animation formats. Supports full model and animation import/export (v2). Alternative to Milkshape and Maya 2.5.

### Terminal Reality

- [NocturneDecomp (decomp)](https://github.com/NearlyTRex/NocturneDecomp) - Matching decompilation of Nocturne.

#### BloodRayne

- [br2proj](https://github.com/PavelSharp/br2proj) - BloodRayne 2 Blender add-on for importing `.tex` textures, `.smb` models, and `.bfm`/`.skb` skeletal meshes.

### THQ / Rainbow Studios

- [OpenBarnyard (decomp)](https://github.com/InfiniteC0re/OpenBarnyard) - Matching decompilation of Barnyard and TOSHI 2.0 engine (Blue Tongue Entertainment).
- [OpenToshi (decomp)](https://github.com/AdventureT/OpenToshi) - Matching decompilation of de Blob and Toshi engine (Blue Tongue Entertainment).
- [OpenJPOG (decomp)](https://github.com/AdventureT/OpenJPOG) - Matching decompilation of Jurassic Park: Operation Genesis and Toshi Engine v1.0 (Blue Tongue Entertainment).

#### Cars

- [carsraceorama](https://github.com/leeao/carsraceorama) - Noesis plugin for Cars Mater-National and Cars Race-O-Rama. Model importer/exporter supporting multiple platform formats: XNG (Xbox 360/PC), P3G (PS3), GCG (Wii/GameCube), DXG (PC/Xbox), PSG (PS2), SLT (text).

#### MX vs ATV

- [3ds Export script (MX vs ATV Reflex)](https://www.moddb.com/games/mx-vs-atv-reflex/downloads/3ds-export-script) - 3DS Max export plugin for MX vs ATV Reflex.

#### Twisted Metal

- [tm1_decomp (decomp)](https://github.com/abelbriggs1/tm1_decomp) - Matching decompilation of Twisted Metal (PS1, NTSC-J).
- [tmb_decomp (decomp)](https://github.com/abelbriggs1/tmb_decomp) - Matching decompilation of Twisted Metal: Black (PS2).
- [tmhc (decomp)](https://github.com/jacobleeharris/tmhc) - Matching decompilation of Twisted Metal: Harbor City (PS2).

### 3D Realms

- [BioMenaceDecomp (decomp)](https://github.com/lethal-guitar/BioMenaceDecomp) - Matching decompilation of Bio Menace.
- [cosmore (decomp)](https://github.com/smitelli/cosmore) - Matching decompilation of Cosmo's Cosmic Adventure (96% complete).

#### Duke Nukem 3D

- [Landscaping Tools (Duke Nukem 3D)](https://www.moddb.com/games/duke-nukem-3d/downloads/landscaping-tools) - Files and resources for creating landscape terrain in Duke Nukem 3D. Includes tutorial files and example maps (not intended for gameplay).
- [Duke Nukem 3D source code](https://www.moddb.com/games/duke-nukem-3d/downloads/duke-nukem-3d-source-code) - Full source code to the classic first person shooter Duke Nukem 3D. Based on the v1.5 code. Installations on how to compile can be found in the included README.TXT.

#### Duke Nukem: Manhattan Project

- [Duke Nukem Manhattan Project Mesh & Bones Editing Tool](https://www.moddb.com/games/duke-nukem-manhattan-project/downloads/duke-nukem-manhattan-project-mesh-bones-editing-tool) - Official mesh and bones editing tool for Duke Nukem Manhattan Project

#### Duke Nukem Forever (2001)

- [Blender to CPJ Plugin for DNF2001](https://www.moddb.com/mods/dnf2001-restoration-project/downloads/blender-to-cpj-plugin-for-dnf2001) - This plugin will allow you to export to the proprietary CPJ format for DNF2001 from blender.
- [Updated Blender to CPJ Plugin (Duke Nukem Forever 2001)](https://www.moddb.com/mods/dnf2001-restoration-project/downloads/updated-blender-to-cpj-plugin) - This plugin will allow you to export to the proprietary CPJ format for DNF2001 from blender.

#### Duke Nukem Forever (2011)

- [MegaPackageExtractor](https://github.com/DaZombieKiller/MegaPackageExtractor) - Duke Nukem Forever (2011) MegaPackage.dat extractor.

#### The Outforce

- [Outforce meshes extractor](https://www.moddb.com/games/the-outforce/downloads/outforce-meshes-extractor) - Mesh and model extractor for The Outforce. Created by szkaradek123.
- [The Outforce Box extractor tool](https://www.moddb.com/games/the-outforce/downloads/the-outforce-box-extractor-tool) - *.box archive extractor tool for the game "The Outforce"

### Techland

- [Call of Juarez: Bound In Blood - Map Pak Tool](https://www.moddb.com/mods/cojbib-map-pak-tool/downloads/call-of-juarez-bound-in-blood-map-pak-tool) - Convert CoJBiB custom maps into Pak file with required folder structure by the game. Portable (no installation) just start and create, Enjoy!

### Thekla Inc

- [noclip.website (The Witness)](https://github.com/magcius/noclip.website/tree/main/src/TheWitness) - In-browser The Witness viewer.
- [Braid Editor Universe Tools](https://www.moddb.com/games/braid/downloads/braid-editor-universe-tools) - For information on how to start and use the Braid Universe Tools, make sure you click the link to the official tutorial on ModDB, which you can find after the jump.

### Slitherine / Proxy Studios

- [Blender Gladius Addon v1.1 (Warhammer 40,000: Gladius - Relics of War)](https://www.moddb.com/mods/blender-gladius-addon/downloads/blender-gladius-addon-v11) - The first release. It should mostly work but may still have some bugs.

### Visceral Games

- [Gibbed.Visceral](https://github.com/gibbed/Gibbed.Visceral) - Tools and code for use with Visceral developed games (Dante's Inferno, Dead Space 2).
- [Noesis-Plugins (Durik256)](https://github.com/Durik256/Noesis-Plugins) - Community Noesis plugins collection including Visceral Games support.
- [MeltyTool (Visceral)](https://github.com/MeltyPlayer/MeltyTool/tree/main/FinModelUtility/Libraries/VisceralGames) - Format viewer/exporter for Visceral Games titles.
- [ZenHAX Thread](https://zenhax.com/viewtopic.php?t=15376) - Forum discussion and research on Visceral Games file formats. *(Link archived/dead)*
- [VisceralToolkit](https://github.com/Greavesy1899/VisceralToolkit) - Set of tools for editing Visceral Games after "The Godfather (2006)" including Dead Space and Dante's Inferno.

### Wargaming

- [yretenai/Akizuki](https://github.com/neptuwunium/Akizuki/tree/csharp) - World of Warships file format research project.

### Ubisoft

- [rgh (decomp)](https://github.com/rghdecomp/rgh) - Matching decompilation of Rabbids Go Home (2009).
- [Rayman2Lib](https://github.com/szymski/Rayman2Lib) - Various tools for Rayman 2 modding and content extraction.
- [Rayman2FunBox](https://github.com/rtsonneveld/Rayman2FunBox) - Pack of a few fun mods for Rayman 2 on PC using memory editing, notably the First Person Mod.
- [raymap](https://github.com/byvar/raymap) - Map viewer/editor for OpenSpace games including Rayman 2, Rayman 3, Rayman Arena, and Tonic Trouble. Supports multiple platforms (PC, PS1, PS2, N64, GameCube, Xbox, iOS, DS, 3DS). Web version available at raym.app.
- [GangstarVegasTextTool](https://github.com/efimandreev0/GangstarVegasTextTool) - Tool to work with ".lng" archives from Gangstar Vegas games on any platforms.
- [Jormungandr](https://github.com/neptuwunium/Jormungandr) - Anvil Engine research and tools for Ubisoft's Anvil Engine (Assassin's Creed series).
- [Ubitunedec](https://github.com/ldeon/Ubitunedec) - Program for decoding and exporting .SPK audio files found in Ubisoft game .dat files. Can play back and decode sound and music encoded into the game files.
- [Ray1Editor](https://github.com/RayCarrot/Ray1Editor) - 2D game editor derived from Ray1Map for modifying maps in Rayman 1 games. Supports Rayman 1 PS1, PC (multiple versions), Educational, Designer, by his Fans, and 60 Levels versions.
- [CyArchiveTool](https://github.com/Surihix/CyArchiveTool) - Tool to extract and repack the .pack archive files from the PC version of the game Zone of Enders 2 MARS.
- [SabTool](https://github.com/BoBoBaSs84/SabTool) - CLI tool for managing files for The Saboteur.
- [FCI.FAT.Tool](https://github.com/Ekey/FCI.FAT.Tool) - Tool for extracting FAT/DAT archives from Far Cry Instincts.
- [Hawx Model Tool 1.04 (Tom Clancy's H.A.W.X.)](https://www.moddb.com/games/tom-clancys-hawx/downloads/hawx-model-tool-104) - The Original Hawx Modding tool, and the most asked for. This lets you modify the models, All the models in Tom Clancy's hawx. Made by lotsbiss
- [Complete UMP40 Source Code and Assets (Tom Clancy's Rainbow Six 3: Raven Shield)](https://www.moddb.com/mods/raven-shield-software-development-kit/downloads/complete-ump40-source-code-and-assets) - All the source code, textures, and models for Twi's custom UMP40 submachine gun. Great for learning to make custom guns!
- [Damage Triggers - mapping tool (Tom Clancy's Rainbow Six 3: Raven Shield)](https://www.moddb.com/games/tom-clancys-rainbow-six-3-raven-shield/downloads/damage-triggers-mapping-tool) - Mappers can use this simple tool to add damage ability to their triggers. Set it to kill players or tangos nearby, or to damage objects in your map. SOURCE CODE INCLUDED.
- [Flashlights for enemies - mapping tool (Tom Clancy's Rainbow Six 3: Raven Shield)](https://www.moddb.com/games/tom-clancys-rainbow-six-3-raven-shield/downloads/flashlights-for-enemies-mapping-tool) - Mappers can use this simple tool to give flashlights to tangos in their nighttime maps. Flashlights work in singleplayer and multiplayer.
- [.forge extractor/replacer by Turfster (Assassin's Creed)](https://www.moddb.com/mods/aci-texmod-clothes-mod/downloads/forge-extractorreplacer-by-turfster) - Data/files extractor for Assassin's Creed and Assassin's Creed II and some other games using Scimitar engine. It's also capable of replacing archived files, including textures. Its additional plugins are already installed. The program is made by Turfster and it belongs to him (and the full credit...

#### Anno 1800

- [Anno 1800 Mod Loader](https://github.com/magicalcookie/anno1800-mod-loader) - The one and only mod loader for Anno 1800. Supports loading of unpacked RDA files, XML merging, and Python mods.
- [Modding Tools for Anno](https://marketplace.visualstudio.com/items?itemName=JakobHarder.anno-modding-tools) - Visual Studio Code extension with utilities to build Anno 1800 mods.

### Bethesda

*The Elder Scrolls, Fallout series, and Starfield.*

- [BAE](https://www.nexusmods.com/starfield/mods/165) - Bethesda Archive Extractor application for BSA/BA2 archives.
- [BSA Browser](https://github.com/AlexxEG/BSA_Browser) - Bethesda Archive browser and extractor for BSA and BA2 archives.
- [Gibbed.Fallout4](https://github.com/gibbed/Gibbed.Fallout4) - Tools for Fallout 4 file formats.
- [xEdit](https://tes5edit.github.io) - Advanced graphical module editor and conflict detector for Bethesda games.
- [F2 TOOLS PAK BY LEONARDO (Fallout 2)](https://www.moddb.com/games/fallout-2/downloads/f2-tools-pak-by-leonardo) - Toolset for creating Fallout 2 mods. For more information, see Readme.txt in the archive. Archive contains: BIS mapper, Dims mapper, SFall script editor, Notepad++, Frame animator.
- [Fallout2 FRM converter v 2.0](https://www.moddb.com/games/fallout-2/downloads/fallout2-frm-converter-v-20) - Convert Fallout's FRM image files to the BMP, JPG, PNG, TGA, TIF, PBM, PGM and PPM files formats, and then convert BMP, TIF and PNG files back into FRM's! Use your own art in Fallout....
- [Wrye Bash](https://wrye-bash.github.io) - Swiss army knife for modding Bethesda games with features including mod installation, conflict manager, load order manager and automatic merging.
- [Synthesis](https://github.com/Mutagen-Modding/Synthesis) - Framework and GUI to empower people to create mods via code instead of by hand, mainly used to create patches.
- [Spriggit](https://github.com/Mutagen-Modding/Spriggit) - Tool to facilitate converting Bethesda plugin files to a text based format that can be stored in Git.
- [ck-cmd](https://github.com/aerisarn/ck-cmd) - Command-line helper for executing some Creation Kit/Engine commands.
- [hkxc](https://www.nexusmods.com/skyrimspecialedition/mods/126214) - CLI tool to convert between x86/x64 HKX and XML animation files.
- [HKX Conversion Tool](https://www.nexusmods.com/skyrimspecialedition/mods/128839) - hkxc Windows GUI for converting between HKX and XML animations files.
- [hkxPoser](https://www.nexusmods.com/skyrimspecialedition/mods/11783) - .hkx animation file editor.
- [DDS Texture Converter](https://www.nexusmods.com/skyrimspecialedition/mods/111378) - Application for bulk conversion and resizing of DDS textures.
- [DDS Texture Scanner](https://github.com/niston/TextureScan) - Application scanning for DDS textures with abnormal dimensions.
- [nifxml](https://github.com/niftools/nifxml) - Repository for the nif.xml file, which contains the NIF file format description for NetImmerse/Gamebryo NIF model format used in Elder Scrolls and Fallout games.
- [NifTools Blender Addon](https://github.com/niftools/blender_niftools_addon) - Blender add-on to enable import and export of NetImmerse file formats including .nif, .kf, and .egm used in Elder Scrolls and Fallout games.
- [PyNifly](https://github.com/BadDogSkyrim/PyNifly) - Export/import tools between Blender and the NIF format, using Bodyslide/Outfit Studio's Nifly layer. Supports Skyrim LE, Skyrim SE, Fallout 4, Fallout New Vegas, Fallout 76, and Fallout 3.
- [Material-Editor](https://github.com/ousnius/Material-Editor) - Small UI application to edit BGSM/BGEM material files used in Bethesda games.
- [noclip.website (Morrowind)](https://github.com/magcius/noclip.website/tree/main/src/Morrowind) - In-browser Morrowind viewer.
- [Daggerfall utilities](https://www.moddb.com/games/daggerfall/downloads/daggerfall-utilities) - Archive of tools for the DOS version of Daggerfall, including quest editing tools and character modification tools.
- [ES Plugin Cracker 0.001b (Elder Scrolls IV: Oblivion)](https://www.moddb.com/games/oblivion/downloads/es-plugin-cracker-0-001b) - Rudimentary Win32 application for loading plugins authored with a higher Construction Set version (v0.001b).
- [BodySlide and Outfit Studio](https://github.com/ousnius/BodySlide-and-Outfit-Studio) - Tool to convert, create, and customize outfits and bodies for Bethesda games.
- [Cathedral Assets Optimizer](https://www.nexusmods.com/skyrimspecialedition/mods/23316) - Tool to automatically optimize BSAs, meshes, textures and animations for Bethesda games.

### 2K Games / Firaxis Games

- [Civilization IV Plugins for 3DS Max 6](https://www.moddb.com/games/civilization-iv-original/downloads/civilization-iv-plugins-for-3ds-max-6) - Official plugin for 3DS Max 6 with support for 3D models used in Sid Meier's Civilization IV.
- [Civilization IV Plugins for 3DS Max 7+](https://www.moddb.com/games/civilization-iv-original/downloads/civilization-iv-plugins-for-3ds-max-7) - Official plugin for 3DS Max 7 and newer with support for 3D models used in Sid Meier's Civilization IV.

### 2K Czech / Illusion Softworks

- [mafia-re (decomp)](https://github.com/Marvisak/mafia-re) - Matching decompilation of Mafia: The City of Lost Heaven.
- [Max4dsTools](https://github.com/pudingus/Max4dsTools) - 3ds Max plugin for import and export of the 4ds model format used in Mafia: The City of Lost Heaven. Supports meshes, LODs, billboarding, sectors, portals, skinned models, materials, and glows.
- [mafia-formats](https://github.com/RoadTrain/mafia-formats) - 010 Editor templates for Mafia: The City of Lost Heaven file formats. Also partly for Hidden & Dangerous 2 and Wings of War.
- [EffectsBinEditor](https://github.com/legion2809/EffectsBinEditor) - Effects.bin editor for Mafia: The City of Lost Heaven written in C# (WPF application). Program to add or remove particle effects from a particular mission.

### Natsume

- [hm64-decomp (decomp)](https://github.com/harvestwhisperer/hm64-decomp) - Matching decompilation of Harvest Moon 64 (N64).
- [hmawl (decomp)](https://github.com/ChrisNonyminus/hmawl) - Matching decompilation of Harvest Moon: A Wonderful Life (GameCube).

### Falcom

- [YsViDecomp (decomp)](https://github.com/GrantBenR/YsViDecomp) - Matching decompilation of Ys VI (Steam).

### Working Designs

- [lunar2-psx-decomp (decomp)](https://github.com/Zackmon/lunar2-psx-decomp) - Matching decompilation of Lunar 2: Eternal Blue Complete (PS1).

### Toby Fox

- [UndertaleDecomp (decomp)](https://github.com/kittibyte/UndertaleDecomp) - Matching decompilation of UNDERTALE (Xbox One v1.13X).

### Terry Cavanagh

#### VVVVVV

- [extract.vvv](https://github.com/Swyter/extract.vvv) - Simple program to extract original music from VVVVVV game. Extracts all 15 tracks from `vvvvvvmusic.vvv` files and outputs them as OGG Vorbis format.

### Studio MDHR

- [cuphead-decomp (decomp)](https://github.com/jmxamongusmodder/cuphead-decomp) - Matching decompilation of Cuphead.

### TaleWorlds Entertainment

#### Mount&Blade

- [mab-tools](https://github.com/Swyter/mab-tools) - 010 Editor binary templates for Mount&Blade 1.011 and Warband file formats. Includes templates for `.brf` (Binary Resource File), `.sco` (Scene Object), `options.dat` (gameplay and graphics settings including battle size), `controls.dat` (keymapping with support for two assignable key slots per action), and `sg*.sav` savegame files.
- [cartographer](https://github.com/Swyter/cartographer) - Mount&Blade strategic map editor. Allows real-time positioning of world parties/cities. Supports importing/exporting OBJ files, editing map.txt and module_parties.py, with first-person camera controls and terrain visualization.

### TT Games

- [isle (decomp)](https://github.com/isledecomp/isle) - Matching decompilation of LEGO Island (1997).
- [Lego-City-Undercover-Decompilation (decomp)](https://github.com/Nintendocustom/Lego-City-Undercover-Decompilation) - Matching decompilation of Lego City Undercover.
- [BionicleHeroesTools](https://github.com/REDxEYE/BionicleHeroesTools) - Blender plugin for importing Bionicle Heroes files. Supports NUP and HGP model formats and PAK archive extraction. Requires Blender 3.1 to 3.5.
- [LegoTools](https://github.com/REDxEYE/LegoTools) - Tools for working with LEGO game file formats.

### Acclaim Entertainment

- [turok3 (decomp)](https://github.com/Drahsid/turok3) - Matching decompilation of Turok 3: Shadow of Oblivion (N64).

### Whoopee Camp

- [psx_tomba (decomp)](https://github.com/hansbonini/psx_tomba) - Matching decompilation of Tomba! (PS1, 100%).

### Team Shanghai Alice

- [ReC98 (decomp)](https://github.com/nmlgc/ReC98) - Matching decompilation of Touhou PC-98 games (74% complete).

### 5th Cell

- [locksmith (decomp)](https://github.com/redraincatching/locksmith) - Matching decompilation of Lock's Quest.

### Asmik Ace Entertainment

- [lsddecomp (decomp)](https://github.com/FirecatFG/lsddecomp) - Matching decompilation of LSD: Dream Emulator (PS1).

### Stainless Games

- [dethrace (decomp)](https://github.com/dethrace-labs/dethrace) - Matching decompilation of Carmageddon (1997).

### Gumi

- [client (decomp)](https://github.com/decompfrontier/client) - Matching decompilation of Brave Frontier client.

### Ninja Kiwi

- [BTD5-Decomp (decomp)](https://github.com/NKHook/BTD5-Decomp) - Matching decompilation of Bloons TD 5.

### Eutechnyx

- [Gt2 (decomp)](https://github.com/dashr9230/Gt2) - Matching decompilation of Ford Racing (2000).
- [Caper (decomp)](https://github.com/dashr9230/Caper) - Matching decompilation of The Italian Job (2001).

### Eurocom

- [eurochef](https://github.com/eurotools/eurochef) - Rust crates and utilities for Eurocom EngineX(T) files. Supports texture extraction, entity extraction, map extraction, filelist re-packing, EDB to Euroland 4 decompiler, and Blender plugin.
  - Games: Sphinx and the Shadow of Set Demo Disc, Buffy The Vampire Slayer: Chaos Bleeds, Sphinx and the Cursed Mummy, Spyro: A Hero's Tail, Robots, Predator: Concrete Jungle, Batman Begins, Ice Age 2: The Meltdown, Pirates of the Caribbean: At World's End, Ice Age: Dawn of the Dinosaurs, G-Force, Spider-Man 4, GoldenEye 007.
  - Formats: EDB, ELX, SFX, filelist (v4-v10).
  - Platforms: PC, Xbox, Xbox 360, GameCube, Wii, PlayStation 2.
- [eurosound-editor](https://github.com/eurotools/eurosound-editor) - .NET program reimplementing the original EuroSound tool by Eurocom for editing EngineX sound files.
- [eurosound-explorer](https://github.com/eurotools/eurosound-explorer) - C# tool for viewing parameters and extracting audio from SFX files compatible with Eurocom games.
- [eurotext](https://github.com/eurotools/eurotext) - Custom tool to edit and inspect text-based EngineX spreadsheets.
- [binary-templates](https://github.com/eurotools/binary-templates) - 010 Editor binary templates for visually opening Sphinx and EngineX file formats.
- [hashcodes](https://github.com/eurotools/hashcodes) - Public hashcodes list for various Eurocom games, useful for cross-checking.
- [blender-addon](https://github.com/eurotools/blender-addon) - Import and export Eurocom Scene Export (.ESE) files in Blender. Supports 3D models, skins + animations, cameras, maps and scripts.
- [euroland_exporters](https://github.com/eurotools/euroland_exporters) - Import and export Eurocom Scene Export (.ESE) files in Blender; 3D models, skins + animations, cameras, maps and scripts.
- [euroland-elf-texture-extractor](https://github.com/eurotools/euroland-elf-texture-extractor) - Tool to extract textures from random EuroLand data files (*.elf) that may not be inspectable otherwise (e.g. different versions that don't work with the EuroLand .exe).
- [sphinx-savegame-editor](https://github.com/eurotools/sphinx-savegame-editor) - C# tool to edit and view savegame files for The Sphinx and the Cursed Mummy game.
- [sphinxtools](https://github.com/Swyter/sphinxtools) - Unpackers and modding tools for the GameCube version of Sphinx and the Cursed Mummy. Extracts files from Filelist.000 containers, includes 010 Editor binary templates for EDB and SFX formats, and provides demuxing tools for GameCube IMA ADPCM audio.
- [gforce-tools](https://github.com/Swyter/gforce-tools) - 010 Editor binary templates for newer Eurocom/EngineX formats. Includes Filelist extractor script supporting version 7 (Athens 2004, Spyro: A Hero's Tail, Robots, Predator: Concrete Jungle, Batman Begins, Ice Age 2, Pirates of the Caribbean: At World's End, The Mummy: Tomb of the Dragon Emperor, 007: Quantum of Solace, Ice Age: Dawn of the Dinosaurs, G-Force, Dead Space: Extraction, Spider-Man 4 prototype, GoldenEye 007).

### Hasbro Interactive

- [frogger-psx (decomp)](https://github.com/HighwayFrogs/frogger-psx) - Matching decompilation of Frogger (1997, PS1, 100%).

### H2O Entertainment

- [aidyn (decomp)](https://github.com/blackgamma7/aidyn) - Matching decompilation of Aidyn Chronicles: The First Mage (N64).

### Bohemia Interactive

- [BI Editing Tools 2 (ARMA 2)](https://www.moddb.com/games/arma-2/downloads/bi-editing-tools-2) - Complete editing tool suite for Bohemia Interactive's game engine used in ARMA II. This installer will overwrite previously released BI Editing Tools for Arma I (user made data are intact) and it can not be possible to pack and finalize content for Arma I using the newer tools. Despite it may be ...

### Bugbear Entertainment

- [blender_flatout2_trackai_importer](https://github.com/gmazy/blender_flatout2_trackai_importer) - Blender addon for importing trackai.bin files from FlatOut 2.

### Blizzard Entertainment

- [wow.export](https://github.com/Kruithne/wow.export) - Export toolkit for World of Warcraft models and textures.
- [WoWDBDefs](https://github.com/wowdev/WoWDBDefs) - Client database definitions for World of Warcraft (DBD files for extracting game data).
- [OWLib](https://github.com/overtools/OWLib) - DataTool program that lets you extract models, maps, and files from Overwatch.
- [noclip.website (World of Warcraft - Vanilla, The Burning Crusade, Wrath of the Lich King)](https://github.com/magcius/noclip.website/tree/main/src/WorldOfWarcraft) - In-browser World of Warcraft (Vanilla) viewer.
- [3DS/Obj MDX Converter](https://www.moddb.com/games/warcraft-iii/downloads/3ds-obj-mdx-converter)
- [Starcraft Modding Tools](https://www.moddb.com/games/starcraft/downloads/starcraft-modding-tools) - This file contains the four Starcraft Mod Tools used in this tutorial. These files include: Arsenal III by King Arthur For the beginner or advanced custom designer, arsenal III is essential. Arsenal III edits StarCraft's primary data files, also known as DAT files. DAT files control all of the ba...
- [WoW Model Viewer 5.0.7 (World of Warcraft)](https://www.moddb.com/games/world-of-warcraft/downloads/wow-model-viewer-5-0-7) - The WoW Model Viewer is a 3D model viewer for World of Warcraft. It uses the data files included with the game to display the models from the game: creatures, characters, spell effects, doodads, items, etc.
- [Blizzard DATA unpacker (Warcraft: Orcs & Humans)](https://www.moddb.com/games/warcraft-orcs-humans/downloads/blizzard-data-unpacker) - Unpacker DATA archives from Blizzard games: - Warcraft: Orcs and Humans [1994] - Blackthorne [1994] - Lost Vikings [1993] (partially, there may be broken files) With source codes in C.

### Westwood Studios / EA Los Angeles

- [C&C big extractor](https://www.moddb.com/groups/tiberium-essence-fans/downloads/cc-big-extractor) - Tool for extracting files from Command & Conquer BIG archive files. Supports: Generals, Generals: Zero Hour, Tiberium Wars, Kane's Wrath, Red Alert 3, Red Alert 3: Uprising, Tiberian Twilight. Originally uploaded by bibber.
- [Command & Conquer 3 Asset Extractor](https://www.moddb.com/groups/tiberium-essence-fans/downloads/command-conquer-3-asset-extractor) - This program can extract asset files from C&C streams. This program can extract asset files from C&C streams. You can also extract models (W3DAnimation, W3DCollisionBox, W3DContainer, W3DHierarchy, W3DMesh), textures (OnDemandTexture, Texture) and sounds/music (AudioFile, AudioFileMP3Passthrough,...

### Mojang Studios

- [NBTSerializer](https://github.com/gigaherz/NBTSerializer) - Minecraft NBT serialization library.

### Grasshopper Manufacture

- [No-More-RSL](https://github.com/Timo654/No-More-RSL) - Unpacker/repacker for Grasshopper Manufacture .RSL format. Works with most if not all Grasshopper Manufacture games using this format.

### Free Radical Design

- [tspak](https://github.com/OpenRadical/tspak) - Small utility for extracting TimeSplitters .pak files. Supports P4CK (Timesplitters 1 & 2 PS2), P5CK (TimeSplitters: Future Perfect), and P8CK (TimeSplitters 2 GameCube/Xbox).

### Enhance Games

- [Rezun](https://github.com/XAYRGA/Rezun) - Unpacks .dat and .bnk files in Rez Infinite.

### Gravity / Ragnarok Online

- [libgrf](https://github.com/cmbasnett/libgrf) - Library for reading GRF archives found in Ragnarok Online.
- [grf-python](https://github.com/cmbasnett/grf-python) - Python wrapper for libgrf.

### Stencyl

- [MbsEditor](https://github.com/Monkeytron/MbsEditor) - Allows viewing and editing of scene .mbs files from Stencyl games. Can open scene data files and view/edit data within them including positions of level terrain collision and actors.

### Her Interactive

- [AVFExt](https://github.com/puggsoy/AVFExt) - AVF file converter/extractor for Her Interactive games (in particular the Nancy Drew series).

### HeroForge

- [HeroForge_parser](https://github.com/REDxEYE/HeroForge_parser) - Library for parsing CKB files from HeroForge character creation platform.
- [HeroBuilder](https://github.com/REDxEYE/HeroBuilder) - Blender addon for loading HeroForge characters into Blender. Works with CKB files exported from HeroForge.

### Yostar / Revived Witch

- [unneko](https://github.com/lico-n/unneko) - Extraction tool for Revived Witch nekodata files. Supports both regular and patch nekodata files.

### CyberStep

- [CB.KAR.Tool](https://github.com/Ekey/CB.KAR.Tool) - Tool for extracting KAR archives from CosmicBreak Universal.

### Mobile Games

- [RSBR.PAK.Tool](https://github.com/Ekey/RSBR.PAK.Tool) - Tool for extracting PAK (OBB) archives from mobile game Run Sackboy! Run! (Android/iOS).

### Bandai Namco (Dragon Ball)

- [binunpack](https://github.com/shibbo/binunpack) - Program for unpacking the BIN archives in DragonBall: Revenge of King Piccolo, written in Python 3.
- [DBFModToolCollection](https://github.com/Tiniifan/DBFModToolCollection) - Collection of tools to simplify modding on Dragon Ball Fusion. Includes utilities for working with game files and archives.
- [C&C: Renegade Official Modding Tools](https://www.moddb.com/games/cc-renegade/downloads/cc-renegade-official-modding-tools) - Official set of modding tools for Command & Conquer: Renegade.
- [CnC Renegade Tools](https://www.moddb.com/games/cc-renegade/downloads/cnc-renegade-tools) - CnC Renegade Tools by Westwood to help modders in making mods for Renegade.
- [Final Big (C&C: Generals)](https://www.moddb.com/games/cc-generals/downloads/final-big) - No further information avaliable.
- [Final Big 3 (C&C: Generals)](https://www.moddb.com/games/cc-generals/downloads/final-big-3) - Version 0.2 released March 5th, 2003.
- [Gmax+RenX+Renegade Public Tools (C&C: Generals Zero Hour)](https://www.moddb.com/games/cc-generals-zero-hour/downloads/gmaxrenxrenegade-public-tools) - This contains 3 modelling tools for editing C&C Generals and Renegade.

## 🔗 Related Lists

- [Awesome Modding](https://github.com/loicreynier/awesome-modding.bak) - Resources for game modding and customization.
- [Awesome Game Decompilations](https://github.com/CharlotteCross1998/awesome-game-decompilations) - A curated list of awesome game decompilations.
- [Awesome Game Datasets](https://github.com/leomaurodesenv/game-datasets) - Datasets and resources for game research.
- [Awesome Reverse Engineering](https://github.com/tylerha97/awesome-reversing) - List of reverse engineering resources.
- [Awesome Software Reverse Engineering](https://github.com/ReversingID/Awesome-Reversing/blob/master/_software.md) - Comprehensive list of reverse engineering software and tools.
- [Awesome Gamedev](https://github.com/ellisonleao/magictools) - Curated list of game development resources.

## 📄 License

[CC0](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.

## 🙏 Acknowledgments

Shoutout to [MeltyPlayer/awesome-game-file-formats](https://github.com/MeltyPlayer/awesome-game-file-formats) - this started as a fork of it with my own bookmark collection, but I eventually decided to add more sections and reorganize it.