import pytest
from mathutils import factorial

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24)
])
def test_factorial(n, expected):
    assert factorial(n) == expected