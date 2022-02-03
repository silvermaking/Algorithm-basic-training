lst = [int(input()) for _ in range(9)]
max_ans = max(lst)
idx = lst.index(max_ans)
print(max_ans, idx + 1, sep='\n')