from datetime import datetime
import random
import time

from KeyActions import KeyActions
from KeyID import KeyID
from Logger import Logger
from Typings import MapleBuffTimer
from UserInputReader import UserInputReader
from automations.AutomationTick import AutomationTick
from automations.hand.HandAutomation123 import HandAutomation123
from typing import List, Iterator

from maple.interfaces.MapleAction import MapleAction


class AutomationRunner:
    """
    Class to run automation based on ID. Runs in 'ticks' which executes the next action per tick, listening
    for user input to start, cancel, or pause the current automation sequence.

    This class can run an automation based off of a recording (from ./automations/recordings) or from a
    hand tailored automation (./automations/hand).
    """
    maple_logger = Logger()

    key_actions = KeyActions()

    # the minimum amount of time to wait between each tick
    TICK_TIME_BUFFER_SECONDS_MIN: float = 0.123

    # the key to listen for to pause the animation
    PAUSE_KEY = "p"
    START_KEY = "9"
    EXIT_KEY = "0"

    # the interval that nothing but PAUSE_KEY + space needs to be pressed within
    PAUSE_KEY_COMBO_TIMEOUT: float = 0.1

    def __init__(self):
        # number of ticks that have passed
        self.automation_tick_count = 0

        # the loaded automation sequence
        self.loaded_automation_sequence: List[AutomationTick] = []

        # track when buffs started
        self.buff_timers: MapleBuffTimer = {}

        # if automation is paused
        self.paused = False

        # if automation set to exit
        self.exited = False

        # create listeners for pausing and exiting automation
        UserInputReader.on_press_key(self.PAUSE_KEY, self._toggle_pause_callback)

        UserInputReader.on_press_key(self.EXIT_KEY, self._exit_automation)

    def _toggle_pause_callback(self, event):
        self.maple_logger.info("Toggling pause for automation. Paused = {0}", not self.paused)

        self.paused = not self.paused

    def _exit_automation(self, event):
        self.maple_logger.info("Exiting automation after current loop finishes.")
        self.exited = True

    def _wait_for_automation_start_key(self):
        UserInputReader.wait_for_key(self.START_KEY)

    def run_automation(self, automation_id: int, loop=True, loop_count=None) -> None:
        """
        Run the automation with the given id once or in a loop,
        looping the optionally specified number of times, otherwise forever.

        :param automation_id: the automation id
        :param loop: true if automation should be looped
        :param loop_count: the number of times to loop, loop forever if not set
        """
        self._load_automation(automation_id)

        self.maple_logger.info("Waiting for start key ({0}) to be pressed.", self.START_KEY)

        self._wait_for_automation_start_key()

        self.maple_logger.info(
            "Starting automation with ID {0}, loop = {1}, loop_count = {2}",
            automation_id,
            loop,
            loop_count)

        automation_start_time = datetime.now()

        while True:
            # if we are not looping, or if loop_count is specified and there are none remaining
            if self.exited or not loop or (loop_count is not None and loop_count == 0):
                automation_stop_time = datetime.now()
                automation_run_time_seconds = (automation_stop_time - automation_start_time).total_seconds()

                self.maple_logger.info("Automation finished, ran for {0} seconds.", automation_run_time_seconds)
                break

            else:
                loop_count = loop_count - 1 if loop_count else loop_count
                self._run_next_automation_sequence()

    def _load_automation(self, automation_id: int) -> None:
        """
        Load an automation based on the automation_id.
        """
        self.maple_logger.info("Loading automation with ID {0}.", automation_id)

        # TODO load the automation dynamically based on automation_id
        hand_automation = HandAutomation123()

        self.loaded_automation_sequence = hand_automation.get_automation_sequence()

        self.maple_logger.info("Loaded automation with {0} steps.", len(self.loaded_automation_sequence))

    def _run_next_automation_sequence(self) -> None:
        """
        Run the next loop of the loaded automation sequence
        .. only running the subsequent step if automation is not paused
        """
        sequence_iterator = iter(self.loaded_automation_sequence)

        while True:
            # sleep for a bit if we are paused to save resources
            if self.paused:
                time.sleep(0.1)

            else:
                sequence_finished = self._run_next_automation_action(sequence_iterator)

                if sequence_finished:
                    break

    def _run_next_automation_action(self, sequence_iterator: Iterator[AutomationTick]) -> bool:
        """
        Run the next action in the automation sequence.

        :param sequence_iterator: the automation sequence iterator
        :return: True if we have exhausted the sequence iterator
        """
        automation_tick = next(sequence_iterator, None)

        if not automation_tick:
            return True

        action = automation_tick.get_action()

        current_action_key_id: KeyID = action.value

        # sleep for a random amount of time between each tick
        time.sleep(self._get_tick_random_time_buffer())

        self._tick(current_action_key_id, automation_tick.get_duration())

        return False

    def _get_tick_random_time_buffer(self) -> float:
        buffer_time = self.TICK_TIME_BUFFER_SECONDS_MIN + random.uniform(0, 1)

        self.maple_logger.debug("Sleeping for {0} seconds.", buffer_time)

        return buffer_time

    def _tick(self, current_action_key_id: KeyID, duration: float) -> None:
        self.key_actions.pressAndHold(current_action_key_id, duration)

        self.automation_tick_count += 1

    def _get_expired_buffs(self) -> List:
        pass

    def _apply_expired_buffs(self) -> None:
        pass
