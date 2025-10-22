# 2164 카드2
# PyPy3, 메모리: 117336 KB, 시간: 124 ms
# Python3, 메모리: 51848 KB, 시간: 164 ms

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque(range(1, N+1))  # 1부터 N까지 카드 생성

# 카드가 한 장 남을 때까지 반복
while len(q) > 1:
	q.popleft()  # 맨 위 카드 버림
	q.append(q.popleft())  # 다음 카드를 맨 아래로 이동

print(q[0])  # 마지막 남은 카드 출력