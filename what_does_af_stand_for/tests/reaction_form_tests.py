"""Front page tests."""

import pytest
from model_mommy import mommy

from what_does_af_stand_for import forms, models


@pytest.mark.django_db
@pytest.mark.parametrize("reaction", ["thumbs_up", "thumbs_down"])
def test_react_existing(reaction):
    """Test a reaction to an existing combination."""
    a_word = mommy.make("AWord")
    f_word = mommy.make("FWord")
    combination = mommy.make(
        "Combination", a_word=a_word, f_word=f_word, **{reaction: 7}
    )
    form = forms.ReactionForm(
        {"a_word": a_word.id, "f_word": f_word.id, "reaction": reaction}
    )
    assert form.is_valid()
    form.save()
    combination.refresh_from_db()
    assert getattr(combination, reaction) == 8


@pytest.mark.django_db
@pytest.mark.parametrize("reaction", ["thumbs_up", "thumbs_down"])
def test_react_new(reaction):
    """Test a reaction to a new combination."""
    a_word = mommy.make("AWord")
    f_word = mommy.make("FWord")
    form = forms.ReactionForm(
        {"a_word": a_word.id, "f_word": f_word.id, "reaction": reaction}
    )
    assert form.is_valid()
    form.save()
    combination = models.Combination.objects.get(a_word=a_word, f_word=f_word)
    assert getattr(combination, reaction) == 1
