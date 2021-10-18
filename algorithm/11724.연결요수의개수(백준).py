"""
bfs + 선형큐(front, rear)
graph: 2차원인접리스트
"""
import sys

def bfs(v):
    f = 0  # front
    r = 1  # rear
    queue = []
    visited[v] = 1
    queue.append(v)
    while f != r:
        v = queue.pop(f)
        r -= 1
        for nv in graph[v]:
            if not visited[nv]:
                visited[nv] = 1
                queue.append(nv)
                r += 1

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)   # bfs돌릴때마다
        cnt += 1  # 연결횟수 + 1

print(cnt)