"""What Does AF Stand For?"""

import re


class CouldNotParsePhraseError(ValueError):
    pass


def parse_phrase(phrase):
    """Parse an AF phrase into an A word and an F word."""
    match = re.search(r"^(a\S*)\W+(f\S*)$", phrase, re.IGNORECASE)
    if not match:
        raise CouldNotParsePhraseError()

    return match.group(1, 2)
