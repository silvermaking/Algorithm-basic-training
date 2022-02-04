"""
스트라이크 : 확정
볼 : 예비
"""
def solve(arr):
    for x, s, b in N_list:
        x = list(map(int, str(x)))
        for i in range(len(arr)):
            if s:
                if arr[i] == x[i]:
                    s -= 1
                    continue
            else:
                if arr[i] == x[i]:
                    return False
            if b:
                if arr[i] in x and arr[i] != x[i]:
                    b -= 1
            else:
                if arr[i] in x:
                    return False
        if s or b:
            return False
    return True

def dfs(k):
    global cnt

    if k == 3:
        if not solve(arr):
            return
        cnt += 1
        return

    for i in range(1, 10):
        if used[i]: continue
        used[i] = 1
        arr.append(i)
        dfs(k+1)
        used[i] = 0
        arr.pop()


arr = []
num_list = [i for i in range(1, 10)]
N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
used = [0] * 10
dfs(0)
print(cnt)
