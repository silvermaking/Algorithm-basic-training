def gcd_get(x, y):
    if y == 0:
        return x
    return gcd_get(y, x % y)


a, b = map(int, input().split())

ans1 = gcd_get(a, b)
print(ans1)
ans2 = ans1 * (a // ans1) * (b // ans1)
print(ans2)