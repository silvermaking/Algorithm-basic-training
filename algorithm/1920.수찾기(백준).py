import sys
input = sys.stdin.readline

def binary_search(target, start, end, lst):
    if start > end:
        return print(0)

    mid = (start + end) // 2

    if lst[mid] == target:
        return print(1)
    elif lst[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search(target, start, end, lst)

N = int(input())
lst = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))
for target in targets:
    binary_search(target, 0, N-1, lst)

