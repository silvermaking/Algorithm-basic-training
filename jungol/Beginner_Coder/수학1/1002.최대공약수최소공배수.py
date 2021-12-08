def gcd_get(x, y):
    if y == 0:
        return x
    return gcd_get(y, x % y)

N = int(input())
nums_list = list(map(int, input().split()))
ans1 = ans2 = nums_list[0]
for i in range(1, N):
    ans1 = gcd_get(ans1, nums_list[i])
    ans2 = ans2 / gcd_get(ans2, nums_list[i]) * nums_list[i]

print(ans1)
print(int(ans2))
