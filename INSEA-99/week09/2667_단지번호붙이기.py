# pypy3
# 시간(ms) : 108
# 공간(KB) : 113496

import sys
from collections import deque
input = sys.stdin.readline
# 방향: ↑, ↓, ←, → 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    global n
    map[r][c] = 0 # 방문 처리 (1 -> 0으로 변경하여 재방문 방지)
    cnt = 1  # 현재 위치의 집을 카운트

    # 4방향 탐색
    for d in range(4):
        nr = r + dr[d]  # 다음 행 위치
        nc = c + dc[d]  # 다음 열 위치

        # 범위 내에 있고, 집이 있는 경우(map[nr][nc] == 1)
        if 0 <= nr < n and 0 <= nc < n and map[nr][nc] == 1:
            cnt += dfs(nr, nc)  # 재귀적으로 DFS 수행하여 카운트 누적

    return cnt

n = int(input())  # 지도의 크기 N
map = [list(map(int, input().strip())) for _ in range(n)]  # N×N 지도 (0: 집 없음, 1: 집 있음)

anw = []  # 각 단지별 집의 개수를 저장할 리스트

# 전체 지도를 순회하며 단지 찾기
for r in range(n):
    for c in range(n):
        # 집이 있고 아직 방문하지 않은 경우
        if map[r][c] == 1:
            anw.append(dfs(r, c))  # BFS로 단지 크기 계산 후 저장

# 출력
print(len(anw))  # 총 단지 수
print(*sorted(anw), sep='\n')  # 각 단지 내 집의 수를 오름차순으로 출력