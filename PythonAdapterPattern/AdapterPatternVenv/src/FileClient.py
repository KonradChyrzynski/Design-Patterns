from PythonAdapterPattern.AdapterPatternVenv.src.Interfaces.IFileClient import IFileClient


class FileClient(IFileClient):

    def __init__(self):
        self.file_content = None

    def print_file(self):
        if self.file_content is not None:
            print(self.file_content)
        else:
            print("No file loaded.")

    def find_element_value(self, element_name):
        if self.file_content is not None:
            return self._find_element_value(element_name)
        else:
            return None

    def load_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.file_content = file.read()
            print(f"Loaded file: {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            self.file_content = None

    def _find_element_value(self, element_name):
        lines = self.file_content.split('\n')
        for line in lines:
            if element_name in line:
                return line.strip()
        return None
