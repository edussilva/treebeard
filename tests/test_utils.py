import unittest

from treebeard.utils import tree_to_dict


class UtilsTestCases(unittest.TestCase):

    def test_tree_to_dict(self):
        expected = {
            "type": "directory",
            "name": "example",
            "children": [
                {
                    "type": "directory",
                    "name": "dict-a1",
                    "children": [
                        {
                            "type": "directory",
                            "name": "dict-b1",
                            "children": [
                                {
                                    "type": "file",
                                    "name": "file-c1"
                                }
                            ]
                        },
                        {
                            "type": "file",
                            "name": "file-b1"
                        }
                    ]
                },
                {
                    "type": "directory",
                    "name": "dict-a2",
                    "children": [
                        {
                            "type": "file",
                            "name": "file-b2"
                        }
                    ]
                },
                {
                    "type": "file",
                    "name": "file-a1"
                },
                {
                    "type": "file",
                    "name": "file-a2"
                }
            ]
        }
        self.assertEqual(tree_to_dict('example'), expected)
