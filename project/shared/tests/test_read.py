import unittest
from mock import patch

from shared.read import read


class TestRead(unittest.TestCase):

    @patch("builtins.input", return_value="test")
    def test_print_list(self, input_mock):
        result = read()
        self.assertGreaterEqual(input_mock.call_count, 1)
        self.assertEqual(result, "test")
