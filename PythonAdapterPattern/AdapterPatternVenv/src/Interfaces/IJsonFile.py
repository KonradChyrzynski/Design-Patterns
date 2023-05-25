from abc import ABCMeta, abstractmethod

class IJsonFile(metaclass=ABCMeta):

    @abstractmethod
    def load_json_file(self, filename):
        raise NotImplementedError("load_yaml_file method not implemented")
        
    def find_element_in_json(element):
        raise NotImplementedError("find_element_in_json method not implemented")
        
    def print_json_file():
        raise NotImplementedError("print_json_file method not implemented")