# pypy3
# 시간(ms) : 116
# 공간(KB) : 245360
#
# 공유 :
# - 예시가 이진트리라서 이진트리인줄 알았는데 그런 언급은 없어서 3개 이상의 자식 노드 고려 필요했음

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(root):
    """현재 노드에서 가장 긴 경로의 길이를 반환"""
    global ans
    visited[root] = True
    dist = [0, 0]   # 가장 긴 두 경로를 저장
    for neighbor, weight in adj[root]:
        if not visited[neighbor]:
            maintain_top_two(dist, dfs(neighbor) + weight)  # 자식 노드로부터 가장 긴 경로 + 간선 가중치
    
    ans = max(ans, dist[0] + dist[1])   # 가장 긴 두 경로를 합쳐서 지름 후보 갱신
    return dist[0]

def maintain_top_two(list, n):
    """리스트에서 가장 큰 두 값을 유지"""
    if n > list[0]:
        list[1] = list[0]
        list[0] = n
    elif n > list[1]:
        list[1] = n

n = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(n-1):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

ans = 0 
dfs(1)
print(ans)