def plates_h(plates):
    if plates:
        height = 10
    else:
        return 0

    n = len(plates)
    for i in range(1, n):
        if plates[i-1] != plates[i]:
            height += 10
        else:
            height += 5

    return height


plates = input()
print(plates_h(plates))