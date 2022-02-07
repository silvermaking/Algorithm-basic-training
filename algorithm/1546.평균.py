N = int(input())
lst = list(map(int, input().split()))
max_num = max(lst)

for i in range(N):
    temp = lst[i]
    lst[i] = temp / max_num * 100

print(sum(lst) / len(lst))