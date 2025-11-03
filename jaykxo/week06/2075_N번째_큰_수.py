# 2075 N번째 큰 수
# PyPy3, 메모리: 134040 KB, 시간: 444 ms
# Python3, 메모리 초과 ...

import heapq
import sys
input = sys.stdin.readline

N = int(input())
hq = []

# N×N 크기의 표 입력: 행렬 형태로 저장
board = [list(map(int, input().split())) for _ in range(N)]

# 각 열의 맨 아래 원소(해당 열의 최댓값)를 초기 후보로 힙에 삽입
for c in range(N):

	# (-값, 행, 열) 형태로 저장 → 최대값부터 pop할 수 있게 구성
	heapq.heappush(hq, (-board[N-1][c], N-1, c))

answer = 0

# 힙에서 가장 큰 값부터 N번 꺼내며 N번째로 큰 수를 찾음
for _ in range(N):

	# 힙에서는 가장 작은 음수지만, 실제로는 가장 큰 값 pop
	neg, r, c = heapq.heappop(hq)

	# 음수를 다시 양수로 변환하여 실제 값 저장
	answer = -neg

	# 같은 열에서 바로 위에 있는 값이 남아 있다면
	if r - 1 >= 0:

		# 해당 열의 위쪽 원소를 다음 후보로 힙에 추가
		heapq.heappush(hq, (-board[r-1][c], r-1, c))

print(answer)