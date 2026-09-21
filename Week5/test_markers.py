import pytest

@pytest.mark.smoke
def test_critical_login():
    assert True

@pytest.mark.smoke
def test_critical_checkout():
    assert True

@pytest.mark.slow
def test_full_report_generation():
    assert True

@pytest.mark.regression
def test_old_bug_fixed():
    assert True