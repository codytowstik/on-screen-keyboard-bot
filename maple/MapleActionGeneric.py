from maple.interfaces.MapleAction import MapleAction


class MapleActionGeneric(MapleAction):
    """
    Actions that are non-class specific that can be done within the Maplestory client.
    """
    def quitGame(self):
        pass

    def login(self):
        pass

    def enterPIC(self):
        pass

    def enterSecurityPin(self):
        pass

    def enterExitCashShop(self):
        pass

    def changeChannels(self, channel_number: int):
        pass

    def openInventory(self):
        pass

    def dropItem(self):
        pass

    def useItem(self):
        pass

    def lootItems(self):
        pass

    def addAP(self):
        pass

    def addSP(self):
        pass

    def jump(self):
        pass
