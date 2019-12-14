from features.operation import Operation
import utils.common_utils
from utils.string_utils import print_result
from utils.constants import OS
from errors.invalid_command import InvalidCommand
import subprocess


class Password(Operation):
    def __init__(self, wifi_name):
        self.wifi_name = wifi_name

    def __form_result_string(self, password):
        result_string = "Password for wifi " + \
            self.wifi_name + " is : " + str(password, 'utf-8')
        print_result(result_string)

    def __find_password(self):
        cmd = ['security']
        args = ['find-generic-password', '-wa', self.wifi_name]
        blocking_process = subprocess.Popen(cmd + args,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT)
        password, stderr = blocking_process.communicate()
        if (password == b''or stderr is not None):
            raise InvalidCommand()
        else:
            return password

    def operation(self) -> bool:
        operating_system = utils.common_utils.get_os()
        password = None
        if (operating_system == OS.mac):
            password = self.__find_password()
        self.__form_result_string(password)
        return True
