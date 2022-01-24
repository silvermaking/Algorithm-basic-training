"""
소문자 : 97 ~ 122
대문자 : 65 ~ 90
"""
password_dict = dict()
password_dict[" "] = " "
password = input()
words = input()
number = 97
NUMBER = 65
for a in password:
    password_dict[chr(number)] = a
    password_dict[chr(NUMBER)] = a.upper()
    number += 1
    NUMBER += 1

for word in words:
    print(password_dict[word], end='')

