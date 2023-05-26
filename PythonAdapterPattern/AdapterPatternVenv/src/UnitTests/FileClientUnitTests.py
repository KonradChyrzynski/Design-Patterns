import unittest
from unittest.mock import patch
import os

from PythonAdapterPattern.AdapterPatternVenv.src.FileClient import FileClient


class FileClientTest(unittest.TestCase):
    def setUp(self):
        self.file_client = FileClient()


    def test_print_file_no_content(self):
        with patch('builtins.print') as mock_print:
            self.file_client.print_file()
            mock_print.assert_called_with("No file loaded.")

    def test_print_file_with_content(self):
        self.file_client.file_content = "Example content"
        with patch('builtins.print') as mock_print:
            self.file_client.print_file()
            mock_print.assert_called_with("Example content")

    def test_find_element_value_no_content(self):
        element_value = self.file_client.find_element_value("Element")
        self.assertIsNone(element_value)

    def test_find_element_value_with_content(self):
        self.file_client.file_content = "Element: Value"
        element_value = self.file_client.find_element_value("Element")
        self.assertEqual(element_value, "Element: Value")

    def test_find_element_value_not_found(self):
        self.file_client.file_content = "AnotherElement: Value"
        element_value = self.file_client.find_element_value("ElementNotFound")
        self.assertIsNone(element_value)

    def test_load_file_exists(self):
        with patch('builtins.open', create=True) as mock_open:
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.read.return_value = "File content"
            with patch('builtins.print') as mock_print:
                self.file_client.load_file(os.getcwd().replace("\\UnitTests", "\\Files\\existing_file.txt"))
                mock_print.assert_called_with('Loaded file: G:\\PythonScripts\\PythonAdapterPattern\\AdapterPatternVenv\\src\\Files\\existing_file.txt')
            self.assertEqual(self.file_client.file_content, "File content")

    def test_load_file_not_found(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            with patch('builtins.print') as mock_print:
                self.file_client.load_file(os.getcwd().replace("\\UnitTests", "\\Files\\nonexistent_file.txt"))
                mock_print.assert_called_with('File not found: G:\\PythonScripts\\PythonAdapterPattern\\AdapterPatternVenv\\src\\Files\\nonexistent_file.txt')
            self.assertIsNone(self.file_client.file_content)

if __name__ == '__main__':
    unittest.main()