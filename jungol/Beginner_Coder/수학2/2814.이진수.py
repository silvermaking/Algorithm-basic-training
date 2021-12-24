bin_num = input()[::-1]

i = 0
dec_num = 0
for num in bin_num:
    if int(num):
        dec_num += 2 ** i
    i += 1

print(dec_num)
