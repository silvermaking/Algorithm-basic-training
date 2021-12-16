def type1(k):
    if k == N:
        print(*arr)
        return

    for i in range(1, 7):
        arr.append(i)
        type1(k+1)
        arr.pop()


def type2(k, num):
    if k == N:
        print(*arr)
        return
    for i in range(num, 7):
        arr.append(i)
        type2(k+1, i)
        arr.pop()


def type3(k):
    if k == N:
        print(*arr)
        return

    for i in range(1, 7):
        if used[i]: continue
        used[i] = 1
        arr.append(i)
        type3(k+1)
        used[i] = 0
        arr.pop()


N, M = map(int, input().split())
arr = []
used = [0] * 7
if M == 1:
    type1(0)
elif M == 2:
    type2(0, 1)
else:
    type3(0)
