# pypy3
# 재귀
# 시간(ms) : 568
# 공간(KB) : 346740
#
# 스택
# 시간(ms) : 320
# 공간(KB) : 136564
#
# 공유 : 
# - 스택(반복문) DFS가 재귀 DFS보다 대부분 더 빠르다. 그리고 안정성도 높다.
# - 파이썬은 재귀에 최적화 되어 있지 않고, 재귀는 함수를 호출하는거라 호출할 때마다 오버헤드가 발생한다.


import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# 재귀를 이용한 dfs
def dfs(node):
    global idx
    visited[node] = idx
    idx += 1
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor)

n, m, r = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
idx = 1
for _ in range(m):  # 인접리스트 생성
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for neighbors in adj:   # 인접리스트 정렬
    neighbors.sort(reverse=True)

dfs(r)
print(*visited[1:], sep='\n')

# # 스택을 이용한 dfs
# def dfs2(start):
#     idx = 1
#     queue = deque([start])
#     while queue:
#         node = queue.popleft()
#         if not visited[node]:
#             visited[node] = idx
#             idx += 1
#             for neighbor in adj[node]:
#                 if not visited[neighbor]:
#                     queue.appendleft(neighbor)

# n, m, r = map(int, input().split())
# adj = [[] for _ in range(n+1)]
# visited = [0] * (n+1)
# for _ in range(m):   # 인접리스트 생성
#     u, v = map(int, input().split())
#     adj[u].append(v)
#     adj[v].append(u)

# for neighbors in adj: # 인접리스트 정렬
#     neighbors.sort()              

# dfs2(r)     
# print(*visited[1:], sep='\n')