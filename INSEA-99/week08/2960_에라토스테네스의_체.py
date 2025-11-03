# pypy3
# 시간(ms) : 92
# 공간(KB) : 109544

import sys
input = sys.stdin.readline

n, K = map(int, input().strip().split())

sieve = [True] * (n + 1)
sieve[0] = sieve[1] = False

def find_kth_removed(n, K) :
    k = 0
    for i in range(2, n + 1):   # 소수를 포함하여 지워지는 수를 확인해야하므로 n까지 탐색
        if sieve[i]:  # 소수라면 본인과 배수 제거
            for j in range(i, n + 1, i): 
                if sieve[j]:
                    sieve[j] = False
                    k +=1
                    if k == K: return j
print(find_kth_removed(n, K))
