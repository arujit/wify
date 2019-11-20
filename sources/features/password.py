from features.operation import Operation
import utils.other_utils


class Password(Operation):
    def __init__(self, wifi_name):
        self.wifi_name = wifi_name
        pass

    def __form_result_string(self, password):
        result_string = "Password for wifi " + self.wifi_name + " is " + password 
        pass

    def operation(self) -> bool:
        operating_system = utils.other_utils.get_os()
        
        return True
