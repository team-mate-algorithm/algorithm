# pypy3
# 시간(ms) : 476
# 공간(KB) : 140540

import sys
from collections import deque
input = sys.stdin.readline

# 명령어 수행 할 함수 정의
def push_stack(x): stack.append(x)
def pop_stack(): return stack.pop() if stack else -1
def get_stack_size(): return len(stack)
def is_stack_empty(): return 1 if not stack else 0
def peek_stack(): return stack[-1] if stack else -1

# 명령어와 함수 맵핑
commands = {
    1: push_stack,
    2: pop_stack,
    3: get_stack_size,
    4: is_stack_empty,
    5: peek_stack
}

stack = deque() # stack 선언
for _ in range(int(input().strip())) :
    cmd = list(map(int, input().strip().split()))
    result = commands[cmd[0]](*cmd[1:])  # 명령어 dict을 이용하여 함수 실행
    if result is not None : print(result)


