def alphabet():
    global number
    if number == 90:
        number = 65
        return number
    number += 1
    return number


def diamond(x, y):
    global number
    for i in range(4):
        if i == 0:
            graph[x][y] = chr(alphabet())
            for _ in range(k):
                x += 1
                y -= 1
                graph[x][y] = chr(alphabet())
        elif i == 1:
            for _ in range(k):
                x += 1
                y += 1
                graph[x][y] = chr(alphabet())
        elif i == 2:
            for _ in range(k):
                x -= 1
                y += 1
                graph[x][y] = chr(alphabet())
        else:
            for _ in range(k - 1):
                x -= 1
                y -= 1
                graph[x][y] = chr(alphabet())
    return x, y


N = int(input())
M = 2 * N - 1
graph = [[' '] * M for _ in range(M)]
s_x, s_y = 0, N-1
x, y = 0, N-1
k = N-1
number = 64

while True:
    if k == 0:
        graph[x][y] = chr(alphabet())
        break
    x, y = diamond(x, y)
    y -= 1
    k -= 1

for g in graph:
    print(*g)
