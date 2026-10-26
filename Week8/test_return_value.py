from unittest.mock import Mock

def test_return_value():
    mock = Mock()
    mock.get_status.return_value = 123 
    print(mock.get_status())
    print(mock.get_status())
    print(mock.get_status())
    assert mock.get_status() == "OK"