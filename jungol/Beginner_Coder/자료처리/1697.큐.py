"""
1102번 처럼 푸는데 안됨(문제 오류같음)
--> list(input.split)으로 요소를 직접 나눔

"""
q = []
for i in range(int(input())):
    x = list(input().split())
    if x[0] == 'o':
        if q:
            print(q.pop(0))
        else:
            print('empty')
    elif x[0] == 'c':
        print(len(q))
    else:
        temp = x[1]
        q.append(temp)

