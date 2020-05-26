import pyautogui
import time


# TODO:
    # Selling function


def active_window():
    '''
    Make maplelegends the active window
    '''
    print("Finding MapleLegends Window...")

    try:
        maple_window = pyautogui.getWindowsWithTitle("MapleRoyals")[0]
        print("MapleLegends Window Found...")
    except:
        print("Cannot Find MapleLegends Window... Program Terminating")
        exit(1)

    print("MapleLegends Window Activation Successful")

def get_window_coordinates():
    maple_window = pyautogui.getWindowsWithTitle("MapleRoyals")[0]
    return maple_window.box

active_window() # Activates MapleLegends window
maple_window_box = get_window_coordinates()

print(maple_window_box)

time.sleep(3)
pyautogui.press("a")

pyautogui.click