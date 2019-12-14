import platform
import sys
from errors.no_command_found import NoCommandFound


def get_os():
    return platform.system()


def get_wifiname_in_command():
    if len(sys.argv) != 3:
        return None
    else:
        return sys.argv[2]

def string_from_bytes(stdout) -> str:
    return str(stdout, 'utf-8')
