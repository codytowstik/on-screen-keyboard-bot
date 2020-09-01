import datetime


class MapleClericActions:
    """
    Actions specific to the cleric class path, like specific abilities.
    """

    def heal(self):
        pass

    def magic_guard(self, last_used_time: datetime.datetime):
        # check if current time is past last time for expiration
        pass