num1 = int(input())
num2 = input()

# 3
num3 = num1 * int(num2[2])
print(num3)

# 4
num4 = num1 * int(num2[1])
print(num4)
num4 = int(str(num4) + '0')

# 5
num5 = num1 * int(num2[0])
print(num5)
num5 = int(str(num5) + '00')

num6 = num3 + num4 + num5
print(num6)