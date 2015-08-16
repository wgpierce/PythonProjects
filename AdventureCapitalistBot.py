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
distance_between_buttons = .148
indicator = (220, 123, 54)
'''Game-Specific Variables'''
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
'''Screen functions'''
def screenGrab():
    im = ImageGrab.grab()
    #to save as file
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def boxGrab():
    im = ImageGrab.grab(box)
    return im
    
'''
#Need to fix numpy build environment for this
#This function specifically allows averaging of an area to determine identity
def grab():
    im = ImageOps.grayscale(ImageGrab.grab(box))
 #   a = np.array(im.getcolors())
    a = a.sum()
    #print a
    return a
'''
def bindWidth(supposed_width):
    if supposed_width < 640:
        return 512
    if supposed_width < 800:
        return 640
    if supposed_width < 1024:
        return 800
    if supposed_width < 1280:
        return 1024
    if supposed_width < 1360:
        return 1280
    if supposed_width < 1366:
        return 1360
    return 1366
    
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
                try:
                    #while s.getpixel((k,j)) == (87, 79, 71):
                    while s.getpixel((k,j)) <= (105, 91, 81):
                        k = k + 1
                except: 
                    #in case of fullscreen, the k value is fine
                    pass
                #We will use if this width is > 100, we assume we have found the game
                if (k - i) > 100:
                    #find height, as long as it does not go off the box
                    #do so by finding first pixel that is not the background colors
                    l = j
                    try:
                        while (87, 79, 70) <= s.getpixel((i,l)) <= (100, 92, 82):
                            l = l + 1
                    except:
                        #in case of full screen, l is fine
                        pass
                    x_pad = i
                    y_pad = j
                    supposed_width = int((k - i) * 5.26) #this is ~20% of the screen
                    print 'supposed_width: %d' % supposed_width
                    width = bindWidth(supposed_width) # we bind this to an exact value
                    height = l - j + 1            #this is the height we just found
                    game_found = True
                    box = (x_pad,y_pad,x_pad + width,y_pad + height)
                    #Populate sell and buy coordinates dynamically
                    for i in range(5):
                        #first column
                        cord_sale.append((int(width * .29), int(height * (.21 + distance_between_buttons * i))))
                        cord_buy.append((int(width * .39), int(height * (.27 + distance_between_buttons * i) - 2)))
                    for i in range(5):
                        #second column 
                        cord_sale.append((int(width * .64), int(height * (.21 + distance_between_buttons * i))))
                        cord_buy.append((int(width * .75), int(height * (.27 + distance_between_buttons * i) - 2)))
                    #Populate upgrade buttons dynamically
                    cord_upgrade_buy = (int(width * .71), int(height * .5))
                    cord_X = (int(width * .93), int(height * .065))
                    for i in range(3):
                        cord_upgrade_indicator.append((int(width * .025), int(height * (.44 + .115 * i))))
                        cord_upgrade.append((int(width * .05), int(height * (.44 + .115 * i))))
                    return
    print "AdVenture Capitalist! not found on this %d by %d screen." % (x, y)
'''Helper functions'''
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
'''Action functions'''
def buyManager():
    mousePos(cord_upgrade[1])
    leftClick()
    mousePos(cord_upgrade[1]) #buy
    leftClick()
    #if point is still orange, click again
    mousePos(cord_upgrade[1])
    leftClick()
'''
def upGrade()
def AngelInvestorSacrifice()
'''

'''Game code'''    
def startGame():
    s = boxGrab()
    #for i in cord_buy: 
    i = 0
    while True:
        mousePos(cord_sale)
        leftClick()
        #If we can buy, buy
        if s.getpixel(cord_buy[i]) == (224, 136, 74):
            mousePos(cord_sale[i])
            leftClick()   
        #if we can purchase a new one, do so 
        if s.getpixel(cord_buy[i + 1]) == indicator:
            mousePos(cord_sale[i + 1])
            leftClick()
        if s.getpixel(cord_upgrade_indicator[1]) == indicator:
            #we can buy a manager
            mousePos(cord_upgrade_indicator[1])
            leftClick()
            mousePos(cord_upgrade_buy)
            leftClick()
            
            
            
        
        #image Process next location
        print "Entering Execution Stage 2"
    #once Broken, we continue onto the long-game strategy


def continueGame():
    while True:
        s = boxGrab()
        if s.getpixel(cord_upgrade_indicator[1]) == (220, 123, 24):
            buyManager()
        mousePos(cord_buy[1])
        leftClick()

def main():
    #time.sleep(5)
    lockOn();
    print "x_pad: %d\ny_pad: %d\nwidth: %d\nheight: %d" % (x_pad, y_pad, width, height)
    print box
    if game_found == False:
        print "Bot not Started"
        return
    #Check if game is already initialized, past introduction
    s = boxGrab()
    #for i in range(3):
    print s.getpixel(cord_upgrade[1])
    mousePos(cord_upgrade[1])
    time.sleep(2)
    leftClick()
    mousePos(cord_upgrade_buy)
    print s.getpixel(cord_upgrade_buy)
        
        #leftClick()
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
