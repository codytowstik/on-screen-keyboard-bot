import datetime
import os
import pathlib

import pyautogui

from Typings import KeyLocation, ScreenCoordinate
from Logger import Logger


class Keys:
    maple_logger = Logger()
    key_image_base_path = "onscreenkeyboard"
    script_path = pathlib.Path(__file__).parent.absolute()
    key_image_full_path = os.path.join(script_path, key_image_base_path)

    key_locations: KeyLocation = {}

    def __init__(self):
        self.maple_logger.info("Initializing keys from path: {0}...", self.key_image_full_path)

        now = datetime.datetime.now()

        self.__getKeyboardRegion()
        self.__loadKeys()

        self.maple_logger.debug("Loaded keys in {0} seconds.", datetime.datetime.now() - now)

    def __getKeyboardRegion(self):
        keyboard_file_path = os.path.join(self.key_image_full_path, "onscreenkeyboard.png")

        self.maple_logger.info("Loading keyboard at path: {0}", keyboard_file_path)

        self.keyboard_region = pyautogui.locateOnScreen(keyboard_file_path, confidence=0.9, grayscale=True)

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

    def __loadKey(self, key_image_file_name: str) -> None:
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

        key_location = pyautogui.locateOnScreen(key_file_path, region=self.keyboard_region, confidence=0.8)

        if key_location is None:
            self.maple_logger.warning("Unable to find key {0}", key_image_file_name)
        else:
            self.maple_logger.debug("Found at coord: {0}", key_location)

        return key_location


my_keys = Keys()