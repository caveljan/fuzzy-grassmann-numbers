from .context import fuzzy_grassmann_number


def simple_add():
    fgn1 = fuzzy_grassmann_number.FGN(1)
    fgn2 = fuzzy_grassmann_number.FGN(1)
    return fgn1.add(fgn1, fgn2)

def test_simple_add():
    assert simple_add() == [4, 4, 4]
