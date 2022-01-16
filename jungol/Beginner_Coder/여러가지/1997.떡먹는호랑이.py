memo = [1, 1]
def fibo(n): #memoization
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

tmp = fibo(30)
D, K = map(int, input().split())
a = 1  # D -2
b = 1  # D - 1
x = memo[D-3]
y = memo[D-2]
while True:
    while b * y < K - a * x:
        b += 1

    if b * y == K - a * x:
        print(a, b, sep="\n")
        break
    a += 1
    b = a

