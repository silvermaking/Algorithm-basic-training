"""
memoization
재귀
"""
import time
import sys
n = int(sys.stdin.readline())
start = time.time()
memo = [0, 1]
def fibo(n): #memoization
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

def fibo1(n): #기본
    if n < 2:
        return n
    return fibo1(n-1) + fibo1(n-2)

print(fibo(n))
print(fibo1(n))
print(time.time() - start)
