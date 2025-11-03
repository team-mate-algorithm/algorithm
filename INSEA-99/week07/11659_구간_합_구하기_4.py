# pypy3
# 시간(ms) : 172
# 공간(KB) : 127164

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
sum_arr = [0] # 누적합 리스트
arr = list(map(int, input().strip().split())) # input list

sum = 0
for x in arr :  # 누적합 구하기
    sum+=x
    sum_arr.append(sum)

for _ in range(m) : # 구간합 구하기
    l, r = map(int, input().strip().split())
    print(sum_arr[r] - sum_arr[l-1])