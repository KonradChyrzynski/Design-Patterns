import unittest
from unittest.mock import mock_open, patch
from io import StringIO

import yaml

from PythonAdapterPattern.AdapterPatternVenv.src.YamlClient import YamlClient


class TestYamlClient(unittest.TestCase):

    def setUp(self):
        self.yaml_client = YamlClient()

    def test_print_yaml_file(self):
        # Redirect print statements to a buffer
        with patch("sys.stdout", new=StringIO()) as output_buffer:
            # Set the file content
            self.yaml_client.file = yaml.dump(yaml.safe_load("age: 30\nname: John\n"))

            # Call the method
            self.yaml_client.print_yaml_file()

            # Check the printed output
            expected_output = yaml.dump("age: 30\nname: John\n")
            self.assertEqual(output_buffer.getvalue().strip(), expected_output.strip())

    def test_find_element_in_yaml(self):
        self.yaml_client.file = '''
        name: John
        address:
            city: New York
            state: NY
        phone_numbers:
            - "123456789"
            - "987654321"
        '''

        # Test finding an existing element
        result = self.yaml_client.find_element_in_yaml("address.city")
        self.assertEqual(result, "New York")

        # Test finding a non-existing element
        result = self.yaml_client.find_element_in_yaml("address.country")
        self.assertIsNone(result)

    def test_load_yaml_file(self):
        # Set up a mock for the open function
        with patch("builtins.open", mock_open(read_data='name: John')) as mock_file:
            filename = "test_file.yaml"
            self.yaml_client.load_yaml_file(filename)

            # Verify that the file is opened with the correct filename
            mock_file.assert_called_once_with(filename, "r")

            # Verify that the file content is loaded correctly
            expected_file_content = {"name": "John"}
            self.assertEqual(self.yaml_client.file, expected_file_content)


if __name__ == "__main__":
    unittest.main()
