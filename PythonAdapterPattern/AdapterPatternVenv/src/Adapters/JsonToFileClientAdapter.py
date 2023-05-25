from PythonAdapterPattern.AdapterPatternVenv.src.Interfaces import IFileClient


class JsonToFileClientAdapter(IFileClient):
    def __init__(self, _json_file_client):
        self.json_file_client = _json_file_client

    def print_file(self):
        self.json_file_client.print_json_file()

    def find_element_value(self, element_name):
        self.json_file_client.find_element_in_json(element_name)

    def load_file(self, file_name):
        self.json_file_client.load_json_file(file_name)
