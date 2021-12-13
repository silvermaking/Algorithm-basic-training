"""
이유는 모르겠지만
int(input()) 으로 받아야 됨
"""
while True:
    N = int(input())
    if N == 0:
        break
    print(int(str(N)[::-1]), sum(map(int, str(N))))