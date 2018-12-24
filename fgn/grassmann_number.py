class GN():
    """Grassmann Number

    """

    def __init__(self, values):
        self.grade = len(values)
        self.values = values
        print(self.values)

    def add(self, other):
        newGN = []
        for i in range(len(self.values)):
            newGN.append(self.values[i] + other.values[i])
        return GN(newGN)

    def subtract(self, other):
        newGN = []
        for i in range(len(self.values)):
            newGN.append(self.values[i] - other.values[i])
        return GN(newGN)

    def multiply(self, other):
        newGN = []
        for i in range(len(self.values)):
            newGN.append(self.values[i] * other.values[i])
        return GN(newGN)

    def divide(self, other):
        newGN = []
        for i in range(len(self.values)):
            newGN.append(self.values[i] / other.values[i])
        return GN(newGN)
