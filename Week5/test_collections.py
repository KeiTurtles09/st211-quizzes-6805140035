def test_listEquality():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    assert list1 == list2

def test_listInequality():
    list1 = [1, 2, 3]
    list2 = [2, 1, 3]
    assert list1 != list2

def test_listSorting():
    list1 = [3, 1, 2]
    assert sorted(list1) == [1, 2, 3]

def test_dictEquality():
    dict1 = {"Name": "Alice", "Age": 30}
    dict2 = {"Age": 30, "Name": "Alice"}
    assert dict1 == dict2

def test_setIntersection():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    assert set1 & set2 == {2, 3}

def test_setUnion():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    assert set1 | set2 == {1, 2, 3, 4}