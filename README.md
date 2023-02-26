# Zombie Lab Escape - Michael Elrod

## Motivation
I have created a 2D game engine before in C++, but the game I built with it was a top down game that didnt have a platform the player could move on. So for this project I wanted to try doing a side scrolling style game like classic Mario or Vagante on Steam.

## Reasoning
I went with the stucture that I did becasue I have already built a 2D game engine in C++ so I mostly just transfered over a lot of the logic from that but simpified it since python works a bit differetly. I have classes that just simply hold data or do work for other classes (Models), classes that interact between game objects, the player and the level (Controllers), and the classes that handle the calls to render objects on the screen (View).

## Work Flow
### Game Loop
![Game Loop](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Main.png)

Main.py - This file initializes the screen to render on and runns the "game loop" for the suration of the game. The game update function is level.run().

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
