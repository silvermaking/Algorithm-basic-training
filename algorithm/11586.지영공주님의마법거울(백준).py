"""
문자열, 구현
readline() 은 뒤의 개행문자(ex, '\n') 까지 받아옴
strip() 추가해주기
----------------
1 => 그대로
2 => 좌/우 반전
3 => 상/하 반전

"""
import sys
input = sys.stdin.readline
N = int(input())
picture = [input().strip() for _ in range(N)]
type123 = int(input())
if type123 == 1:
    print(*picture, sep='\n')
elif type123 == 2:
    print(*[i[::-1] for i in picture], sep='\n')
elif type123 == 3:
    print(*picture[::-1], sep='\n')

