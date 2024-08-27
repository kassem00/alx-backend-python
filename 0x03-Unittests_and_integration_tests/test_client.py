#!/usr/bin/env python3
"""
unit test for utils.access_nested_map.
"""
from unittest import unittest.TestCase
from utils import access_nested_map


class TestGithubOrgClient(unittest.TestCase):
    """ unit test for utils.access_nested_map. """


    def test_access_nested_map(self, nested_map, path, expected):
        """ test_access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
