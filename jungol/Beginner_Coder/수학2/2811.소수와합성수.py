import math


def is_prime_or_composite(n):
    if n == 1:
        return "number one"

    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return "composite number"
    return "prime number"


n_list = list(map(int, input().split()))
for n in n_list:
    print(is_prime_or_composite(n))