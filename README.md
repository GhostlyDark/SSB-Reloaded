# SSB Reloaded

SSB Reloaded is an HD texture pack for GLideN64, [Dolphin](https://github.com/GhostlyDark/SSB-Reloaded-Dolphin), rt64 and BattleShip.

> [!IMPORTANT]
> Release files can be found over at [evilgames.eu](https://evilgames.eu/texture-packs/ssb-reloaded.htm) and [GitHub Releases](https://github.com/GhostlyDark/SSB-Reloaded/releases/latest).

![](/ssb-reloaded.jpg)



## Porting scripts

> [!Tip]
> This repository contains scripts for automated porting of textures to supported platforms. They require bash v4 and a native Linux environment. On Windows, it is recommended to use WSL2 from within the `wsl.localhost` file system. The scripts will also work using MSYS2, but file operations are going to run much slower. Currently available are `dolphin.sh` (WIP) and `battleship.sh`.

For the Battleship script, `python3` is required:

```
sudo apt install python3
```

Make script executable and run it:

```
chmod u+x battleship.sh
```

```
./battleship.sh
```

Ported files will be available inside `_build`.



## Texture rescaling

The `ssb.tdb` file contains information about the original texture sizes, which can be used by [Bighead's Custom Texture Tool](https://forums.dolphin-emu.org/Thread-custom-texture-tool-ps-v52-5) to rescale them to a new upscale ratio. This way, an HD replacement for a 32x32 texture can be rescaled to 8x the original resolution (256x256), down from however big the given HD texture might be.



## GLideN64

> [!NOTE]
> Latest [WIP build](https://github.com/gonetz/GLideN64/releases/github-actions) required. Use `PJ64Legacy-Qt-x86` if Project64 is your emulator of choice.

Pre-compiled `.hts` files are `cache` files and have to be located inside:

- Project64: `Project64/Plugin/GFX/cache`
- RMG: `RMG/Cache/cache`
- mupen64plus:
-- Windows: `%appdata%/mupen64plus/cache`
-- Linux: `~/.cache/mupen64plus/cache`
-- macOS: `~/Library/Application Support/Mupen64plus/cache`
- mupen64plus-nx (RetroArch): `RetroArch/system/Mupen64plus/cache`


**Only for advanced users:** HTS cache can be generated from the source PNG textures:

- Project64: `Project64/Plugin/GFX/hires_texture/SMASH BROTHERS`
- RMG: `RMG/Data/hires_texture/SMASH BROTHERS`
- mupen64plus:
-- Windows: `%appdata%/mupen64plus/hires_texture/SMASH BROTHERS`
-- Linux: `~/.local/share/mupen64plus/hires_texture/SMASH BROTHERS`
-- macOS: `~/Library/Application Support/Mupen64plus/hires_texture/SMASH BROTHERS`
- mupen64plus-nx (RetroArch): `RetroArch/system/Mupen64plus/hires_texture/SMASH BROTHERS`


Required graphics settings (named differently depending on emulator):

- Set texture pack usage: `Use texture pack` | `txHiresEnable` | `Use High-Res textures` to **On**
- Set use of full alpha: `Use full transparencies` | `txHiresFullAlphaChannel` | `Use High-Res Full Alpha Channel` to **On**
- Set use of HTS over HTC: `Use file storage instead of memory cache` | `txHiresTextureFileStorage` | `Use enhanced Hi-Res Storage` to **On**


Optional (but recommended) settings:

- Set cache compression: `Compress texture cache` | `txCacheCompression` | `Use High-Res Texture Cache Compression` to **Off**
- Fix black lines: `Fix black lines between 2D elements: For adjacent 2D elements` | `CorrectTexrectCoords: 1 (Auto)` | `Continuous texrect coords: Auto`



## Dolphin

> [!NOTE]
> Download a recent [release build](https://dolphin-emu.org/download). DDS textures for playing are highly recommended.

- Click `File --> Open User Folder` and copy the texture folder into `Load/Textures`
- Open `Graphics --> Advanced` and activate `Load Custom Textures`



## BattleShip

> [!NOTE]
> Download the port from [here](https://github.com/JRickey/BattleShip/releases/latest).

Unpack the `.zip` file into the `mods` directory. In-game, press `Escape` and `Enable Hi-Res Texture Pack` under `Assets/Mods`.



## Credits

Texture packs:

- [Nerrel's MM N64HD](http://www.emutalk.net/threads/56677-Majora-s-Mask-N64HD-Project)
- [OoT Community Retexture](http://www.emutalk.net/threads/55307-Zelda-Ocarina-of-time-Community-Retexture-Project-V7)
- [Pietschie & Bad Randolph's Super Smash Bros. HD](http://www.emutalk.net/threads/44911-Pietschie-amp-Bad-Randolphs-Super-Smash-Bros-HD)
- [Poke Headroom's Render96 HD Texture Pack](https://github.com/pokeheadroom/RENDER96-HD-TEXTURE-PACK)

Additional contributors:

- **Admentus:** Original Dolphin port
