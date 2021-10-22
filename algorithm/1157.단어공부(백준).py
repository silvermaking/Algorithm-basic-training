"""
문자열, 구현
sys 사용할 때는 strip() 붙이기  (에러나는경우가 있음)
.count()  : 단어수 세기
.index()  : 정답 도출
"""
import sys

words = sys.stdin.readline().strip().upper()
unique_words = list(set(words))
cnt_list = []
for word in unique_words:
    cnt_list.append(words.count(word))

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(unique_words[cnt_list.index(max(cnt_list))])


