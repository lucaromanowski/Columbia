import pygame as pg 

from settings import *


# Menu items

class Button(pg.sprite.Sprite):
	def __init__(self, program):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((20, 20))
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 200
		self.rect.y = 200
		


# Base level items

class Bank(pg.sprite.Sprite):
	def __init__(self, program):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((20, 20))
		self.image.fill(BANK_COLOR)
		self.rect = self.image.get_rect()
		self.rect.x = 200
		self.rect.y = 200
		print("BANK created2")


# Battlefield level items

class Enemy(pg.sprite.Sprite):
	def __init__(self, program):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((20, 20))
		self.image.fill(ENEMY_COLOR)
		self.rect = self.image.get_rect()
		self.rect.x = 200
		self.rect.y = 200
		print("Enemy created2")

