# Dr. Adkins' Zombie Lab Escape - Michael Elrod

## Motivation
I have created a 2D game engine before in C++, but the game I built with it was a top down game that didnt have a platform the player could move on. So for this project I wanted to try doing a side scrolling style game like classic Mario or Vagante on Steam.

## Reasoning
I went with the stucture that I did becasue I have already built a 2D game engine in C++ so I mostly just transfered over a lot of the logic from that but simpified it since python works a bit differetly. I have classes that just simply hold data or do work for other classes (Models), classes that interact between game objects, the player and the level (Controllers), and the classes that handle the calls to render objects on the screen (View).

## Work Flow
![Game Loop](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Images/Main.png)
Main.py - This file initializes the screen to render on and runns the "game loop" for the suration of the game. The game update function is level.run().

![World Initialization](https://github.com/Michael-Elrod-dev/Zombie-Lab/blob/main/Src/Level.py)

## Future Work
