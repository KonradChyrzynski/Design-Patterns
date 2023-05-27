from abc import ABCMeta, abstractmethod


class IFileClient(metaclass=ABCMeta):

    @abstractmethod
    def print_file(self):
        raise NotImplementedError("print_file method not implemented")

    @abstractmethod
    def find_element_value(self, element_name):
        raise NotImplementedError("update_file method not implemented")

    @abstractmethod
    def load_file(self, file_path):
        raise NotImplementedError("load_file method not implemented")
