# pypy3
# 시간(ms) : 1028
# 공간(KB) : 122816
#
# 공유 : 
# - int(1_000_000_000)은 약 29바이트
# - 1500개 -> 약 0.05 MB
# - 1500*1500개 -> 약 77 MB


import sys
import heapq
input = sys.stdin.readline

pq = []
n = int(input().strip())
for _ in range(n):
    for x in list(map(int, input().strip().split())) :
        if len(pq) < n : heapq.heappush(pq, x)                   # 리스트가 n개 이하면 추가
        else : heapq.heappush(pq, max(x, heapq.heappop(pq)))  # 리스트가 n개 이상이면 리스트의 가장 작은 값보다 크다면 추가
print(heapq.nsmallest(1, pq)[0])
