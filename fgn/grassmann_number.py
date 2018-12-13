class Generate():
    def __init__(self, *args):
        self.args = args
        print(args)

    def add(self, first_number, second_number):
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

