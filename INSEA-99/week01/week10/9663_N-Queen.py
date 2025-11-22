# pypy3
# 시간(ms) : 4760
# 공간(KB) : 245896

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def backtrack(row):
    """row번째 행에 퀸을 배치하는 백트래킹 함수"""
    if row == N + 1:  # 모든 행에 퀸을 배치했으면
        count[0] += 1
    else:
        for col in range(1, N + 1):  # 각 열에 퀸을 배치 시도
            if used_col[col] == 1: continue  # 이미 해당 열에 퀸이 있으면 스킵
            if is_safe(row, col):  # 대각선 체크
                # 퀸 배치
                used_col[col] = 1
                diag_sum[row + col] = 1  # 우상향 대각선 (row+col 값이 같음)
                diag_sub[row - col] = 1  # 좌하향 대각선 (row-col 값이 같음)

                backtrack(row + 1)  # 다음 행으로 이동

                # 백트래킹: 퀸 제거
                used_col[col] = 0
                diag_sum[row + col] = 0
                diag_sub[row - col] = 0

def is_safe(row, col):
    """(row, col) 위치에 퀸을 놓을 수 있는지 대각선 체크"""
    if diag_sum[row + col] == 1 or diag_sub[row - col] == 1:
        return False
    return True

# 변수 초기화
count = [0]  # 경우의 수 (리스트로 선언하여 함수 내에서 수정 가능)
N = int(input())  # 체스판 크기
used_col = [0] * (N + 1)  # 각 열에 퀸이 있는지 체크
diag_sum = [0] * (N * 2 + 1)  # 우상향 대각선 체크 (row+col 인덱스)
diag_sub = [0] * (N * 2 - 1)  # 좌하향 대각선 체크 (row-col 인덱스)

backtrack(1)  # 1번 행부터 시작
print(count[0])

