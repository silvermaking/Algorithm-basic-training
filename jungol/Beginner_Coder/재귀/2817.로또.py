def lotto(i, n):
    if n == 6:
        print(*arr)
        return

    for i in range(i, K-5+n):
        if used[i]: continue
        arr.append(lotto_list[i])
        used[i] = 1
        lotto(i, n+1)
        arr.pop()
        used[i] = 0


lotto_list = list(map(int, input().split()))
K = lotto_list.pop(0)
used = [0] * K
arr = []
lotto(0, 0)