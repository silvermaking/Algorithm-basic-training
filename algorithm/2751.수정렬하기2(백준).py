import sys

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
"""
1번풀이 : 내장함수
"""
lst.sort()

for i in lst:
    print(i)
"""
2번 풀이 : merge sort 
"""
### 병합정렬 0(nlogn) 시간초과
def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    left_lst = merge_sort(lst[:mid])
    right_lst = merge_sort(lst[mid:])

    temp = []
    l = h = 0 # low, hight
    while l < len(left_lst) and h < len(right_lst): #비교 & 정렬
        if left_lst[l] < right_lst[h]:
            temp.append(left_lst[l])
            l += 1
        else:
            temp.append(right_lst[h])
            h += 1
    # 남은거(정렬할 필요없는것들) 병합
    temp += left_lst[l:]
    temp += right_lst[h:]
    return temp

# lst2 = merge_sort(lst)
# for i in lst2:
#     print(i)