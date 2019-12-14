from features.operation import Operation
import utils.common_utils
from utils.string_utils import print_result
from utils.common_utils import string_from_bytes
from utils.constants import OS
from errors.invalid_command import InvalidCommand
import subprocess


class Current(Operation):
    def __init__(self):
        pass

    def __form_result_string(self, current_network):
        result_string = "Current Connected Wifi network is : " + current_network
        print_result(result_string)

    @classmethod
    def find_current_network(self):
        cmd = ['networksetup']
        args = ['-getairportnetwork', 'en0']
        blocking_process = subprocess.Popen(cmd + args,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT)
        stdout, stderr = blocking_process.communicate()
        string_out = string_from_bytes(stdout)
        if ('Error' in string_out or stderr is not None):
            raise InvalidCommand()
        else:
            current_network = string_out.split(" ")[-1].strip('\n')
            return current_network

    def operation(self) -> bool:
        operating_system = utils.common_utils.get_os()
        current_network = None
        if (operating_system == OS.mac):
            current_network = self.find_current_network()
        self.__form_result_string(current_network)
        return True
