import pygame
import pymunk
from pymunk.vec2d import Vec2d
import pymunk.pygame_util
from pygame.color import *

class Target():
    def __init__(self, space, position):
        self.start_pos = position
        self.mass = 1
        self.radius = 25
        self.moment = pymunk.moment_for_circle(self.mass, self.radius/2, self.radius)
        self.target_body = pymunk.Body(self.mass, self.moment, pymunk.Body.STATIC)
        self.target_outerCircle = pymunk.Circle(self.target_body, self.radius)
        self.target_outerCircle.group = 3
        self.target_outerCircle.color = (255,55,55)

        self.target_body.position = Vec2d(self.start_pos[0],self.start_pos[1] + self.radius)

        space.add(self.target_body, self.target_outerCircle)


class Tank():
    def __init__(self, space, position):
        self.start_pos = position
        self.wheel_offset = (20, 0)
        self.chassi_offset = (0, 13)
        self.turret_offset = (0, 32.5)
        self.cannon_offset = (15, 22)
        self.create_tank(space)
        # self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        # self.shape = pymunk.Circle(self.body, 25)
        # self.shape.sensor = True
        # self.shape.color = (255,50,50)
        # self.body.position = 100,HEIGHT/5 + 28
        # space.add(self.shape)

        #self.arrow_body, self.arrow_shape = self.create_arrow()
        #space.add(self.arrow_shape)

    def create_tank(self, space):
        self.mass = 100
        self.wheel_radius = 10
        self.cannon_radius = 15
        self.moment = pymunk.moment_for_circle(self.mass, self.wheel_radius/2, self.wheel_radius)
        self.create_wheels(space)
        self.create_chassis(space)
        self.create_cannon(space)
        self.set_positions()
        self.create_joints(space)
        self.create_motors(space)

    def create_motors(self, space):
        self.speed = 0
        self.motors = [
            pymunk.SimpleMotor(self.wheel1_body, self.chassi_body, self.speed),
            pymunk.SimpleMotor(self.wheel2_body, self.chassi_body, self.speed)
        ]
        space.add(self.motors[0], self.motors[1])

    def create_wheels(self, space):
        self.wheel1_body = pymunk.Body(self.mass, self.moment)
        self.wheel1_object = pymunk.Circle(self.wheel1_body, self.wheel_radius)
        self.wheel1_object.friction = 1.5
        self.wheel1_object.filter = pymunk.ShapeFilter(categories=1, mask=2)
        space.add(self.wheel1_body, self.wheel1_object)
        self.wheel2_body = pymunk.Body(self.mass, self.moment)
        self.wheel2_object = pymunk.Circle(self.wheel2_body, self.wheel_radius)
        self.wheel2_object.friction = 1.5
        self.wheel2_object.filter = pymunk.ShapeFilter(categories=1, mask=2)
        space.add(self.wheel2_body, self.wheel2_object)

    def create_cannon(self, space):
        self.cannon_size = (30,10)
        self.cannon_moment = pymunk.moment_for_circle(self.mass, self.cannon_radius/2,self.cannon_radius)
        self.cannon_body = pymunk.Body(self.mass, self.cannon_moment)
        self.turret_body = pymunk.Body(self.mass, self.cannon_moment)
        self.turret = pymunk.Circle(self.turret_body, self.cannon_radius)
        self.cannon_obj = pymunk.Poly.create_box(self.cannon_body, self.cannon_size)
        self.turret.filter = pymunk.ShapeFilter(categories=1, mask=2)
        self.cannon_obj.filter = pymunk.ShapeFilter(categories=1, mask=2)
        space.add(self.cannon_body, self.turret_body, self.turret, self.cannon_obj)
        #space.add(self.turret_body, self.turret)

    def create_chassis(self, space):
        self.size = (50,20)
        self.moment_body = pymunk.moment_for_box(self.mass, self.size)
        self.chassi_body = pymunk.Body(self.mass, self.moment_body)
        self.chassi_obj = pymunk.Poly.create_box(self.chassi_body, self.size)
        self.chassi_obj.filter = pymunk.ShapeFilter(categories=1, mask=2)
        space.add(self.chassi_body, self.chassi_obj)

    def set_positions(self):
        self.wheel1_body.position = self.start_pos - self.wheel_offset
        self.wheel2_body.position = self.start_pos + self.wheel_offset
        self.chassi_body.position = self.start_pos + self.chassi_offset
        self.turret_body.position = self.start_pos + self.turret_offset
        self.cannon_body.position = self.get_cannon_body_position()


    def get_cannon_body_position(self):
        return self.turret_body.position + Vec2d((self.cannon_size[0]/2,0)).rotated(self.turret_body.angle)

    def create_joints(self, space):
        self.joints = [
            pymunk.PinJoint(self.wheel1_body, self.chassi_body, (0, 0), (-15,-5)),
            pymunk.PinJoint(self.wheel1_body, self.chassi_body, (0, 0), (0, -5)),
            pymunk.PinJoint(self.wheel2_body, self.chassi_body, (0, 0), (0, -5)),
            pymunk.PinJoint(self.wheel2_body, self.chassi_body, (0, 0), (15, -5)),
            pymunk.PivotJoint(self.chassi_body, self.turret_body, (0,10),(0,0))]
        for joint in self.joints:
            joint.collide_bodies=False
            space.add(joint)

    def get_arrow_angle(self):
        return self.turret_body.angle

    def fire_arrow(self, space, flying_arrows, impulse):
        self.arrow_body, self.arrow_shape = self.create_arrow()
        space.add(self.arrow_shape)
        self.arrow_body.apply_impulse_at_world_point(impulse, self.arrow_body.position)

        space.add(self.arrow_body)

        return self.arrow_body

    def update_angle(self, space, mouse_pos):
        # Update cannon angle
        self.turret_body.angle = (mouse_pos - self.turret_body.position).angle
        self.cannon_body.position = self.get_cannon_body_position()
        self.cannon_body.angle = self.turret_body.angle
        space.reindex_shapes_for_body(self.cannon_body)
        # self.body.angle = (mouse_pos - self.body.position).angle
        # self.arrow_body.position = self.body.position + Vec2d(self.shape.radius + 40, 0).rotated(self.body.angle)
        # self.arrow_body.angle = self.body.angle

    def create_arrow(self):
        vs = [(-10, 0), (0, 3), (10, 0), (0, -3)]
        mass = 1
        moment = pymunk.moment_for_poly(mass, vs)
        arrow_body = pymunk.Body(mass, moment)

        arrow_shape = pymunk.Poly(arrow_body, vs)
        arrow_shape.friction = .5
        arrow_shape.collision_type = 1
        arrow_shape.filter = pymunk.ShapeFilter(categories = 3, mask = 2)
        arrow_body.position = self.get_cannon_body_position() + (10,10)
        arrow_body.angle = self.get_arrow_angle()
        return arrow_body, arrow_shape

class Level():
    def __init__(self, WIDTH, HEIGHT, space, display, tank_pos, target_pos):
        self.w = WIDTH
        self.h = HEIGHT
        self.create_border_walls(WIDTH, HEIGHT, space)
        self.setup_space(space, display)
        self.create_level(WIDTH, HEIGHT, space, display)
        self.tank = Tank(space, tank_pos)
        self.target = Target(space, target_pos)

    def create_border_walls(self, WIDTH, HEIGHT, space):
        self.bottom = HEIGHT/10
        self.walls = [pymunk.Segment(space.static_body, (0, self.bottom), (0, HEIGHT), 5)
        , pymunk.Segment(space.static_body, (0, HEIGHT), (WIDTH, HEIGHT), 5)#Top
        , pymunk.Segment(space.static_body, (WIDTH, HEIGHT), (WIDTH, self.bottom), 5)
        , pymunk.Segment(space.static_body, (0, self.bottom), (WIDTH, self.bottom), self.bottom)]#Bot
        for wall in self.walls:
            wall.friction = 1.
            wall.group = 2
        self.walls[3].group = 1
        self.walls[3].friction = 1.
        space.add(self.walls)

    def setup_space(self, space, display):
        display.fill((135,206,250))
        space.gravity = (0.0,-900.0)

    def moveTank(self, speed):
        for motor in self.tank.motors:
            motor.rate = speed

    def create_level(self, WIDTH, HEIGHT, space, display):
        raise NotImplementedError

    def update_level(self, space, mouse_pos):
        self.tank.update_angle(space, mouse_pos)

    def write_to_screen(self, screen):
        raise NotImplementedError

class Level1(Level):
    def create_level(self, WIDTH, HEIGHT, space, display):
        pass
    def write_to_screen(self, screen):
        tar_pos = self.target.target_body.position
        tank_pos = self.tank.chassi_body.position
        screen.blit(pygame.font.SysFont("Arial", 22).render("LEFT and RIGHT arrow keys to move!", 1, THECOLORS["black"]), (tank_pos[0]-85,self.h - tank_pos[1]+60))
        screen.blit(pygame.font.SysFont("Arial", 22).render("^HIT THIS^", 1, THECOLORS["black"]), (tar_pos[0]-42,self.h - tar_pos[1]+self.target.radius))
        screen.blit(pygame.font.SysFont("Arial", 22).render("Aim with mouse, hold LMB to powerup, release to fire", 1, THECOLORS["black"]),
                    (10, 250))

class Level2(Level):
    def create_level(self, WIDTH, HEIGHT, space, display):
        self.wall_body = pymunk.Body(1000, 5, pymunk.Body.STATIC)
        self.wall = pymunk.Poly.create_box(self.wall_body, (150, 4*HEIGHT/8))
        self.wall_body.position = (WIDTH/2, 350)
        #wall = pymunk.Segment(space.static_body, (WIDTH/2, 5*HEIGHT/8), (WIDTH/2, 0), 150)
        self.wall.group = 1
        self.wall.friction = 1.
        space.add(self.wall_body, self.wall)
    def write_to_screen(self, screen):
        pass

class Level3(Level):
    def create_level(self, WIDTH, HEIGHT, space, display):
        pass
    def write_to_screen(self, screen):
        pass