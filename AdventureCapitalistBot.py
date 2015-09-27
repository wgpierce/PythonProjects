'''
Adventure Capitalist Bot
This bot locks onto AdVenture Capitalist program running and dynamically plays
the game for you based on the notifications it receives

#TODO: integrate image word processing to keep track of numbers
#TODO: add quit button
@date:   August 13, 2015
@author: William Pierce

'''
import win32api
import win32con

import ImageGrab
import time
import ImageOps
import numpy as np    #TODO: Need to fix build environment

'''Global Variables'''
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
cord_upgrade= []
cord_upgrade_buy = []
cord_X = ()
'''
Screen functions
'''
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
    global cord_upgrade
    global cord_upgrade_buy
    global cord_X
    s = screenGrab()
    x,y = s.size
    for i in xrange(x):
        for j in xrange(y):
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
                    #print 'supposed_width: %d' % supposed_width
                    width = bindWidth(supposed_width) # we bind this to an exact value
                    height = l - j + 1            #this is the height we just found
                    game_found = True
                    box = (x_pad,y_pad,x_pad + width,y_pad + height)
                    #Populate sell and buy coordinates dynamically
                    for i in xrange(5):
                        #first column
                        cord_sale.append((int(width * .29), int(height * (.21 + distance_between_buttons * i))))
                        cord_buy.append((int(width * .39), int(height * (.27 + distance_between_buttons * i) - 2)))
                    for i in xrange(5):
                        #second column 
                        cord_sale.append((int(width * .64), int(height * (.21 + distance_between_buttons * i))))
                        cord_buy.append((int(width * .75), int(height * (.27 + distance_between_buttons * i) - 2)))
                    #Populate upgrade buttons dynamically
                    cord_upgrade_buy.append((int(width * .71), int(height * .65)))
                    cord_upgrade_buy.append((int(width * .71), int(height * .5)))
                    cord_X = (int(width * .93), int(height * .065))
                    for i in xrange(3):
                        cord_upgrade.append((int(width * .025), int(height * (.44 + .115 * i))))
                        #cord_upgrade.append((int(width * .05), int(height * (.44 + .115 * i))))
                    return
    print "AdVenture Capitalist! not found on this %d by %d screen." % (x, y)
    
#turn off sound
#def soundToggle():    
'''Helper functions'''
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.15)
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
def pressEsc():
    win32api.keybd_event('0x1B',0,0,0)
    time.sleep(.05)
    win32api.keybd_event('0x1B',0 ,win32con.KEYEVENTF_KEYUP ,0)
            
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))     
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y
'''Action functions'''
def upgrade():
    print 'mew'
    
def buyManager():
    s = boxGrab()
    mousePos(cord_upgrade[1])
    leftClick()
    mousePos(cord_upgrade_buy)
    leftClick()
    #We can still buy more
    while s.getpixel(cord_upgrade_buy) == (140, 129, 118):
        leftClick()
        i = i = 1
        print "Entering Execution Stage %d" % i
    #We no longer need to manage
    i = i + 1
    print "Entering Execution Stage %d" % i 
    
def AngelInvestorSacrifice():
    print 'mew'

'''Game code'''    
def startGame(): 
    i = 0
    j = 1 
    counter = 0
    print "Entering Execution Stage %d" % i
    #May need adjustment to avoid OOB
    #TODO: This may encounter an OOB exception, since managers take precedence
    while i < 9:
        #TODO: Add quit button
        s = boxGrab()
        #We can buy a manager
        if s.getpixel(cord_upgrade[1]) == indicator:
            mousePos(cord_upgrade[1])
            leftClick()
            time.sleep(.2)
            mousePos(cord_upgrade_buy[1])
            leftClick()
            time.sleep(.5)
            #We no longer need to manage i
            i = i + 1
            print "Entering Execution Stage %d" % i
            '''
            s = boxGrab()
            testLocation = cord_upgrade_buy[1] - (0, 2)    #to avoid catching the mouse
            while s.getpixel(testLocation) == (139, 184, 207):
                #We can still buy more
                s = boxGrab()
                leftClick()
                i = i + 1
                time.sleep(.2)
                print "Entering Execution Stage %d" % i
            '''
            time.sleep(.2)
            mousePos(cord_X)
            leftClick()
            time.sleep(.2)
            
        #if we can purchase a new business, do so 
        if (219, 122, 54) <= s.getpixel(cord_buy[j]) <= indicator:
            mousePos(cord_buy[j])
            time.sleep(.2)
            leftClick()
            time.sleep(.2)
            leftClick()
            j = j + 1
            
        if s.getpixel(cord_upgrade[0]) == indicator:
            #purchase upgrade
            mousePos(cord_upgrade[0])
            leftClick()
            time.sleep(.2)
            mousePos(cord_upgrade_buy[0])
            leftClick()
            time.sleep(.5)
            '''
            s = boxGrab()
            testLocation = cord_upgrade_buy[0] - (0, 2)    #to avoid catching the mouse
            while s.getpixel(testLocation) == (220, 123, 54):
                #We can still upgrade more
                s = boxGrab()
                leftClick()
                time.sleep(.2)
            '''
            time.sleep(.2)
            mousePos(cord_X)
            leftClick()
            time.sleep(.2)
        time.sleep(.2)
        for k in xrange(i, j):
            #We click all unmanaged and buy
            mousePos(cord_sale[k])
            time.sleep(.2)
            leftClick()
            time.sleep(.2)
        
        if counter == 2:
            counter = 0
            for k in xrange(0, j):
                #If we can buy, buy, in reverse order
                #print s.getpixel(cord_buy[i])
                s = boxGrab()
                if s.getpixel(cord_buy[j - k - 1]) == (224, 136, 74):
                    mousePos(cord_buy[j - k - 1])
                    leftClick()   
                    time.sleep(.2)
        time.sleep(.1)
        counter = counter + 1
        # Angel Investors not handled here
    #Once broken, all businesses are bought and we enter the long-term game strategy    
    

def continueGame():
    while True:
        s = boxGrab()
        if s.getpixel(cord_upgrade[1]) == (220, 123, 24):
            buyManager()
        mousePos(cord_buy[1])
        leftClick()

def diagnostics():
    #print "x_pad: %d\ny_pad: %d\nwidth: %d\nheight: %d" % (x_pad, y_pad, width, height)
    #print box
    s = boxGrab()
    print s.getpixel(cord_upgrade[0])
    mousePos(cord_upgrade[0])
    time.sleep(2)
    leftClick()
    leftClick()
    mousePos(cord_upgrade_buy)
    time.sleep(5)
    print 'mew'
    print s.getpixel(cord_upgrade_buy)
    #if win32api.GetAsyncKeyState(ord('q')) == 1:
    #        return
    #leftClick()
        
    '''
    print 'meow'
    s = screenGrab()
    for i in xrange(3):
        print s.getpixel(cord_upgrade_indicator[i])
    '''
'''
    
def main():
    lockOn()
    #diagnostics()
    if game_found == False:
        print "Bot not Started"
        return
    try:
        #startGame()
        #continueGame()
        print "meow"
    except:
        "Game interrupted"
        
if __name__ == '__main__':
    main()
