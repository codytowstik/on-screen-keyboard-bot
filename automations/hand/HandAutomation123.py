from automations.HandAutomation import HandAutomation
from maple.MapleActionCleric import MapleActionCleric
from maple.MapleActionGeneral import MapleActionGeneral


class HandAutomation123(HandAutomation):
    def __init__(self):
        super().__init__(123)
        self._load()

    def _load(self):
        self._add(MapleActionCleric.HEAL)
        self._add(MapleActionCleric.HEAL)
        self._add(MapleActionGeneral.MOVE_LEFT)
        self._add(MapleActionGeneral.MOVE_LEFT)
