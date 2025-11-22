# pypy3
# 시간(ms) : 152
# 공간(KB) : 115588
#
# 공유 : 
# - 정상인과 적록색약이 겹치는 구역이 있어 동시에 탐색하는게 좋지 않을까 생각
# - 함수는 한가지 기능만 구현하는게 좋은데, 위 방식은 2가지를 한 번에 탐색하려해서 코드 복잡도가 올라감
# - 오히려 코드 리뷰/유지보수 측면에서 안좋고 디버깅하기 어려움
# - 결론 : 따로 탐색하는게 낫다. 미세한 성능차이를 얻으려다 많은 것을 잃는다약간의 

import sys
from collections import deque
input = sys.stdin.readline
# 방향: ↑, ↓, ←, → 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, is_normal, is_colorblind):
    """
    정상인과 적록색약인 사람의 구역을 동시에 탐색하는 BFS
    :param r, c: 시작 좌표
    :param is_normal: 정상인 시각으로 탐색할지 여부
    :param is_colorblind: 적록색약 시각으로 탐색할지 여부
    """
    global n
    dq = deque([(r, c, is_normal, is_colorblind)])

    while dq:
        r, c, is_normal, is_colorblind = dq.popleft()  # BFS는 FIFO

        # 상하좌우 4방향 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 범위 체크: 벗어나면 스킵
            if not (0 <= nr < n and 0 <= nc < n):
                continue

            n_is_normal = n_is_colorblind = False

            # 정상인 시각: 같은 색(R, G, B)끼리만 연결
            if is_normal and not normal_visited[nr][nc] and area[nr][nc] == area[r][c]:
                normal_visited[nr][nc] = True
                n_is_normal = True

            # 적록색약 시각: R과 G는 같은 색으로 취급, B는 따로
            if is_colorblind and not colorblind_visited[nr][nc]:
                # (현재와 다음이 모두 R 또는 G) 또는 (같은 색)이면 연결
                if (area[r][c] in 'RG' and area[nr][nc] in 'RG') or area[r][c] == area[nr][nc]:
                    colorblind_visited[nr][nc] = True
                    n_is_colorblind = True

            # 하나라도 방문했으면 큐에 추가
            if n_is_normal or n_is_colorblind:
                dq.append((nr, nc, n_is_normal, n_is_colorblind))


# 입력
n = int(input())
area = [list(input().strip()) for _ in range(n)]

# 구역 개수 카운트
normal_area = 0
colorblind_area = 0

# 방문 체크 배열
normal_visited = [[False] * n for _ in range(n)]
colorblind_visited = [[False] * n for _ in range(n)]

# 모든 칸을 순회하며 새로운 구역 발견 시 BFS 시작
for r in range(n):
    for c in range(n):
        is_normal = False
        is_colorblind = False

        # 정상인 시각에서 미방문 구역이면 새 구역 시작
        if not normal_visited[r][c]:
            normal_visited[r][c] = True
            is_normal = True
            normal_area += 1

        # 적록색약 시각에서 미방문 구역이면 새 구역 시작
        if not colorblind_visited[r][c]:
            colorblind_visited[r][c] = True
            is_colorblind = True
            colorblind_area += 1

        # 하나라도 새 구역이면 BFS로 연결된 칸 모두 방문 처리
        if is_normal or is_colorblind:
            bfs(r, c, is_normal, is_colorblind)

print(normal_area, colorblind_area)