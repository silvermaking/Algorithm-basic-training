"""
부분집합
backtraking
"""
def dfs(idx, score, kcal):
    global max_score
    if kcal > L:
        return
    if score > max_score:
        max_score = score

    if idx == N:
        return

    dfs(idx+1, score, kcal)
    dfs(idx+1, score + hamburgers[idx][0], kcal + hamburgers[idx][1])

for tc in range(1, int(input()) + 1):
    #N: 재료의 수, L: 제한 칼로리
    N, L = map(int, input().split())
    hamburgers = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    dfs(0, 0, 0)
    print(f'#{tc} {max_score}')