def multiplicationTable(s, e):
    if not 2 <= s <= 9 or not 2 <= e<= 9:
        print("INPUT ERROR!")
        s, e = map(int, input().split())
        multiplicationTable(s, e)
        return

    if s < e:
        for i in range(1, 10):
            temp = ''
            for j in range(s, e+1):
                if j * i < 10:
                    temp += f'{j} * {i} =  {j * i}   '
                else:
                    temp += f'{j} * {i} = {j * i}   '
            print(temp)

    else:
        for i in range(1, 10):
            temp = ''
            for j in range(s, e-1, -1):
                if j * i < 10:
                    temp += f'{j} * {i} =  {j * i}   '
                else:
                    temp += f'{j} * {i} = {j * i}   '
            print(temp)


s, e = map(int, input().split())
multiplicationTable(s, e)
