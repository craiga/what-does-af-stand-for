"""Tests for parse_phrase."""

import pytest

import what_does_af_stand_for


@pytest.mark.parametrize(
    "phrase, a_word, f_word",
    [
        ("Artfully Flatulent", "Artfully", "Flatulent"),
        ("always funny", "always", "funny"),
        ("Aha! Friday!", "Aha!", "Friday!"),
        ("Abercrombie & Fitch", "Abercrombie", "Fitch"),
        ("Atima Fwitbread.", "Atima", "Fwitbread"),
    ],
)
def test_parse_phrase(phrase, a_word, f_word):
    """Test parse_phrase."""
    assert what_does_af_stand_for.parse_phrase(phrase) == (a_word, f_word)


@pytest.mark.parametrize(
    "bad_phrase",
    ["Alpha Beta", "Egg Farts", "Awful", "AWFUL", "zebra aardvark falcon gibbon"],
)
def test_bad_phrase(bad_phrase):
    """Test that bad phrases result in CouldNotParsePhraseErrors."""
    with pytest.raises(what_does_af_stand_for.CouldNotParsePhraseError):
        what_does_af_stand_for.parse_phrase(bad_phrase)
