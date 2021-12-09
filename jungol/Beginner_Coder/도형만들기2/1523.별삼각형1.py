class StarTriangle:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def make_star(self):
        if not 0 < self.n < 100 or not 0 < m < 4:
            return print("INPUT ERROR!")

        if self.m == 1:
            for i in range(1, self.n + 1):
                print('*' * i)
        elif self.m == 2:
            for i in range(self.n, 0, -1):
                print('*' * i)
        else: # 2n - 1
            for i in range(1, self.n + 1):
                temp = ' ' * (n - i)
                print(temp + '*' * (2*i - 1) + temp)


n, m = map(int, input().split())
my_star = StarTriangle(n, m)
my_star.make_star()
