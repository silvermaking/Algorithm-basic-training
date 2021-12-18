import math

def is_prime_num(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return False
    return True


def find_prime_number(n):
    a = b = n
    while a > 1:
        if is_prime_num(a):
            break
        a -= 1
    while True:
        b += 1
        if is_prime_num(b):
            break

    if b - n == n - a:
        print(a, b)
    elif b - n > n - a:
        print(a)
    else:
        print(b)


T = int(input())
for _ in range(T):
    find_prime_number(int(input()))