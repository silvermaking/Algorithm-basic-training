st = []
for _ in range(int(input())):
    x = input()
    if x == "o":
        if st:
            d = st.pop()
            print(d)
        else:
            print("empty")
    elif x == "c":
        print(len(st))
    else:
        temp = x[2:]
        st.append(temp)

