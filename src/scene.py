from pygame import Color, Rect, Surface
from src.shape import Shape
from pygame.draw import polygon
from pygame.mouse import get_rel
from math import sqrt

class Scene():
    def __init__(self):
        self.shape_count = 800
        self.shapes = []

    def start(self):
        for i in range(0, self.shape_count):
            self.shapes.append(Shape.get_shape())
            self.shapes[i].start()
        
        return True

    def update(self, delta):
        mouse_mov = get_rel() # (x, y)

        scroll_dir = 0
        if mouse_mov[0] < 0:
            scroll_dir = -1
        else:
            scroll_dir = 1
        
        rot_speed = sqrt(mouse_mov[0]**2 + mouse_mov[1]**2) * scroll_dir
        
        for shape in self.shapes:
            shape.rotate(rot_speed)

    def render(self, target):
        target.fill((255,255,255))
        for shape in self.shapes:
            polygon(target, shape.colour, shape.vertex_positions)
        
