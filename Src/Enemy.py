import pygame
from Src.Tiles import AnimatedTile
from Src.Assets import import_folder
from Src.Effects import *
from random import randint

class Enemy(AnimatedTile):
    # Initialize
    def __init__(self, size, x, y, type, path, death):
        if type == 'skeleton':
            super().__init__(size, x, y, path)
            self.death_animation = death
            self.death_frames = import_folder(self.death_animation)
        elif type == 'wisp':
            super().__init__(size, x, y, path)
            self.death_animation = death
            self.death_frames = import_folder(self.death_animation)
        elif type == 'tauro':
            super().__init__(size, x, y, path)
            self.death_animation = death
            self.death_frames = import_folder(self.death_animation)
            
        self.speed = randint(3, 5)
        
    # Call Enemy Death Animation
    def death(self, effects_group):
        death = Effects(self.rect.center, 'death', self.death_animation)
        effects_group.add(death)

    # Move Sprite Based On Speed
    def move(self):
        self.rect.x += self.speed

    # Flip Sprite Based On Velocity
    def reverse_image(self):
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image, True, False)

    # Reverse Sprite SPeed When Flipped
    def reverse(self):
        self.speed *= -1

    # Update
    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()