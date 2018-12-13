from .context import grassmann_fuzzy_number


def simple_add():
    gfn1 = grassmann_fuzzy_number.GFN(1)
    gfn2 = grassmann_fuzzy_number.GFN(1)
    return gfn1.add(gfn1, gfn2)

def test_simple_add():
    assert simple_add() == [4, 4, 4]
