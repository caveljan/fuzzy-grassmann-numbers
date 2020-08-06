class GN():
    """Grassmann Number

    """

    def __init__(self, values):
        self.grade = len(values)
        self.values = values
        print(self.values)

    def __repr__(self):
        return 'Grassmann Number(*{!r})'.format(self.values)

    def add(self, other):
        if isinstance(other, GN):
            newGN = []
            for i in range(len(self.values)):
                newGN.append(self.values[i] + other.values[i])
            return GN(newGN)
        else:
            print('The number needs to be a Grassmann Number (GN instance).')


    def subtract(self, other):
        if isinstance(other, GN):
            newGN = []
            for i in range(len(self.values)):
                newGN.append(self.values[i] - other.values[i])
            return GN(newGN)
        else:
            print('The number needs to be a Grassmann Number (GN instance).')


    def multiply(self, other):
        if isinstance(other, GN):
            newGN = []
            for i in range(len(self.values)):
                newGN.append(self.values[i] * other.values[i])
            return GN(newGN)
        else:
            print('The number needs to be a Grassmann Number (GN instance).')


    def divide(self, other):
        if isinstance(other, GN):
            newGN = []
            for i in range(len(self.values)):
                newGN.append(self.values[i] / other.values[i])
            return GN(newGN)
        else:
            print('The number needs to be a Grassmann Number (GN instance).')


    def display(self):
        gn = ''
        for i in range(len(self.values)):
            if (i == 0):
                gn += str(self.values[i])
            else:
                gn += ' + ' + str(self.values[i]) + '⋅e_' + str(i)
        return gn
