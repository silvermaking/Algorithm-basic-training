import math

M, N = map(int, input().split())
arr = [1 for i in range(N + 1)]
arr[0] = arr[1] = 0
cnt = 0

for i in range(2, int(math.sqrt(N) + 1)):
    if arr[i]:
        j = 2
        while i * j <= N:
            arr[i * j] = 0
            j += 1

print(sum(arr[M:N+1]))