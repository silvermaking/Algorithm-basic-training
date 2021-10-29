"""
brute-force
------------------
1씩 증가시키면서
'666' 문자열이 포함되어있는 순으로 체크
"""
import sys
input = sys.stdin.readline

N = int(input().strip())
devil = 666
cnt = 0
while True:
    if '666' in str(devil):
        cnt += 1
    if cnt == N:
        print(devil)
        break
    devil += 1