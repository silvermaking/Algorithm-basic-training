a, b = input().split()

a = a[::-1]
b = b[::-1]

a = int(a)
b = int(b)
if a > b:
    print(a)
else:
    print(b)