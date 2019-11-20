import platform
import sys
from errors.no_command_found import NoCommandFound


def get_os():
    return platform.system()


def get_wifiname_in_command():
    if len(sys.argv) != 3:
        raise NoCommandFound()
    else:
        return sys.argv[2]
