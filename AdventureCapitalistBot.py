'''
Adventure Capitalist Bot
This bot locks onto AdVenture Capitalist program running and dynamically plays
the game for you based on the notifications it receives

#TODO: integrate image word processing to keep track of numbers

@date:   August 13, 2015
@author: William Pierce

'''
import win32api
import win32con

import ImageGrab
import time
import ImageOps
# import numpy as np    #TODO: Need to fix build environment

#Global Variables
width = 640
height = 400
x_pad = 363
y_pad = 193
game_found = False
box = ()

#Game-Specific Variables
'''
Coordinates for starting a sale and buying a thing
Assuming 4 x 2 layout
These are dynamic and should fill to a given screen position and size
These are dynamically generated in the lockon function to ensure
they match the game size parameters
0 Lemon     5 Shrimp
1 News      6 Hockey
2           7 Movie
3           8 Bank
4 Donut     9 Oil
'''
cord_sale = []
cord_buy = []

'''
Indicator and Upgrades
    Unlock
0 Upgrade
1 Manager
2 Angel Investor
'''
cord_upgrade_indicator = []
cord_upgrade = []
cord_upgrade_buy = ()
cord_X = ()

def screenGrab():
    im = ImageGrab.grab()
    #to save as file
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def boxGrab():
    im = ImageGrab.grab(box)
    return im

def lockOn():
    global x_pad
    global y_pad
    global width
    global height
    global game_found
    global box
    global cord_sale
    global cord_buy
    global cord_upgrade_indicator
    global cord_upgrade
    global cord_upgrade_buy
    global cord_X
    s = screenGrab()
    x,y = s.size
    for i in range(x):
        for j in range(y):
            if s.getpixel((i,j)) == (87, 79, 71):
                #find width, if this is the box
                k = i + 1
                while s.getpixel((k,j)) == (87, 79, 71):
                    k = k + 1
                #We will use if this width is > 100, we assume we have found the game
                if (k - i) > 100:
                    #find height, as long as it does not go off the box
                    #do so by finding first pixel that is not the background color
                    #TODO: probably need to make this more robust
                    l = j
                    while s.getpixel((i,l)) > (70, 70, 70):
                        l = l + 1
                    x_pad = i
                    y_pad = j
                    width = int((k - i) * 5.1)   #this is ~20% of the screen
                    height = l - j               #this is the height we just found
                    game_found = True
                    box = (x_pad,y_pad,x_pad + width,y_pad + height)
                    #Populate sell and buy coordinates dynamically
                    for i in range(5):
                        #first column
                        cord_sale.append((int(width * .29), int(height * (.21 + .165 * i))))
                        cord_buy.append((int(width * .40), int(height * (.25 + .165 * i))))
                    for i in range(5):
                        #second column 
                        cord_sale.append((int(width * .64), int(height * (.21 + .165 * i))))
                        cord_buy.append((int(width * .75), int(height * (.25 + .165 * i))))
                    #Populate upgrade buttons dynamically
                    cord_upgrade_buy = (int(width * .71), int(height * .5))
                    cord_X = (int(width * .93), int(height * .065))
                    for i in range(3):
                        cord_upgrade_indicator.append((int(width * .025), int(height * (.44 + .12 * i))))
                        cord_upgrade.append((int(width * .5), int(height * (.44 + .12 * i))))
                    return
    print "AdVenture Capitalist! not found on this %d by %d screen." % (x, y)

#Helper functions
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
'''
def upGrade()
def AngelInvestorSacrifice()
'''
    
def buyManager():
    mousePos(cord_upgrade[1])
    leftClick()
    mousePos(cord_upgrade[1]) #buy
    leftClick()
    #if point is still orange, click again
    mousePos(cord_upgrade[1])
    leftClick()
'''
def grab():
    box = (x_pad + 1,y_pad+1,bottom_right_x,bottom_right_y)
    im = ImageOps.grayscale(ImageGrab.grab(box))
 #   a = np.array(im.getcolors())
    a = a.sum()
    #print a
    return a
'''

# Start Game Code
def startGame():
    s = boxGrab()
    while (s.getpixel(cord_buy[1]) != (115, 105, 96)):
        while (s.getpixel(cord_buy[0]) != (115, 105, 96)):
            mousePos(cord_sale[0])
            for j in range(4):
                leftClick()
                time.sleep(.2)
        mousePos(cord_buy[0])
        for j in range(i):
            leftClick()
            time.sleep(.2)
                
                
                
        mousePos(cord_sale[1])
        leftClick()
        mousePos(cord_buy[1])
        leftClick()
    #image Process next location
    
    
    print "Entering Execution Stage 2"

def continueGame():
    while True:
        s = boxGrab()
        if s.getpixel(cord_upgrade_indicator[1]) == (220, 123, 24):
            buyManager()
        mousePos(cord_buy[1])
        leftClick()

def main():
    #lockOn();
    print "x_pad: %d\ny_pad: %d\nwidth: %d\nheight: %d" % (x_pad, y_pad, width, height)
    print box
    if game_found == False:
        print "defaults used"
        return
    #Check if game is already initialized, past introduction
    print 'meow'
    try:
        #startGame()
        #continueGame()
        print "meow"
    except:
        "Game interrupted"
        
    '''
    print 'meow'
    s = screenGrab()
    for i in range(3):
        print s.getpixel(cord_upgrade_indicator[i])
    '''
        
        
if __name__ == '__main__':
    main()
