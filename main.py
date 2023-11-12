import pyautogui as pg #importing the PyAutoGUI package
import time #time is part of the default Python installation

dino_position = pg.locateOnScreen('dino.png') #for this to work, change the dino.png file with your own screenshot

print(dino_position)
