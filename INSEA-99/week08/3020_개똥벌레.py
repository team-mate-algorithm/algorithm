# pypy3
# 시간(ms) : 152
# 공간(KB) : 118540
#
# 공유 : 
# - gpt가 파이썬은 인덱스를 음수로 반복적으로 접근하면 내부적으로 인덱스 변환을 계속 해야 하므로 느리다함
#   이 문제 기준으로는 8ms 차이라서 크게 신경 안써도 될듯 (백만 단위 이상 인덱싱에서 3~5% 정도 느리다고)

import sys
input = sys.stdin.readline

n, h = map(int, input().strip().split())

top = [0] * (h+1)       # 종유석
bottom = [0] * (h+1)    # 석순

for _ in range(n//2) :  # 종유석, 석순 각각 같은 길이 카운팅 
    bottom[int(input())] += 1
    top[-int(input())] += 1

for i in range(1, h+1) :    # 종유석, 석순 각각 누적합을 통해 구간에 따른 hit 구하기
    top[i] += top[i-1]
    bottom[-(i+1)] += bottom[-i] 

min_hit = n     # 최소 hit
min_hit_cnt = 1 # 최소 hit 개수
for i in range(1, h+1) :
    hit = top[i] + bottom[i]    # 종유석, 석순 합쳐서 최종 hit 구하기
    if min_hit > hit :
        min_hit = hit
        min_hit_cnt = 1
    elif min_hit == hit :
        min_hit_cnt += 1
        
print(min_hit, min_hit_cnt)


