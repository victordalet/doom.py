import pygame
import sys
from settings import *
from map import * 
from player import * 
from raycasting import *
from object_rendered import *
from sprite_object import * 
from object_handler import * 

class Game:
	def __init__(self):
		pygame.init()
		pygame.mouse.set_visible(False)
		self.screen = pygame.display.set_mode(RES)
		self.clock = pygame.time.Clock()
		self.delta_time = 1
		self.new_game()

	def new_game(self):
		self.map = Map(self)
		self.player = Player(self)
		self.object_rendered = ObjectRendered(self)
		self.raycasting = Raycasting(self)
		self.object_handler = ObjectHandler(self)

	def update(self):
		self.player.update()
		self.raycasting.update()
		self.object_handler.update()
		pygame.display.flip()
		self.delta_time =  self.clock.tick(FPS)
		pygame.display.set_caption(f'{self.clock.get_fps() : .1f}')

	def draw(self):
		#self.screen.fill('black')
		self.object_rendered.draw()
		#self.map.draw()
		#self.player.draw()

	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit()

	def run(self):
		while 42:
			self.check_event()
			self.update()
			self.draw()


def main():
	game = Game()
	game.run()

main()
