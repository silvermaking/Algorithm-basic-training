a, b = map(int, input().split())
if a > b:
    k = b
else:
    k = a

while True:
    if a % k == 0 and b % k == 0:
        print(k)
        break
    k -= 1

print(k * (a//k) * (b//k))
