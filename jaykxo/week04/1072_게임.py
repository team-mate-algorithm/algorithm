# 1072 게임
# PyPy3, 메모리: 108384 KB, 시간: 84 ms
# Python3, 메모리: 32412 KB, 시간: 36 ms

import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = (Y * 100) // X

# 현재 승률이 99% 이상이면 더 올라가지 않음 → -1
if Z >= 99:
    print(-1)

else:
    # 이분탐색: Z가 처음 증가하는 최소 추가 경기 수
    lo, hi = 1, 1_000_000_000  # 탐색 범위
    ans = -1                   # 정답 후보

    while lo <= hi:
        mid = (lo + hi) // 2                  # 추가 경기 수 후보
        newZ = ((Y + mid) * 100) // (X + mid) # 새 승률(정수 나눗셈)

        if newZ > Z:          # 승률이 증가함 → 더 작은 해가 있는지 왼쪽으로
            ans = mid
            hi = mid - 1
        else:                  # 아직 증가 안 함 → 오른쪽으로
            lo = mid + 1

    print(ans)
