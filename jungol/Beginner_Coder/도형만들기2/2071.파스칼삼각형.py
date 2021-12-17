n, m = map(int, input().split())
lst = [[1] * i for i in range(1, n+1)]


def paskal_tri(n, m):
    if n < 2:
        print(*lst[0])

    for i in range(2, n):
        for j in range(1, i):
            lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

    if m == 1:
        for ans in lst:
            print(*ans)
        return
    elif m == 2:
        ans_lst = lst[::-1]
        for i in range(n):
            if i < 1:
                print(*ans_lst[i])
            else:
                print(' ' * i, end='')
                print(*ans_lst[i])
        return
    else:
        for i in range(n-1, -1, -1):
            for j in range(n-1, i-1, -1):
                print(lst[j][i], end=" ")
            print()


paskal_tri(n, m)