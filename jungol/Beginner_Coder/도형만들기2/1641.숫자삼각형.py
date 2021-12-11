class NumberTriangle:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def make_num(self):
        if not self.n % 2 or not 0 < self.n < 100 or not 0 < m < 4:
            return print("INPUT ERROR!")

        if self.m == 1:
            lst = [[' '] * self.n for _ in range(self.n)]
            num = 1
            y, x = 0, 0
            idx = 0
            while True:
                lst[y][x] = num
                if (y, x) == (self.n - 1, self.n - 1):
                    for i in lst:
                        print(*i)
                    return

                if y % 2: # 홀수층일 때
                    if x == 0:
                        y += 1
                        idx += 1
                    else:
                        x -= 1
                else: # 짝수층일 때
                    if x == idx:
                        y += 1
                        idx += 1

                    x += 1

                num += 1

        elif self.m == 2:
            num = 0
            lst = [[' '] * (self.n * 2 - 1) for _ in range(self.n)]
            s = 0
            e = self.n * 2 - 1
            for i in range(self.n):
                for j in range(s, e):
                    lst[i][j] = num
                num += 1
                s += 1
                e -= 1
            for i in lst:
                print(*i)

        else:
            lst = [[' '] * (self.n // 2 + 1) for _ in range(self.n)]
            for i in range(self.n // 2 + 1):
                for j in range(i + 1):
                    lst[i][j] = j + 1
                    lst[-1-i][j] = j + 1

            for i in lst:
                print(*i)


n, m = map(int, input().split())
my_num = NumberTriangle(n, m)
my_num.make_num()