import pygame
from Src.Tiles import Tile
from Src.Settings import tile_size, screen_width
from Src.Player import Player
from Src.Effects import Effects


class Level:
    # Level Setup
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0        

        # Particles
        self.particle_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False


    def init_jump_particles(self, pos):
        jump_particle = Effects(pos, 'jump')
        self.particle_sprite.add(jump_particle)


    # Checks If Player Lost/Regain Ground Contact
    def init_landing_particles(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.particle_sprite.sprites():
            offset = pygame.math.Vector2(0,20)
            landing_particle = Effects(self.player.sprite.rect.midbottom - offset, 'land')
            self.particle_sprite.add(landing_particle)

    
    # Place Map Tiles
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        # Enumerate method gets the position & the information
        for row_index,row in enumerate(layout):
            for col_index,col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                
                if col == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if col == 'P':
                    player_sprite = Player((x, y), self.display_surface, self.init_jump_particles)
                    self.player.add(player_sprite)
    
    
    # To Animate Landing Particle
    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False


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


    # X Axis Colission Checking
    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
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
        
        for sprite in self.tiles.sprites():
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
        

    # Update & Render
    def run(self):
        #Particles
        self.particle_sprite.update(self.world_shift)
        self.particle_sprite.draw(self.display_surface)

        # Map Tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.camera_x()

        # Player
        self.player.update()
        self.horizontal_collision()
        self.get_player_on_ground()
        self.vertical_collision()
        self.init_landing_particles()
        self.player.draw(self.display_surface)