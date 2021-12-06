N, K = map(int, input().split())
temp = 0

for i in range(1, N+1):
    if not N % i:
        temp += 1

    if temp == K:
        print(i)
        break

if temp < K:
    print(0)