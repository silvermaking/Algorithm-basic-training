def solve(n):
    temp = (n * N) % P
    if temp in lst:
        if 0 in lst:
            print(1)
        else:
            print(len(lst))
        return
    lst.append(temp)
    return solve(temp)


N, P = map(int, input().split())
lst = []
solve(N)