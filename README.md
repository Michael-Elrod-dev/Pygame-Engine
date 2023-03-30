# Zombie Lab Escape - Michael Elrod

## Game Image
![Game](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Game.png)

## Sprites
All sprites used in this project can be found in the /Assets/ folder. These sprites were bought from Craftpix.net by me.

## Program Versions
OS Version: Ubuntu 22.04.1 LTS<br>
Python Version: Python 3.10.6<br>
Pygame Version: Pygame 2.1.2<br>
Enviorment: Visual Studio Code

## Motivation
I have created a 2D game engine before in C++ which can be viewed [HERE](https://github.com/Michael-Elrod-dev/2DGameEngine), but the game I built with it was a top-down game that didn't have a platform the player could move on. For this project, I wanted to challenge myself by creating a side-scrolling game like classic Mario or Vagante on Steam.

## Reasoning
I used a similar structure for this project as my C++ game engine, but simplified it for Python. I created classes that hold data or perform supportive work for other classes (Models), classes that track interactions between game objects, the player, and the level (Controllers), and classes that handle rendering objects on the screen and runnig the game loop (View).

## Work Flow
### Game Loop
![Game Loop](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Main.png)

Main.py - This file initializes the screen and runs the "game loop" for the duration of the game based on the level passed into the Level class from the settings file. The game update function is level.run().

### World Initialization
![World Initialization](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Level.png)

Level.py - This file is the core of the project. It handles object initialization, terrain setup, camera view, and the state of the game and player. This file also tracks all collisions between the player sprite the terrain, enemies and coins. The update function within Level.py which runs every frame and updates all sprites based on user input and camera movement.

### Player Initialization
![Player Initialization](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Player.png)

Player.py - This file handles the player's status by getting user input and updating the status of the player character based on its velocity and applys gravity. This file also calls the classes that import game assets. The update function within Player.py runs every frame.

### Animation
![Animation](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Animation.png)

Animation.py - This file is used the sprite to produce an animation effect on the player character based on input like changing direction. Animation.py is run on update and does not update itself.

### Tiles
![Tiles](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Tiles.png)

Tiles.py - This file initializes the tiles and moves them based on the camera shift which is based on player input. This includes enemies, coins and eventually more. This class is called from other classes and does not update itself.

### Assets
![Assets](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Assets.png)

Assets.py - This file is responsible for importing the sprite png's for the game. This includes the CSV file for the map, the setions of the tiles image and particles.

### Effects
![Effects](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Effects.png)

Effects.py - This file is responsible for looping the particle animations one time per player status, such as jumping and landing.

### Enemy
![Enemy](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Enemy.png)

Enemy.py - This file is responsible for controlling the movement speeds and animations for the enemy tiles based on map constraints in the CSV file from settings.

### Settings
![Settings](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Settings.png)

Settings.py - This file holds hard-coded settings like the terrain structure, the size of the game window, and the tile size.

## Future Work
Crossed out sections have been added to the game since the last update. ~~EDxample.~~
~~I had planned to bring this project much further, but I had many conflicts with exams, interviews, and other coursework. As the project currently stands, the developer can upload any sprite images to the appropriate files. As long as they are correctly sized, the landscape and player character can be reimagined into any form, making this implementation quite generic in terms of a 2D platformer. The implementation for importing assets uses a Python built-in function to search folders and loop through their full contents. This way, not only different images can be used, but animation frames can easily be reduced or extended.~~

As I review the program, I struggle to find any portion of the engine that would not be considered a generic implementation. For the most part, this engine lacks quite a few components and capabilities, but the ones that are implemented are done so in a way that the world and player character can be changed to anything within the realm of a 2D platformer by simply changing the PNG files within the project and creating a new level CSV file in Settings.py. The only thing I can think of is that my game currently does not allow the player to move the camera up and down but only left and right. If I were to implement this, you could even change the assets in the Assets folder to make a top down 2d game with this engine instead of a side scroller.

One mistake about this implementation that is very different from my C++ engine is that the developer cannot choose which "components" an entity has. For example, the player character can always jump once and move at the same speed. Although the sprites for animation and the character can be changed, the abilities of the character are hard-coded (although easily changed). I hope to implement this in the future, as well as the following: ~~enemies,~~ attacks, ~~terrain sprites,~~ background image, user interface, and SFX/music. ~~I would also like to add that in this project I have more than one file that technically handles getting assets from the Assets folder and looping them based on player status. In the futre it may be a good idea to combine these functions to one file as right now it can be a little confusing to understand. Another thing I would like to change is in the Settings.py file. I would like to change level_data to a map that takes in a csv file instead of a hand built map with X's. This way the engine could use csv tile maps built by 3rd party software for more creativity.~~


## Diagram
![Diagram](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Diagram.png)

## Contributions
In order to learn more about implementing the animation methods by searching through directories in Python, as well as some of the method structures needed for collision detection and map structuring in this project, I referenced a few videos made by Clear Code on YouTube
