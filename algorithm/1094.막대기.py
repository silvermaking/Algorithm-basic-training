X = int(input())

sticks = [64, 32, 16, 8, 4, 2, 1]
cnt = 0

for stick in sticks:
    if X >= stick:
        X -= stick
        cnt += 1

    if X == 0:
        break
print(cnt)