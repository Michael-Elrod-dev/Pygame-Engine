# Predefined Map Structure

#screen_height = vertical_tile_num * tile_size

#level_data = [
# '                                                   ',
# '                                                   ',
# '                                                   ',
# ' XX P  XXX            XX                           ',
# ' XX                                                ',
# ' XXXX         XX         XX                        ',
# ' XXXX       XX                                     ',
# ' XX    X  XXXX    XX  XX    XXXXXXXXXXXXXXXXXXXXXXX',
# '       X  XXXX    XX  XXX                          ',
# '    XXXXXXXXXXXX  XXXXXXXX                         ',
# 'XXXXXXXX  XXXXXXXXXX  XXXX                         ']

level_data = {
    'terrain': 'Assets/levels/level_data/level_0.csv'
}

vertical_tile_num = 22
tile_size = 32
screen_width = 1280
screen_height = vertical_tile_num * tile_size