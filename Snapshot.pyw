import ImageGrab
import os
import time

#constant to change in different game sizes = could probably automate this
#box_size_x =
#box_size_y = 

top_left_x = 719
top_left_y = 321
bottom_right_x = 1358   #top_left_x + box_size_x
bottom_right_y = 720    #top_left_y + box_size_y
def screenGrab():
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    time.sleep(5)
    screenGrab()


if __name__ == '__main__':
    main()