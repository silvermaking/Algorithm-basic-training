import sys
input = sys.stdin.readline
N = int(input())
lst = sorted([list(map(int, input().strip().split())) for _ in range(N)],
             key= lambda x: (x[1], x[0]))

for ans in lst:
    print(*ans)