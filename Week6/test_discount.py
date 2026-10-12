import pytest
from discount import apply_discount

@pytest.mark.parametrize("price, percentage, expected", [
    (100, 0, 100), 
    (100, 50, 50),
    (100, 100, 0), 
    (200, 25, 150),   
    (80, 10, 72),  
])
def test_apply_discount(price, percentage, expected):
    assert apply_discount(price, percentage) == expected
