# 11659 구간 합 구하기 4
# Python3, 메모리: 52312 KB, 시간: 204 ms
# PyPy3, 메모리: 121852 KB, 시간: 144 ms

import sys
input = sys.stdin.readline

N, M =  map(int, input().strip().split())
arr = list(map(int, input().split()))

# 누적합 배열 초기화 (0번째 인덱스는 0으로 패딩)
prefix_sum = [0] * (N + 1)

# (1 ~ i)까지의 누적합 계산
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

answers = []

# (i ~ j) 구간합 = prefix_sum[j] - prefix_sum[i - 1]
for _ in range(M):
    i, j = map(int, input().split())
    s = prefix_sum[j] - prefix_sum[i - 1]
    answers.append(s)

print('\n'.join(map(str, answers)))