n, m = map(int, input().split()) # n: λμ΄, m: λλΉ

i = 1
for _ in range(n):
    for _ in range(m):
        print(i, end=" ")
        i += 1
    print()
