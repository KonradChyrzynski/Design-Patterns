import unittest
from unittest.mock import MagicMock

from PythonAdapterPattern.AdapterPatternVenv.src.Adapters.YamlToFileClientAdapter import YamlToFileClientAdapter


class TestYamlToFileClientAdapter(unittest.TestCase):

    def setUp(self):
        self.yaml_file_client_mock = MagicMock()
        self.adapter = YamlToFileClientAdapter(self.yaml_file_client_mock)

    def test_print_file(self):
        self.adapter.print_file()
        self.yaml_file_client_mock.print_yaml_file.assert_called_once()

    def test_find_element_value(self):
        element_name = "city"
        self.adapter.find_element_value(element_name)
        self.yaml_file_client_mock.find_element_in_yaml.assert_called_once_with(element_name)

    def test_load_file(self):
        file_name = "test_file.yaml"
        self.adapter.load_file(file_name)
        self.yaml_file_client_mock.load_yaml_file.assert_called_once_with(file_name)


if __name__ == "__main__":
    unittest.main()
