from enum import Enum

from KeyID import KeyID
from maple.interfaces.MapleAction import MapleAction


class MapleActionGeneral(Enum, MapleAction):
    MOVE_LEFT = KeyID.LEFT
    MOVE_RIGHT = KeyID.RIGHT
    MOVE_DOWN = KeyID.DOWN
    MOVE_UP = KeyID.UP

    JUMP = KeyID.ALT
    # JUMP_RIGHT = KeyID.ALT, KeyID.RIGHT
