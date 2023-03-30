import pygame
from os import walk
from csv import reader
from Src.Settings import tile_size

# Open and read CSV file from path
def import_csv_layout(path):
    terrain_map = []

    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map
    
# Cut PNG into sections for tiles
def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surface = pygame.Surface((tile_size, tile_size), flags = pygame.SRCALPHA)
            new_surface.blit(surface, (0,0), pygame.Rect(x, y, tile_size, tile_size))
            cut_tiles.append(new_surface)
    
    return cut_tiles

# Import Asset Folder
def import_folder(path):

    surface_list = []
    for _,__,image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
            
    return surface_list

# Find Asset File Paths & Import
def import_assets(self):
    character_path = 'Assets/Character/'
    self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[]}

    for animation in self.animations.keys():
        full_path = character_path + animation
        self.animations[animation] = import_folder(full_path)

# Find Particle Assets
def import_particles(self):
    self.run_particles = import_folder('Assets/Character/particles/run')