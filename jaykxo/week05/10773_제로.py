# 10773 제로
# PyPy3, 메모리: 114580 KB, 시간: 112 ms
# Python3, 메모리: 33192 KB, 시간: 68 ms

import sys
input = sys.stdin.readline

N = int(input())
stack = []  # 숫자를 저장할 스택

for _ in range(N):
	num = int(input())

	if num != 0:  # 0이 아니면 스택에 추가
		stack.append(num)
	else:  # 0이면 마지막 숫자 제거
		stack.pop()

print(sum(stack))  # 남은 숫자들의 합 출력