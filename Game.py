import pygame, sys
from Src.UI import *
from Src.Settings import *
from Src.Level import Level
from Src.Overworld import *

#Intitialize Game State
class Game:
	def __init__(self):

		# Attributes
		self.max_level = 0
		self.max_health = 100
		self.cur_health = 100
		self.coins = 0

		# Audio
		self.bg_music = pygame.mixer.Sound('Assets/Audio/level_music.wav')
		self.bg_music.set_volume(.2)
		self.overworld_music = pygame.mixer.Sound('Assets/Audio/overworld_music.wav')
		self.overworld_music.set_volume(.2)

		# Overworld
		self.overworld = Overworld(0,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.overworld_music.play(loops = -1)

		# UI
		self.ui = UI(screen)

	# Init Game State
	def create_level(self,current_level):
		self.level = Level(current_level,screen,self.create_overworld,self.reset_coins,self.reset_health,self.change_coins,self.change_health)
		self.status = 'level'
		self.overworld_music.stop()
		self.bg_music.play(loops = -1)

	# Init Overworld Screen
	def create_overworld(self,current_level,new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.overworld_music.play(loops = -1)
		self.bg_music.stop()

	def reset_coins(self):
		self.coins = 0
  
	def reset_health(self):
		self.cur_health = 100

	def change_coins(self,amount):
		self.coins += amount

	def change_health(self,amount):
		self.cur_health += amount

	# Reset Game
	def check_game_over(self):
		if self.cur_health <= 0:
			self.cur_health = 100
			self.coins = 0
			self.max_level = 0
			self.overworld = Overworld(0,self.max_level,screen,self.create_level)
			self.status = 'overworld'
			self.overworld_music.play(loops = -1)
			self.bg_music.stop()

	# Update
	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
		else:
			self.level.run()
			self.ui.show_health(self.cur_health,self.max_health)
			self.ui.show_coins(self.coins)
			self.check_game_over()


# Initialize Pygame Setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mystic Meadows")
clock = pygame.time.Clock()
game = Game()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
            
    screen.fill((40, 40, 40))
    game.run()
    pygame.display.update()
    clock.tick(60)
