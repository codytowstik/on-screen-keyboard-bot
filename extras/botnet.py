import win32gui
import win32con
import win32api
from time import sleep

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def getCursorPos():
    cursor_pos = win32api.GetCursorPos()

click(10,10)
# getCursorPos()

# print existing windows

search_key = "MapleRoyals"

# def winEnumHandler( hwnd, ctx ):
#     if win32gui.IsWindowVisible( hwnd ):
#         print (hex(hwnd), win32gui.GetWindowText( hwnd ))

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        window_text = win32gui.GetWindowText( hwnd )

        if window_text == search_key:
            global hwndChild
            hwndChild = hwnd

win32gui.EnumWindows( winEnumHandler, None )

#[hwnd] No matter what people tell you, this is the handle meaning unique ID,
#["Notepad"] This is the application main/parent name, an easy way to check for examples is in Task Manager
#["test - Notepad"] This is the application sub/child name, an easy way to check for examples is in Task Manager clicking dropdown arrow
#hwndMain = win32gui.FindWindow("Notepad", "test - Notepad") this returns the main/parent Unique ID
# hwndMain = win32gui.FindWindow("Notepad", "Untitled - Notepad")

#["hwndMain"] this is the main/parent Unique ID used to get the sub/child Unique ID
#[win32con.GW_CHILD] I havent tested it full, but this DOES get a sub/child Unique ID, if there are multiple you'd have too loop through it, or look for other documention, or i may edit this at some point ;)
#hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD) this returns the sub/child Unique ID
# hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)

# print(hwndMain) #you can use this to see main/parent Unique ID
print(hwndChild)  #you can use this to see sub/child Unique ID

#While(True) Will always run and continue to run indefinitely
while(True):
    #[hwndChild] this is the Unique ID of the sub/child application/proccess
    #[win32con.WM_CHAR] This sets what PostMessage Expects for input theres KeyDown and KeyUp as well
    #[0x44] hex code for D
    #[0]No clue, good luck!
    #temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x44, 0) returns key sent
    temp = win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x44, 0)

    #print(temp) prints the returned value of temp, into the console

    print(temp)
    #sleep(1) this waits 1 second before looping through again
    sleep(1)