# Netplay Setup

<!-- [:fontawesome-brands-youtube: Video Guide by Maafia](https://www.youtube.com/watch?v=l78N0rqMRac){ class="md-button md-button--primary" target="_blank" rel="noopener" data-md-color-primary="red" data-md-color-accent="red" } -->

This page's contents will help you set up Smash Remix to play with others online on a computer.

## 1. Patching the ROM

Smash Remix is a **ROM hack**, meaning you must apply the Remix data to the original game. Smash remix does not include the original game's copyrighted material.

1.  Open the [Web Patcher](../patcher/index.md).
2.  **Version:** Select the desired Smash Remix version. Default is latest release.
3.  **ROM File:** Select your original Super Smash Bros. ROM.
4.  Click **Apply** and save the new `.z64` file.

## 2. Emulator Installation
1.  Download the latest version of [<img alt="RMG-K" class="twemoji" src="RMG.svg"> RMG-K](https://github.com/Jay-Day/RMG-K/releases). Using the portable version is recommended.
> **Linux/Mac users:** use the Windows version with `wine` to enable netplay.
2.  Extract the package, run the program and click **Select ROM Directory**.
3.  Point the emulator to the folder where you saved your patched ROM.

## 3. Controller Configuration

If using a controller to play, these are the recommended plugins:

| Controller | Plugin |
|---|---|
| Modern Controller | `Generic USB Input` (Default) |
| GameCube Controller with adapter | `GameCube Adapter` |
| N64 Controller with adapter | `Raphnetraw N64 Adapter` |

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
4.  1. To **Host** a room: **Right-click** the bottom section, select the game in your list and select **Host**.
    2. To **join** a room: Find the game you want to join in the bottom section and double click it.
![Netplay Server Window](netplay4.png)

### Tips

- **Desyncs:** If a game desyncs, hit the **Drop** button and **Start** again to restart the game. There's no need to close the emulator or create a new room.
- **Chat:** Messages appear as an overlay in the game window, even in Full Screen.

## 5. Other tips

- **Full Screen mode:** Use `Alt+Enter`
- **Updates:** You can check for updates on the menu `Help>Check for Updates`
- **Volume:** You can adjust the volume using `Ctrl+A` or `Settings>Audio`