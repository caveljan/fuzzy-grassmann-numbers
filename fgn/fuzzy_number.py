class FN():
    """Fuzzy Number

    """

    def __init__(self, limits, granularity=0.1):
        self.lower_limit = limits[0]
        self.upper_limit = limits[1]
        self.granularity = granularity


    def add(self, other):
        if isinstance(other, FN):
            newFN = []
            newFN.append(self.lower_limit + other.lower_limit)
            newFN.append(self.upper_limit + other.upper_limit)
            return FN(newFN)
        else:
            print('The number needs to be a Fuzzy Number (FN instance).')


    def subtract(self, other):
        if isinstance(other, FN):
            newFN = []
            newFN.append(self.lower_limit - other.lower_limit)
            newFN.append(self.upper_limit - other.upper_limit)
            return FN(newFN)
        else:
            print('The number needs to be a Fuzzy Number (FN instance).')


    def display(self):
        fn = '[' + str(self.lower_limit) + ', ' + str(self.upper_limit) + ']'
        return fn
