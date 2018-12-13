class FuzzyNumber():
    def __init__(self, granularity, limits):
        self.granularity = granularity
        self.lower_limit = limits[0]
        self.upper_limit = limits[1]
        print(f'granularity is {self.granularity}')
        print(f'limits are {self.lower_limit} - {self.upper_limit}')

