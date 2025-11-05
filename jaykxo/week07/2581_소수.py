# 2581 소수
# Python3, 메모리: 32412 KB, 시간: 40 ms
# PyPy3, 메모리: 110736 KB, 시간: 100 ms

import sys
input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return False
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            return False
    return True             # 위 조건 통과 시 소수

# -------------------- main --------------------

M = int(input())
N = int(input())   

primes = []

for i in range(M, N + 1):
    if is_prime(i):
        primes.append(i)

if not primes:
    print(-1)

else: 
    print(sum(primes))
    print(min(primes))