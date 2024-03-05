#!/usr/bin/env python3
"""Test for utils.py
"""

import unittest
import utils
from unittest.mock import Mock
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Access nested map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path_map, result_expec):
        """ Access nested method

            args:
                nested_map: {"a"} : Le dict. dans lequel accéder à la valeur
                path: ("a",) : Le chemin pour accéder au dict.
                result_expec: 1 : Le résultat attendu après l'accès à la valeur

            return
                Ok if its correct
        """
        self.assertEqual(access_nested_map(nested_map, path_map), result_expec)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path_map):
        """ Exception access nested method

            args:
                nested_map: {}
                path: ("a",)

            return:
                ok if its correct
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path_map)

        self.assertEqual(
            f'KeyError({str(error.exception)})', repr(error.exception))


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """ Test get_json method

            args:
                test_url: "http://example.com"
                test_payload: {"payload": True}
                mock_requests_get: Mock()

            return:
                ok if its correct
        """
        # Create a mock object for requests.get
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests_get.return_value = mock_response

        # Call the function to be tested
        result = utils.get_json(test_url)

        # Assertions
        # Check if requests.get was called exactly once with test_url
        mock_requests_get.assert_called_once_with(test_url)
        # Check if the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ Test memoize method """

    def test_memoize(self):
        """ Test memoize method

            return:
                ok if its correct
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass,
                          'a_method',
                          return_value=42) as mock_method:
            tc = TestClass()
            self.assertEqual(tc.a_property, 42)
            self.assertEqual(tc.a_property, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
