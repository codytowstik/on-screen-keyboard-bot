from maple.MapleClass import MapleClass


class MapleChar:
    """
    Maple character base class for tracking non-class specific data like health, mana,
    potion count, current direction, etc.
    """

    def __init__(self, character_class: MapleClass):
        self.character_class = character_class

    def get_character_class(self):
        return self.character_class