# pypy3
# 시간(ms) : 92
# 공간(KB) : 109544


import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

sieve = [True] * (n + 1)
sieve[0] = sieve[1] = False

for i in range(2, int(n ** 0.5) + 1):   
    if sieve[i]:  # 소수라면 배수 제거
        for j in range(i * i, n + 1, i): # i*i보다 작은 배수는 중복 처리이기 때문에 i*i 부터 확인
            sieve[j] = False

primes = [i for i in range(m, n + 1) if sieve[i]]   # 범위 내 소수들

print(-1 if not primes else f"{sum(primes)}\n{primes[0]}")