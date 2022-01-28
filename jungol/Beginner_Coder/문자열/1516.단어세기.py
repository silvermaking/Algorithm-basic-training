while True:
    words = input()
    if words == 'END':
        break
    word_dict = {}
    word_list = words.split()
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    word_dict = sorted(word_dict.items())

    for dic in word_dict:
        print(f'{dic[0]} : {dic[1]}')
