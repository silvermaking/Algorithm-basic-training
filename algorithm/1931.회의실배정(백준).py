"""
list 는 인덱싱하는 시간이 많이 걸린다.

"""

import sys
input = sys.stdin.readline
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: (x[1], x[0]))
cnt = 0
start = 0
end = 0
for s, e in lst:
    if s >= end:
        end = e
        cnt += 1

print(cnt)