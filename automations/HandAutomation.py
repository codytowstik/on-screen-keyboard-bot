from abc import ABC
from typing import List

from maple.interfaces.MapleAction import MapleAction
from Logger import Logger

class HandAutomation(ABC):
    maple_logger = Logger()

    def __init__(self, automation_id: int):
        self.automation_id = automation_id
        self.automation_sequence: List[MapleAction] = []

    def _add(self, action: MapleAction) -> None:
        self.maple_logger.debug(
            "Adding {0}, which maps to {1}",
            action.name,
            action.value)

        self.automation_sequence.append(action.value)

    @abstractmethod
    def _load(self):
        pass

    def get_automation_sequence(self) -> List[MapleAction]:
        return self.automation_sequence