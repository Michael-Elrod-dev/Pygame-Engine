import pygame
from Src.Assets import *
from Src.Animation import *

class Player(pygame.sprite.Sprite):
    # Initialize Player Character
    def __init__(self, pos, surface, init_jump_particles):
        super().__init__()
        import_assets(self)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        
        # Particles
        import_particles(self)
        self.particle_frame_index = 0
        self.particle_animation_speed = 0.15
        self.display_surface = surface
        self.init_jump_particles = init_jump_particles

        # Movement
        self.speed = 8
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.8
        self.jump_speed = -16
        self.jump_cooldown = 0

        # Status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    
    # Get User Input
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]: # Left
            self.direction.x = -1
            self.facing_right = False
        elif keys[pygame.K_RIGHT]: # Right
            self.direction.x = 1
            self.facing_right = True
        else:
            self.direction.x = 0 # Idle
                                 
        if keys[pygame.K_SPACE] and self.direction.y > 0 and self.jump_cooldown < 1:# Jump 
            self.jump()
            self.init_jump_particles(self.rect.midbottom)
       
            
    # Get Player Character Status
    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        elif self.direction.x != 0:
            self.status = 'run'
        else:
            self.status = 'idle'


    # Apply Gravity To Character
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
       
    
    # Initiate Jump Velocity
    def jump(self):
        self.jump_cooldown += 1
        self.direction.y = self.jump_speed

    
    # Update Functions 
    def update(self):
        self.get_input()
        self.get_status()
        Animation.animate(self)
        Animation.particle_run_animation(self)