# Initial Tile Sizes
vertical_tile_number = 11
tile_size = 64

# Initialize Game Window Size
screen_height = vertical_tile_number * tile_size
screen_width = 1280

# Initialize CSV Files Per Level
level_0 = {
    'terrain': 'Assets/levels/0/level_0_terrain.csv',
    'coins':'Assets/levels/0/level_0_coins.csv',
    'enemies':'Assets/levels/0/level_0_enemies.csv',
    'constraints':'Assets/levels/0/level_0_constraints.csv',
    'player': 'Assets/levels/0/level_0_player.csv',
    'grass': 'Assets/levels/0/level_0_grass.csv',
    'node_pos': (110,400),
    'unlock': 1,
    'node_graphics': 'Assets/Overworld/0'
}
level_1 = {
    'terrain': 'Assets/levels/0/level_0_terrain.csv',
    'coins':'Assets/levels/0/level_0_coins.csv',
    'enemies':'Assets/levels/0/level_0_enemies.csv',
    'constraints':'Assets/levels/0/level_0_constraints.csv',
    'player': 'Assets/levels/0/level_0_player.csv',
    'grass': 'Assets/levels/0/level_0_grass.csv',
    'node_pos': (300,220),
    'unlock': 2,
    'node_graphics': 'Assets/Overworld/1'
}
level_2 = {
    'terrain': 'Assets/levels/0/level_0_terrain.csv',
    'coins':'Assets/levels/0/level_0_coins.csv',
    'enemies':'Assets/levels/0/level_0_enemies.csv',
    'constraints':'Assets/levels/0/level_0_constraints.csv',
    'player': 'Assets/levels/0/level_0_player.csv',
    'grass': 'Assets/levels/0/level_0_grass.csv',
    'node_pos': (480,610),
    'unlock': 2,
    'node_graphics': 'Assets/Overworld/2'
}
levels = {
    0: level_0,
    1: level_1,
    2: level_2
}