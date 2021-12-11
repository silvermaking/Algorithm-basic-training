def star_triangle3(n):
    if not n % 2 or not 0 < n < 100:
        print("INPUT ERROR!")
        return

    x = 0
    for i in range(1, n+1, 2):
        print(' ' * x + '*' * i)
        x += 1

    x -= 2
    for i in range(n-2, 0, -2):
        print(' ' * x + '*' * i)
        x -= 1


star_triangle3(int(input()))