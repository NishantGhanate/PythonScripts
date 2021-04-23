
# https://pyautogui.readthedocs.io/en/latest/

import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
print(screenWidth, screenHeight)
print(currentMouseX, currentMouseY )
# pyautogui.move(0, 10)   
# pyautogui.write('Firefox', interval=0.25)
# pyautogui.press('enter') 
# pyautogui.moveRel(xOffset, yOffset, duration=num_seconds) 
