import argparse
import logging
import sys
from utils import string_utils
from utils import constants
from utils import common_utils
import sys
from features.password import Password
from features.version import Version
from features.list import ListConnections
from features.speed_test import Speed
from features.connect import Connect
from errors.no_command_found import NoCommandFound


class CLIHandler:
    logging.basicConfig(level=logging.INFO)
    _logger = logging.getLogger("CLIHandler")

    @classmethod
    def arguments(cls):
        parser = argparse.ArgumentParser(
            description="A helper for your wifi")
        parser.add_argument(
            '-v', "--version", help="Print the current version and exit.", action="store_true")
        parser.add_argument('-l', "--list",
                            help="Display list available wifi.", action="store_true")
        parser.add_argument(
            '-c', "--connect", help="Connect to your desired wifi.", action="store_true")
        parser.add_argument(
            '-p', "--password", help="Password of the given network", action="store_true")
        parser.add_argument(
            '-s', "--speed", help="Speed test.", action="store_true")
        return parser

    @classmethod
    def commands(cls):
        parser = cls.arguments()
        arguments, unknown_args = parser.parse_known_args()
        operation = None
        # add features here
        try:
            if arguments.version:
                operation = Version()
                pass

            elif arguments.list:
                operation = ListConnections()
                pass

            elif arguments.connect:
                wifi_name = common_utils.get_wifiname_in_command()
                operation = Connect()
                pass

            elif arguments.password:
                wifi_name = common_utils.get_wifiname_in_command()
                operation = Password(wifi_name)
                pass

            elif arguments.speed:
                operation = Speed()
                pass

            else:
                raise NoCommandFound()

            result_status = operation.operation()
            if not result_status:
                raise NoCommandFound()

        except:
            string_utils.print_error("invalid command")
