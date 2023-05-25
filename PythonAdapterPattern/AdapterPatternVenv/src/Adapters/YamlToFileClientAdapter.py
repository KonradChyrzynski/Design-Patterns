from PythonAdapterPattern.AdapterPatternVenv.src.Interfaces import IFileClient


class YamlToFileClientAdapter(IFileClient):

    def __init__(self, _yaml_file):
        self.yaml_file = _yaml_file

    def print_file(self):
        self.yaml_file.print_yaml_file()

    def find_element_value(self, element_name):
        self.yaml_file.find_element_in_yaml(element_name)
        pass

    def load_file(self, file_name):
        self.yaml_file.load_yaml_file(file_name)
        pass
