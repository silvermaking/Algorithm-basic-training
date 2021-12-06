def gcd_get(x, y):
    if y == 0:
        return x
    return gcd_get(y, x % y)


a = int(input())
b = int(input())

ans1 = gcd_get(a, b)
print(ans1)
ans2 = ans1 * (a // ans1) * (b // ans1)
print(ans2)