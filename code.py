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
    image = ImageGrab.grab(box)

    # Time module works (First argument save the file and second is the file format).
    # os.getcwd() current directory the code.
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return image


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
        sizeOfFood['rice'] -= 1
        sizeOfFood['nori'] -= 1
        sizeOfFood['fishegg'] -= 1
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
        sizeOfFood['rice'] -= 2
        sizeOfFood['nori'] -= 1
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
        sizeOfFood['rice'] -= 1
        sizeOfFood['nori'] -= 1
        sizeOfFood['fishegg'] -= 2
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


def buy_food(food):
    if food == 'rice':
        mouse_pos(Cord.phone)
        time.sleep(.1)
        left_click()
        mouse_pos(Cord.menu_rice)
        time.sleep(.05)
        left_click()
        rgb = screen_grab()
        if rgb.getpixel(Cord.buy_rice) != (109, 123, 127):
            print("rice is available")
            mouse_pos(Cord.buy_rice)
            time.sleep(.1)
            left_click()
            mouse_pos(Cord.deliver_normal)
            sizeOfFood['rice'] += 10
            print(" %d rice is available" % sizeOfFood['rice'])
            time.sleep(.1)
            left_click()
            time.sleep(2.5)
        else:
            print("rice is not available")
            mouse_pos(Cord.menu_exit)
            time.sleep(.1)
            left_click()
            buy_food(food)

    if food == 'nori':
        mouse_pos(Cord.phone)
        time.sleep(.1)
        left_click()
        mouse_pos(Cord.menu_toppings)
        time.sleep(.05)
        left_click()
        rgb = screen_grab()
        if rgb.getpixel(Cord.buy_nori) != (53, 53, 39):
            print("nori is available")
            mouse_pos(Cord.buy_nori)
            time.sleep(.1)
            left_click()
            mouse_pos(Cord.deliver_normal)
            sizeOfFood['nori'] += 10
            print(" %d nori is available" % sizeOfFood['nori'])
            time.sleep(.1)
            left_click()
            time.sleep(2.5)
        else:
            print("nori is not available")
            mouse_pos(Cord.menu_exit)
            time.sleep(.1)
            left_click()
            buy_food(food)

    if food == 'fishegg':
        mouse_pos(Cord.phone)
        time.sleep(.1)
        left_click()
        mouse_pos(Cord.menu_toppings)
        time.sleep(.05)
        left_click()
        rgb = screen_grab()
        if rgb.getpixel(Cord.buy_fish_egg) != (127, 61, 0):
            print("fish egg is available")
            mouse_pos(Cord.buy_fish_egg)
            time.sleep(.1)
            left_click()
            mouse_pos(Cord.deliver_normal)
            sizeOfFood['fishegg'] += 10
            print(" %d fishegg is available" % sizeOfFood['fishegg'])
            time.sleep(.1)
            left_click()
            time.sleep(2.5)
        else:
            print("fish egg is not available")
            mouse_pos(Cord.menu_exit)
            time.sleep(.1)
            left_click()
            buy_food(food)


def get_seat_one():
    box = (x_pad + 26, y_pad + 61, x_pad + 26 + 61, y_pad + 61 + 15)
    image = ImageOps.grayscale(ImageGrab.grab(box))
    arr = array(image.getcolors())
    arr = arr.sum()
    print(arr)
    image.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return arr


def get_seat_two():
    box = (x_pad + 127, y_pad + 61, x_pad + 127 + 61, y_pad + 61 + 15)
    image = ImageOps.grayscale(ImageGrab.grab(box))
    arr = array(image.getcolors())
    arr = arr.sum()
    print(arr)
    image.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return arr


def get_seat_three():
    box = (x_pad + 228, y_pad + 61, x_pad + 228 + 61, y_pad + 61 + 15)
    image = ImageOps.grayscale(ImageGrab.grab(box))
    arr = array(image.getcolors())
    arr = arr.sum()
    print(arr)
    image.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return arr


def get_seat_four():
    box = (x_pad + 329, y_pad + 61, x_pad + 329 + 61, y_pad + 61 + 15)
    image = ImageOps.grayscale(ImageGrab.grab(box))
    arr = array(image.getcolors())
    arr = arr.sum()
    print(arr)
    image.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return arr


def get_seat_five():
    box = (x_pad + 430, y_pad + 61, x_pad + 430 + 61, y_pad + 61 + 15)
    image = ImageOps.grayscale(ImageGrab.grab(box))
    arr = array(image.getcolors())
    arr = arr.sum()
    print(arr)
    image.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return arr


def get_seat_six():
    box = (x_pad + 531, y_pad + 61, x_pad + 531 + 61, y_pad + 61 + 15)
    image = ImageOps.grayscale(ImageGrab.grab(box))
    arr = array(image.getcolors())
    arr = arr.sum()
    print(arr)
    image.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return arr


def get_all_seat():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()


sizeOfFood = {'shrimp': 5,
              'rice': 10,
              'nori': 10,
              'fishegg': 10,
              'salmon': 5,
              'unagi': 5}


def check_food():
    for i, j in sizeOfFood.items():
        if i == 'nori' or i == 'rice' or i == 'fishegg':
            if j <= 4:
                print('%s is low' % i)
                buy_food(i)


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
    start_game()
    while 1:

        input_food = input()
        make_sushi(input_food)
        check_food()



if __name__ == '__main__':
    main()
