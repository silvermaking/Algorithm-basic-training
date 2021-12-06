import math
n = int(input())
lst1 = [1]
lst2 = [n]
for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
        if (n // i) == i:
            lst1.append(i)
            continue
        lst1.append(i)
        lst2.append(n // i)

lst = lst1 + lst2[::-1]
print(*lst)