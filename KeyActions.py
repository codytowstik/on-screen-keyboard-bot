import time

from KeyLocationLoader import KeyLocationLoader
from KeyID import KeyID
from Logger import Logger

import pyautogui


class KeyActions:
    """
    Actions for interacting with the On-Screen Keyboard (OSK).
    """
    maple_logger = Logger()

    # pre-load all the key locations so we don't have to constantly find them (expensive!)
    _loaded_keys = KeyLocationLoader()

    def pressAndHold(self, key_name: KeyID, hold_length_seconds: float):
        key_location = self._loaded_keys.getKeyLocation(key_name.value)

        self.maple_logger.debug("Found key ({0}) at location {1}, pressing for {2} seconds.")

        pyautogui.mouseDown(key_location)
        time.sleep(hold_length_seconds)
        pyautogui.mouseUp()

    def tap(self, key_name: KeyID):
        self.pressAndHold(key_name, 0)
