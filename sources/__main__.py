__version__ = "0.0.1"

from commands.cli import CLIHandler
from utils import string_utils


def main():
    string_utils.base_print("\r\n" +
                            '====================================\r\n' +
                            ('             WiFy %s\r\n' % __version__) +
                            '====================================\r\n' +
                            '     (By james.bondu @ Github)\r\n')
    CLIHandler.commands()


if __name__ == "__main__":
    main()
