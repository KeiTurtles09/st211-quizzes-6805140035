from unittest.mock import Mock

def test_mock_returns_confrigured_value():
    mock = Mock()
    mock.get_data.return_value = "fake data"
    assert mock.get_data() == "fake data"

def test_mock_accepts_any_call():
    mock = Mock()
    mock.anything()
    assert mock.whatever(1, 2, 3)

def test_mock_attributes():
    mock = Mock()
    mock.name = "TestUser"
    assert mock.name == "TestUser"

def test_mock_basics():
    mock = Mock()
    result = mock.mock.whatever(1, 2, 3)
    print(result)
    assert isinstance(result, Mock)