from KeyActions import KeyActions
from KeyID import KeyID
from Logger import Logger
from Typings import MapleBuffTimer
from automations.hand.HandAutomation123 import HandAutomation123
from typing import List

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

    def __init__(self):
        # number of ticks that have passed
        self.automation_tick_count = 0

        # the loaded automation sequence
        self.loaded_automation_sequence: List[MapleAction] = []

        # track when buffs started
        self.buff_timers: MapleBuffTimer = {}

        # if automation is paused
        self.paused = False

    def run_automation(self, automation_id: int, loop=True) -> None:
        """
        Run the automation with the given id once or in a loop.

        :param automation_id: the automation id
        :param loop: true if automation should be looped
        :return:
        """
        self._load_automation(automation_id)

        self.maple_logger.info(
            "Starting automation with ID {0}, loop = {1}",
            automation_id,
            loop)

        while True:
            sequence_iterator = iter(self.loaded_automation_sequence)

            while action := next(sequence_iterator, None):
                current_action_key_id = action.value

                if not self._is_paused():
                    self._tick(current_action_key_id)

            if not loop:
                break

    def _load_automation(self, automation_id: int) -> None:
        """
        Load an automation based on the automation_id.
        """
        self.maple_logger.info("Loading automation with ID {0}.", automation_id)

        # TODO load the automation dynamically based on automation_id
        hand_automation = HandAutomation123()

        self.loaded_automation_sequence = hand_automation.get_automation_sequence()

        self.maple_logger.info("Loaded automation with {0} steps.", len(self.loaded_automation_sequence))

    def _tick(self, current_action_key_id: KeyID) -> None:
        self.key_actions.tap(current_action_key_id)

        self.automation_tick_count += 1

    def _is_paused(self) -> bool:
        """
        Check if there is currently a user input to toggle pause, toggle paused if so
        .. then check if the automation is currently paused.

        :return: true if paused
        """
        toggle_pause = self._check_for_toggle_pause_input()

        if toggle_pause:
            self.paused = not self.paused

        return self.paused

    def _check_for_toggle_pause_input(self) -> bool:
        """
        Check if the user is currently inputting the key to toggle pause.
        """
        return False

    def _get_expired_buffs(self) -> List:
        pass

    def _apply_expired_buffs(self) -> None:
        pass
