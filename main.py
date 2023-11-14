import pyautogui as pg #importing the PyAutoGUI package
import time #time is part of the default Python installation
pg.FAILSAFE = True

time.sleep(5)
pg.press('space')
while True:
  t = []
  ss = pg.screenshot(region=(700,750,200,70))
  for i in range(200):
    for j in range(70):
      t.append(ss.getpixel((i,j))==(172,172,172))
  if any(t):
    pg.press('space')
    time.sleep(0.25)
    pg.keyDown('down')
    pg.keyUp('down') 