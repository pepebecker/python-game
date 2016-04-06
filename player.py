import pygame, spritesheet
from geometry import *
from tile import *

class Player(object):
	def __init__(self, x, y, size, ssheet_path):
		self.pos = Vector(x, y)
		self.destpos = Vector(x, y)
		self.velocity = Vector(0, 0)
		self.speed = 5
		self.size = size
		self.ssheet = spritesheet.spritesheet(ssheet_path)
		self.set_direction('down')
		self.health = 100
		self.items = []
		self.idle = True

	def get_tile_number(self):
		x = self.pos.x
		y = self.pos.y
		number = ((x / self.size) + Tile.H) + ((y / self.size) * Tile.V)
		return number + Tile.V

	def get_tile(self):
		return Tile.get_tile(self.get_tile_number())

	def spritesheet_size(self):
		rect = self.ssheet.sheet.get_rect()
		size = Vector(rect.width, rect.height)
		return size

	def draw(self, surface):
		surface.blit(self.image, [self.pos.x, self.pos.y])

	def get_sprite(self, frame, direction):
		row = 0
		if direction == 'down':
			row = 0
		if direction == 'left':
			row = 1
		if direction == 'right':
			row = 2
		if direction == 'up':
			row = 3

		sprite_size = self.spritesheet_size().x/4
		image = self.ssheet.image_at((frame*sprite_size, row*sprite_size, sprite_size, sprite_size), [255,0,255])
		image = pygame.transform.scale(image, [self.size, self.size])
		return image

	def set_direction(self, direction):
		self.image = self.get_sprite(0, direction)
		self.direction = direction

	def walk(self, direction):
		if self.idle:
			self.set_direction(direction)

			if direction == 'down':
				self.destpos.y = self.pos.y + self.size
				self.velocity.y = self.speed
			if direction == 'left':
				self.destpos.x = self.pos.x - self.size
				self.velocity.x = -self.speed
			if direction == 'right':
				self.destpos.x = self.pos.x + self.size
				self.velocity.x = self.speed
			if direction == 'up':
				self.destpos.y = self.pos.y - self.size
				self.velocity.y = -self.speed

			self.idle = False

	def update(self):
		if self.idle == False:
			if self.pos.equal_to(self.destpos):
				self.idle = True
				self.velocity.x = 0
				self.velocity.y = 0
			else:
				self.pos.x += self.velocity.x
				self.pos.y += self.velocity.y

				if get_distance(self.pos, self.destpos) <= self.size*.25:
					self.image = self.get_sprite(0, self.direction)
				elif get_distance(self.pos, self.destpos) <= self.size*.5:
					self.image = self.get_sprite(1, self.direction)
				elif get_distance(self.pos, self.destpos) <= self.size*.75:
					self.image = self.get_sprite(2, self.direction)
				else:
					self.image = self.get_sprite(3, self.direction)

