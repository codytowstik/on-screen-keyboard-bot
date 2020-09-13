from enum import Enum

from KeyID import KeyID


class MapleKeybindingsCleric(Enum):
    # (KeyID, timer?)
    HEAL = KeyID.A,
    MAGIC_GUARD = (KeyID.PAGE_DOWN, 10)
