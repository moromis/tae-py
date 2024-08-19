from project.parser.grammar.seek_verb import seek_verb


def get_verb(command: list[str]) -> str:
    # get the first two words of the string, then start with the second and see if it matches
    # any secondary verb strings. If so, match the base verb with the primary string and return. Otherwise, return the first word
    # as the primary verb
    # for example:
    # `look at`: at -> look
    # pass the secondary verb as an optional argument for the primary verb
    # TODO: how do we avoid making this complicated: i.e. should all objects have to handle
    # look toward and look at differently? Is there a grammatical change in response that's consistent
    # which would allow us to handle them both relatively the same?
    primary_verb = command[0]
    secondary_verb = command[1]
    seek_verb(secondary_verb)
