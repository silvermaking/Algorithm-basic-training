n = int(input())

for i in range(1, n + 1):
    for j in range(i, i + n * n, n):
        print(j, end=" ")
    print()
