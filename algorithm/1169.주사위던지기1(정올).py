"""
순열, 조합, 중복순열
N : 던진횟수
M : type
==============
함수 3개로 각각 구현
"""
def run1(x): #순열
    if x == N:
        print(*arr)
        return
    for i in range(1, 7):
        arr.append(i)
        run1(x+1)
        arr.pop()

def run2(x, num): #조합
    if x == N:
        print(*arr)
        return
    for i in range(num, 7):
        arr.append(i)
        run2(x+1, i)
        arr.pop()

def run3(x):
    if x == N:
        print(*arr)
        return
    for i in range(1, 7):
        if used[i]:
            continue
        arr.append(i)
        used[i] = 1
        run3(x+1)
        arr.pop()
        used[i] = 0

N, M = map(int, input().split())
arr = []
used = [0] * 7
if M == 1:
    run1(0)
elif M == 2:
    run2(0, 1)
else:
    run3(0)