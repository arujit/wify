from abc import abstractmethod


class Operation:
    @abstractmethod
    def operation(self) -> bool:
        pass