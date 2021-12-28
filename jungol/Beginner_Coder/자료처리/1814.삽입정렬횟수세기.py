def ins_sort(lst):
    cnt = 0
    for i in range(1, n):
        temp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > temp:
            lst[j+1] = lst[j]
            j -= 1
            cnt += 1
        lst[j+1] = temp
    return cnt


n = int(input())
lst = list(map(int, input().split()))
print(ins_sort(lst))
