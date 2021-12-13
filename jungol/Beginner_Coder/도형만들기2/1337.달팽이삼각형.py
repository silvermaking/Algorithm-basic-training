"""
대각선: 0
왼쪽: 1
위로: 2
6 -> 5 -> 4 -> ... -> 1
이중 for문
"""

N = int(input())
graph = [[0] * i for i in range(1, N+1)]
number = 0
i = j = -1
for dir in range(N):
    for _ in range(dir, N):
        if dir % 3 == 0:
            i += 1
            j += 1
        elif dir % 3 == 1:
            j -= 1
        else:
            i -= 1
        graph[i][j] = number
        number = (number + 1) % 10

for ans in graph:
    print(*ans)