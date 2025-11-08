# 2960 에라토스테네스의 체
# Python3, 메모리: 32412 KB, 시간: 32 ms
# PyPy3, 메모리: 109544 KB, 시간: 88 ms

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

prime = [True] * (N + 1)
cnt = 0

for i in range(2, N + 1):

    # 아직 지우지 않은 수 중 가장 작은 수를 찾는다 → 이 수가 P이다 (소수)
    if prime[i]:
        for j in range(i, N + 1, i):
            if prime[j]:
                # 아직 지우지 않은 P의 배수를 크기 순서대로 지운다
                prime[j] = False
                cnt += 1
                if cnt == K:             # K번째로 지워진 수를 찾으면 출력
                    print(j)
                    raise SystemExit
