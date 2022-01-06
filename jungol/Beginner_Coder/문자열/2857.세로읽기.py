a = [[' '] * 15 for _ in range(5)]
for i in range(5):
    b = input()
    for j in range(len(b)):
        a[i][j] = b[j]

ans = ''
col = 0

while col < 15:
    for r in range(5):
        temp = a[r][col]
        if temp != ' ':
            ans += temp

    col += 1

print(ans)