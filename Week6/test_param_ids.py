import pytest
from discount import apply_discount

@pytest.mark.parametrize("price, percentage, expected", [
    pytest.param(100, 0, 100, id="no-discount"),
    pytest.param(100, 50, 50, id="half-price"),
    pytest.param(100, 100, 0, id="free"),
])
def test_apply_discount(price, percentage, expected):
    assert apply_discount(price, percentage) == expected