import pygame
from Src.Tiles import *
from Src.Assets import *
from Src.Settings import *
from Src.Decoration import *
from Src.Enemy import *
from Src.Player import Player
from Src.Effects import Effects

class Level:
    # Initialize
    def __init__(self, current_level, surface, create_overworld, reset_coins, reset_health, change_coins, change_health):
        # Init Settings
        self.display_surface = surface
        self.world_shift = 0
        self.current_x = None
        
        # Init Audio
        self.coin_sound = pygame.mixer.Sound('Assets/Audio/coin.wav')
        self.coin_sound.set_volume(.2)
        self.stomp_sound = pygame.mixer.Sound('Assets/Audio/stomp.wav')
        self.stomp_sound.set_volume(.2)

        # Init Overworld
        self.create_overworld = create_overworld
        self.current_level = current_level
        self.reset_coins = reset_coins
        self.reset_health = reset_health
        level_data = levels[self.current_level]
        self.new_max_level = level_data['unlock']

        # Init Player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.effects_group = pygame.sprite.GroupSingle()
        self.player_setup(player_layout, change_health)
        
        # Init UI
        self.change_coins = change_coins

        # Particles
        self.particle_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False

        # Init Terrain
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')
        
        # Init Grass
        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprites = self.create_tile_group(grass_layout,'grass')

        # Init Coins 
        coin_layout = import_csv_layout(level_data['coins'])
        self.coin_sprites = self.create_tile_group(coin_layout,'coins')

        # Init Enemy 
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout,'enemies')

        # Init Constraint 
        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constraint_sprites = self.create_tile_group(constraint_layout,'constraint')
        
        # Init Background 
        self.sky = Sky(8)
        level_width = len(terrain_layout[0]) * tile_size
        self.water = Water(screen_height - 20,level_width)
        self.clouds = Clouds(400,level_width,30)

    # Place Player And End Goal
    def player_setup(self, layout, change_health):
        for row_index, row in enumerate(layout):
            for col_index, value in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if value == '0':
                    sprite = Player((x, y), self.display_surface, self.init_jump_particles, change_health)
                    self.player.add(sprite)
                    
                if value == '1':
                    player_surface = pygame.image.load('Assets/Overworld/goal.png').convert_alpha()
                    sprite = StaticTile(tile_size, x, y, player_surface)
                    self.goal.add(sprite)

    # Turn CSV File Into Sprite Group
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
                        
                    if type == 'grass':
                        grass_tile_list = import_cut_graphics('Assets/Decorations/grass/grass.png')
                        tile_surface = grass_tile_list[int(value)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)

                    if type == 'coins':
                        if value == '0': 
                            sprite = Coin(tile_size, x, y, 'Assets/Coins/silver', 1)
                        if value == '1': 
                            sprite = Coin(tile_size, x, y, 'Assets/Coins/gold', 3)

                    if type == 'enemies':
                        if value == '0': 
                            sprite = Enemy(tile_size, x, y, 'skeleton', 'Assets/Enemy/skeleton/run', 'Assets/Enemy/skeleton/die')
                        if value == '1':
                            sprite = Enemy(tile_size, x, y, 'wisp', 'Assets/Enemy/wisp/run', 'Assets/Enemy/wisp/die')
                        if value == '2': 
                            sprite = Enemy(tile_size, x, y, 'tauro', 'Assets/Enemy/tauro/run', 'Assets/Enemy/tauro/die')

                    if type == 'constraint':
                        sprite = Tile(tile_size,x,y)

                    sprite_group.add(sprite)
            
        return sprite_group

    # Check Enemy Collision With Map Constraints
    def enemy_collision(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraint_sprites, False):
                enemy.reverse()

    # Create Jump Particles (Player)
    def init_jump_particles(self, pos):
        jump_particle = Effects(pos, 'jump', 'Assets/Character/particles/jump')
        self.particle_sprite.add(jump_particle)

    # Checks If Player Lost/Regains Ground Contact
    def init_landing_particles(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.particle_sprite.sprites():
            offset = pygame.math.Vector2(0,20)
            landing_particle = Effects(self.player.sprite.rect.midbottom - offset, 'land', 'Assets/Character/particles/land')
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
        player.collision_rect.x += player.direction.x * player.speed
        collidable_sprites = self.terrain_sprites.sprites()

        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.collision_rect):
                if player.direction.x < 0: 
                    player.collision_rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.collision_rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
          
    # Y Axis Colission Checking          
    def vertical_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        collidable_sprites = self.terrain_sprites.sprites()

        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.collision_rect):
                if player.direction.y > 0: 
                    player.collision_rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                    player.jump_cooldown = 0
                elif player.direction.y < 0:
                    player.collision_rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        # Reset Ground/Ceiling Checks
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False

    # X Axis Camera Scroll                
    def camera_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        # Control Camera Relative To Player Pos
        if player_x < (screen_width/2) and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > (screen_width - (screen_width/2)) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    # Check Player Fall
    def check_death(self):
            if self.player.sprite.rect.top > screen_height:
                self.reset_coins()
                self.reset_health()
                self.create_overworld(self.current_level,0)

    # Check Goal Reached
    def check_win(self):
        if pygame.sprite.spritecollide(self.player.sprite,self.goal,False):
            self.create_overworld(self.current_level,self.new_max_level)

    # Pick Up Coins
    def check_coin_collisions(self):
        collided_coins = pygame.sprite.spritecollide(self.player.sprite,self.coin_sprites,True)
        if collided_coins:
            for coin in collided_coins:
                self.coin_sound.play()
                self.change_coins(coin.value)

    # Check Enemy vs Player Collision
    def check_enemy_collisions(self):
        enemy_collisions = pygame.sprite.spritecollide(self.player.sprite,self.enemy_sprites,False)
        
        if enemy_collisions:
            for enemy in enemy_collisions:
                enemy_center = enemy.rect.centery
                enemy_top = enemy.rect.top
                player_bottom = self.player.sprite.rect.bottom
                if enemy_top < player_bottom < enemy_center and self.player.sprite.direction.y >= 0:
                    self.stomp_sound.play()
                    self.player.sprite.direction.y = -15
                    death_effect = enemy.death(self.effects_group)
                    enemy.kill()
                else:
                    self.player.sprite.get_damage()

    # Update
    def run(self):
        # Background 
        self.sky.draw(self.display_surface)
        self.clouds.draw(self.display_surface,self.world_shift)
        
        #Particles
        self.particle_sprite.update(self.world_shift)
        self.particle_sprite.draw(self.display_surface)
        
        # Terrain
        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)

        # Coins
        self.coin_sprites.update(self.world_shift)
        self.coin_sprites.draw(self.display_surface)

        # Enemies & Constraints
        self.enemy_sprites.update(self.world_shift)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_collision()
        self.enemy_sprites.draw(self.display_surface)
        self.effects_group.update(self.world_shift)
        self.effects_group.draw(self.display_surface)

        # Player
        self.player.update()
        self.horizontal_collision()
        self.get_player_on_ground()
        self.vertical_collision()
        self.init_landing_particles()
        self.camera_x()
        self.player.draw(self.display_surface)
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)
        self.check_death()
        self.check_win()
        self.check_coin_collisions()
        self.check_enemy_collisions()
        
        # Grass
        self.grass_sprites.update(self.world_shift)
        self.grass_sprites.draw(self.display_surface)
        
        # Water 
        self.water.draw(self.display_surface,self.world_shift)