ans_list = []
while True:
    x = input()
    if x == 'END':
        break

    words = x.split()
    for word in words:
        if word in ans_list: continue
        ans_list.append(word)

    print(*ans_list)
