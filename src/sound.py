import pygame


class Sound:
	def __init__(self,game):
		self.game = game 
		pygame.mixer.init()
		self.path = '../assets/sound/'
		self.shotgun = pygame.mixer.Sound(self.path + 'shotgun.wav')