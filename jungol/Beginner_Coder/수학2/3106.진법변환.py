change_dict = dict()
for i in range(10, 36):
    change_dict[i] = chr(i + 55)

dec_dict = dict()
for i in range(10, 36):
    dec_dict[chr(i + 55)] = i

def dec_sub(n):
    if n < 10:
        return str(n)
    return change_dict[n]

def dec_sub2(n):
    if n.isdigit() and int(n) < 10:
        return n
    return dec_dict[n]

def a_to_dec(a, s):
    ans = 0
    x = 0
    for i in range(len(s)-1, -1, -1):
        ans += int(dec_sub2(s[i])) * (int(a) ** x)
        x += 1
    return ans


def dec_to_b(ans, n):

    if n < b:
        return print(dec_sub(n) + ans)

    dec_to_b(str(dec_sub(n % b)) + ans, n // b)


while True:
    x = input()
    if x == "0":
        break

    a, s, b = x.split()
    dec_num = a_to_dec(a, s)
    b = int(b)
    dec_to_b("", dec_num)