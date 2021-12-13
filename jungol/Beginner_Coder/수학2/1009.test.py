while True:
    N = input()
    if N == "0":
        break

    reverse = N[::-1]
    plus = sum(map(int, N))

    print(int(reverse), plus)