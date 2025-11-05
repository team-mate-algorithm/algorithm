# 3020 개똥벌레
# Python3, 메모리: 71968 KB, 시간: 436 ms
# PyPy3, 메모리: 118544 KB, 시간: 144 ms

import sys
input = sys.stdin.readline

N, H = map(int, input().split())

# 석순과 종유석의 길이 빈도를 저장할 배열
# 인덱스 = 장애물의 길이, 값 = 해당 길이 장애물 개수
# +2 여유 공간은 인덱스 범위 오류 방지용
down = [0] * (H + 2)   # 석순(바닥에서 위로)
up   = [0] * (H + 2)   # 종유석(천장에서 아래로)

# 장애물 길이 입력 받기
for i in range(N):
    L = int(input())
    if i % 2 == 0:
        # 짝수 번째는 석순
        down[L] += 1
    else:
        # 홀수 번째는 종유석
        up[L] += 1

# 누적합으로 변환
# down[h] = 높이 h 이상인 석순의 개수
# up[h]   = 길이 h 이상인 종유석의 개수
# → 뒤에서부터 누적해야 “길이 이상(≥)” 형태의 합
for h in range(H - 1, 0, -1):
    down[h] += down[h + 1]
    up[h]   += up[h + 1]

# 각 높이 h(1 ~ H)에서의 충돌 개수 계산
min_hit = N + 1   # 최소 충돌 횟수: 초기값 충분히 크게 설정
count_min = 0     # 최소 충돌이 발생하는 높이 개수

for h in range(1, H + 1):
    # 석순은 높이 h 이상일 때 충돌
    # 종유석은 천장에서 내려오므로 (H - h + 1) 이상일 때 충돌
    hit = down[h] + up[H - h + 1]

    # 최솟값 갱신
    if hit < min_hit:
        min_hit = hit
        count_min = 1   # 새 최솟값이 나왔으니 개수 1로 초기화
    elif hit == min_hit:
        count_min += 1  # 같은 최솟값이 또 나왔으니 개수 +1

print(min_hit, count_min)