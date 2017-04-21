#!/usr/bin/python
from GameClasses import *
from tkinter import *
from MenuDisplay import *
from GameDisplay import *
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
from pymunk.vec2d import Vec2d
import pymunk.pygame_util
import sys

#    Tank             Target
levelInfo = [
    (Vec2d(100, 200), Vec2d(1000,175)),
    (Vec2d(100, 200), Vec2d(1300,175)),
    (Vec2d(100, 200), Vec2d(1000,600))
]

def stick_arrow_to_target(space, arrow_body, target_body, position, flying_arrows):
    pivot_joint = pymunk.PivotJoint(arrow_body, target_body, position)
    phase = target_body.angle - arrow_body.angle
    gear_joint = pymunk.GearJoint(arrow_body, target_body, phase, 1)
    space.add(pivot_joint)
    space.add(gear_joint)
    try:
        flying_arrows.remove(arrow_body)
    except:
        pass

def remove_arrow(space, self, a, arrow_body, b, other_body, flying_arrows):
    if b.group == 3:
        #end level
        ApplicationGUI.beat_current_level(self)
        space.remove(other_body, b)
    try:
        flying_arrows.remove(arrow_body)
    except:
        pass
    space.remove(arrow_body, a)

def post_solve_arrow_hit(arbiter, space, data):
    if arbiter.total_impulse.length > 30:
        a, b = arbiter.shapes
        position = arbiter.contact_point_set.points[0].point_a
        b.collision_type = 0
        b.group = 1
        other_body = a.body
        arrow_body = b.body
        space.add_post_step_callback(
        #    stick_arrow_to_target, arrow_body, other_body, position, data["flying_arrows"])
            remove_arrow, data["self"], b, arrow_body, a, other_body, data["flying_arrows"])

class ApplicationGUI():
    def __init__(self, WIDTH, HEIGHT):
        self.running = False
        self.w = WIDTH
        self.h = HEIGHT
        self.clock = pygame.time.Clock()
        self.frameRate = 60
        self.start_root(WIDTH, HEIGHT)
        self.create_widgets(MainMenu)

    def close(self):
        self.end_gameplay()
        self.top.destroy()

    def create_widgets(self, menu):
        self.master = Frame(self.top)
        self.master.pack(side="top", fill="both", expand=True)
        self.master.rowconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.frames = {}
        for f in (MainMenu, PlayGameMenu, LevelSelectMenu, InstructionsMenu, GameScreen):
            frame = f(self.master, self)
            frame.frame.grid(row=0, column=0, sticky=N+W+S+E)
            self.frames[f] = frame
        self.show_frame(menu)
    def show_frame(self, cls):
        self.frames[cls].frame.lift()

    def start_root(self, WIDTH, HEIGHT):
        self.top = Tk()
        self.top.rowconfigure(0, weight=1)
        self.top.columnconfigure(0, weight=1)
        self.top.wm_title("Tank Shooting Game")
        self.top.geometry(str(WIDTH) + "x" + str(HEIGHT))
        self.top.resizable(0, 0)
        self.top.protocol("WM_DELETE_WINDOW", self.close)

    def end_gameplay(self):
        pygame.quit()
        self.running = False
        self.space = None

    def beat_current_level(self):
        if self.current_level == 1:
            self.frames[LevelSelectMenu].level2Button.config(state = NORMAL, command=lambda:self.frames[LevelSelectMenu].playGame(2))
        elif self.current_level ==2:
            self.frames[LevelSelectMenu].level3Button.config(state=NORMAL, command=lambda: self.frames[LevelSelectMenu].playGame(3))

        self.screen.blit(pygame.font.SysFont("Arial", 64).render("COMPLETED", 1, THECOLORS["green"]), (self.w*1.3, self.h/2))
        pygame.display.flip()
        #Then Wait for a time displaying a victory message then go back to Level Select
        pygame.time.wait(5000)
        self.top.attributes("-fullscreen",False)
        self.running = False
        self.show_frame(LevelSelectMenu)

    def start_game(self, WIDTH, HEIGHT, level_to_play):
        #pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.current_level = level_to_play

        #pymunk
        self.space = pymunk.Space()
        self.flying_arrows = []
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.handler = self.space.add_collision_handler(0,1)
        self.handler.data["flying_arrows"] = self.flying_arrows
        self.handler.data["self"] = self
        self.handler.post_solve = post_solve_arrow_hit

        self.handler = self.space.add_collision_handler(0,3)


        #### TEMPORARY ####
        #Load levels
        i = 1
        for level in (Level1, Level2, Level3):
            if i == level_to_play:
                tank_pos, tar_pos = levelInfo[level_to_play-1]
                self.level=level(WIDTH,HEIGHT, self.space, self.screen, tank_pos=tank_pos,target_pos=tar_pos)
                break
            i += 1
        self.running = True

    def get_mouse_pos(self):
        return pymunk.pygame_util.from_pygame(Vec2d(pygame.mouse.get_pos()), self.screen)

    def run(self):

        firstClick = False
        start_time = -1
        while True:
            fps = 60
            dt = 1. / fps
            self.top.update()

            if self.running:
                for event in pygame.event.get():
                    if event.type == QUIT or \
                                            event.type == KEYDOWN and (event.key in [K_ESCAPE, K_q]):
                        self.running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and firstClick:
                        start_time = pygame.time.get_ticks()
                    elif event.type == KEYDOWN and event.key == K_p:
                        pygame.image.save(self.screen, "arrows.png")
                    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and firstClick and start_time != -1:
                        end_time = pygame.time.get_ticks()

                        diff = end_time - start_time
                        power = max(min(diff, 1000), 10) * 1.5
                        impulse = power * Vec2d(1, 0)
                        impulse.rotate(self.level.tank.get_arrow_angle())
                        self.flying_arrows.append(self.level.tank.fire_arrow(self.space,self.flying_arrows,impulse))
                    elif not firstClick and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        firstClick = True

                keys = pygame.key.get_pressed()

                speed = 7
                #if (keys[K_UP]):
                #    cannon_body.position += Vec2d(0, 1) * speed
                #if (keys[K_DOWN]):
                #    cannon_body.position += Vec2d(0, -1) * speed
                if (keys[K_LEFT]):
                    self.level.moveTank(1 * speed)
                elif (keys[K_RIGHT]):
                    self.level.moveTank(-1 * speed)
                else:
                    self.level.moveTank(0)

                self.level.update_level(self.space,self.get_mouse_pos())
                for flying_arrow in self.flying_arrows:
                    drag_constant = 0.0002

                    pointing_direction = Vec2d(1, 0).rotated(flying_arrow.angle)
                    flight_direction = Vec2d(flying_arrow.velocity)
                    flight_speed = flight_direction.normalize_return_length()
                    dot = flight_direction.dot(pointing_direction)
                    # (1-abs(dot)) can be replaced with (1-dot) to make arrows turn
                    # around even when fired straight up. Might not be as accurate, but
                    # maybe look better.
                    drag_force_magnitude = (1 - dot) * flight_speed ** 2 * drag_constant * flying_arrow.mass
                    arrow_tail_position = Vec2d(-50, 0).rotated(flying_arrow.angle)
                    flying_arrow.apply_impulse_at_world_point(drag_force_magnitude * -flight_direction,
                                                              arrow_tail_position)

                    flying_arrow.angular_velocity *= 0.5
                self.screen.fill(pygame.color.THECOLORS["lightgrey"])
                self.space.debug_draw(self.draw_options)
                self.level.write_to_screen(self.screen)
                if pygame.mouse.get_pressed()[0]:
                    current_time = pygame.time.get_ticks()
                    diff = current_time - start_time
                    power = max(min(diff, 1000), 10)
                    h = power / 2
                    pygame.draw.line(self.screen, pygame.color.THECOLORS["red"], (30, 550), (30, 550 - h), 10)
                self.screen.blit(pygame.font.SysFont("Arial", 16).render("fps: " + str(self.clock.get_fps()), 1, THECOLORS["black"]), (10, 10))
                self.screen.blit(
                    pygame.font.SysFont("Arial", 16).render("Angle: " + str(self.level.tank.get_arrow_angle()*57.2958)[0:6] + "°", 1, THECOLORS["black"]),
                    (self.level.tank.get_cannon_body_position()[0], 2*self.h - self.level.tank.get_cannon_body_position()[1]))

                if not firstClick:
                    self.screen.blit(pygame.font.SysFont("Arial", 46).render("CLICK TO BEGIN", 1,
                                                                             THECOLORS["black"]), (self.w*1.3, self.h/2))
                pygame.display.flip()
                self.space.step(dt)
            else:
                firstClick = False
                start_time = -1
            self.clock.tick(fps)


def main():
    WIDTH = 500
    HEIGHT = 400
    app = ApplicationGUI(WIDTH, HEIGHT)

    app.run() #Forever Loops


if __name__ == "__main__":
    main()