from abc import ABCMeta, abstractmethod


class IFileClient(metaclass=ABCMeta):

    @abstractmethod
    def load_file(self, element_name):
        raise NotImplementedError("load_file method not implemented")

    @abstractmethod
    def print_file(self, file_name):
        raise NotImplementedError("print_file method not implemented")

    @abstractmethod
    def find_element_value(self, element_name):
        raise NotImplementedError("update_file method not implemented")
