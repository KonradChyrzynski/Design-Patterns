import yaml

from PythonAdapterPattern.AdapterPatternVenv.src.Interfaces.IYamlFile import IYamlFile


class YamlClient(IYamlFile):

    def __init__(self):
        self.file = None

    def print_yaml_file(self):
        print(yaml.dump(self.file))

    def find_element_in_yaml(self, element_key):
        if self.file is None:
            raise ValueError("No YAML file loaded.")

        return None

    def load_yaml_file(self, element_key):
        with open(element_key, "r") as file:
            data = yaml.safe_load(file)
            self.file = data
