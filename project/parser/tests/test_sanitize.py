from parser.sanitize import sanitize
import unittest


class TestSanitize(unittest.TestCase):
    # sanitize should make strings lowercase
    def test_lower(self):
        assert sanitize("TeSt TEST") == "test test"
