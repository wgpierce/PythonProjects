import win32api
import win32con

import ImageGrab
import time
import ImageOps
# import numpy as np

#constant to change in different game sizes = could probably automate this
width = 640
height = 400
x_pad = 363
y_pad = 193
bottom_right_x = x_pad + width
bottom_right_y = y_pad + height

def screenGrab():
    box = (x_pad,y_pad,bottom_right_x,bottom_right_y)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

'''
to compare pixel value
s = screenGrab
s.getPixel(pixelLocation) == (R,G,B) # From 0 to 255
'''

'''
Coordinates for starting a sale and buying a thing
These are dynamic and should fill to a given screen position and size
Assuming 4 x 2 layout
We could generalize these, but I'm not sure it would make it go faster
0 Lemon     5 Shrimp
1 News      6 Hockey
2           7 Movie
3           8 Bank
4 Donut     9 Oil
'''
cord_s = []
cord_b = []
#Populate these dynamically
for i in range(5):
    cord_s.append((int(width * .29), int(height * (.21 + .165 * i))))
    cord_b.append((int(width * .40), int(height * (.25 + .165 * i))))
for i in range(5):
    cord_s.append((int(width * .64), int(height * (.21 + .165 * i))))
    cord_b.append((int(width * .75), int(height * (.25 + .165 * i))))
'''
Indicator and Upgrades
1 Upgrade
2 Manager
3 Angel Investor
'''
cord_ui = []
cord_u = []
#Populate dynamically
for i in range(3):
    cord_ui.append((int(width * .025), int(height * (.44 + .12 * i))))
    cord_u.append((int(width * .5), int(height * (.44 + .12 * i))))
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    ###print "Click."          #completely optional. But nice for debugging purpo    
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    #print 'left Down'     
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    #print 'left release'
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))     
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

# Start Game Code
def startGame():
    s = screenGrab()
    while (s.getpixel(cord_b[1]) != (115, 105, 96)):
        while (s.getpixel(cord_b[0]) != (115, 105, 96)):
            mousePos(cord_s[0])
            for j in range(4):
                leftClick()
                time.sleep(.2)
        mousePos(cord_b[0])
        for j in range(i):
            leftClick()
            time.sleep(.2)
                
                
                
        mousePos(cord_s[1])
        leftClick()
        mousePos(cord_b[1])
        leftClick()
    #image Process next location
    
    
    print "Entering Execution Stage 2"
    
'''
def upGrade()
def AngelInvestorSacrifice()
'''
'''
def buyManager()
    #image process point (int(width * .025), int(height * .4375)
    mousePos(cord_b[1])
    leftClick()
    mousePos(cord_b[1]) #buy
    leftClick()
    #if point is still orange, click again
    
    mousePos(cord)
    leftClick()
'''
'''
def grab():
    box = (x_pad + 1,y_pad+1,bottom_right_x,bottom_right_y)
    im = ImageOps.grayscale(ImageGrab.grab(box))
 #   a = np.array(im.getcolors())
    a = a.sum()
    #print a
    return a
'''

   
def main():
    #Init image grab to lock on to screen and dimensions
    #Check if game is already initialized, past introduction
    startGame()
    print 'meow'
    s = screenGrab()
    for i in range(3):
        print s.getpixel(cord_ui[i])

if __name__ == '__main__':
    main()
