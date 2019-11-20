from colorama import Fore, Style, init
import sys
from utils.constants import Colours


def base_print(string_output, end='\n'):
    colour = Colours.yellow
    string_output = "%s%s" % (colour+Style.BRIGHT, string_output) + end
    sys.stdout.write(string_output)


def print_result(string_output, end='\n'):
    colour = Colours.green
    string_output = "%s%s" % (colour+Style.BRIGHT, string_output) + end
    sys.stdout.write(string_output)

def print_error(string_error, end='\n'):
    colour = Colours.red
    string_output = "%s%s" % (colour+Style.BRIGHT, string_error) + end
    sys.stdout.write(string_output)
