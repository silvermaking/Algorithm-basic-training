dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def count_length(x, y):
    n = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if graph[nx][ny] == 0:
            n += 1
    return n


graph = [[0] * 101 for _ in range(101)]
ans = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            graph[i][j] = 1

for i in range(100):
    for j in range(100):
        if graph[i][j]:
            ans += count_length(i, j)


print(ans)