import pytest
from mathutils import is_even
#test for even numbers
@pytest.mark.parametrize("n", [
    2,
    4,
    6,
    8,
    100
])
def test_even_numbers(n):
    assert is_even(n) == True

#test for odd numbers
@pytest.mark.parametrize("n", [
    1,
    3,
    5,
    7
])
def test_is_not_even(n):
    assert is_even(n) == False
