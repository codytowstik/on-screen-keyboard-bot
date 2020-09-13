from typing import Dict, Tuple

from maple.interfaces.MapleBuff import MapleBuff

ScreenCoordinate = Tuple[str, str]
KeyLocation = Dict[str, ScreenCoordinate]

MapleBuffTimer = Dict[MapleBuff, float]