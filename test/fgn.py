from .context import fgn


def simple_add():
    a = fgn.GrassmannNumber(2, 3, 4)
    b = fgn.GrassmannNumber(2, 1, 0)
    return fgn.GrassmannAdd(a, b)

def test_simple_add():
    assert simple_add() == [4, 4, 4]
