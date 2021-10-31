"""
조합

"""

def combination(x, num):
    if x == 3:
        a = sum(arr)
        if a in sum_list:
            return
        else:
            sum_list.append(a)
            return

    for i in range(num, N):
        if used[i]: continue
        used[i] = 1
        arr.append(nums[i])
        combination(x+1, i)
        used[i] = 0
        arr.pop()

for tc in range(1, int(input()) + 1):
    nums = list(map(int, input().split()))
    N = len(nums)
    sum_list = []
    arr = []
    used = [0] * N
    combination(0, 0)
    sum_list.sort()
    print(f'#{tc} {sum_list[-5]}')