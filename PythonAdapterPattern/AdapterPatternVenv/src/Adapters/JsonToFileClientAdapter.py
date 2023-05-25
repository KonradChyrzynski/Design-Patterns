from PythonAdapterPattern.AdapterPatternVenv.src.Interfaces import IFileClient


class JsonToFileClientAdapter(IFileClient):
    def __init__(self, jsonFile):
        self.json_file = jsonFile

    def print_file(self):
        print(self.json_file)

    def find_element_value(self, element_name, filename):
        # Update JSON file implementation
        self.json_file.upadte_json_file(element_name)
        pass

    def load_file(self, filename):
        self.json_file.load_json_file(filename)
        pass
