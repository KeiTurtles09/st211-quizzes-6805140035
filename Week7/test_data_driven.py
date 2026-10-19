import json
import pytest

def load_test_cases():
    with open("test_cases.json") as f:
        data = json.load(f)
    return [{case["input"], case['expected']} for case in data]

@pytest.mark.parametrize("text, expected", load_test_cases())
def test_uppercase(text, expected):
    assert text.upper() == expected     