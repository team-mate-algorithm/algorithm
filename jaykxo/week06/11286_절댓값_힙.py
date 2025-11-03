# 11286 절댒값 힙
# PyPy3, 메모리: 116424 KB, 시간: 168 ms
# Python3, 메모리: 43168 KB, 시간: 120 ms

# 절댓값 힙: 절댓값이 가장 작은 값이 먼저 나오며, 같을 경우 실제 값이 작은 수(음수)가 우선

import heapq
import sys
input = sys.stdin.readline

N = int(input())
hq = []  
result = []  

for _ in range(N):
    x = int(input())
    
    if x != 0:
        heapq.heappush(hq, (abs(x), x))  # (절댓값, 실제값) 튜플형태로 저장 → 절댓값 기준, 동률 시 실제값 기준 정렬
    else:
        if not hq:  # 힙이 비었으면 0 출력
            result.append(0)
        else:
            result.append(heapq.heappop(hq)[1])  # 힙에서 (abs, 값) 튜플을 꺼내 실제값 출력

print('\n'.join(map(str, result))) 