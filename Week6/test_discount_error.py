import pytest
from discount import apply_discount

@pytest.mark.parametrize("bad_percentage", [-1, -50, 101, 150])
def test_apply_discount_invalid_percentage(bad_percentage):
    with pytest.raises(ValueError):
        apply_discount(100, bad_percentage)