"""
n개일 때
재귀 과정

1: hanoi(n-1) 을 1->2
2: n번째 원판을 1->3
3: hanoi(n-1) 을 2->3

"""


def hanoi(n, start, end):
    if n == 1:
        print(f'{n} : {start} -> {end}')
        return
    hanoi(n-1, start, 6-start-end)
    print(f'{n} : {start} -> {end}')
    hanoi(n-1, 6-start-end, end)


N = int(input())
hanoi(N, 1, 3)