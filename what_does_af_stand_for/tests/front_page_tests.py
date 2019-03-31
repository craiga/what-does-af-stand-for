"""Front page tests."""

import pytest
from model_mommy import mommy


@pytest.mark.django_db
def test_af(client):
    """Test that an AF phrase is returned."""
    mommy.make("AWord", word="Albatross")
    mommy.make("FWord", word="Fury")
    response = client.get("/")
    assert "Albatross Fury" in response.content.decode()
