from PythonAdapterPattern.AdapterPatternVenv.src.Interfaces.IFileClient import IFileClient


class YamlToFileClientAdapter(IFileClient):
    def __init__(self, _yaml_file_client):
        self.yaml_file_client = _yaml_file_client

    def print_file(self):
        self.yaml_file_client.print_yaml_file()

    def find_element_value(self, element_name):
        self.yaml_file_client.find_element_in_yaml(element_name)

    def load_file(self, file_name):
        self.yaml_file_client.load_yaml_file(file_name)
