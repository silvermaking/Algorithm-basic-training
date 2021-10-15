"""
코드참고
재귀
"""
import sys
N = int(sys.stdin.readline())
s = [[0] * N for _ in range(N)]
def star(n):
    global s
    if n == 3:
        s[0][:3] = s[2][:3] = [1] * 3
        s[1][:3] = [1, 0, 1]
        return
    a = n//3
    star(n//3)
    for i in range(3):
        for j in range(3):
            if (i, j) == (1, 1):
                continue
            for k in range(a):
                s[a*i + k][a*j:a*(j+1)] = s[k][:a]

star(N)
for i in s:
    for j in i:
        if j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()