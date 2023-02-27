# Zombie Lab Escape - Michael Elrod

## Motivation
I have created a 2D game engine before in C++ which can be viewed [HERE](https://github.com/Michael-Elrod-dev/2DGameEngine), but the game I built with it was a top down game that didnt have a platform the player could move on. So for this project I wanted to try doing a side scrolling style game like classic Mario or Vagante on Steam.

## Reasoning
I went with the stucture that I did becasue I have already built a 2D game engine in C++ so I mostly just transfered over a lot of the logic from that but simpified it since python works a bit differetly. I have classes that just simply hold data or do work for other classes (Models), classes that interact between game objects, the player and the level (Controllers), and the classes that handle the calls to render objects on the screen (View).

## Work Flow
### Game Loop
![Game Loop](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Main.png)

Main.py - This file initializes the screen to render on and runs the "game loop" for the suration of the game. The game update function is level.run().

### World Initialization
![World Initialization](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Level.png)

Level.py - This file handles the terrain setup and camera view as well as the state of the game and player. This file also tracks all collisions between the player sprite and the terrain. Here is the update fuction within Level.py.

### Player Initialization
![Player Initialization](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Player.png)

Player.py - This file handles the players status by getting user input and imports assets. Here is the update function within Player.py.

### Animation
![Animation](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Animation.png)
![Animation2](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Animation2.png)

Animation.py - This file handles changing the sprite to poroduce an animation effect on the player character based on input. Animation.py is run on update and does not update itself.

### Tiles
![Tiles](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Tiles.png)

Tiles.py - This file initializes the tiles and moves them based on the camera shift which is based on player input.

### Effects
![Effects](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Effects.png)

Effects.py - This file initializes and updates the effect sprites based on the camera shift which is based on player input.

### Settings
![Settings](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Settings.png)

Settings.py - This file holds hard codeded setting like the terrain structure, the size of the game window and the tile size.

## Future Work
I had planned to bring this project much further but I had many time conflicts with exams, interviews and other course work. As the project currently stands, the developer could upload any sprite images to the appropriate files. As long as they were correctly sized the landscape and player character could be reimagined into any form making this implementation quite generic on its own in terms of a 2D platformer. The implementation for importing assets uses a python built in function to search folders and loop thourgh its full contents. This way, not only different images could be used but animation frames could easily be reduced or extended.

As I review the program I struggle to find any portion of the engine that would not be considered a generic implementation. For the most part this engine lacks quite a few components and capabilities but the ones that are implemented are done so in a way that the world and player character can be changed to anything within the realm of a 2D platformer by simply changing the PNG files within the project and creating a new level_data map in the Settings.py file. One mistake about this implementation that is very different from my C++ engine is that the developer cannot choose which "components" an entity has. For example, the player charcter can always jump once and moves at the same speed. Although the sprites for animation and the character can be changed, the abilities of the charcter are hard coded (although easily changed). I hope to implement this in the future as well as the following: enemies, attacks, terrain sprites,  background image, user interface and SFX/music.


## Contributions
In order to learn more about implementing the animation methods by searching thorugh directories in Python as well as some of the method structures needed for the collision detection and map structuring in this project I referenced a few videos made by Clear Code on youtube.
