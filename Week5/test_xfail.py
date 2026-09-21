import pytest

@pytest.mark.xfail(reason="known bug, needs fixing")
def test_known_bug():
    assert 1 == 2  # This test is expected to fail due to a known bug

@pytest.mark.xfail(reason="might pass sometimes, needs investigation")
def test_unstable_feature():
    assert 1 == 1  # This test may pass or fail depending on previous bugs
