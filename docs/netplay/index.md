# Netplay Setup

<!-- [:fontawesome-brands-youtube: Video Guide](https://www.youtube.com/watch?v=placeholder){ class="md-button md-button--primary" target="_blank" rel="noopener" data-md-color-primary="red" data-md-color-accent="red" } -->

{% include "disclaimer.md" %}

This page's contents will help you set up Smash Remix to play with others online on a computer.

## 1. Patching the ROM

Smash Remix is a **ROM hack**, meaning you must apply the Remix patch to the original game.

1.  Open the [Web Patcher](../patcher/index.md).
2.  **Version:** Select the desired Smash Remix version. Default is latest release.
3.  **ROM File:** Select your original Super Smash Bros. ROM.
4.  Click **Apply patch** and save the new `.z64` file.

## 2. Emulator Installation
1.  Download the latest version of [<img alt="RMG-K" class="twemoji" src="RMG.svg"> RMG-K](https://github.com/Jay-Day/RMG-K/releases/latest). Using the portable version is recommended.
> **Linux/Mac users:** use the Windows version via `wine`, as native netplay support currently isn't available for these platforms.
2.  Extract the package, run the program and click **Select ROM Directory**.
3.  Point the emulator to the folder where you saved your patched ROM.

## 3. Controller Configuration

If using a controller to play, these are the recommended plugins:

| Controller | Plugin |
|---|---|
| Modern Controller | `Generic USB Input` (Default) |
| GameCube Controller with adapter | `GameCube Adapter` |
| N64 Controller with adapter | `Raphnetraw N64 Adapter` |

=== "Modern Controller"

    Modern USB/Wireless controllers (Xbox/PS/Switch/etc.) work with the `Generic USB Input` input plugin (selected by default).

    Controls are configurable via the **Input** button.

=== "N64 Controller"

    N64 controllers connected to a [Raphnet N64 to USB adapter](https://www.raphnet-tech.com/products/n64_usb_adapter_gen3/index.php) work with the `Raphnetraw N64 Adapter` input plugin. No configuration required.

    If you have a different N64 to USB adapter, you'll have to use the `Generic USB Input` input plugin and configure your controls manually via the **Input** button.

=== "GameCube Controller"

    GameCube controllers connected to a GC to USB adapter (Lossless/Nintendo/Mayflash) work with the `GameCube Adapter` input plugin.

    If your adapter has different modes available, make sure it's set to **Switch** or **Wii U** mode, otherwise the input plugin won't detect it.

    Controls are configurable via the **Input** button.

=== "Keyboard"

    Keyboards work with the `Generic USB Input` input plugin (selected by default).

    Controls are configurable via the **Input** button.

??? info "Using the Right Stick for Smash Attacks or Tilt Attacks (usually NOT tournament legal)"
    If you want to use the right stick for smash or tilt attacks,
    map the **N64 D-Pad** to your controller's **Right Stick**.
    Then, when selecting characters in-game, set the desired
    **Dpad Map** option.

    ![Dpad Map Option](dpad1.png)
    ![Dpad Map Option](dpad2.png)

## 4. Online Play (Netplay)

### How to Connect

1. Click the **Netplay** button.
![Netplay Button](netplay1.png)
2. Set your **Username** at the top of the netplay window, then click on **Live Server List** for a complete list of available servers.
![Netplay Nickname](netplay2.png)
3. The `ping` column indicates the connection latency between you and the server, meaning **the lower the better**.
![Netplay Servers](netplay3.png)
4.  1. To **host:** Once connected to a server, press the `Create` button (or right-click on the lobby list) and select the game to host a lobby for.
    2. To **join** a room: Find the game you want to join in the bottom section and double click it.
![Netplay Server Window](netplay4.png)

### Tips

- **Desyncs:** If a game desyncs, the host should hit the **Drop** button and **Start** again to restart the game. There's no need to close the emulator or create a new room.
- **Chat:** Messages appear as an overlay in the game window, even in Full Screen.

## 5. Other tips

- **Full Screen mode:** Use `Alt+Enter`
- **Updates:** Automatic update notifications are enabled by default, though you can check for updates manually via `Help > Check for Updates`
- **Volume:** You can adjust the volume using `Ctrl+A` or `Settings>Audio`