from abc import ABCMeta, abstractmethod


class IJsonFile(metaclass=ABCMeta):

    @abstractmethod
    def load_json_file(self, file_name):
        raise NotImplementedError("load_yaml_file method not implemented")

    @abstractmethod
    def find_element_in_json(self, element):
        raise NotImplementedError("find_element_in_json method not implemented")

    @abstractmethod
    def print_json_file(self):
        raise NotImplementedError("print_json_file method not implemented")
