def factorial(n):
    if n == 1:
        print(f'1! = 1')
        return 1
    print(f'{n}! = {n} * {n-1}!')
    return n * factorial(n-1)


n = int(input())
print(factorial(n))