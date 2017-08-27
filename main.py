import pygame as pg 

from eventUtils import *
from gameobjects import *
from levels import *
from settings import *


class MainGame:

	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		self.clock = pg.time.Clock()

		self.current_level = None
		self.all_levels = []
		self.levelNumber = 0


	def new(self):
		
		# Creating levels
		for level in LEVEL_LIST:
			l = levelsCreator(self, level)
			# Creating items for levels
			#Menu items
			if level == "menu":
				b = Button(self)
				l.all_level_objects.add(b)
				print('button created')

			# Base items
			if level == "baza":
				b = Bank(self)
				l.all_level_objects.add(b)
				print('bank created')

			# Base items
			if level == "pole_bitwy":
				e = Enemy(self)
				l.all_level_objects.add(e)
				print('enemy created')

			self.all_levels.append(l)

		print("All levels:" ,str(self.all_levels))

		# Setting up current level 
		self.current_level = self.all_levels[self.levelNumber]
		print('Current level: ', str(self.current_level.name))

		



		self.run()
	

	#--------------------------------#
	#           MAIN LOOP            #
	#--------------------------------#

	def run(self):
		self.running = True
		while self.running:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()
			


	#--------------------------------#
	#            EVENTS              #
	#--------------------------------#

	def events(self):
		
		'''
		We check for any event from the user
		'''
		checkEvents(self)




	#--------------------------------#
	#            UPDATE              #
	#--------------------------------#
	def update(self):
		# Current level update
		self.current_level.all_level_objects.update()
		


	#--------------------------------#
	#            DRAW                #
	#--------------------------------#
	def draw(self):
		self.screen.fill(BLACK)


		# Current level update
		self.current_level.all_level_objects.draw(self.screen)


		# Updating the screen
		pg.display.update()


		#DEBUG INFOS
		#print("Current level: ", str(self.current_level.name))
		#print(str(self.levelNumber))
		#print(str(self.current_level.all_level_objects))
		




if __name__ == "__main__":
	mg = MainGame()
	mg.new()