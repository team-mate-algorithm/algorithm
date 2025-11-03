# 18258 큐 2
# PyPy3, 메모리: 225152 KB, 시간: 776 ms
# Python3, 메모리: 136696 KB, 시간: 1388 ms

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()  # 큐 저장용 덱
result = []  # 출력 결과 저장

for _ in range(N):
	cmd = input().split()
	op = cmd[0]  # 명령어 종류 (push, pop, size, empty, front, back)

	if op == 'push':  # push: 큐에 값 추가
		X = int(cmd[1])
		queue.append(X)

	elif op == 'pop':  # pop: 맨 앞 값 제거, 없으면 -1
		if not queue:
			result.append('-1')
		else:
			result.append(str(queue.popleft()))  # 메서드 한 줄만 써먹음,,

	elif op == 'size':  # 큐 크기 출력
		result.append(str(len(queue)))

	elif op == 'empty':  # 큐가 비었는지 여부 출력
		if not queue:
			result.append('1')
		else:
			result.append('0')

	elif op == 'front':  # 맨 앞 값 출력, 없으면 -1
		if not queue:
			result.append('-1')
		else:
			result.append(str(queue[0]))

	elif op == 'back':  # 맨 뒤 값 출력, 없으면 -1
		if not queue:
			result.append('-1')
		else:
			result.append(str(queue[-1]))

print('\n'.join(result))