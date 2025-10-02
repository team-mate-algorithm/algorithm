# 10816 숫자 카드 2
# 메모리: 117520 KB, 시간: 1384 ms


import bisect  # 이분 탐색을 내장 함수로 제공
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()  # 이분 탐색을 위한 정렬
M = int(input())
K = list(map(int, input().split()))

# bisect_left, bisect_right 내장 함수를 이용하여 구간(개수) 계산
for t in K:
  left = bisect.bisect_left(A, t)  # t가 처음 등장하는 인덱스
  right = bisect.bisect_right(A, t)  # t가 마지막으로 끝난 뒤 인덱스
  count = (right - left)  # 두 위치 차이가 t의 개수
  
  print(count, end=" ")  # 개수를 공백으로 구분하여 출력