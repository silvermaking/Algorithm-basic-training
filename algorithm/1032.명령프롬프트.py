import sys

input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
ans = list(words[0])
for word in words:
    for i in range(len(word)):
        if ans[i] == word[i] or ans[i] == '?':
            continue
        ans[i] = '?'

for a in ans:
    print(a, end='')