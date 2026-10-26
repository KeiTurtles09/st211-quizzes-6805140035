import csv, pytest
from validate import is_valid_login

def load_test_cases(): 
    cases = []
    with open("login.csv") as f:
        for row in csv.DictReader(f):          # reads header row as dict keys
            expected = row["valid"] == "True"  # convert string to boolean
            cases.append((row["username"], row["password"], expected))
    return cases

@pytest.mark.parametrize("username, password, expected", load_test_cases())
def test_login_validation(username, password, expected):
    assert is_valid_login(username, password) == expected