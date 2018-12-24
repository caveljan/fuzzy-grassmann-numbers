from .context import grassmann_number


# add
def simple_add():
    gn1 = grassmann_number.GN([2, 3, 4])
    gn2 = grassmann_number.GN([2, 1, 0])
    # gn2 = [2, 1, 0]
    return gn1.add(gn2)

def test_simple_add():
    assert simple_add().values == [4, 4, 4]


# subtract
def simple_subtract():
    gn1 = grassmann_number.GN([2, 3, 4])
    gn2 = grassmann_number.GN([2, 1, 0])
    return gn1.subtract(gn2)

def test_simple_subtract():
    assert simple_subtract().values == [0, 2, 4]


# multiply
def simple_multiply():
    gn1 = grassmann_number.GN([2, 3, 4])
    gn2 = grassmann_number.GN([2, 1, 0])
    return gn1.multiply(gn2)

def test_simple_multiply():
    assert simple_multiply().values == [4, 3, 0]


# divide
def simple_divide():
    gn1 = grassmann_number.GN([2, 3, 4])
    gn2 = grassmann_number.GN([2, 1, 1])
    return gn1.divide(gn2)

def test_simple_divide():
    assert simple_divide().values == [1, 3, 4]


def display():
    gn1 = grassmann_number.GN([1, 2, 3, 4, 5, 6, 7, 8])
    return gn1.display()

def test_display():
    assert display() == '1 + 2⋅e_1 + 3⋅e_2 + 4⋅e_3 + 5⋅e_4 + 6⋅e_5 + 7⋅e_6 + 8⋅e_7'
