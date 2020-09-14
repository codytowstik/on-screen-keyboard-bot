import datetime
import os
import pathlib

import pyautogui

from Typings import KeyLocation, ScreenCoordinate
from Logger import Logger


class KeyLocationLoader:
    """
    Load all of the coordinates of the OSK keys into a dictionary key_locations. Loads from the directory
    specified in KEY_IMAGE_BASE_PATH. Looks for keys in the region of the OSK by first looking for
    a match for OSK_FILE_NAME.
    """
    KEY_IMAGE_BASE_PATH = "onscreenkeyboard"
    OSK_FILE_NAME = "onscreenkeyboard.png"

    script_path = pathlib.Path(__file__).parent.absolute()
    key_image_full_path = os.path.join(script_path, KEY_IMAGE_BASE_PATH)

    # maps the key name to the coordinates of it's location on screen
    # key name is loaded from the file name minus the extension
    key_locations: KeyLocation = {}

    maple_logger = Logger()

    def __init__(self):
        self.maple_logger.info("Initializing keys from path: {0}...", self.key_image_full_path)

        now = datetime.datetime.now()

        self.__getKeyboardRegion()
        self.__loadKeys()

        self.maple_logger.debug("Loaded keys in {0} seconds.", datetime.datetime.now() - now)

    def __getKeyboardRegion(self):
        keyboard_file_path = os.path.join(self.key_image_full_path, self.OSK_FILE_NAME)

        self.maple_logger.info("Loading keyboard at path: {0}", keyboard_file_path)

        self.keyboard_region = pyautogui.locateOnScreen(keyboard_file_path, confidence=0.9)

        if self.keyboard_region is None:
            self.maple_logger.warning(
                "Unable to find OSK keyboard. Ensure the OSK window is "
                "at the smallest size and screen resolution is at 1920x1080.")

            raise Exception("Unable to find OSK.")
        else:
            self.maple_logger.debug("Found keyboard at region: {0}", self.keyboard_region)

    def __loadKeys(self):
        """
        Load all of the key locations on the currently open On-Screen Keyboard (OSK), since finding them is expensive
        since it needs to scan the entire screen for a match (or a specified location, but ... whatever)
        """
        key_image_file_names = os.listdir(self.key_image_full_path)

        self.maple_logger.info("Loading {0} keys.", len(key_image_file_names))

        for key_image_file_name in key_image_file_names:
            self.__loadKey(key_image_file_name)

    def __loadKey(self, key_image_file_name: str):
        """
        Load key into our key_locations dictionary.
        :param key_image_file_name: the key image file name (should match the file name e.g. ${key_name}.png)
        """
        # get the key name from the file name e.g. ${key_name}.png
        key_name = key_image_file_name.split('.')[0]

        self.maple_logger.debug("Loading key: {0}", key_name)

        self.key_locations[key_name] = self.__getKeyLocation(key_image_file_name)

    def __getKeyLocation(self, key_image_file_name: str) -> ScreenCoordinate:
        key_file_path = os.path.join(self.key_image_full_path, key_image_file_name)

        self.maple_logger.debug("Looking in path {0}", key_file_path)

        key_location = pyautogui.locateOnScreen(key_file_path, region=self.keyboard_region, confidence=0.9)

        if key_location is None:
            self.maple_logger.warning("Unable to find key {0}", key_image_file_name)
        else:
            self.maple_logger.debug("Found at coord: {0}", key_location)

        return key_location

    def getKeyLocation(self, key_name: str) -> ScreenCoordinate:
        return self.key_locations[key_name]
