import pygame, sys, Src
from Src.Settings import *
from Src.Tiles import Tile
from Src.Level import Level

# Initialize Window
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dr. Adkins' Zombie Lab Escape!")
clock = pygame.time.Clock()
level = Level(level_data, screen)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
            
    screen.fill((40, 40, 40))
    level.run()
    pygame.display.update()
    clock.tick(60)