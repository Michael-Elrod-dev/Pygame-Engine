import pygame
from Src.Tiles import AnimatedTile
from random import randint

class Enemy(AnimatedTile):
    # Initialize
    def __init__(self, size, x, y):
        super().__init__(size, x, y, 'Assets/Enemy/run')
        self.speed = randint(3, 5)

    # Move sprite based on speed
    def move(self):
        self.rect.x += self.speed

    # Flip sprite based on velocity
    def reverse_image(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    # Reverse sprites speed when flipped
    def reverse(self):
        self.speed *= -1

    # Update
    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()