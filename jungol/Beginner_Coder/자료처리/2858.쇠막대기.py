laser_list = input()
st = []
ans = 0

for i in range(len(laser_list)):
    if laser_list[i] == "(":
        st.append(laser_list[i])

    elif laser_list[i] == ")":
        st.pop()
        if laser_list[i-1] == "(":
            ans += len(st)
        else:
            ans += 1

print(ans)