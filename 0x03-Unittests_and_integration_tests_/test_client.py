#!/usr/bin/env python3
"""
unit test for utils.access_nested_map.
"""
import unittest
from utils import access_nested_map
from unittest import TestCase
from test_client import access_nested_map 


class TestGithubOrgClient(unittest.TestCase):
    """ unit test for utils.access_nested_map. """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": {"b": {"c": 3}}}, ("a", "b", "c"), 3),
        ({"a": {"b": {"c": 3}}}, ("a", "b", "d"), None),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with valid paths."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    def test_public_repos(self):
        """ test_access_nested_map """
        pass


if __name__ == "__main__":
    unittest.main()
