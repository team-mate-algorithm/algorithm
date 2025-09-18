# 2750 수 정렬하기
# 메모리: 32412 KB, 시간: 40 ms

import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

A.sort()  # 리스트 오름차순 정렬

for num in A:
  print(num)