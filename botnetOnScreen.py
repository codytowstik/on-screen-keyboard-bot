import win32con
import win32api
from time import sleep
import pyautogui

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def getCursorPos():
    return win32api.GetCursorPos()

# while(True):
#     sleep(.5)
#     print(getCursorPos())

# sleep(5)
# while(True):
#     sleep(.5)
#     click(151, 971)

# need to run as administrator to click on screen keyboard
# pyautogui.click(151, 971)
# pyautogui.click(151, 971)
# pyautogui.click(151, 971)
alt_location = pyautogui.locateOnScreen('onscreenkeyboard/alt-key2.png')
print(alt_location)

pyautogui.click(alt_location)



