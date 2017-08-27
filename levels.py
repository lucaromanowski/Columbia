import pygame as pg



class Level:
	'''
	Level represents all objects that are in each level.

	'''
	def __init__(self,
				 program,
				 name):
		self.program = program
		self.name = name

		# Level objects
		self.all_level_objects = pg.sprite.Group()
	

def levelsCreator(program, level):
	'''
	This function creates level. Takes level parameter that determins what level we want to create
	and passes it to Level class. 
	It returns level object.
	'''
	return Level(program, level)




