from enum import Enum

from KeyID import KeyID
from maple.interfaces.MapleAction import MapleAction


class MapleActionCleric(MapleAction):
    HEAL = KeyID.A
    MAGIC_GUARD = KeyID.PAGE_DOWN
