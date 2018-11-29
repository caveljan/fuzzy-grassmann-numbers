class GrassmannNumber():
    def __init__(self, *args):
        self.args = args
        print(args)


def GrassmannAdd(first_number, second_number):
    print(f'The first GrassmannNumber: {first_number.args}')
    print(f'The second GrassmannNumber: {second_number.args}')
    first_number = first_number.args
    second_number = second_number.args
    sum_number = []
    if len(first_number) == len(second_number):
        for i in range(len(first_number)):
            sum = first_number[i] + second_number[i]
            sum_number.append(sum)
    return sum_number


class FuzzyNumber():
    def __init__(self, granularity, limits):
        self.granularity = granularity
        self.lower_limit = limits[0]
        self.upper_limit = limits[1]
        print(f'granularity is {self.granularity}')
        print(f'limits are {self.lower_limit} - {self.upper_limit}')


gn1 = GrassmannNumber(-3, 2, 3)
gn2 = GrassmannNumber(3, 4, 235)

gn3 = GrassmannAdd(gn1, gn2)

print('Grassmann add', gn3)
print('----')

fn1 = FuzzyNumber(0.2, [2, 3])
fn2 = FuzzyNumber(0.2, [1, 2])

gn3 = GrassmannNumber(fn1, fn2)
