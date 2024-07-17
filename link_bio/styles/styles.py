import reflex as rx
from enum import Enum

# Constants
MAX_WITDH = "560px"

# Sizes


class Size(Enum):

SMALL = "0.5em"
DEFAULT = "1em"
BIG = "2em"

# Styles
BASE_STYLE = {
  rx.Button: {
    "width":"100%",
    "height":"100%",
    "displa":"block",
    "padding": Size.SMALL.value,
    "border_radius": Size.DEFAULT.value
  }
}