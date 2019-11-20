from features.operation import Operation
from utils import constants
from utils import string_utils

class Version(Operation):
    def __init__(self):
        pass

    def operation(self) -> bool:
        result_string = "wifi, version : " + constants.VERSION
        string_utils
        return True
