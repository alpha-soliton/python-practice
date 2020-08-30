#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480) # size of screnn (width, height)
STEP = 10 # sensitivity of keyboard/hat switch

MODE = "JOY"    #KEY: keyborad input
                #JOY: joystick analog input
                #HAT: hatswitch / the cross key


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("window test")
    X_CENTER = int(SCREEN_SIZE[0]/2)
    Y_CENTER = int(SCREEN_SIZE[1]/2)
    [circle_x, circle_y] = [X_CENTER, Y_CENTER]

    pygame.joystick.init()
    try:
        joy = pygame.joystick.Joystick(0)
        joy.init()
        print("Joystick Name: "+ joy.get_name())
        print("Number of Button: "+ str(joy.get_numbuttons()))
        print("Number of Axis: "+str(joy.get_numaxes()))
        print("Number of Hats: " +str(joy.get_numhats()))
    except pygame.error:
        print('Joystick was not detected.')
    
    while True:
        screen.fill((0,0,0)) # fill in blue
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        
        if MODE == "KEY":
            # get current satus of keyboard
            pressed_keys = pygame.key.get_pressed()
            # move in the direction depending on pressed key
            if pressed_keys[K_LEFT]:
                circle_x = circle_x - STEP
            if pressed_keys[K_RIGHT]:
                circle_x = circle_x + STEP
            if pressed_keys[K_UP]:
                circle_y = circle_y - STEP
            if pressed_keys[K_DOWN]:
                circle_y = circle_y + STEP

        elif MODE == "JOY":
            circle_x = int((joy.get_axis(0)+1) * X_CENTER)
            circle_y = int((joy.get_axis(1)+1) * Y_CENTER)


        # check the limit of window
        if circle_x <0:
            circle_x = 0
        elif circle_x > SCREEN_SIZE[0]:
            circle_x = SCREEN_SIZE[0]

        if circle_y<0:
            circle_y = 0
        elif circle_y > SCREEN_SIZE[1]:
            circle_y = SCREEN_SIZE[1]

        # draw
        pygame.draw.circle(screen, (255,0,0), (circle_x, circle_y), 10)
        pygame.display.update()
        pygame.time.wait(30)
