class multifilter:
    def judge_half(self, pos, neg):
        if pos >= neg:
            return True

    def judge_any(self, pos, neg):
        if pos >= 1:
            return True

    def judge_all(self, pos, neg):
        if neg == 0 and pos != 0:
            return True

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.pos = 0
        self.neg = 0

    def __iter__(self):
        for i in self.iterable:
            for func in self.funcs:
                if func(i):
                    self.pos += 1
                else:
                    self.neg += 1

            if self.judge(self, self.pos, self.neg):
                yield i
            self.pos = 0
            self.neg = 0


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
