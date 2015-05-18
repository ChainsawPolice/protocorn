# -*- coding: utf-8 -*-

if __name__ == '__main__':
	print '\nYou must import protocorn as a module.\nImport it by putting protocorn.py in the same directory as your Unicorn HAT project and using:\n\n\timport protocorn as unicornhat\n\nto temporarily replace all unicornhat functions with the protocorn equivalents.\n'

else:
	import pygame
	from random import randint
	from pygame.locals import *

	factor = 70

	pygame.init()
	pygame.display.set_caption('🐴')
	DISPLAYSURF = pygame.display.set_mode(((8*factor-2), (8*factor-2)))
	DISPLAYSURF.fill((20,20,20))

	# Build pixel matrix
	pixel_coords = []
	for x in range(0,(8*factor), factor):
		temp_row = []
		for y in range(0,(8*factor), factor):
			temp_row.append(pygame.Rect(x,y,factor-2,factor-2))
		pixel_coords.append(temp_row)

	# Build color matrix
	pixel_colours = []
	for x in range(0,8):
		temp_row = []
		for y in range(0,8):
			temp_row.append((0,0,0))
		pixel_colours.append(temp_row)

	def set_pixel(x,y, r,g,b):
		pixel_colours[x][y] = (r,g,b)

	def show():
		for y, row in enumerate(pixel_coords):
			for x, neopixel in enumerate(row):
				pygame.draw.rect(DISPLAYSURF, (pixel_colours[x][y]), neopixel)
		pygame.display.update()

	def brightness(brightness): print "brightness: Not implemented yet, sorry!"
	def rotation(rotation): print "rotation: Not implemented yet, sorry!"
	def get_brightness(x): print "get_brightness: Not implemented yet, sorry!"
	def clear(x): print "clear: Not implemented yet, sorry!"
	def off(x): print "off: Not implemented yet, sorry!"
	def get_index_from_xy(x): print "get_index_from_xy: Not implemented yet, sorry!"
	def get_pixel(x): print "get_pixel: Not implemented yet, sorry!"
	def set_pixels(x): print "set_pixels: Not implemented yet, sorry!"
	def get_pixels(x): print "get_pixels: Not implemented yet, sorry!"

	show()
