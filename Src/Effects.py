import pygame    
from Src.Assets import import_folder

class Effects(pygame.sprite.Sprite):
    # Initialize
    def __init__(self, pos, type, path):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.5
        
        if type == 'jump':
            self.frames = import_folder(path)
        elif type == 'land':
            self.frames = import_folder(path)
        elif type == 'death':
            self.frames = import_folder(path)
   
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    # Loop Frames Once
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    # Update
    def update(self, camera_x):
        self.animate()
        self.rect.x += camera_x