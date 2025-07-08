from pythonings.ex11_antipatterns_gotchas import append_item, Counter, aliasing_bug

def test_append_item():
    a = append_item(1)
    b = append_item(2)
    c = append_item(3, [])
    assert a == [1]
    assert b == [2]
    assert c == [3]

def test_counter():
    c1 = Counter()
    c2 = Counter()
    c1.inc()
    assert c1.count == 1
    assert c2.count == 0

def test_aliasing_bug():
    l = [1, 2]
    l2 = aliasing_bug(l)
    assert l is not l2  # Should be a new list
    assert l2 == [1, 2, 999]
    assert l == [1, 2]
