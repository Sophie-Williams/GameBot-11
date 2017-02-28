from PIL import ImageGrab
import os # To easily navigate around our operating syste's directory.
import time

x_pad = 464
y_pad = 242

def screenGrab():
    # Coordinates (x,y,x,y).
    box = (x_pad + 1,y_pad + 1,x_pad + 660,y_pad + 500)
    # Full SnapShot of your screen. (x,y,x,y) First pair (x,y.. top left of the box,
    # Second pair (..,x,y) bottom right.
    im = ImageGrab.grab(box)
    # Time module works (First argument save the file and second is the file format).
    # os.getcwd() current directory the code.
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


def main():
    screenGrab()

if __name__ == '__main__':
    main()
