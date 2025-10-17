# pypy3
# 시간(ms) : 932 
# 공간(KB) : 162568

import sys
from collections import deque
input = sys.stdin.readline

# 명령어 수행 할 함수 정의
def push_queue(x): queue.append(int(x))
def pop_queue(): return queue.popleft() if queue else -1
def get_queue_size(): return len(queue)
def is_queue_empty(): return 1 if not queue else 0
def queue_front(): return queue[0] if queue else -1
def queue_back(): return queue[-1] if queue else -1

# 명령어와 함수 맵핑
commands = {
    'push': push_queue,
    'pop': pop_queue,
    'size': get_queue_size,
    'empty': is_queue_empty,
    'front': queue_front,
    'back': queue_back,
}

queue = deque() # queue 선언
for _ in range(int(input().strip())) :
    cmd = list(input().strip().split())
    result = commands[cmd[0]](*cmd[1:])  # 명령어 dict을 이용하여 함수 실행
    if result is not None : print(result)
