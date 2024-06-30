#!/usr/bin/env python3
import unittest
from typing import Dict, List
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import MagicMock, Mock, PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """ Tests the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, response: Dict, mock_fn: MagicMock) -> None:
        """ Test org function.
        """
        mock_fn.return_value = MagicMock(return_value=response)
        github_org_client = GithubOrgClient(org)
        self.assertEqual(github_org_client.org(org), response)
        mock_fn.assert_called_once_with("https://api.github.com/orgs/{}".format(org))
