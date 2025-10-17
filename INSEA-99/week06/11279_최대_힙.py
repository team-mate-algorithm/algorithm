# pypy3
# 시간(ms) : 164
# 공간(KB) : 10604

import sys
import heapq
input = sys.stdin.readline

pq = []
for _ in range(int(input().strip())) :
    x = int(input().strip())
    if x : heapq.heappush(pq, -x)                       # 0이 아닌 경우 추가
    else : print(-heapq.heappop(pq) if len(pq) else 0)  # 0인 경우 길이가 0이 아니면 pop, 맞다면 0 출력