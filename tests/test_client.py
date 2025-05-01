# tests/test_client.py
import unittest
from linear_client.client import LinearClient
from linear_client.operations import get_viewer

class TestLinearClient(unittest.TestCase):
    def setUp(self):
        self.client = LinearClient(token='your_test_token')

    def test_get_viewer(self):
        op = get_viewer()
        data = self.client.execute(op)
        self.assertIn('viewer', data)
