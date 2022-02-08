def dice(k):
    if sum(arr) > M:
        return
    if k > N:
        return

    if k == N:
        if sum(arr) == M:
            print(*arr)
        return

    for i in range(1, 7):
        arr.append(i)
        dice(k+1)
        arr.pop()


N, M = map(int, input().split())
arr = []
dice(0)