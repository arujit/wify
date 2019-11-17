import argparse
import logging


class CLIHandler:
    logging.basicConfig(level=logging.INFO)
    _logger = logging.getLogger("CLIHandler")

    @classmethod
    def arguments(cls):
        parser = argparse.ArgumentParser(
            description="A helper for your wifi")
        parser.add_argument('-l', "--list",
                            help="Display a list functionalities.", action="store_true")
        parser.add_argument(
            '-v', "--version",  help="Print the current version and exit.", action="store_true")
        args, unknown_args = parser.parse_known_args()

    @classmethod
    def commands(cls):
        parser = cls.arguments()
        pass
