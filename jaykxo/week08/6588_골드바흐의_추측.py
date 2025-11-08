# 6588 골드바흐의 추측
# Python3, 시간 초과........
# PyPy3, 메모리: 130980 KB, 시간: 440 ms

import sys
input = sys.stdin.readline

MAX_N = 1_000_000  # 문제 제한: n ≤ 1,000,000 → 한 번만 체를 만들어 재사용

# --- [준비 단계] 에라토스테네스의 체로 0~MAX_N까지 소수 여부 미리 계산 ---
prime = [True] * (MAX_N + 1)
prime[0] = prime[1] = False          

# i가 소수(True)면 i*i부터 i의 배수들을 소수 아님(False)으로 표시
# - i*i 이전의 배수들은 더 작은 소수에서 이미 처리됨(중복 제거를 위한 최적화)
for i in range(2, int(MAX_N ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            prime[j] = False

# --- [입력 & 처리] 여러 줄의 짝수 n을 받으며, 0이 나오면 종료 ---
result = []
while True:
    n = int(input())
    if n == 0:                       # 종료 신호
        break

    # --- [골드바흐 쌍 탐색] n = a + b (a, b 모두 소수) ---
    # 탐색 전략:
    # 1) a ≤ b만 보면 충분 → a는 3부터 n//2까지
    # 2) 2를 제외하면 짝수는 소수가 아니므로, a는 홀수만 확인(3,5,7,...) → step=2
    # 3) b는 n - a 로 자동 결정되므로, prime[a]와 prime[b]만 빠르게 체크
    found = False
    for a in range(3, (n // 2) + 1, 2):
        b = n - a
        if prime[a] and prime[b]:    # 두 수가 모두 소수면 골드바흐 표현 성립
            result.append(f"{n} = {a} + {b}")
            found = True
            break                     # 가장 먼저 찾은 한 쌍을 출력 형식대로 사용

    # 문제 형식상 항상 존재한다고 가정하지만, 못 찾으면 아래 문구 출력
    if not found:
        result.append("Goldbach's conjecture is wrong.")

print('\n'.join(result))