"""
set 으로 만들면  a in b 해도 빠름
이진탐색
"""

import sys
input = sys.stdin.readline

def binary_search(target, start, end, lst):
    if start > end:
        ans.append(0)
        return

    mid = (start + end) // 2

    if lst[mid] == target:
        ans.append(1)
        return
    elif lst[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search(target, start, end, lst)

N = int(input())
lst = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))
ans = []
for target in targets:
    binary_search(target, 0, N-1, lst)

print(*ans)
