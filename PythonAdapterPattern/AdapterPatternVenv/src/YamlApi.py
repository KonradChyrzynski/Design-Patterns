import yaml

from PythonAdapterPattern.AdapterPatternVenv.src.Interfaces import IYamlFile

class YamlApi(IYamlFile):

    def __init__(self):
        self.file = None

    def print_yaml_file(self, filename):
        print(self.load_yaml_file("configuration_yaml_9_0"))

    def update_yaml_file(self, element_name, filename):
        data = self.load_yaml_file(filename)

        # Update the YAML node
        if element_name in data:
            data[element_name] = "updated value"

        # Write the updated YAML back to the file
        with open(filename, "w") as file:
            yaml.safe_dump(data, file)

    def load_yaml_file(self, filename):
        with open(filename, "r") as file:
            data = yaml.safe_load(file)
            self.file = data
