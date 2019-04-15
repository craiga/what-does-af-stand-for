"""Front page tests."""

import pytest
from model_mommy import mommy

from what_does_af_stand_for import models


@pytest.mark.django_db
def test_af(client):
    """Test that an AF phrase is returned."""
    mommy.make("AWord", word="Albatross")
    mommy.make("FWord", word="Fury")
    response = client.get("/")
    assert "Albatross Fury" in response.content.decode()


@pytest.mark.django_db
def test_post_reaction(client):
    """Test a reaction to a new combination."""
    a_word = mommy.make("AWord")
    f_word = mommy.make("FWord")
    response = client.post(
        "/", {"a_word": a_word.id, "f_word": f_word.id, "reaction": "thumbs_up"}
    )
    assert models.Combination.objects.filter(
        a_word=a_word, f_word=f_word, thumbs_up=1, thumbs_down=0
    ).exists()
    assert response.status_code == 302
