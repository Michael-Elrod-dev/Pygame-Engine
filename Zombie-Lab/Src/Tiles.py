import pygame


class Tile(pygame.sprite.Sprite):
    # Initialize Map Tiles
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect  = self.image.get_rect(topleft = pos)
        
    
    # Update Tiles To Camera
    def update(self, x_shift):
        self.rect.x += x_shift