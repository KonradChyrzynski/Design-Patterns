from PythonAdapterPattern.AdapterPatternVenv.src.Interfaces import IFileClient


class JsonToFileClientAdapter(IFileClient):
    def __init__(self, json_file):
        self.json_file = json_file

    def print_file(self):
        print(self.json_file)

    def find_element_value(self, element_name, filename):
        # Update JSON file implementation
        self.json_file.upadte_json_file(element_name)
        pass

    def load_file(self, file_name):
        self.json_file.load_json_file(file_name)
        pass
