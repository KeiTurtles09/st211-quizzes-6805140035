import pytest

def test_floatEquality():
    assert 0.1 + 0.2 == pytest.approx(0.3)

def test_floatWithoutApprox():
    assert 0.1 + 0.2 != 0.3