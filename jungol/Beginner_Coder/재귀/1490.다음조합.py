def comb(k, n):
    global ans
    if k == K:
        if a == arr:
            ans = 1
            return
        if ans:
            ans = 0
            print(*arr)
            return

    for i in range(n, N + 1):
        if used[i]: continue
        arr.append(i)
        used[i] = 1
        comb(k+1, i)
        arr.pop()
        used[i] = 0


N, K = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
last_arr = [i for i in range(N-K+1, N+1)]
arr = []
used = [0] * (N + 1)
if a == last_arr:
    print('NONE')
else:
    comb(0, 1)
