from pygame import Color, Rect, Surface
from random import randint
from pygame.math import Vector2

class Shape():
    @staticmethod
    def get_shape():
        shape = None
        shape_id = randint(0,4)
        if shape_id == 0:
            shape = Rectangle()
        elif shape_id == 1:
            shape = RightTriangle()
        elif shape_id == 2:
            shape = IsoscelesTriangle()
        elif shape_id == 3:
            shape = Pentagon()
        elif shape_id == 4:
            shape = Hexagon()

        return shape
    
    def __init__(self):
        self.rect = Rect(randint(0, 800), randint(0, 450), randint(10, 80), randint(10, 80))
        self.spin_rate = (randint(1, 10) / 10) * 3
        self.colour = (randint(0,255), randint(0,255), randint(0,255))

        self.vertices = []
        self.vertex_positions = []

    def start(self):
        return True

    def update(self, delta):
        pass

    def rotate(self, rot_speed):
        for vertex in self.vertices:
            vertex.rotate_ip(self.spin_rate * rot_speed)

        self.vertex_positions = []
        for vertex in self.vertices:
            self.vertex_positions.append((vertex.x + self.rect.x, vertex.y + self.rect.y))

    def render(self, target):
        pass

class Rectangle(Shape):
    
    def start(self):
        w = self.rect.width/2
        h = self.rect.height/2
        self.vertices = [Vector2(w, h), Vector2(-w,h), Vector2(-w,-h), Vector2(w,-h)]
        
        return True

class RightTriangle(Shape):
    
    def start(self):
        w = self.rect.width/2
        h = self.rect.height/2
        self.vertices = [Vector2(w, h), Vector2(-w,h), Vector2(-w,-h)]
        
        return True

class IsoscelesTriangle(Shape):

    def start(self):
        w = self.rect.width/2
        h = self.rect.height/2
        self.vertices = [Vector2(w, h), Vector2(-w,h), Vector2(0,-h)]

        return True

class Pentagon(Shape):

    def start(self):
        w = self.rect.width/2
        vert = Vector2(w, 0)
        for i in range(5):
            self.vertices.append(vert.rotate(72*i))

        return True

class Hexagon(Shape):

    def start(self):
        w = self.rect.width/2
        vert = Vector2(w, 0);
        for i in range(6):
            self.vertices.append(vert.rotate(60*i))

        return True

class Octogon(Shape):

    def start(self):
        w = self.rect.width/2
        vert = Vector2(w, 0);
        for i in range(8):
            self.vertices.append(vert.rotate(45*i))

        return True

class Isosagon(Shape):

    def start(self):
        w = self.rect.width/2
        vert = Vector2(w, 0);
        for i in range(20):
            self.vertices.append(vert.rotate(18*i))

        return True

class Circle(Shape):

    def start(self):
        w = self.rect.width/2
        vert = Vector2(w, 0);
        for i in range(90):
            self.vertices.append(vert.rotate(4*i))

        return True
