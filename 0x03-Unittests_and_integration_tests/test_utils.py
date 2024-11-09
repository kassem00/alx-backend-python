#!/usr/bin/env python3
"""
unit test for utils.access_nested_map.
"""


from unittest import unittest.TestCase
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase, nested_map, path, expected):
    """ unit test for utils.access_nested_map. """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    """ main test file"""
    unittest.main()
