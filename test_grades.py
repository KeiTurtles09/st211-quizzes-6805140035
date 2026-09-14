import pytest
from grades import letterGrade

def test_letterGradeA():
    assert letterGrade(95) == 'A'   # normal case
    assert letterGrade(80) == 'A'   # minimum boundary case
    assert letterGrade(100) == 'A'  # maximum boundary case

def test_letterGradeB():
    assert letterGrade(75) == 'B'   # normal case
    assert letterGrade(70) == 'B'   # minimum boundary case
    assert letterGrade(79) == 'B'   # maximum boundary case

def test_letterGradeC():
    assert letterGrade(65) == 'C'   # normal case
    assert letterGrade(60) == 'C'   # minimum boundary case
    assert letterGrade(69) == 'C'   # maximum boundary case

def test_letterGradeF():
    assert letterGrade(0) == 'F'    # minimum boundary case
    assert letterGrade(59) == 'F'   # maximum boundary case

def test_letterGradeInvalid():
    with pytest.raises(ValueError):
        letterGrade(-1)             # just below the minimum boundary case
    with pytest.raises(ValueError):
        letterGrade(101)            # just above the maximum boundary case
