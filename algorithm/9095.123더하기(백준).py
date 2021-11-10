"""
dp
1 : 1
2 : 1+1, 2
3 : 1+1+1, 1+2, 2+1, 3
4 : 3번째 case + 1 , 2번째 case + 2, 1번째 case + 3
...
n : [n-1] + [n-2] + [n-3]

"""
import sys
input = sys.stdin.readline

T = int(input())
dp = [1, 2, 4]
for i in range(3, 10):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for i in range(T):
    N = int(input())
    print(dp[N-1])