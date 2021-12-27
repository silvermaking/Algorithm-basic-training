def sel_sort(a):
    for i in range(n-1):
        min_idx = i
        for j in range(i, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

        print(*a)


n = int(input())
lst = list(map(int, input().split()))
sel_sort(lst)