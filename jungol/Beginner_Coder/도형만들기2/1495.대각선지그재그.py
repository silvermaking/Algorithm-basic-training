n = int(input())
arr = [[0] * n for _ in range(n)]
number = 1
i = j = 0
arr[i][j] = number
while True:
    # 1. 아래로 한번 이동 or 오른쪽으로 이동
    if i + 1 < n:
        i += 1
    else:
        j += 1
    number += 1
    arr[i][j] = number

    # 2. 오른쪽 위 대각선으로 이동
    while i > 0 or j < n-1:
        i -= 1
        j += 1
        number += 1
        arr[i][j] = number

    # 3. 오른쪽으로 한번 이동 or 아래로 이동
    if j + 1 < n:
        j += 1
    else:
        i += 1
    number += 1
    arr[i][j] = number

    # 4. 왼쪽 아래 대각선으로 이동
    while j > 0 or i < n-1:
        i += 1
        j -= 1
        number += 1
        arr[i][j] = number

for a in arr:
    print(*a)