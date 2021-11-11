import sys
input = sys.stdin.readline

def solve(w, h):
    cnt = 1
    for j in range(N):
        tmp_w, tmp_h = lst[j]
        if w < tmp_w and h < tmp_h:
            cnt += 1

    return cnt

N = int(input())
lst = [list(map(int, input().strip().split())) for _ in range(N)]
ans_lst = [0] * N
for i in range(N):
    w, h = lst[i]
    print(solve(w, h), end=" ")

