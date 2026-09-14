import pytest
from validators import validateEmail, validateAge

def test_validateEmail_withoutAtSymbol():
    with pytest.raises(ValueError):
        validateEmail("6805140035siam.edu")      # Email without @ symbol

def test_validateEmail_withoutDomain():
    with pytest.raises(ValueError):
        validateEmail("6805140035@")             # Email without domain
    
def test_validateAge_negative():
    with pytest.raises(ValueError):
        validateAge(-1)                          # Age is negative/under minimum boundary case

def test_validateAge_overMaximum():
    with pytest.raises(ValueError):
        validateAge(121)                         # Age is over maximum boundary case

def test_validateAge_nonInteger():
    with pytest.raises(TypeError):
        validateAge("twenty")                    # Age is a string instead of an integer
