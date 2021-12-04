"""
0,4 1,3 (2,2) --- (4, 0)
(1,4), --- (4, 1)

"""

n = int(input())
arr = [[" " for _ in range(n)] for _ in range(n)]
alphabet = 65
for i in range(n):
    k = 0
    for j in range(i, n):
        arr[j][n-1-k] = chr(alphabet)
        k += 1

        alphabet += 1

        if alphabet > 90:
            alphabet = 65

for lst in arr:
    print(*lst)