import pygame
from Src.Settings import vertical_tile_number, tile_size, screen_width
from Src.Tiles import AnimatedTile, StaticTile
from Src.Assets import import_folder
from random import choice, randint

# Init Sky Image
class Sky:
	def __init__(self,horizon,style = 'level'):
		self.top = pygame.image.load('Assets/Decorations/sky/sky_top.png').convert()
		self.bottom = pygame.image.load('Assets/Decorations/sky/sky_bottom.png').convert()
		self.middle = pygame.image.load('Assets/Decorations/sky/sky_middle.png').convert()
		self.horizon = horizon

		# Stretch To Screen
		self.top = pygame.transform.scale(self.top,(screen_width,tile_size))
		self.bottom = pygame.transform.scale(self.bottom,(screen_width,tile_size))
		self.middle = pygame.transform.scale(self.middle,(screen_width,tile_size))

		self.style = style
		if self.style == 'overworld':
			cloud_surfaces = import_folder('Assets/Decorations/clouds')
			self.clouds = []

			for surface in [choice(cloud_surfaces) for image in range(10)]:
				x = randint(0,screen_width)
				y = randint(0,(self.horizon * tile_size) - 100)
				rect = surface.get_rect(midbottom = (x,y))
				self.clouds.append((surface,rect))

	def draw(self,surface):
		for row in range(vertical_tile_number):
			y = row * tile_size
			if row < self.horizon:
				surface.blit(self.top,(0,y))
			elif row == self.horizon:
				surface.blit(self.middle,(0,y))
			else:
				surface.blit(self.bottom,(0,y))

		if self.style == 'overworld':
			for cloud in self.clouds:
				surface.blit(cloud[0],cloud[1])

# Init Background Clouds
class Clouds:
	def __init__(self,horizon,level_width,cloud_number):
		cloud_surf_list = import_folder('Assets/Decorations/clouds')
		min_x = -screen_width
		max_x = level_width + screen_width
		min_y = 0
		max_y = horizon
		self.cloud_sprites = pygame.sprite.Group()

		for cloud in range(cloud_number):
			cloud = choice(cloud_surf_list)
			x = randint(min_x,max_x)
			y = randint(min_y,max_y)
			sprite = StaticTile(0,x,y,cloud)
			self.cloud_sprites.add(sprite)

	def draw(self,surface,shift):
		self.cloud_sprites.update(shift/3)
		self.cloud_sprites.draw(surface)
  
# Init Water Boundary
class Water:
	def __init__(self,top,level_width):
		water_start = -screen_width
		water_tile_width = 192
		tile_x_amount = int((level_width + screen_width * 2) / water_tile_width)
		self.water_sprites = pygame.sprite.Group()

		for tile in range(tile_x_amount):
			x = tile * water_tile_width + water_start
			y = top
			sprite = AnimatedTile(192,x,y,'Assets/Decorations/water')
			self.water_sprites.add(sprite)

	def draw(self,surface,shift):
		self.water_sprites.update(shift)
		self.water_sprites.draw(surface)