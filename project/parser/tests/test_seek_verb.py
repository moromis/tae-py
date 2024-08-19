from project.parser.grammar.seek_verb import seek_verb
from unittest.mock import patch


def test_seek_verb():
    with patch("project.parser.grammar.verbs") as verbs:
        # if the verb is in our library of verbs, then it should return something
        verb = seek_verb("look")
        assert verb != None
        # if the verb doesn't exist in the standard verbs, we should get None
        verb = seek_verb("asdf-test-not-in-verbs")
        assert verb == None
