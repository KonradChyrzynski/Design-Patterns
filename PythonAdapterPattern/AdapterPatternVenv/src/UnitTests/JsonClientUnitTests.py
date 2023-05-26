import unittest
from io import StringIO
from unittest.mock import mock_open, patch
from PythonAdapterPattern.AdapterPatternVenv.src.JsonClient import JsonClient

class TestJsonClient(unittest.TestCase):

    def setUp(self):
        self.json_client = JsonClient()

    def test_print_json_file(self):
        # Redirect print statements to a buffer
        with patch("sys.stdout", new=StringIO()) as output_buffer:
            # Set the file content
            self.json_client.file = {"name": "John", "age": 30}

            # Call the method
            self.json_client.print_json_file()

            # Check the printed output
            expected_output = '{\n    "name": "John",\n    "age": 30\n}\n'
            self.assertEqual(output_buffer.getvalue(), expected_output)

    def test_find_element_in_json(self):
        # Set the file content
        self.json_client.file = {
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
        result = self.json_client.find_element_in_json("city")
        self.assertEqual(result, ["New York"])

        # Test finding a non-existing element
        result = self.json_client.find_element_in_json("country")
        self.assertEqual(result, [])

        # Test finding elements in an empty JSON file
        self.json_client.file = {}
        result = self.json_client.find_element_in_json("name")
        self.assertEqual(result, [])

    def test_load_json_file(self):
        # Set up a mock for the open function
        with patch("builtins.open", mock_open(read_data='{"name": "John"}')) as mock_file:
            file_name = "test_file.json"
            self.json_client.load_json_file(file_name)

            # Verify that the file is opened with the correct file_name
            mock_file.assert_called_once_with(file_name, "r")

            # Verify that the file content is loaded correctly
            expected_file_content = {"name": "John"}
            self.assertEqual(self.json_client.file, expected_file_content)


if __name__ == "__main__":
    unittest.main()
