from .context import fuzzy_number


def simple_add():
    fn1 = fuzzy_number.FN(0.2, [2, 3])
    fn2 = fuzzy_number.FN(0.2, [1, 2])
    return fn1.add(fn1, fn2)

def test_simple_add():
    assert simple_add() == [4, 4, 4]
