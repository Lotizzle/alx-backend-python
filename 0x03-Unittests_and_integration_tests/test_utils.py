#!/usr/bin/env python3
"""
This module contains the test case for the utils module
"""

import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Class to test AccessNestedMap
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Function to test AccessNestedMap
        Parameters:
        nested_map
        path
        expected result
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_error_message):
        """
        Function to test AccessNestedMap exception error
        Parameters:
        nested_map
        path
        expected error message
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_error_message)

class TestGetJson(unittest.TestCase):
    """ Class to test utils.get_json method """

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """
        Test that utils.get_json returns the expected result.
        """
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]

        for test_url, test_payload in test_cases:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)

            mock_get.reset_mock()


if __name__ == '__main__':
    unittest.main()
