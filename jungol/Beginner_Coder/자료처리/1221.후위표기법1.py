n = int(input())
n_list = list(input().split())
stack = []

for i in n_list:
    if i.isdigit():
        stack.append(int(i))
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            temp = b + a
        elif i == '-':
            temp = (b - a)
        elif i == '*':
            temp = b * a
        else:
            temp = (b // a)

        stack.append(temp)
print(temp)
