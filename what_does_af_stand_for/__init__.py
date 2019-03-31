import re


class CouldNotParsePhraseError(ValueError):
    pass


def parse_phrase(phrase):
    match = re.search(r"^(a\S*)\W+(f\S*)$", phrase, re.IGNORECASE)
    if not match:
        raise CouldNotParsePhraseError()

    return match.group(1, 2)
