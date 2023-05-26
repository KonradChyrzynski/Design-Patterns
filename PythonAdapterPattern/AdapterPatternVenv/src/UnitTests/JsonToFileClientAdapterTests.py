import unittest
from io import StringIO
from unittest.mock import mock_open, patch

from PythonAdapterPattern.AdapterPatternVenv.src.Adapters.JsonToFileClientAdapter import JsonToFileClientAdapter
from PythonAdapterPattern.AdapterPatternVenv.src.JsonClient import JsonClient


class JsonToFileClientAdapterTests(unittest.TestCase):

    def setUp(self):
        self.json_to_file_client_adapter = JsonToFileClientAdapter(JsonClient())

    def test_print_json_file(self):
        # Redirect print statements to a buffer
        with patch("sys.stdout", new=StringIO()) as output_buffer:
            # Set the file content
            self.json_to_file_client_adapter.json_file_client.file = {"name": "John", "age": 30}

            # Call the method
            self.json_to_file_client_adapter.print_file()

            # Check the printed output
            expected_output = '{\n    "name": "John",\n    "age": 30\n}\n'
            self.assertEqual(output_buffer.getvalue(), expected_output)

    def test_find_element_in_json(self):
        # Set the file content
        self.json_to_file_client_adapter.json_file_client.file = {
            "name": "John",
            "address": {
                "city": "New York",
                "state": "NY"
            },
            "phone_numbers": [
                "123456789",
                "987654321"
            ]
        }

        # Test finding an existing element
        result = self.json_to_file_client_adapter.find_element_value("city")
        self.assertEqual(result, ["New York"])

        # Test finding a non-existing element
        result = self.json_to_file_client_adapter.find_element_value("country")
        self.assertEqual(result, [])

        # Test finding elements in an empty JSON file
        self.json_to_file_client_adapter.json_file_client.file = {}
        result = self.json_to_file_client_adapter.find_element_value("name")
        self.assertEqual(result, [])

    def test_load_json_file(self):
        # Set up a mock for the open function
        with patch("builtins.open", mock_open(read_data='{"name": "John"}')) as mock_file:
            file_name = "test_file.json"
            self.json_to_file_client_adapter.load_file(file_name)

            # Verify that the file is opened with the correct file_name
            mock_file.assert_called_once_with(file_name, "r")

            # Verify that the file content is loaded correctly
            expected_file_content = {"name": "John"}
            self.assertEqual(self.json_to_file_client_adapter.json_file_client.file, expected_file_content)


if __name__ == '__main__':
    unittest.main()
