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
        self.yaml_client.file = yaml.safe_load('''
        name: John
        city: Rio
        address:
            city: New York
            state: NY
        phone_numbers:
            - "123456789"
            - "987654321"
        ''')

        # Test finding an existing element
        result = self.yaml_client.find_element_in_yaml("city")
        self.assertEqual(result, ['Rio', 'New York'])

        # Test finding a non-existing element
        result = self.yaml_client.find_element_in_yaml("country")
        self.assertEqual(result, [])

    def test_find_element_in_yaml_docker_file(self):
        self.yaml_client.file = yaml.safe_load('''
            services:
              app:
                image: node:18-alpine
                command: sh -c "yarn install && yarn run dev"
                ports:
                  - 3000:3000
                working_dir: /app
                volumes:
                  - ./:/app
                environment:
                  MYSQL_HOST: mysql
                  MYSQL_USER: root
                  MYSQL_PASSWORD: secret
                  MYSQL_DB: todos

              mysql:
                image: mysql:8.0
                volumes:
                  - todo-mysql-data:/var/lib/mysql
                environment:
                  MYSQL_ROOT_PASSWORD: secret
                  MYSQL_DATABASE: todos

            volumes:
              todo-mysql-data:
            ''')

        # Test finding an existing element
        result = self.yaml_client.find_element_in_yaml("image")
        self.assertEqual(result, ['node:18-alpine', 'mysql:8.0'])
        print(result)

        # Test finding a non-existing element
        result = self.yaml_client.find_element_in_yaml("country")
        self.assertEqual(result, [])

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
