n, m = map(int, input().split()) # n: 변의 길이, m: 종류

if m == 1:
    for i in range(1, n+1):
        print(f'{i} ' * n)
elif m == 2:
    for i in range(n):
        if i % 2:
            for j in range(n, 0, -1):
                print(j, end=" ")
            print()
        else:
            for j in range(1, n+1):
                print(j, end=" ")
            print()
else:
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(j*i, end=" ")
        print()