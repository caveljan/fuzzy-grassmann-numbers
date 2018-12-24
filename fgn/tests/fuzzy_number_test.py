from .context import fuzzy_number


# add
def simple_add():
    fn1 = fuzzy_number.FN([2, 3])
    fn2 = fuzzy_number.FN([1, 2])
    return fn1.add(fn2)

def test_simple_add():
    assert simple_add().lower_limit == 3
    assert simple_add().upper_limit == 5


# subtract
def simple_subtract():
    fn1 = fuzzy_number.FN([2, 3])
    fn2 = fuzzy_number.FN([1, 2])
    return fn1.subtract(fn2)

def test_simple_subtract():
    assert simple_subtract().lower_limit == 1
    assert simple_subtract().upper_limit == 1


# display
def display():
    fn = fuzzy_number.FN([5, 6])
    return fn.display()

def test_display():
    assert display() == '[5, 6]'
