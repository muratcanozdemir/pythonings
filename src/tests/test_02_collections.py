from pythonings.ex02_collections import count_items

def test_count_items():
    assert count_items(['a', 'b', 'a', 'c', 'b', 'a']) == {'a': 3, 'b': 2, 'c': 1}
    assert count_items([]) == {}
