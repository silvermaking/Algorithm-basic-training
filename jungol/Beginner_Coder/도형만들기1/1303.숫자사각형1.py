n, m = map(int, input().split()) # n: 높이, m: 너비

i = 1
for _ in range(n):
    for _ in range(m):
        print(i, end=" ")
        i += 1
    print()
