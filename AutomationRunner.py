from maple.MapleClass import MapleClass


class AutomationRunner:
    """
    Class to run automation based on ID. Runs in 'ticks' which executes the next action per tick, listening
    for user input to start, cancel, or pause the current automation sequence.
    """

    def __init__(self):
        # number of ticks that have passed
        self.automation_tick_count = 0

        # the loaded automation sequence
        self.loaded_automation = []

        # track when buffs started
        self.buff_timers = {}

    def run_automation(self, automation_id: int, loop = True) -> None:
        pass

    def _load_automation(self):
        pass

    def _tick(self):
        pass

    def _check_user_input(self):
        pass

    def _check_buffs(self, character_class: MapleClass):
        pass


