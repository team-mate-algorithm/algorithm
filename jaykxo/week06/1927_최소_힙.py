# 2075 최소 힙
# PyPy3, 메모리: 114204 KB, 시간: 148 ms
# Python3, 메모리: 41172 KB, 시간: 92 ms

# 최소 힙: 가장 작은 값이 항상 루트에 위치하도록 자동 정렬됨

import heapq
import sys
input = sys.stdin.readline

N = int(input())
hq = []  
result = []  

for _ in range(N):
	x = int(input())

	if x != 0:  # 0이 아니면 힙에 추가
		heapq.heappush(hq, x)  # 힙에 값 추가 (자동으로 최소값이 루트로 정렬)

	else:  # 0이면 최소값 출력 (없으면 0)
		if not hq:
			result.append(0)
		else:
			result.append(heapq.heappop(hq))  # 힙에서 최소값 꺼냄

print('\n'.join(map(str, result)))