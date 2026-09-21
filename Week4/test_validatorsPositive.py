from validators import validateEmail, validateAge

def test_validateEmail():
    assert validateEmail("6805140035@siam.edu") == True             # Email without subdomain

def test_validateEmail_subDomain():
    assert validateEmail("6805140035@subdomain.siam.edu") == True   # Email with subdomain

def test_validateAge():
    assert validateAge(25) == True        # normal case
    assert validateAge(0) == True         # minimum boundary case
    assert validateAge(120) == True       # maximum boundary case

