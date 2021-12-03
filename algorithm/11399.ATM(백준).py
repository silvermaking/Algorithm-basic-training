N = int(input())
lst = sorted(list(map(int, input().split())))
temp = 0
ans = 0
for i in range(N):
    ans += temp + lst[i]
    temp += lst[i]

print(ans)
