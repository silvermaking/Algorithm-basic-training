"""
왼쪽 위 i -= 1
      j -= 1
"""


n = int(input())
arr = [[0] * n for _ in range(n)]
number = 1
i = 0
j = n // 2
arr[i][j] = number
while number < n ** 2:
    if number % n:
        i -= 1
        j -= 1
        number += 1
        if i < 0:
            i = n-1
        if j < 0:
            j = n-1
        arr[i][j] = number
    else:
        i += 1
        number += 1
        if i > n-1:
            i = 0
        arr[i][j] = number

for a in arr:
    print(*a)