# 1431 시리얼 번호
# PyPy3, 메모리: 109544 KB, 시간: 100 ms
# Python3, 메모리: 32412 KB, 시간: 40 ms

import sys
input = sys.stdin.readline

N = int(input().strip())
serials = [input().strip() for _ in range(N)]

serials.sort(
    key=lambda s: (
        len(s),                                    # 1순위: 시리얼 길이 (짧을수록 먼저). 길이가 같지 않다면 여기서 순서가 확정된다.
        sum(int(ch) for ch in s if ch.isdigit()),  # 2순위: 숫자 합 (작을수록 먼저). 각 글자가 숫자인지 확인( ch.isdigit() ) 후 int로 변환해 합산.
        s                                          # 3순위: 사전순 (문자열 기본 비교). 앞의 두 기준이 같을 때만 사용된다.
    )
)

# 정렬된 시리얼 번호를 한 줄에 하나씩 출력
for s in serials:
    print(s)