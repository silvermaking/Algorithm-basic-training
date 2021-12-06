n = int(input())
n_list = list(map(int, input().split()))
m = int(input())

ans1 = 0 # 약수의 합
ans2 = 0 # 배수의 합

for num in n_list:
    if not m % num:
        ans1 += num

    if not num % m:
        ans2 += num

print(ans1, ans2, sep='\n')