def ins_sort(lst):
    for i in range(1, n):
        temp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > temp:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp
        print(*lst)


n = int(input())
lst = list(map(int, input().split()))
ins_sort(lst)
