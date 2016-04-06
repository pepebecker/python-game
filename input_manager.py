import pygame, sys
from tile import *

def manage_input(player):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			print ('Good bye')
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_b:
				Tile.debug = not Tile.debug

	keys = pygame.key.get_pressed()

	LEFT = -Tile.H
	RIGHT = Tile.H
	UP = -Tile.V
	DOWN = Tile.V

	if player.idle:
		if keys[pygame.K_DOWN]:
			player.set_direction('down')
			future_tile = Tile.get_tile(player.get_tile_number()+DOWN)
			if not future_tile.is_wall:
				player.walk('down')

		if keys[pygame.K_LEFT]:
			player.set_direction('left')
			future_tile = Tile.get_tile(player.get_tile_number()+LEFT)
			if not future_tile.is_wall:
				player.walk('left')

		if keys[pygame.K_RIGHT]:
			player.set_direction('right')
			future_tile = Tile.get_tile(player.get_tile_number()+RIGHT)
			if not future_tile.is_wall:
				player.walk('right')

		if keys[pygame.K_UP]:
			player.set_direction('up')
			future_tile = Tile.get_tile(player.get_tile_number()+UP)
			if not future_tile.is_wall:
				player.walk('up')

	if keys[pygame.K_s]:
		player.set_direction('down')
	if keys[pygame.K_a]:
		player.set_direction('left')
	if keys[pygame.K_d]:
		player.set_direction('right')
	if keys[pygame.K_w]:
		player.set_direction('up')
