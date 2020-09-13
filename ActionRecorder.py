import json
import os
import pathlib
import sys
from datetime import datetime

from Logger import Logger


class ActionRecorder:
    """
    Records actions and adds them to a list of tuples until 'esc' key is pressed.
    The tuple consists of (button pressed, duration)
    """
    logger = Logger()

    AUTOMATION_DIRECTORY = "automation"
    AUTOMATION_BASE_FILENAME = "automation-"

    script_path = pathlib.Path(__file__).parent.absolute()
    automation_full_path = os.path.join(script_path, AUTOMATION_DIRECTORY)

    def __init__(self, automation_tag: str):
        self._check_for_existing_tag()

        # tag to be appended to the dumped automation sequence file
        self.automation_tag = automation_tag

        # list to store the recorded action sequence
        self.action_sequence = []

    def _check_for_existing_tag(self):
        pass

    def record_action_sequence(self):
        self.logger.info("Recording action sequence with tag {0}", self.automation_tag)

        # action_timer = None

        previous_input = None

        while True:
            current_input = self._check_current_input()

            # if stop recording button is pressed, dump action sequence to file
            if self._check_for_stop_recording(current_input):
                self._dump_recording_to_file()

            # if a new input is being pressed, start recording the timer for that input
            elif not previous_input and current_input:
                action_start_timer = datetime.now()
                previous_input = current_input

            # if a different input is being pressed, stop the timer for the previous_input
            # and add the action and time pressed to the sequence
            elif previous_input and current_input != previous_input:
                action_stop_timer = datetime.now()
                action_duration = (action_stop_timer - action_start_timer).total_seconds()
                self.action_sequence.append((previous_input, action_duration))

                # update previous input to the current input
                previous_input = current_input

    def _check_current_input(self):
        # return the current input, or None if nothing is being pressed
        pass

    def _check_for_stop_recording(self, current_input):
        pass

    def _check_for_pause_recording(self):
        pass

    def _check_for_continue_recording(self):
        pass

    def _dump_recording_to_file(self):
        automation_filename = os.path.join(self.automation_full_path,
                                           self.AUTOMATION_BASE_FILENAME + self.automation_tag)

        self.logger.info(
            "Dumping action sequence with tag {0} into file {1}",
            self.automation_tag,
            automation_filename)

        with open(automation_filename, mode="w") as file:
            json.dump(self.action_sequence, file)

        self.logger.info("Dumped successfully. Exiting.")

        sys.exit()
