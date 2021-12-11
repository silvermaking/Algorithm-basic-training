class StarTriangle2:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def make_star(self):
        if not self.n % 2 or not 0 < self.n < 100 or not 0 < m < 5:
            return print("INPUT ERROR!")

        if self.m == 1:
            for i in range(1, self.n // 2 + 2):
                print('*' * i)
            temp = self.n // 2
            for _ in range(self.n // 2):
                print('*' * temp)
                temp -= 1

        elif self.m == 2:
            x = self.n // 2
            for i in range(1, self.n // 2 + 2):
                print(' ' * x + '*' * i)
                x -= 1
            temp = self.n // 2
            x += 2
            for _ in range(self.n // 2):
                print(' ' * x + '*' * temp)
                temp -= 1
                x += 1

        elif self.m == 3:
            x = 0
            for i in range(self.n, 0, -2):
                print(' ' * x + '*' * i)
                x += 1
            x -= 2
            for i in range(3, self.n + 1, 2):
                print(' ' * x + '*' * i)
                x -= 1

        else:
            x = 0
            for i in range(self.n // 2 + 1, 0, -1):
                print(' ' * x + '*' * i)
                x += 1
            x -= 1
            for i in range(2, self.n // 2 + 2):
                print(' ' * x + '*' * i)


n, m = map(int, input().split())
my_star = StarTriangle2(n, m)
my_star.make_star()
