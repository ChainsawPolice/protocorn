# -*- coding: utf-8 -*-

if __name__ == '__main__':
	print '\nYou must import protocorn as a module.\nImport it by putting protocorn.py in the same directory as your Unicorn HAT project and using:\n\n\timport protocorn as unicornhat\n\nto temporarily replace all unicornhat functions with the protocorn equivalents.\n'

else:
	import pygame
	from pygame.locals import *

	factor        = 20
	size          = 8*factor

	pygame.init()
	pygame.display.set_caption('🐴')
	DISPLAYSURF = pygame.display.set_mode(((size-2), (size-2)))
	DISPLAYSURF.fill((20,20,20))

	######## Build pixel matrix ########
	# The "LEDs" are stored in a 2D list, with each index containing a pygame.Rect() object and a colour tuple.
	# Referencing matrix[1][3] will pull up the Rect() object (at [0]) and the colours (at [1]) of the "LED" at x1 y3 in a two-item list.
	matrix = []
	for x in range(0,size, factor):
		temp_row = []
		for y in range(0,(size), factor):
			temp_row.append([pygame.Rect(x,y,factor-2,factor-2), (0,0,0)]) # All pixels start off as pure black.
		matrix.append(temp_row)

	######## unicornhat functions ########

	def set_pixel(x,y, r,g,b):
		''' Set a single pixel to RGB colour '''
		matrix[x][y][1] = (r,g,b)

	def show():
		''' Update UnicornHat with the contents of the display buffer '''
		for row in matrix:
			for neopixel in row:
				pygame.draw.rect(DISPLAYSURF, neopixel[1], neopixel[0])
		pygame.display.update()

	def clear():
		''' Clear the buffer '''
		for row in matrix:
			for neopixel in row:
				pygame.draw.rect(DISPLAYSURF, (0,0,0), neopixel[0])

	def off():
		''' Clear the buffer and immediately update UnicornHat to turn off all pixels. '''
		clear()
		show()

	def _matrix():
		''' Print out the matrix of "pixels". For my own personal testing. Not to be shipped. '''
		for row in matrix:
			print row

	######## Non-implemented functions ########

	def brightness(brightness): print "brightness(): Not implemented yet, sorry!"
	def rotation(rotation): print "rotation(): Not implemented yet, sorry!"
	def get_brightness(x): print "get_brightness(): Not implemented yet, sorry!"
	def get_index_from_xy(x): print "get_index_from_xy(): Not implemented yet, sorry!"
	def get_pixel(x): print "get_pixel(): Not implemented yet, sorry!"
	def set_pixels(x): print "set_pixels(): Not implemented yet, sorry!"
	def get_pixels(x): print "get_pixels(): Not implemented yet, sorry!"

	show()
