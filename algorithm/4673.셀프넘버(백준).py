def self_number(n):
    if n > 10000:
        return
    temp = n
    temp += n // 1000 + (n % 1000) // 100 + (n % 100) // 10 + n % 10
    return temp

nums = set()
for i in range(1, 10001):
    nums.add(self_number(i))

for i in range(1, 10001):
    if i not in nums:
        print(i)