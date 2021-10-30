"""
memoization(DP), 재귀
memo = [[0, 1, 0], [1, 0 , 1]]

기존 memoization에 0호출 횟수, 1 호출 횟수 추가
"""
import sys
input = sys.stdin.readline

def fibonacci(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append([fibonacci(n-1) + fibonacci(n-2),
                     memo[n-1][1] + memo[n-2][1],
                     memo[n-1][2] + memo[n-2][2]])
    return memo[n][0]


T = int(input())
for _ in range(T):
    N = int(input())
    memo = [[0, 1, 0], [1, 0, 1]]
    fibonacci(N)
    print(memo[N][1], memo[N][2])
