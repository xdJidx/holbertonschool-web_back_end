#!/usr/bin python3
"""Unittests for client.py"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test for GithubOrgClient"""

    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        test_obj = GithubOrgClient(org_name)

        # Define the expected URL
        url = f"https://api.github.com/orgs/{org_name}"

        self.assertEqual(test_obj.org, {'key': 'value'})
        mock_get_json.assert_called_once_with(url)


if __name__ == '__main__':
    unittest.main()
