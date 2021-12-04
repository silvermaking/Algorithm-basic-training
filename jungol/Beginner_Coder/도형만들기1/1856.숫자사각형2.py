n, m = map(int, input().split()) # n: 높이, m: 너비
j = 1
for i in range(1, n+1):
    if i % 2:
        for _ in range(m):
            print(j, end=" ")
            j += 1
    else:
        j += m
        temp_j = j - 1
        for _ in range(m):
            print(temp_j, end=" ")
            temp_j -= 1
    print()