"""
자료를 찾는데 ( a in list 등)
list => O(n)
set => O(1), set.add() 끝
"""

import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(cnt, num, y, x):
    if cnt == 6:
        if num not in ans:
            ans.add(num)
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not 0 <= nx < 5 or not 0 <= ny < 5: continue
        dfs(cnt+1, num+str(graph[ny][nx]), ny, nx)


graph = [list(input().strip().split()) for _ in range(5)]
ans = set()

for i in range(5):
    for j in range(5):
        num = str(graph[i][j])
        dfs(1, num, i, j)

print(len(ans))