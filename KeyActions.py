import time

from KeyLocationLoader import KeyLocationLoader
from KeyID import KeyID

import pyautogui


class KeyActions:
    """
    Actions for interacting with the On-Screen Keyboard (OSK).
    """
    loaded_keys = KeyLocationLoader()

    def pressAndHold(self, key_name: KeyID, hold_length_seconds):
        key_location = self.loaded_keys.getKeyLocation(key_name.value)

        pyautogui.mouseDown(key_location)
        time.sleep(hold_length_seconds)
        pyautogui.mouseUp()

    def tap(self, key_name: KeyID):
        self.pressAndHold(key_name, 0)
