from .context import grassmann_number


def simple_add():
    gn1 = grassmann_number.GN(2, 3, 4)
    gn2 = grassmann_number.GN(2, 1, 0)
    return gn1.add(gn1, gn2)

def test_simple_add():
    assert simple_add() == [4, 4, 4]
