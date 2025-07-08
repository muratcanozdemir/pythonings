from pythonings.ex01_intertools import find_triples

def test_find_triples():
    assert set(find_triples(2)) == {
        (0,0,2), (0,1,1), (0,2,0),
        (1,0,1), (1,1,0),
        (2,0,0)
    }
    # Spot check for larger n
    triples = find_triples(5)
    assert all(sum(x) == 5 for x in triples)
    assert (1,2,2) in triples
