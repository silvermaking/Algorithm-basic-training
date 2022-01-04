N, B = map(int, input().split())
hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def binary(ans, n):
    if n <= 1:
        return print(str(n) + ans)

    binary(str(n % 2) + ans,  n // 2)


def octal(ans, n):
    if n <= 7:
        return print(str(n) + ans)

    octal(str(n % 8) + ans, n // 8)


def hex_sub(n):
    if n < 10:
        return str(n)
    return hex_dict[n]


def hexadecimal(ans, n):
    if n <= 15:
        return print(hex_sub(n)+ ans)

    hexadecimal(str(hex_sub(n % 16)) + ans, n // 16)


if B == 2:
    binary("", N)
elif B == 8:
    octal("", N)
else:
    hexadecimal("", N)
