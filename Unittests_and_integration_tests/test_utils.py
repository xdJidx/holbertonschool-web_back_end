#!/usr/bin/env python3
"""Test for utils.py
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == '__main__':
    unittest.main()
