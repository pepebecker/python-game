import pygame, math
class Vector(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def equal_to(self, vector):
		if self.x == vector.x and self.y == vector.y:
			return True
		return False

def get_distance(vec1, vec2):
	return math.sqrt(math.pow(vec2.x-vec1.x, 2) + math.pow(vec2.y-vec1.y, 2))

def text_to_screen(screen, text, x, y, size = 15, color = [255, 255, 255], font_type = 'arialblack'):
	try:
		text = str(text)
		font = pygame.font.SysFont(font_type, size)
		text = font.render(text, True, color)
		screen.blit(text, (x, y))
	except (Exception, e):
		print ('Font Error, saw it coming')
		raise e