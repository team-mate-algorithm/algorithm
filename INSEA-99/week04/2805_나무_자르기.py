# pypy3
# 시간(ms) : 460
# 공간(KB) : 258500

import sys
input = sys.stdin.readline

def count(h):  # h미터로 자르고 남은 나무 길이 합 구하기
    n = 0
    for tree in trees:
        if tree-h > 0:
            n+= tree-h
    return n

def bs(N):
    left = 0
    right = trees[-1]
    mid = right // 2
    
    while left <= right:
        m = count(mid)
        if m < N: right = mid-1     # 가져가야하는 길이보다 적은 경우
        elif m >=  N: left = mid+1  # 가져가야하는 길이보다 많거나 같은 경우 (최대 H를 구해야하므로 중지하지 않고 진행)
        mid = (left+right)//2
    return mid 


k, N = map(int, input().strip().split())
trees = sorted(list(map(int, input().strip().split())))
print(bs(N))