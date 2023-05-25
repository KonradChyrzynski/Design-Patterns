from PythonAdapterPattern.AdapterPatternVenv.src.Interfaces import IFileClient


class YamlToFileClientAdapter(IFileClient):

    def __init__(self, _yaml_file):
        self.yaml_file = _yaml_file

    def print_file(self, filename):
        print(self.yaml_file.load_yaml_file(filename + ".yaml"))

    def update_file(self, element_name, filename):
        self.yaml_file.update_yaml_file(element_name, filename)
        pass

    def load_file(self, element_name):
        # Load YAML file implementation
        pass
