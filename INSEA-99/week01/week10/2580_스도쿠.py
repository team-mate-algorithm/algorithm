# pypy3
# 시간(ms) : 540
# 공간(KB) : 241236

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def backtrack(depth):
    """depth번째 빈 칸을 채우는 백트래킹 함수"""
    if depth == total_blanks:  # 모든 빈 칸을 채웠으면
        return True

    row_idx, col_idx = blank_positions[depth]  # 튜플 언패킹으로 가독성 향상
    box_idx = box_number[row_idx][col_idx]  # 반복 계산 제거

    for num in range(9):  # 1~9까지 시도 (인덱스 0~8)
        # 같은 행, 열, 3x3 박스에 num+1이 없는지 한 번에 체크 (is_valid 함수 인라인화)
        if not (used_in_row[row_idx][num] or used_in_col[col_idx][num] or used_in_box[box_idx][num]):
            # 숫자 배치
            board[row_idx][col_idx] = num + 1
            used_in_row[row_idx][num] = 1
            used_in_col[col_idx][num] = 1
            used_in_box[box_idx][num] = 1

            if backtrack(depth + 1):  # 다음 빈 칸으로 이동
                return True

            # 백트래킹: 숫자 제거
            board[row_idx][col_idx] = 0
            used_in_row[row_idx][num] = 0
            used_in_col[col_idx][num] = 0
            used_in_box[box_idx][num] = 0

    return False


# 입력 받기: 9x9 스도쿠 보드
board = []
for _ in range(9):
    board.append(list(map(int, input().split())))

# 각 칸이 속한 3x3 박스 번호 (0~8)
# 0 1 2
# 3 4 5
# 6 7 8
box_number = [[0,0,0,1,1,1,2,2,2] for _ in range(3)] + \
             [[3,3,3,4,4,4,5,5,5] for _ in range(3)] + \
             [[6,6,6,7,7,7,8,8,8] for _ in range(3)]

blank_positions = []  # 빈 칸(0인 칸)의 위치 저장
total_blanks = 0  # 빈 칸의 총 개수

# 각 행, 열, 3x3 박스에서 1~9 숫자 사용 여부 체크 (인덱스 0~8이 1~9를 의미)
used_in_row = [[0] * 9 for _ in range(9)]  # used_in_row[i][n]: i행에 n+1이 있으면 1
used_in_col = [[0] * 9 for _ in range(9)]  # used_in_col[j][n]: j열에 n+1이 있으면 1
used_in_box = [[0] * 9 for _ in range(9)]  # used_in_box[b][n]: b번 박스에 n+1이 있으면 1

# 초기 보드 분석: 빈 칸 찾기 및 사용된 숫자 체크
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:  # 빈 칸 발견
            blank_positions.append([i, j])
            total_blanks += 1
        else:  # 이미 채워진 칸
            num = board[i][j] - 1  # 1~9를 0~8 인덱스로 변환
            used_in_row[i][num] = 1
            used_in_col[j][num] = 1
            used_in_box[box_number[i][j]][num] = 1

backtrack(0)  # 0번째 빈 칸부터 시작
for row in board: print(*row)