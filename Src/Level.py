import pygame
from Src.Tiles import *
from Src.Assets import *
from Src.Settings import *
from Src.Enemy import Enemy
from Src.Player import Player
from Src.Effects import Effects

class Level:
    # Initialize
    def __init__(self, level_data, surface):
        # Init Settings
        self.display_surface = surface
        self.world_shift = 0
        self.current_x = None

        # Init Player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        # Particles
        self.particle_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False

        # Init Terrain
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

        # Init Coins 
        coin_layout = import_csv_layout(level_data['coins'])
        self.coin_sprites = self.create_tile_group(coin_layout,'coins')

        # Init Enemy 
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout,'enemies')

        # Init Constraint 
        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constraint_sprites = self.create_tile_group(constraint_layout,'constraint')

    # Place player sprite and end goal
    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, value in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if value == '0':
                    sprite = Player((x, y), self.display_surface, self.init_jump_particles)
                    self.player.add(sprite)
                    
                if value == '1':
                    player_surface = pygame.image.load('Assets/Overworld/hat.png').convert_alpha()
                    sprite = StaticTile(tile_size, x, y, player_surface)
                    self.goal.add(sprite)

    # Turn CSV file into sprite group
    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, value in enumerate(row):
                if value != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('Assets/Terrain/terrain_tiles.png')
                        tile_surface = terrain_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'coins':
                        if value == '0': 
                            sprite = Coin(tile_size, x, y, 'Assets/Coins/gold')
                        if value == '1': 
                            sprite = Coin(tile_size, x, y, 'Assets/Coins/silver')

                    if type == 'enemies':
                        sprite = Enemy(tile_size,x,y)

                    if type == 'constraint':
                        sprite = Tile(tile_size,x,y)

                    sprite_group.add(sprite)
            
        return sprite_group

    # Check enemy collision with map constraints
    def enemy_collision(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraint_sprites, False):
                enemy.reverse()

    # Create jump particles (player)
    def init_jump_particles(self, pos):
        jump_particle = Effects(pos, 'jump')
        self.particle_sprite.add(jump_particle)

    # Checks If Player Lost/Regains Ground Contact
    def init_landing_particles(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.particle_sprite.sprites():
            offset = pygame.math.Vector2(0,20)
            landing_particle = Effects(self.player.sprite.rect.midbottom - offset, 'land')
            self.particle_sprite.add(landing_particle)

    # To Animate Landing Particle
    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    # X Axis Colission Checking
    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        collidable_sprites = self.terrain_sprites.sprites()

        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0: 
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        # Reset Left/Right Contact Checks
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False
          
    # Y Axis Colission Checking          
    def vertical_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        collidable_sprites = self.terrain_sprites.sprites()

        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                    player.jump_cooldown = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        # Reset Ground/Ceiling Checks
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0.1:
            player.on_ceiling = False

    # X Axis Camera Scroll                
    def camera_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        # Control Camera Relative To Player Pos
        if player_x < (screen_width/3) and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > (screen_width - (screen_width/3)) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    # Update
    def run(self):
        # Terrain
        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)

        # Coins
        self.coin_sprites.update(self.world_shift)
        self.coin_sprites.draw(self.display_surface)

        # Enemies & Constraints
        self.enemy_sprites.update(self.world_shift)
        self. constraint_sprites.update(self.world_shift)
        self.enemy_collision()
        self.enemy_sprites.draw(self.display_surface)

        #Particles
        self.particle_sprite.update(self.world_shift)
        self.particle_sprite.draw(self.display_surface)

        # World
        self.camera_x()

        # Player
        self.player.update()
        self.horizontal_collision()
        self.get_player_on_ground()
        self.vertical_collision()
        self.init_landing_particles()
        self.player.draw(self.display_surface)
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)