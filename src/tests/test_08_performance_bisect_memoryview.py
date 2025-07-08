from pythonings.ex08_performance_bisect_memoryview import insert_sorted, zero_copy_prefix

def test_insert_sorted():
    lst = [1, 3, 5, 7]
    insert_sorted(lst, 4)
    assert lst == [1, 3, 4, 5, 7]
    insert_sorted(lst, 8)
    assert lst == [1, 3, 4, 5, 7, 8]

def test_zero_copy_prefix():
    b = bytearray(b"abcdef")
    prefix = zero_copy_prefix(b, 3)
    # Should be a memoryview, not a bytes/bytearray copy
    assert isinstance(prefix, memoryview)
    assert prefix.tobytes() == b"abc"
