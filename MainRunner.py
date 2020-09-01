import time

from ActionRecorder import ActionRecorder
from KeyActions import KeyActions
from KeyID import KeyID
from Logger import Logger

maple_logger = Logger()

maple_logger.info("MapleBot started, welcome!")
maple_logger.info("Please ensure this program is being 'Run as administrator...'"
                  " so that it can interact with the On Screen Keyboard.")

time.sleep(1)

user_input = input("Which action should be taken? 1: Record Action, 2: Run Action, 3: Debug Record Action, 4: Debug Run Action\n")

maple_logger.info("Running action {0}", user_input)

if user_input == "1":
    automation_tag = input("Choose an automation tag \n")
    action_recorder = ActionRecorder(automation_tag)

elif user_input == "2":
    pass

elif user_input == "3":
    pass

else:
    maple_logger.info(". . . . . . 2 seconds")
    time.sleep(2)

    key_actions = KeyActions()

    key_actions.pressAndHold(KeyID.C, 1)
    key_actions.pressAndHold(KeyID.O, 1)
    key_actions.pressAndHold(KeyID.DOWN, 0.2)
    key_actions.pressAndHold(KeyID.D, 1)
    key_actions.tap(KeyID.Y)

    key_actions.sayHello()

    key_actions.saySomethingRandom()

