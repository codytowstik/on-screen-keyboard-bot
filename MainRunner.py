import time

from KeyActions import KeyActions
from KeyID import KeyID
from Logger import Logger

maple_logger = Logger()

maple_logger.info("MapleBot started, welcome!")
maple_logger.info("Please ensure this program is being 'Run as administrator...'"
                  " so that it can interact with the On Screen Keyboard.")

maple_logger.info("Pausing for 5 seconds")
time.sleep(3)
maple_logger.info(". . . . . . 2 seconds")
time.sleep(2)

key_actions = KeyActions()

key_actions.pressAndHold(KeyID.C, 1)
key_actions.pressAndHold(KeyID.O, 1)
key_actions.pressAndHold(KeyID.DOWN, 0.2)
key_actions.pressAndHold(KeyID.D, 1)
key_actions.tap(KeyID.Y)
