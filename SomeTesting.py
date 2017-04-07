#!/usr/bin/python
import pygame
import pymunk
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
pygame.display.update()
space = pymunk.Space()
draw_options = pymunk.pygame_util.DrawOptions(screen)
space.gravity = (0.0,-900.0)

wall = pymunk.Segment(space.static_body, (0, 0), (500, 0), 50)
wall.friction = 1
space.add(wall)

#Attempt to build car
x,y = 100,100
xOff, yOff = 10,10
body = pymunk.Body(1,1)  # Create a Body with mass and moment
body.position = x,y     # Set the position of the body
wheel1Body = pymunk.Body(body_type = pymunk.Body.KINEMATIC)  # Create a Body with mass and moment
wheel1Body.position = x+xOff,y+yOff     # Set the position of the body
wheel2Body = pymunk.Body(body_type = pymunk.Body.KINEMATIC)  # Create a Body with mass and moment
wheel2Body.position = x-xOff,y-yOff     # Set the position of the body

poly = pymunk.Segment(body,(-10,0),(10,0), 10) # Create a box shape and attach to body
wheel1 = pymunk.Circle(body,10,(xOff,-1*yOff))
wheel1.friction = 0.01
wheel1Joint = pymunk.GrooveJoint(body, wheel1Body, (0,0),(x,y),(x+xOff,y-yOff))
wheel2 = pymunk.Circle(body,10,(-1*xOff,-1*yOff))
wheel2.friction = 0.01
wheel2Joint = pymunk.GrooveJoint(body, wheel2Body, (0,0),(x,y),(x+xOff,y-yOff))
space.add(body, poly, wheel1, wheel2, wheel1Joint, wheel2Joint)       # Add both body and shape to the simulation

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
        body.apply_force_at_local_point((0,-100),(0,0))
    if pressed[pygame.K_a]:
        body.apply_force_at_local_point((0,100),(0,0))
    if pressed[pygame.K_s]:
        body.apply_force_at_local_point((0,0),(0,0))

    fps = 30
    dt = 1. / fps
    space.step(.001)
    screen.fill(pygame.color.THECOLORS["black"])
    space.debug_draw(draw_options)
    pygame.display.flip()
    root.update()