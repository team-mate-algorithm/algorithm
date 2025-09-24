import sys
input = sys.stdin.readline

# 1) 5줄 입력받아 리스트에 저장
lines = []
for _ in range(5):
    line = input().strip()     # 한 줄 입력받고 개행 제거
    lines.append(line)

# 2) 가장 긴 문자열의 길이 구하기
max_len = max(len(line) for line in lines)

# 3) 세로로 읽기: 열을 기준으로 각 줄을 돌며 문자 추가
result = ""
for c in range(max_len):            # 열(column) 기준
    for r in range(len(lines)):     # 행(row) 기준
        if c < len(lines[r]):       # 해당 줄에 문자가 존재하면
            result += lines[r][c]

# 4) 결과 문자열 출력
print(result)