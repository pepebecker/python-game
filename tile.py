import pygame
from geometry import *

class Tile(object):
	List = []
	World = []
	H, V = 1, 16
	debug = False
	def __init__(self, x, y, size, props = {}):
		self.pos = Vector(x, y)
		self.size = size
		self.color = [0,0,0]
		self.layer = 0
		self.outline = 0
		self.is_wall = False
		self.offset = size*.4
		self.image = None
		self.id = len(Tile.List)+1
		Tile.List.append(self)

	def draw(self, surface):
		if self.image:
			surface.blit(self.image, [self.pos.x, self.pos.y+self.offset])
		else:
			pygame.draw.rect(surface, self.color, [self.pos.x, self.pos.y+self.offset, self.size, self.size], self.outline)

	@staticmethod
	def draw_all(surface, layer):
		for tile in Tile.List:
			if tile.layer == layer:
				tile.draw(surface)

			if Tile.debug:
				text_to_screen(surface, tile.id, tile.pos.x, tile.pos.y+tile.offset)
				text_to_screen(surface, tile.layer, tile.pos.x+20, tile.pos.y+15+tile.offset)
				if tile.is_wall:
					text_to_screen(surface, 'X', tile.pos.x, tile.pos.y+15+tile.offset)
				else:
					text_to_screen(surface, 'O', tile.pos.x, tile.pos.y+15+tile.offset)

	@staticmethod
	def draw_shadow(surface):
		for tile in Tile.List:
			if not tile.is_wall and tile.layer == 0:
				if Tile.get_tile(tile.id-Tile.V).is_wall and Tile.get_tile(tile.id+Tile.H).is_wall:
					s = pygame.Surface((50,12))
					s.set_alpha(128)
					s.fill((0,0,0))
					surface.blit(s, (tile.pos.x, tile.pos.y+tile.offset))
					s = pygame.Surface((12,38))
					s.set_alpha(128)
					s.fill((0,0,0))
					surface.blit(s, (tile.pos.x+38, tile.pos.y+tile.offset+12))

				elif Tile.get_tile(tile.id-Tile.V).is_wall:
					s = pygame.Surface((50,12))
					s.set_alpha(128)
					s.fill((0,0,0))
					surface.blit(s, (tile.pos.x, tile.pos.y+tile.offset))

				elif Tile.get_tile(tile.id+Tile.H).is_wall:
					s = pygame.Surface((12,50))
					s.set_alpha(128)
					s.fill((0,0,0))
					surface.blit(s, (tile.pos.x+38, tile.pos.y+tile.offset)) 

				elif Tile.get_tile(tile.id+Tile.H-Tile.V).is_wall:
					s = pygame.Surface((12,12))
					s.set_alpha(128)
					s.fill((0,0,0))
					surface.blit(s, (tile.pos.x+38, tile.pos.y+tile.offset)) 
			

	@staticmethod
	def get_tile(number):
		for tile in Tile.List:
			if tile.id == number:
				return tile

	@staticmethod
	def generate_world(size, boundx, boundy, props = {}):
		for y in range(-size, boundy, size):
			for x in range(0, boundx, size):
				tile = Tile(x, y, size, props)
				for prop in props:
					setattr(tile, prop, props[prop])

	@staticmethod
	def generate_terrain(positions, props = {}):
		for pos in positions:
			for tile in Tile.List:
				if pos == tile.id:
					for prop in props:
						setattr(tile, prop, props[prop])
					break