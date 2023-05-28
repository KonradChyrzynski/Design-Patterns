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

        values = []
        self._find_element_recursive(self.file, element_key, values)

        return values

    def _find_element_recursive(self, data, element_key, values):
        if isinstance(data, dict):
            if element_key in data:
                values.append(data[element_key])
            for value in data.values():
                self._find_element_recursive(value, element_key, values)
        elif isinstance(data, list):
            for item in data:
                self._find_element_recursive(item, element_key, values)

    def load_yaml_file(self, element_key):
        with open(element_key, "r") as file:
            data = yaml.safe_load(file)
            self.file = data
