from project.parser.split_by_and import split_by_and


def test_split_by_and():
    assert split_by_and("command1 and command2 and command3andbadcommand") == [
        "command1",
        "command2",
        "command3andbadcommand",
    ]
