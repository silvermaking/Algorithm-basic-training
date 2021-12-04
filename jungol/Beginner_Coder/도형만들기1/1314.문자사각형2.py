"""
arr 생성하고 채워넣기
"""

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
alphabet = 65
for i in range(n):
    for j in range(n):
        if i % 2:
            arr[n-j-1][i] = chr(alphabet)
        else:
            arr[j][i] = chr(alphabet)
        alphabet += 1

        if alphabet > 90:
            alphabet = 65

for lst in arr:
    print(*lst)