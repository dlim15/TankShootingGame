#!/usr/bin/python
import pygame
import pymunk
from pymunk import Vec2d
import pymunk.pygame_util
import tkinter as tk
from tkinter import *
import os

root = tk.Tk()
embed = tk.Frame(root, width = 500, height = 500) #creates embed frame for pygame window
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
buttonwin = tk.Frame(root, width = 75, height = 500)
buttonwin.pack(side = LEFT)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
screen = pygame.display.set_mode((500,500))
#screen.fill(pygame.Color(255,255,255))
pygame.display.init()
pymunk.pygame_util.positive_y_is_up = False
pygame.display.update()
space = pymunk.Space()
draw_options = pymunk.pygame_util.DrawOptions(screen)
space.gravity = (0.0,900.0)

wall = pymunk.Segment(space.static_body, (0, 500), (500,500), 50)
wall.friction = 1
space.add(wall)

#Attempt to build car
pos = Vec2d(100,200)

wheel_color = 52,219,119
wheel2_color = 52,219,119
shovel_color = 219,119,52
mass = 100
radius = 25
moment = pymunk.moment_for_circle(mass, 20, radius)
wheel1_b = pymunk.Body(mass, moment)
wheel1_s = pymunk.Circle(wheel1_b, radius)
wheel1_s.friction = 1.5
#wheel1_s.color = wheel_color
space.add(wheel1_b, wheel1_s)

mass = 100
radius = 25
moment = pymunk.moment_for_circle(mass, 20, radius)
wheel2_b = pymunk.Body(mass, moment)
wheel2_s = pymunk.Circle(wheel2_b, radius)
wheel2_s.friction = 1.5
#wheel2_s.color = wheel2_color
space.add(wheel2_b, wheel2_s)

mass = 100
size = (50,30)
moment = pymunk.moment_for_box(mass, size)
chassi_b = pymunk.Body(mass, moment)
chassi_s = pymunk.Poly.create_box(chassi_b, size)
space.add(chassi_b, chassi_s)

vs = [(0,0),(25,45),(0,45)]
shovel_s = pymunk.Poly(chassi_b, vs, transform = pymunk.Transform(tx=85))
shovel_s.friction = 0.5
shovel_s.color = shovel_color
space.add(shovel_s)

wheel1_b.position = pos - (55,0)
wheel2_b.position = pos + (55,0)
chassi_b.position = pos + (0,-25)

space.add(
    pymunk.PinJoint(wheel1_b, chassi_b, (0,0), (-25,-15)),
    pymunk.PinJoint(wheel1_b, chassi_b, (0,0), (-25, 15)),
    pymunk.PinJoint(wheel2_b, chassi_b, (0,0), (25,-15)),
    pymunk.PinJoint(wheel2_b, chassi_b, (0,0), (25, 15))
    )
speed = 4
motors = [pymunk.SimpleMotor(wheel1_b, chassi_b, 0),
    pymunk.SimpleMotor(wheel2_b, chassi_b, 0)]
space.add(
    motors[0], motors[1]
)
ch = space.add_collision_handler(0, 0)
ch.data["surface"] = screen

def draw():
    pygame.draw.circle(screen, (0,0,0), (250,250), 125)
    pygame.display.flip()
button1 = Button(buttonwin,text = 'Draw',  command=draw)
button1.pack(side=LEFT)
root.update()

while True:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        motors[0].rate = speed
        motors[1].rate = speed
    elif pressed[pygame.K_a]:
        motors[0].rate = -1*speed
        motors[1].rate = -1*speed
    else:
        motors[0].rate = 0
        motors[1].rate = 0

    fps = 30
    dt = 1. / fps
    space.step(.001)
    screen.fill(pygame.color.THECOLORS["black"])
    space.debug_draw(draw_options)
    pygame.display.flip()
    root.update()