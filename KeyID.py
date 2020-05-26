from enum import Enum


class KeyID(Enum):
    """
    Mapping an enumerated value to the key name, which is expected to match the filename (without the extension).
    """
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    G = "g"
    H = "h"
    I = "i"
    K = "k"
    M = "m"
    N = "n"
    O = "o"
    S = "s"
    X = "x"
    Y = "y"
    Z = "z"

    ALT = "alt"
    CTRL = "ctrl"
    END = "end"
    ENTER = "enter"
    TAB = "tab"
    TILDE = "tilde"

    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    ONE = "1"
    TWO = "2"

    PAGE_UP = "pup"
    PAGE_DOWN = "pdn"
