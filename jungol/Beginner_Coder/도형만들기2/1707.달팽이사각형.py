"""
N = 5 일 때
5, 4, 4, 3, 3, 2, 2, 1, 1 번

2N-1 번
"""
N = int(input())
graph = [[0] * N for _ in range(N)]

i = 0
j = -1
k = 0
number = 1
for dir in range(2*N - 1): # 0 ~ 8
    if dir >= 2*k + 1:
        k += 1
    for _ in range(N - k):
        if j < N-1 and dir % 4 == 0:
            j += 1
        elif i < N-1 and dir % 4 == 1:
            i += 1
        elif j > 0 and dir % 4 == 2:
            j -= 1
        elif i > 0 and dir % 4 == 3:
            i -= 1
        graph[i][j] = number
        number += 1

for ans in graph:
    print(*ans)
