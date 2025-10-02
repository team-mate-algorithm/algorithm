# pypy3
# 시간(ms) : 88
# 공간(KB) : 108384

import sys
input = sys.stdin.readline
MAX = 1000000000

def bs(left, right, x, y, z) :
    mid = (left + right) // 2   # 추가 게임 횟수
    while (left <= right) :
        if ((y + mid) * 100 // (x + mid) <= z) : left = mid + 1  # 초기승률이 추가게임승률보다 크거나 같은 경우 업데이트
        else : right = mid - 1                                   # 초기승률이 추가게임승률보다 작은 경우 업데이트
        mid = (left + right) // 2
    return mid + 1

x, y = map(int, input().strip().split())    # 입력 받기
z = y * 100 // x  
print(-1 if z >= 99 else bs(0, MAX, x, y, z))