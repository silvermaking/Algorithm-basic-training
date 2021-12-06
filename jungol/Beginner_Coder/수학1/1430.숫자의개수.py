num_list = [0] * 10
ans = 1
for _ in range(3):
    ans *= int(input())

ans = str(ans)
for a in ans:
    num_list[int(a)] += 1

for num in num_list:
    print(num)

