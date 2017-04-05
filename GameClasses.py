import pygame
import pymunk

class Level():
    def __init__(self, WIDTH, HEIGHT, space, display):
        self.create_border_walls(WIDTH, HEIGHT, space)
        self.setup_space(space, display)
        #self.create_level(WIDTH, HEIGHT, space, display)

    def create_border_walls(self, WIDTH, HEIGHT, space):
        self.bottom = HEIGHT/10
        self.walls = [pymunk.Segment(space.static_body, (0, self.bottom), (0, HEIGHT), 5)
        , pymunk.Segment(space.static_body, (0, HEIGHT), (WIDTH, HEIGHT), 5)#Top
        , pymunk.Segment(space.static_body, (WIDTH, HEIGHT), (WIDTH, self.bottom), 5)
        , pymunk.Segment(space.static_body, (0, self.bottom), (WIDTH, self.bottom), 5)]#Bot
        for wall in self.walls:
            wall.friction = 1.
            wall.group = 1
        space.add(self.walls)

    def setup_space(self, space, display):
        display.fill((255,255,255))
        space.gravity = (0.0,-900.0)


    def create_level(self, WIDTH, HEIGHT, space, display):
        raise NotImplementedError

class Level1(Level):
    def create_level(self, WIDTH, HEIGHT, space, display):
        self.tank = Tank(x = 15, y= self.bottom)
        self.target = Target(x= 300, y = 300)