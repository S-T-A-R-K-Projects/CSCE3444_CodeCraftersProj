# CSCE3444_CodeCraftersProj
The project from CSCE 3444 Code Crafters group

## Prerequisites

You must have Ren'Py installed on your system. Download the Ren'Py SDK from the official website at https://www.renpy.org/latest.html and extract it to a location of your choice. We used Ren'Py 8.3.6.

## Running the Game

To launch and test the game, follow these steps:

1. Open the Ren'Py Launcher application from your Ren'Py SDK installation directory.

2. In the Ren'Py Launcher, select "preferences" and add the project directory by navigating to the location where this repository is cloned.

3. Once the projects list refreshes, locate "Whispers_in_the_Dark" in the project list.

4. Click on "Whispers_in_the_Dark" to select it.

5. Click the "Launch Project" button to run the game in development mode.

## Building Distributions

To compile and build distributable versions of the game:

1. Open the Ren'Py Launcher.

2. Select the "Whispers_in_the_Dark" project from the list.

3. Click "Build Distributions" in the launcher menu.

4. Select the platforms you want to build for. The project is configured to support Windows, Mac, and Linux builds as defined in project.json.

5. Click "Build" to generate the distribution packages.

6. The built distributions will be located in the project directory under a folder named with the project name and version number.

## Testing and Development

To test changes made to the game:

1. Modify the .rpy script files located in the "code-crafters/Whispers_in_the_Dark/game" directory.

2. Launch the game using the Ren'Py Launcher as described above.

3. Ren'Py will automatically recompile modified .rpy files into .rpyc bytecode files when you launch the game.

4. Use the Ren'Py console during gameplay by pressing Shift+O to access debugging features.

5. Enable developer mode in the Ren'Py Launcher for additional debugging tools and features.

## Project Structure

The main game files are located in:
- code-crafters/Whispers_in_the_Dark/game/ - Contains all game scripts, assets, and configuration files
- code-crafters/Whispers_in_the_Dark/game/script.rpy - Main game script entry point
- code-crafters/Whispers_in_the_Dark/game/images/ - Game image assets
- code-crafters/Whispers_in_the_Dark/game/audio/ - Game audio files
