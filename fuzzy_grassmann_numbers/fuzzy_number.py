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


    def multiply(self, other):
        if isinstance(other, FN):
            newFN = []
            x1 = self.lower_limit
            x2 = self.upper_limit
            y1 = other.lower_limit
            y2 = other.upper_limit
            calculation = [ x1*y1, x1*y2, x2*y1, x2*y2 ]

            lower_limit_min = min(calculation)
            upper_limit_max = max(calculation)

            newFN.append(lower_limit_min)
            newFN.append(upper_limit_max)
            return FN(newFN)


    def divide(self, other):
        if isinstance(other, FN):
            newFN = []
            x1 = self.lower_limit
            x2 = self.upper_limit
            y1 = other.lower_limit
            y2 = other.upper_limit
            calculation = [ x1/y1, x1/y2, x2/y1, x2/y2 ]

            lower_limit_min = min(calculation)
            upper_limit_max = max(calculation)

            newFN.append(lower_limit_min)
            newFN.append(upper_limit_max)
            return FN(newFN)


    def display(self):
        fn = '[' + str(self.lower_limit) + ', ' + str(self.upper_limit) + ']'
        return fn
