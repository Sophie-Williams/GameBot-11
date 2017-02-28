from PIL import ImageGrab
import os
import time
import win32api, win32con
import sys
import csv
from PIL import ImageOps
from numpy import *

#----Global Variables
x_pad = 464
y_pad = 242


def screen_grab():
    # Coordinates (x,y,x,y).
    box = (x_pad + 1, y_pad + 1, x_pad + 660, y_pad + 500)
    # Full SnapShot of your screen. (x,y,x,y) First pair (x,y.. top left of the box,
    # Second pair (..,x,y) bottom right.
    im = ImageGrab.grab(box)
    # Time module works (First argument save the file and second is the file format).
    # os.getcwd() current directory the code.
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def left_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)


def left_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)


def mouse_pos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def start_game():
    # location of first menu
    mouse_pos((311, 204))
    left_click()
    time.sleep(.1)

    # location of second menu
    mouse_pos((311, 390))
    left_click()
    time.sleep(.1)

    # location of third menu
    mouse_pos((313, 402))
    left_click()
    time.sleep(.1)

    # location of fourth menu
    mouse_pos((583, 452))
    left_click()
    time.sleep(.1)

    # location of fifth menu
    mouse_pos((315, 376))
    left_click()
    time.sleep(.1)


def clear_tables():
    mouse_pos((78, 206))
    left_click()

    mouse_pos((177, 206))
    left_click()

    mouse_pos((280, 206))
    left_click()

    mouse_pos((380, 205))
    left_click()

    mouse_pos((484, 205))
    left_click()

    mouse_pos((583, 205))
    left_click()
    time.sleep(1)


def make_sushi(food):
    if food == 'caliroll':
        mouse_pos(Cord.food_rise)
        left_click()
        time.sleep(.05)
        mouse_pos(Cord.food_nori)
        left_click()
        time.sleep(.05)
        mouse_pos(Cord.food_fish_egg)
        left_click()
        time.sleep(.1)
        mouse_pos(Cord.enter)
        left_click()
        time.sleep(1.5)

    elif food == 'onigiri':
        mouse_pos(Cord.food_rise)
        left_click()
        time.sleep(.05)
        mouse_pos(Cord.food_rise)
        left_click()
        time.sleep(.05)
        mouse_pos(Cord.food_nori)
        left_click()
        time.sleep(.1)
        mouse_pos(Cord.enter)
        left_click()
        time.sleep(1.5)
    elif food == 'gunkan':
        mouse_pos(Cord.food_rise)
        left_click()
        time.sleep(.05)
        mouse_pos(Cord.food_nori)
        left_click()
        time.sleep(.05)
        mouse_pos(Cord.food_fish_egg)
        left_click()
        time.sleep(.05)
        mouse_pos(Cord.food_fish_egg)
        left_click()
        time.sleep(.1)
        mouse_pos(Cord.enter)
        left_click()
        time.sleep(1.5)


class Cord:
    food_shrimp = (35, 334)
    food_rise = (92, 334)
    food_nori = (35, 387)
    food_fish_egg = (92, 387)
    food_salmon = (35, 445)
    food_unagi = (92, 445)
    enter = (200, 385)
    # PHONE CORD
    phone = (585, 365)

    menu_toppings = (541, 271)
    buy_shrimp = (494, 221)
    buy_unagi = (576, 271)
    buy_nori = (494, 276)
    buy_fish_egg = (576, 276)
    buy_salmon = (494, 331)
    #RICE
    menu_rice = (541, 292)
    buy_rice = (541, 292)
    #SAKE
    menu_sake = (541, 309)
    buy_sake = (541, 309)
    #Normal Selected
    deliver_normal = (492, 293)


def main():
    screen_grab()
    start_game()
    input_food = input() #TODO: loop while
    make_sushi(input_food)



if __name__ == '__main__':
    main()