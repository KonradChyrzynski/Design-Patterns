from abc import ABCMeta, abstractmethod

class IYamlFile(metaclass=ABCMeta):

    @abstractmethod
    def print_yaml_file(self, filename):
        raise NotImplementedError()
    
    @abstractmethod
    def find_element_in_yaml(self, filename):
        raise NotImplementedError()
    
    @abstractmethod
    def load_yaml_file(self, filename):
        raise NotImplementedError()