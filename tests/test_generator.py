import unittest
import os

from treebeard.generator import generate_json


class JsonGeneratorTestCases(unittest.TestCase):

    def setUp(self):
        self.json_file = generate_json('example')

    def test_generate_json_create_a_json_file(self):
        filename, extension = os.path.splitext(self.json_file.name)
        self.assertEqual(extension, '.json')

    def test_generate_json_create_file_in_root_path(self):
        self.assertIn(self.json_file.name, os.listdir())
