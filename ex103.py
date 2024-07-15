class MaxAndMin:
    def __init__(self, numbers:list[int]) -> None:
        self.numbers = numbers

    def _min_and_max(self):
        t = len(self.numbers)
        i = 0
        ma = self.numbers[0]
        mi = self.numbers[0]
        while i < t:
            if ma < self.numbers[i]:
                ma = self.numbers[i]
            if mi > self.numbers[i]:
                mi = self.numbers[i]
            i += 1
        return ma, mi
    
maximum = lambda arr: MaxAndMin(arr)._min_and_max()[0]
minimum = lambda arr: MaxAndMin(arr)._min_and_max()[1]
print(minimum([-52, 56, 30, 29, -54, 0, -110]))