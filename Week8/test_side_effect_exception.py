from unittest.mock import Mock
import pytest

def test_side_effect_exception():
    mock = Mock()
    mock.login.side_effect = RuntimeError(
        "Invalid credentials"
    )
    with pytest.raises(RuntimeError):
        mock.login()