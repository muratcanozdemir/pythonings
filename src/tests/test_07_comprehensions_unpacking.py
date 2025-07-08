from pythonings.ex07_comprehension_unpackaging import squares_until, unique_letters, invert_dict, split_first_rest

def test_squares_until():
    assert squares_until(5) == [0, 1, 4, 9, 16]

def test_unique_letters():
    assert unique_letters(["hi", "apple"]) == {"h", "i", "a", "p", "l", "e"}

def test_invert_dict():
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}

def test_split_first_rest():
    first, rest = split_first_rest([10, 20, 30])
    assert first == 10 and rest == [20, 30]
