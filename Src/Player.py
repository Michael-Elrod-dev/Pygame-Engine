import pygame
from Src.Assets import *
from math import sin

class Player(pygame.sprite.Sprite):
    # Initialize Player Character
    def __init__(self, pos, surface, init_jump_particles, change_health):
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
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
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
        
        # Health
        self.change_health = change_health
        self.invincible = False
        self.invincibility_duration = 500
        self.hurt_time = 0
    
    # Animate Player Movement
    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image
        if self.invincible:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

        # Set Rect Position
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)

    # Loop Run Particles
    def particle_run_animation(self):
        if self.status == 'run' and self.on_ground:
            self.particle_frame_index += self.particle_animation_speed
            if self.particle_frame_index >= len(self.run_particles):
                self.particle_frame_index = 0

            # Switches Particle Pos To Player Direction
            particles = self.run_particles[int(self.particle_frame_index)]
            if self.facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(-5, 10)
                self.display_surface.blit(particles, pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(15, 10)
                flipped_particle = pygame.transform.flip(particles,True,False)
                self.display_surface.blit(flipped_particle, pos)
    
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
  
    # Register Player Damage
    def get_damage(self):
        if not self.invincible:
            self.change_health(-10)
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()

    # Invulnerable Frames
    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.invincible = False

    # Big Math
    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0: return 255
        else: return 0
  
    # Update
    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
        self.particle_run_animation()
        self.invincibility_timer()
        self.wave_value()