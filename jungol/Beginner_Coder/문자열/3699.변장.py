"""
모든 경우의 수 - 1
의상이 2개일 경우: 2 + 1(입지 않은 경우)
"""
for _ in range(int(input())):
    N = int(input())
    clothes_dict = {}
    for _ in range(N):
        a, b = input().split()
        if b in clothes_dict:
            clothes_dict[b] += 1
        else:
            clothes_dict[b] = 1
    ans = 1
    for value in clothes_dict.values():
        ans *= (value + 1)

    print(ans - 1)
