from pprint import pformat
from colorama import Fore, Style, init
import sys


_special_colors = {
    'red': Fore.RED,
    'blue': Fore.BLUE,
    'cyan': Fore.CYAN,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'magenta': Fore.MAGENTA
}


def print_color(colour, string_output, end='\n'):
    if colour.lower() in _special_colors:
        colour = _special_colors[colour]
    string_output = "%s%s" % (colour+Style.BRIGHT, string_output) + end
    sys.stdout.write(string_output)
