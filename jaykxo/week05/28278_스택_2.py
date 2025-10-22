# 28278 스택 2
# PyPy3, 메모리: 191116 KB, 시간: 372 ms
# Python3, 메모리: 74472 KB, 시간: 616 ms

import sys
input = sys.stdin.readline

N = int(input())
stack = []  # 스택 저장 리스트
result = []  # 출력 결과 저장

for _ in range(N):
    cmd = input().split()
    op = cmd[0]  # 명령어 번호 (1~5)

    if op == '1':  # push
        x = int(cmd[1])
        stack.append(x)
    elif op == '2':  # pop, 비어있으면 -1
        if not stack:
            result.append('-1')
        else:
            result.append(str(stack.pop()))
    elif op == '3':  # 현재 스택 크기
        result.append(str(len(stack)))
    elif op == '4':  # 비었으면 1, 아니면 0
        if not stack:
            result.append('1')
        else:
            result.append('0')
    elif op == '5':  # 맨 위 원소, 없으면 -1
        if not stack:
            result.append('-1')
        else:
            result.append(str(stack[-1]))

print('\n'.join(result))