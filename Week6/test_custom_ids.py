import pytest

@pytest.mark.parametrize("user", [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 12},
], ids=["alice-adult", "bob-adult", "charlie-child"])

def test_user_has_name  (user):
    assert "name" in user