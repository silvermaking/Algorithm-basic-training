# chr(65) == A
# chr(90) == Z
"""
첫번째 줄
64 + (n * n) % 26, 64 + (n * (n-1) % 26
64 +
"""
n = int(input())
for i in range(n):
    temp = ""
    for j in range(n, 0, -1):
        x = (n * j) % 26
        while x - i < 1:
            x += 26
        temp += f'{chr(64 + (x - i))} '
    print(temp)