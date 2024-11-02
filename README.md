# Timberman Bot

Timberman Bot is an automation script for the popular Timberman game that leverages screen capture and keyboard simulation to automate gameplay. Highest score made by this bot is 11516

![ezgif com-video-to-gif-converter(4)](https://github.com/user-attachments/assets/325a24d8-9287-4c2a-a50b-0dbffd92ba5c)

## Features

- **Game Mode Selection**: 
  - Choose between solo or multiplayer modes: two, four or eight players
- **Dynamic Screen Capture**: 
  - Continuously monitors the game screen for changes in specified areas.
- **Automated Keyboard Input**: 
  - Uses the `keyboard` library to simulate keystrokes based on screen analysis, allowing for real-time gameplay responses.

## Technical Details

- **Main Libraries Used**:
  - `mss`: For efficient screen capturing.
  - `keyboard`: For simulating user input.
  - `winsound`: For playing sounds based on game events.
  - `pygetwindow`: To handle window operations.
  - `PIL (Pillow)`: For image processing tasks.

- **How It Works**:
  - The script captures a specific portion of the screen and analyzes pixel colors to detect game elements.
  - Based on the analysis, it triggers keyboard events to simulate actions.
  - When branch appears above player it changes sides and continue, ignoring other side.
  - The loop runs until manually stopped, allowing continuous gameplay automation.
 
- **How To Run**
  - Run script
  - Select game mode; solo or multiplayer
  - Start game then play selected mode
  - When in game click `s` to make stript take reference screenshots and start playing game
  - Click `q` to stop script
  - Every new game user need to stop and start script by clicking `q` and `s` to make new reference screenshots
