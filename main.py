import sys, pygame
from input_manager import manage_input
from player import Player
from tile import *


pygame.init()

WIDTH, HEIGHT = 800, 500
tile_size = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pepe's Python Game")

clock = pygame.time.Clock()
FPS = 30
total_frames = 0

player = Player(tile_size, tile_size,  tile_size, 'images/player-spritesheet.png')

Tile.generate_world(tile_size, WIDTH, HEIGHT, {'image': pygame.image.load('images/stone.png')})
Tile.generate_terrain([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
						32,48,64,65,70,81,86,97,113,128,129,144,145,150,160],
						{'is_wall': True, 'image': pygame.image.load('images/wood_birch.png')})
Tile.generate_terrain([17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,66,69,73,74,75,76,77,78,79,80,102,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176], {'is_wall': True, 'image': pygame.image.load('images/wood.png')})

Tile.generate_terrain([49,50,53,54,57,58,59,60,61,62,63,112,134,146,147,148,149,151,152,153,154,155,156,157,158,159], {'layer': 1, 'image': pygame.image.load('images/wood_birch.png')})

while 1: # Game Loop

	# Logic
	manage_input(player)
	player.update()

	# Draw
	screen.fill([0,0,0])

	Tile.draw_all(screen, 0)
	Tile.draw_shadow(screen)
	player.draw(screen)
	Tile.draw_all(screen, 1)

	pygame.display.flip()

	# FPS
	total_frames += 1
	clock.tick(FPS)
