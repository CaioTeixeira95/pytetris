from typing import NamedTuple
from enum import Enum


class Color(NamedTuple):
    red: int
    green: int
    blue: int


class Colors(Enum):
    DARK_GREY = Color(26, 31, 40)
    GREEN = Color(47, 230, 23)
    RED = Color(232, 18, 18)
    ORANGE = Color(226, 116, 17)
    YELLOW = Color(237, 234, 4)
    PURPLE = Color(166, 0, 247)
    CYAN = Color(21, 204, 209)
    BLUE = Color(13, 64, 216)
    WHITE = Color(255, 255, 255)
    DARK_BLUE = Color(44, 44, 127)
    LIGHT_BLUE = Color(59, 85, 162)

    @classmethod
    def get_cell_colors(cls) -> tuple[Color]:
        return (
            cls.DARK_GREY.value,
            cls.GREEN.value,
            cls.RED.value,
            cls.ORANGE.value,
            cls.YELLOW.value,
            cls.PURPLE.value,
            cls.CYAN.value,
            cls.BLUE.value,
        )
