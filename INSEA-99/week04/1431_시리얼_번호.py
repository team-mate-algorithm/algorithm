# pypy3
# 시간(ms) : 92
# 공간(KB) : 109544
#
# Python3
# 시간(ms) : 40
# 공간(KB) : 32412
#
# 공유 : 
#     빠른 입출력 + 내장 함수 (정렬, math 등)
#     → Python3 추천

#     루프 많고 연산-heavy (단순 반복, 시뮬레이션)
#     → PyPy3 추천

import sys
input = sys.stdin.readline


def sort_serial_nums(serial_num) :
    """_summary_

    Args:
        serial_num(string) : 정렬 대상 원소

    Returns:
       정렬 기준 반환
       1. (오름) 길이 
       2. (오름) 원소 내 숫자 합
       3. (오름) 사전순
    """
    sum_digits = sum(int(ch) for ch in serial_num if ch.isdigit())
    return (len(serial_num), sum_digits, serial_num)

serial_nums = [input().strip() for _ in range(int(input().strip()))]
print(*sorted(serial_nums, key=sort_serial_nums), sep='\n')