"""
2,2 (n//2)
(1, 1), (1, 2), (1,3)

"""

n = int(input())  # (1 <= 홀수 < 100)
arr = [[" " for _ in range(n)] for _ in range(n)]

def str_triangle():
    if not 1 <= n < 100 or not n%2:
        return print("INPUT ERROR")
    alphabet = 65
    k = -1
    for i in range(n//2, -1, -1):
        k += 1
        for j in range(n//2 - k, n//2 + k + 1):
            arr[j][i] = chr(alphabet)

            alphabet += 1

            if alphabet > 90:
                alphabet = 65

    for lst in arr:
        print(*lst)
    return

str_triangle()