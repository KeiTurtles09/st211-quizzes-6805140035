import pytest
import sys

@pytest.mark.skip(reason="feature not implemented yet")
def test_future_feature():
    assert False # would fail if ran

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8 or higher")
def test_python38_feature():
    assert True