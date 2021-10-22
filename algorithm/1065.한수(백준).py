"""
math
1. x <= 99 이면 한수
2. 1000까지 이므로 3자리까지만 고려
"""
import sys
def hansu(x):
    if x < 100:
        return 1
    tmp_lst = list(map(int, str(x)))
    if tmp_lst[2] - tmp_lst[1] == tmp_lst[1] - tmp_lst[0]:
        return 1
    return 0

N = int(sys.stdin.readline())
ans = 0
for i in range(1, N+1):
    ans += hansu(i)

print(ans)