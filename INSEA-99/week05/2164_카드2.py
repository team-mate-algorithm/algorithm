# pypy3
# 시간(ms) : 132
# 공간(KB) : 121240

import sys
from collections import deque  
input = sys.stdin.readline

n = int(input().strip())
q = deque(list(range(1, n+1)))    # 1~n 리스트 생성
while len(q) != 1 :             # 1개 남을 때까지 수행
    q.popleft()
    q.append(q.popleft())
print(q[0])