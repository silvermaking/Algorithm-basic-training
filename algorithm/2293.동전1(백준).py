import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]
dp = [0] * (K + 1)
dp[0] = 1

for coin in coins:
    for j in range(coin, K+1):
        dp[j] += dp[j-coin]
print(dp[K])