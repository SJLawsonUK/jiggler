# Python3  software jiggler

import pyautogui,  sys
from time import sleep

screensize = pyautogui.size() # warning - this sees dual screens as one screen
sizelist = list(screensize)
halfsize = list(map(lambda z: int(z/2), sizelist))
halfsizeplus = list(map(lambda y: int(y+1), halfsize)) 
tuplehalfsize = tuple(halfsize)
tuplehalfsizeplus = tuple(halfsizeplus)

whereismouse = pyautogui.position() # returns tuple
x = 0

print("\n\n\t\t\t*** JIGGLING ***\n\n\n")

while (whereismouse < tuplehalfsize):  # top left quadrant of screen
    for x in range(0,5): # jiggle 5 times
        pyautogui.moveTo(100,200)   # moves mouse to X of 100, Y of 200.
        pyautogui.moveTo(101,None)  # moves mouse to X of 101, Y of 200.
        x+=1
    sleep(3)  # wait then start jiggling again
    whereismouse = pyautogui.position()
if (whereismouse > tuplehalfsizeplus):  #  move away from  top left quadrant 
    sys.exit()  # jiggling ends

