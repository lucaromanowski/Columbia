import pygame as pg



class Level:

	def __init__(self,
				 program,
				 name):
		self.program = program
		self.name = name

		# Level objects
		self.all_level_objects = pg.sprite.Group()
	

def levelsCreator(program, level):
	return Level(program, level)




