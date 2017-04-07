import pygame
import pymunk
from pymunk.vec2d import Vec2d
import pymunk.pygame_util

class Tank():
    def __init__(self, space, HEIGHT):
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.shape = pymunk.Circle(self.body, 25)
        self.shape.sensor = True
        self.shape.color = (255,50,50)
        self.body.position = 100,HEIGHT/5 + 28
        space.add(self.shape)

        self.arrow_body, self.arrow_shape = self.create_arrow()
        space.add(self.arrow_shape)

    def get_arrow_angle(self):
        return self.arrow_body.angle

    def fire_arrow(self, space, flying_arrows, impulse):
        self.arrow_body.apply_impulse_at_world_point(impulse, self.arrow_body.position)

        space.add(self.arrow_body)

        temp_body = self.arrow_body

        self.arrow_body, self.arrow_shape = self.create_arrow()
        space.add(self.arrow_shape)
        return temp_body

    def update_angle(self, mouse_pos):
        self.body.angle = (mouse_pos - self.body.position).angle
        self.arrow_body.position = self.body.position + Vec2d(self.shape.radius + 40, 0).rotated(self.body.angle)
        self.arrow_body.angle = self.body.angle

    def create_arrow(self):
        vs = [(-30, 0), (0, 3), (10, 0), (0, -3)]
        mass = 1
        moment = pymunk.moment_for_poly(mass, vs)
        arrow_body = pymunk.Body(mass, moment)

        arrow_shape = pymunk.Poly(arrow_body, vs)
        arrow_shape.friction = .5
        arrow_shape.collision_type = 1
        return arrow_body, arrow_shape

class Level():
    def __init__(self, WIDTH, HEIGHT, space, display):
        self.create_border_walls(WIDTH, HEIGHT, space)
        self.setup_space(space, display)
        self.create_level(WIDTH, HEIGHT, space, display)
        self.tank = Tank(space, HEIGHT)

    def create_border_walls(self, WIDTH, HEIGHT, space):
        self.bottom = HEIGHT/10
        self.walls = [pymunk.Segment(space.static_body, (0, self.bottom), (0, HEIGHT), 5)
        , pymunk.Segment(space.static_body, (0, HEIGHT), (WIDTH, HEIGHT), 5)#Top
        , pymunk.Segment(space.static_body, (WIDTH, HEIGHT), (WIDTH, self.bottom), 5)
        , pymunk.Segment(space.static_body, (0, self.bottom), (WIDTH, self.bottom), self.bottom)]#Bot
        for wall in self.walls:
            wall.friction = 1.
            wall.group = 1
        space.add(self.walls)

    def setup_space(self, space, display):
        display.fill((255,255,255))
        space.gravity = (0.0,-900.0)

    def moveTank(self, speed):
        self.tank.body.position += speed

    def create_level(self, WIDTH, HEIGHT, space, display):
        raise NotImplementedError

class Level1(Level):
    def create_level(self, WIDTH, HEIGHT, space, display):
        print()
        #self.target = Target(x= 300, y = 300)

    def update_level(self, mouse_pos):
        self.tank.update_angle(mouse_pos)