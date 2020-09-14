import time
from typing import Callable

import keyboard


class UserInputReader:
	most_recently_pressed_key = None

	@staticmethod
	def get_user_input_blocking() -> str:
		"""
		Get user input, blocks until a key is pressed.

		:return: the pressed key.
		"""
		return keyboard.read_key()

	@staticmethod
	def listen_for_key(key: str, callback: Callable, timeout=0.1) -> None:
		"""
		Listen for the specified key being pressed and space
		.. invokes the given callback when that happens.
		e.g. press "p" plus space

		Nothing but key + space must have been pressed within the interval to invoke callback.

		:param key: the key to listen for (can be a sequence of characters)
		:param callback: the callback to invoke on key combo press
		"""
		# key + space must be pressed within 0.1 second interval
		keyboard.add_word_listener(key, callback, timeout=timeout)

	@staticmethod
	def key_pressed():
		"""
		Print that a key is pressed, for use as a test callback for listen_for_key.
		"""
		print("Pressed")