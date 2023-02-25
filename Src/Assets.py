# Walk: Searches through directories
from os import walk
from csv import reader
import pygame


# Import Asset Folder
def import_folder(path):

    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)
            
    return surface_list


# Find Asset File Paths & Import
def import_assests(self):
    character_path = 'Assets/Character/'
    self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[]}

    for animation in self.animations.keys():
        full_path = character_path + animation
        self.animations[animation] = import_folder(full_path)


# Find Particle Assets
def import_particles(self):
    self.run_particles = import_folder('Assets/Character/particles/run')
    

def import_csv(path):
    terrain_map = []
    with open(path) as map:
        level = reader(map, delimiter =  ',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map