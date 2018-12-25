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


# multiply
def simple_multiply():
    fn1 = fuzzy_number.FN([2, 3])
    fn2 = fuzzy_number.FN([1, 2])
    return fn1.multiply(fn2)

def test_simple_multiply():
    assert simple_multiply().lower_limit == 2
    assert simple_multiply().upper_limit == 6


# divide
def simple_divide():
    fn1 = fuzzy_number.FN([2, 3])
    fn2 = fuzzy_number.FN([1, 2])
    return fn1.divide(fn2)

def test_simple_divide():
    assert simple_divide().lower_limit == 1
    assert simple_divide().upper_limit == 3


# display
def display():
    fn = fuzzy_number.FN([5, 6])
    return fn.display()

def test_display():
    assert display() == '[5, 6]'
