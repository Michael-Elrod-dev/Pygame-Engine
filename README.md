# Mythical Meadows - Michael Elrod

## In-Game Image
![Game](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/InGame.png)

## Sprites
All sprites used in this project can be found in the /Assets/ folder. These sprites were bought from Craftpix.net by me.

## Software Versions
OS Version: Ubuntu 22.04.1 LTS or Windows 11<br>
Python Version: Python 3.10.6<br>
Pygame Version: Pygame 2.1.2<br>
Environment: Visual Studio Code<br>
Video: https://youtu.be/_754X8bVQW0

## How to play
1. Download the full repository<br>
2. Make sure you have the software versions listed above
3. Run the program with the following command:
```bash
python3 Game.py
```

## Motivation
I have created a 2D game engine before in C++ which can be viewed [HERE](https://github.com/Michael-Elrod-dev/2DGameEngine), but the game I built with it was a top-down game that didn't have a platform the player could move on. For this project, I wanted to challenge myself by creating a side-scrolling game like classic Mario or Vagante on Steam.

## Reasoning
I used a similar structure for this project as my C++ game engine, but simplified it for Python. I created classes that hold data or perform supportive work for other classes (Models), classes that track interactions between game objects, the player, and the level (Controllers), and classes that handle rendering objects on the screen and runnig the game loop (View).

## Work Flow
### Main
![Main](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Game.png)

Game.py - This file initializes the screen and runs the "game loop" for the duration of the game based on the level passed into the Level class. The game update function is level.run(). This file also holds the Game class which stores the game state between levels.

### Overworld Initialization
![Overworld Initialization](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Overworld.png)

Overworld.py - This file initalizes the assets used for the overworld screen and changes there state based on user input and the current level.

### Level Initialization
![Level Initialization](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Level.png)

Level.py - This file is the core of the project. It handles object initialization, terrain setup, asset paths, camera view, and controls the state of the game and player. This file also tracks all collisions between the player sprite, the terrain, enemies and coins. The update function within Level.py which runs every frame and updates all sprites based on user input and camera movement.

### Player Initialization
![Player Initialization](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Player.png)

Player.py - This file handles the player's status by getting user input and updating the status of the player character based on its velocity and applies gravity. This file also calls the classes that import game assets. The update function within Player.py runs every frame.

### User Interface
![UI](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/UI.png)

UI.py - This file initializes and controls the user interface. This includes the health bar and coins collected.

### Tiles
![Tiles](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Tile.png)

Tiles.py - This file initializes the 64x64 tiles and moves them based on the camera shift which is based on player input. This includes enemies, coins, decorations, terrain and more. This class is called from other classes and does not update itself.

### Assets
![Assets](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Assets.png)

Assets.py - This file is responsible for importing the sprite PNG's for the game. This includes the CSV file for the map, the setions of the tiles image, and player particles.

### Decorations
![Decorations](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Decoration.png)

Decorations.py - This file initializes sprites in the background and renders them.

### Effects
![Effects](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Effects.png)

Effects.py - This file is responsible for looping the particle animations one time per player status, such as jumping, landing, and dying.

### Enemy
![Enemy](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Enemy.png)

Enemy.py - This file is responsible for controlling the movement speeds and animations for the enemy sprites based on map constraints in the CSV file from settings.

### Settings
![Settings](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Settings.png)

Settings.py - This file holds the CSV file paths which are the foundation for the level structure as well as the settings for tile size and screen size.

## Future Work
As the engine grows larger with each milestone it slowly becomes slightly more specific towards this exact game and is losing its generic implementations. I am constantly trying to find new ways to achieve the same outputs with different implementations in order to keep the engine as generic as possible as well as keeping editable parts of the code in one place. For example I try to keep all file path inputs for asset initialization in 1 or 2 files to allow for easy modification. Some things that are not so generic that the camera still does not follow the player on the Y axis. If this were implemented then you could truly create and 2D platformer or top down game with this code. In its current state it would be a very simple game but definitely possible. Other things that may not be considered generic is the actions of the enemies which are hard coded.

One mistake about this implementation that is very different from my C++ engine is that the developer cannot choose which "components" an entity has. For example, the player character can always jump once and move at the same speed. Although the sprites for animation and the character can be changed, the abilities of the character are hard-coded (although easily changed)


## Diagram
![Diagram](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/GameDiagram.png)

## Contributions
In order to learn more about implementing the animation methods by searching through directories in Python, as well as some of the method structures needed for collision detection and map structuring in this project, I referenced a few videos made by Clear Code on YouTube
