# pypy3
# 시간(ms) : 136
# 공간(KB) : 238864

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(depth, pre_num) :
    global n, m
    if depth == m : # m 길이라면 출력
        print(*anw)
    else :  # m 길이가 아니라면 탐색
        for num in range(pre_num, n + 1) :  # 비내림차순을 위해 이전 숫자부터 탐색
                anw[depth] = num    # 정답에 추가
                dfs(depth + 1, num)      # 탐색 지속

n, m = map(int, input().split())
anw = [0] * m
dfs(0, 1)
