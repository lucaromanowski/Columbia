'''
Event handling stuff
'''

import pygame as pg

from settings import *

def checkEvents(program):
	'''
	Checking for events
	'''

	for event in pg.event.get():
			if event.type == pg.QUIT:
				program.running= False
			# Keyboard input
			if event.type == pg.KEYDOWN:
				
				# Changing levels (probably temporary solution only for test purposes)
				if event.key == pg.K_d:
					# Change level (by index number)
					try:					
						if program.levelNumber < len(program.all_levels) - 1:
							program.levelNumber += 1
							program.current_level = program.all_levels[program.levelNumber]
							print("level changed")
					except IndexError:
						print('Index error')
						pass
				if event.key == pg.K_a:
					# Change level (by index number)
					try:
						if program.levelNumber > 0:
							program.levelNumber -= 1
							program.current_level = program.all_levels[program.levelNumber]
							print("level changed")
					except IndexError:
						print('Index error')
						pass