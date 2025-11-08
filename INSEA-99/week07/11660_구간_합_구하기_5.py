# pypy3
# 시간(ms) : 276
# 공간(KB) : 120516
#
# 공유 : 
# - enumerate : 파이썬에서 반복문을 쓸 때, 인덱스(index)와 값(value)를 동시에 얻을 수 있게 해주는 내장 함수
# 
#     fruits = ['apple', 'banana', 'cherry']
# 
#     ex1) 
#     for i, fruit in enumerate(fruits):
#         print(i, fruit)
#     ->
#     0 apple
#     1 banana
#     2 cherry  
# 
#     ex2)
#     for i, fruit in enumerate(fruits, start=1):
#         print(i, fruit) 
#     ->
#     1 apple
#     2 banana
#     3 cherry

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
sum_arr = [[0]*(n + 1) for _ in range(n + 1)]   # 누적합 리스트

for i in range(1, n + 1) :  # 누적합 구하기
    for j, x in enumerate(list(map(int, input().strip().split())), start=1) :
         sum_arr[i][j] = x + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1]

for _ in range(m) : # 누적합 이용해서 답 구하기
    x1, y1, x2, y2 = map(int, input().strip().split())
    print(sum_arr[x2][y2] - sum_arr[x2][y1-1] - sum_arr[x1-1][y2] + sum_arr[x1-1][y1-1])