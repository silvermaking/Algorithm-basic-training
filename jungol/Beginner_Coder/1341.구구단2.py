def multiplicationTable2(s, e):
    if s < e:
        for i in range(s, e+1):
            temp_s = 1
            temp_e = 4
            while temp_s < 10:
                temp = ''
                for j in range(temp_s, temp_e):
                    if j * i < 10:
                        temp += f'{i} * {j} =  {j * i}   '
                    else:
                        temp += f'{i} * {j} = {j * i}   '
                print(temp)
                temp_s += 3
                temp_e += 3
            print()

    else:
        for i in range(s, e-1, -1):
            temp_s = 1
            temp_e = 4
            while temp_s < 10:
                temp = ''
                for j in range(temp_s, temp_e):
                    if j * i < 10:
                        temp += f'{i} * {j} =  {j * i}   '
                    else:
                        temp += f'{i} * {j} = {j * i}   '
                print(temp)
                temp_s += 3
                temp_e += 3
            print()


s, e = map(int, input().split())
multiplicationTable2(s, e)
