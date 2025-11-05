# 11660 구간 합 구하기 5
# Python3, 메모리: 116164 KB, 시간: 712 ms
# PyPy3, 메모리: 136748 KB, 시간: 256 ms

import sys
input = sys.stdin.readline

# 한 번 함수로 맨들어 보고 싶어서 해봤읍니다,,,, 
def build_prefix(arr):
    """2차원 누적합 테이블 생성"""
    N = len(arr) - 1
    ps = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # (1,1)~(i,j) 구간합 = 위 + 왼쪽 - 겹친부분 + 현재값
            ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + arr[i][j]
    return ps

def range_sum(ps, x1, y1, x2, y2):
    """(x1,y1)~(x2,y2) 구간합 반환"""
    # 전체 - 위쪽 - 왼쪽 + 겹친부분
    return ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1]

# -------------------- main --------------------
N, M = map(int, input().split())

# 1-index 접근을 위한 0 패딩
arr = [[0] * (N + 1)]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))

# 누적합 생성
ps = build_prefix(arr)

# 구간합 계산
out = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    out.append(str(range_sum(ps, x1, y1, x2, y2)))

print("\n".join(out))