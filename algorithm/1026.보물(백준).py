"""
greedy
A_list 에서 가장 작은 값
B_list 에서 가장 큰 값
곱해줘서 list.pop()
=======
순열 => 시간초과
=======

"""
import sys
input = sys.stdin.readline

N = int(input())
A_list = list(map(int, input().strip().split()))
B_list = list(map(int, input().strip().split()))
i = 0
ans = 0
while i < N:
    a = A_list.pop(A_list.index(min(A_list)))
    b = B_list.pop(B_list.index(max(B_list)))
    ans += a * b
    i += 1

print(ans)