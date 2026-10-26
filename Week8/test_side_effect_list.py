from unittest.mock import Mock

def test_side_effect_list():
    mock = Mock()
    mock.get_data.side_effect = [1, 2]
    
    assert mock.get_data() == 1    
    assert mock.get_data() == 2   
    assert mock.get_data() == 3
    print(mock.get_data())
