# pypy3
# 시간(ms) : 160
# 공간(KB) : 240752

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(depth) :
    global n, m
    if depth == m : # m 길이라면 출력
        print(*anw)
    else :  # m 길이가 아니라면 탐색
        for num in range(1, n + 1) :
            if visited[num] == 0 :  # 아직 사용하지 않았다면 사용
                visited[num] = 1    # 방문처리
                anw[depth] = num    # 정답에 추가
                dfs(depth + 1)      # 탐색 지속

                visited[num] = 0    # 탐색 후 미방문 처리

n, m = map(int, input().split())
anw = [0] * m
visited = [0] * (n + 1)
dfs(0)
