"""
math
승수 이용
2: 2 4 8 6 반복
"""
for _ in range(int(input())):
    a, b = map(int, input().split())
    a = a % 10
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:  # 2개의 수 반복
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:  # 반복수 4개일 때
             print((a**4) % 10)
        else:
            print((a**b) % 10)
