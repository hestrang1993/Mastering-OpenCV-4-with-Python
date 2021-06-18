"""
The :mod:`color_constants` module contains tuples for the most commonly used colors (in BGR color space).
It also contains a dictionary that lists these colors as :obj:`str` : :obj:`tuple(int, int, int)`.
"""

from numpy.random import randint

# Key variables
VALUE_MIN = 0
"""
int: The minimum value any channel can be.

By default, this will be 0.
"""
VALUE_MAX = 255
"""
int: The maximum value any channel can be.

By default, this will be 255.
"""
TUPLE_SIZE = 3
"""
int: The number of color spaces in the RANDOM color.

By default, this will be 3.
"""
RANDOM = randint(VALUE_MIN, high = VALUE_MAX, size = (TUPLE_SIZE,)).tolist()
"""
tuple[int, int, int]: A random color in BGR color space.

Any channel in the color space can be a value :math:`x`, where:

.. math::
    0 \leq x \leq 255
"""
BLUE = (VALUE_MAX, VALUE_MIN, VALUE_MIN)
"""
tuple[int, int, int]: The color blue in BGR color space.

This will be (255, 0, 0).
"""
GREEN = (VALUE_MIN, VALUE_MAX, VALUE_MIN)
"""
tuple[int, int, int]: The color green in BGR color space.

This will be (0, 255, 0).
"""
RED = (VALUE_MIN, VALUE_MIN, VALUE_MAX)
"""
tuple[int, int, int]: The color red in BGR color space.

This will be (0, 0, 255).
"""
YELLOW = (VALUE_MIN, VALUE_MAX, VALUE_MAX)
"""
tuple[int, int, int]: The color yellow in BGR color space.

This will be (0, 255, 255).
"""
MAGENTA = (VALUE_MAX, VALUE_MIN, VALUE_MAX)
"""
tuple[int, int, int]: The color magenta in BGR color space.

This will be (255, 0, 255).
"""
CYAN = (VALUE_MAX, VALUE_MAX, VALUE_MIN)
"""
tuple[int, int, int]: The color magenta in BGR color space.

This will be (255, 255, 0).
"""
WHITE = (VALUE_MAX, VALUE_MAX, VALUE_MAX)
"""
tuple[int, int, int]: The color white in BGR color space.

This will be (255, 255, 255)
"""
BLACK = (VALUE_MIN, VALUE_MIN, VALUE_MIN)
"""
tuple[int, int, int]: The color black in BGR color space.

This will be (0, 0, 0)
"""
COLOR_DICTIONARY = {
        "blue": BLUE,
        "green": GREEN,
        "red": RED,
        "yellow": YELLOW,
        "cyan": CYAN,
        "magenta": MAGENTA,
        "white": WHITE,
        "black": BLACK
}
"""
dict[str: (int, int, int)]: A dictionary of the most common colors in BGR color space.
"""
