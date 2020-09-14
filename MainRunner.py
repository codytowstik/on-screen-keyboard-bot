import time

from ActionRecorder import ActionRecorder
from AutomationRunner import AutomationRunner
from KeyActions import KeyActions
from KeyID import KeyID
from Logger import Logger

maple_logger = Logger()

maple_logger.info("MapleBot started, welcome!")
maple_logger.info("Please ensure this program is being 'Run as administrator...'"
                  " so that it can interact with the On Screen Keyboard.")

time.sleep(1)

# user_input = input("Which action should be taken? 1: Record Action, 2: Run Action, 3: Debug Record Action, 4: Debug Run Action\n")
user_input = "2"

maple_logger.info("Running action {0}", user_input)

# 1. Record action
if user_input == "1":
    automation_tag = input("Choose an automation tag \n")
    action_recorder = ActionRecorder(automation_tag)

    action_recorder.record_action_sequence()

# 2. Run Action
elif user_input == "2":
    time.sleep(3)
    automation_runner = AutomationRunner()

    # run automation once
    automation_runner.run_automation(123, False)

# 3. Debug Record Action
elif user_input == "3":
    pass

# 4. Debug Run Action
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


maple_logger.info("Terminated.")