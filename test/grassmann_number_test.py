from .context import grassmann_number


def simple_add():
    a = grassmann_number.Generate(2, 3, 4)
    b = grassmann_number.Generate(2, 1, 0)
    return a.add(a, b)

def test_simple_add():
    assert simple_add() == [4, 4, 4]
