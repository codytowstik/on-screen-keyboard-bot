
class ActionRecorder:
    """
    Records actions and adds them to a list of tuples until 'esc' key is pressed.
    The tuple consists of (button pressed, duration)
    """
    AUTOMATION_DIRECTORY = "hello"
    AUTOMATION_BASE_FILENAME = "world"
    # script_path = pathlib.Path(__file__).parent.absolute()
    # key_image_full_path = os.path.join(script_path, KEY_IMAGE_BASE_PATH)

    def __init__(self, automation_tag: str):
        self.automation_tag = automation_tag

    def record_action_sequence(self):
        pass

    def _check_for_stop_recording(self):
        pass

    def dump_recording_to_file(self):
        pass