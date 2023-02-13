import pygame


class Animation(pygame.sprite.Sprite):
    # Loop Rendered Image For Animation
    def animate(self):
        animation = self.animations[self.status]

        # Loop
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image

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

            particles = self.run_particles[int(self.particle_frame_index)]
            if self.facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(-5, 10)
                self.display_surface.blit(particles, pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(15, 10)
                flipped_particle = pygame.transform.flip(particles,True,False)
                self.display_surface.blit(flipped_particle, pos)