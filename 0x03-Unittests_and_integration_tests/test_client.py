#!/usr/bin/env python3
"""
unit test for utils.access_nested_map.
"""
from unittest import unittest.TestCase
from utils import access_nested_map


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
        """ test_access_nested_map """
        s
    def test_public_repos(self):
        """ test_access_nested_map """
        pass

if __name__ == "__main__":
    unittest.main()
