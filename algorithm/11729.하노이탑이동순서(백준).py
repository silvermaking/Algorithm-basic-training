"""
규칙
===
1. n-1개를 2번으로
2. n번째를 3번으로
3. n-1개를 3번으로

"""

import sys
N = int(sys.stdin.readline())
def hanoi(n, start, end):

    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, 6 - start - end) # 1 -> 2로
        print(start, end)
        hanoi(n-1, 6 - start - end, end)  # 2-> 3으로

print(2**N - 1)
hanoi(N, 1, 3)
