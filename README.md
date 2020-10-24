# On-Screen Keyboard Bot

If you are looking for a bot to do automated tasks for you, usually you can utilize
a tool like Python's `keyboard` module, or a similar library, package, or module in
your language of choice.

*Unfortunately*, many games that have a desktop client will register a hook that swallows
all keyboard events. Therefore, utilities that rely on sending hooks like `KEYDOWN` for input
cannot be used.

This **On-Screen Keyboard Bot** works around this issue by utilizing Window's native
On-Screen Keyboard to send native keyboard inputs that games can't distinguish between
human input.

> Warning: This software is under active development.

## Note

This bot was created for an old 2D scroller I used to play called Maplestory so the file names
and current implementation is tailored to that. Care has been taken to make the core files
be extensible to other games and inputs, which you can look forward to later!

## Limitations

- The images used to search for the keys on the On-Screen Keyboard (OSK)
have a resolution of `1080P` so you may have to set your screen resolution
to `1080P` for detection

- Only one key can be pressed at one time

## Usage

### Setup

> Active development: Only `HandAutomation123.py` is run.

- Create an automation file in the `automations/hand` directory. Use `HandAutomation123.py`
as a template.

- Add actions that you want to be run in the new file. Using `HandAutomation123.py` as reference,
you can see that the action names are mapped to the keys in `MapleActionCleric.py`, but you can
create any mapping you want with a new class that inherits from `MapleAction`.

### Execute Automations

1. Run the program as Administrator (so Windows registers clicks on the OSK)
using `MainRunner.py`

2. If detection of the OSK was successful, you should see logging output telling you so.

3. Once your automation is loaded, you will be prompted to press the "start" key - currently `9`.
Press start once the software you want to input to work on is in focus.

4. To pause the automation, press `p`, to exit press `0`


