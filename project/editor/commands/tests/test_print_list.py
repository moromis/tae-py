import unittest
from mock import patch
from editor.commands.print_list import print_list


class TestPrintList(unittest.TestCase):

    @patch("editor.commands.print_list.output")
    def test_print_list(self, output_mock):
        print_list()
        self.assertGreaterEqual(output_mock.call_count, 1)
        for s in output_mock.call_args[0][0].split("\n"):
            assert s[0] == "-"
