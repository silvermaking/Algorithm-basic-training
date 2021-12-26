S = input()
n = len(S)
ans1 = 0
ans2 = 0

for i in range(n-2):
    if S[i:i+3] == 'KOI':
        ans1 += 1
    elif S[i:i+3] == 'IOI':
        ans2 += 1

print(ans1, ans2, sep='\n')