from project.parser.sanitize import sanitize


# sanitize should make strings lowercase
def test_lower():
    assert sanitize("TeSt TEST") == "test test"
