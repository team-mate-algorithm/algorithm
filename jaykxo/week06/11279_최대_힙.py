# 11279 최대 힙
# PyPy3, 메모리: 114200 KB, 시간: 148 ms
# Python3, 메모리: 41172 KB, 시간: 96 ms

# 최대 힙: 가장 큰 값이 항상 루트에 위치하도록 음수로 변환하여 저장

import heapq
import sys
input = sys.stdin.readline

N = int(input())
hq = []  
result = []  

for _ in range(N):
	x = int(input())

	# 1927 최소힙과 달리, 음수도 입력 가능하므로 0보다 클 때만 삽입
	if x > 0:
		heapq.heappush(hq, -x)  # 최대 힙 구현 (음수로 변환하여 저장)

	# 0일 때만 출력 명령 수행 (음수는 데이터로 간주)
	elif x == 0:
		if not hq:  # 힙이 비었으면 0 출력
			result.append(0)
		else:
			result.append(-heapq.heappop(hq))  # 힙에서 최대값 꺼내서 부호 복원

print('\n'.join(map(str, result)))  # 결과 한 번에 출력