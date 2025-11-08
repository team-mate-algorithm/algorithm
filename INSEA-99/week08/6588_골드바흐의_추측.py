# pypy3
# 시간(ms) : 316
# 공간(KB) : 119244

import sys
input = sys.stdin.readline
MAX = 1_000_000

def goldbach_conjecture_check(n) :
    for i in range(3, n - 2) :  # 홀수 소수 합이 n이 되는지 확인
        if sieve[i] and sieve[n-i]:
            return f"{n} = {i} + {n-i}"
    return "Goldbach's conjecture is wrong."   
        
# MAX 값 기준 에라토스테네스의 체 생성
sieve = [True] * (MAX + 1)
sieve[0] = sieve[1] = False

for i in range(2, int(MAX ** 0.5) + 1):   
    if sieve[i]:  # 소수라면 배수 제거
        for j in range(i * i, MAX + 1, i): # i*i보다 작은 배수는 중복 처리이기 때문에 i*i 부터 확인
            sieve[j] = False

# 골드바흐의 추측 검증
while True :
    n = int(input())
    if n == 0 : break
    print(goldbach_conjecture_check(n))