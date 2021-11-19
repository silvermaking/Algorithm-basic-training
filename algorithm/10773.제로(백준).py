import sys
input = sys.stdin.readline

K = int(input())
lst = [int(input()) for _ in range(K)]
stack = []
for num in lst:
    stack.pop() if num == 0 else stack.append(num)
print(sum(stack))