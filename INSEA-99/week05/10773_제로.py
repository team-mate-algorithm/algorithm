# pypy3
# 시간(ms) : 132
# 공간(KB) : 114336

import sys
from collections import deque  
input = sys.stdin.readline


q = deque()
for _ in range(int(input().strip())) :
    k = int(input().strip())
    if k : q.append(k)  # 0이 아니면 추가
    else : q.pop()      # 0이면 최근 추가건 제거
print(sum(q))