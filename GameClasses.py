import pygame
import pymunk

class Level():
    def __init__(self, WIDTH, HEIGHT, space, display):
        self.create_border_walls(WIDTH, HEIGHT, space)
        self.setup_space(space, display)
        #self.create_level(WIDTH, HEIGHT, space)

    def create_border_walls(self, WIDTH, HEIGHT, space):
        self.walls = [pymunk.Segment(space.static_body, (0, 0), (0, WIDTH), 5)
        , pymunk.Segment(space.static_body, (0, WIDTH), (HEIGHT, WIDTH), 5)
        , pymunk.Segment(space.static_body, (HEIGHT, WIDTH), (HEIGHT, 0), 5)
        , pymunk.Segment(space.static_body, (0, 0), (HEIGHT, 0), 5)]
        for wall in self.walls:
            wall.friciton = 1.
            wall.group = 1
        space.add(self.walls)

    def setup_space(self, space, display):
        display.fill((255,255,255))
        space.gravity = (0.0,-900.0)


    def create_level(self, WIDTH, HEIGHT):
        raise NotImplementedError