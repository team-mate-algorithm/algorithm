# 2805 나무 자르기
# PyPy3, 메모리: 287292 KB, 시간: 632 ms
# Python3, 메모리: 151788 KB, 시간: 3028 ms

import sys
input = sys.stdin.readline
from typing import Any, Sequence

N, M = map(int, input().split())
A = list(map(int, input().split()))

def bin_search():
    # pl, pr: 절단기 높이의 하한/상한 (inclusive)
    pl = 0
    pr = max(A)  # 탐색 가능 최대 높이 = 가장 큰 나무 높이

    # result: 현재까지 조건을 만족(f(h) ≥ M)한 높이들 중 최댓값을 저장하는 변수
    result = 0

    # 이분탐색 루프: 경계가 교차할 때 종료 (pl > pr)
    while pl <= pr:
        # pc: 현재 시험해 볼 절단기 높이 (중간값)
        pc = (pl + pr) // 2

        # length: 높이 pc에서 잘려 나오는 총 나무 길이
        #  - 나무가 pc 이하이면 잘릴 길이가 없으므로 0
        #  - 나무가 pc 초과이면 (tree - pc)만큼 잘림
        #  ※ 리스트 컴프리헨션을 그대로 사용 (메모리는 조금 더 쓰지만 가독성은 좋음)
        length = sum([max(0, tree - pc) for tree in A])

        # 조건 검사: 현재 높이 pc에서 요구량 M 이상을 확보할 수 있는가?
        if length >= M:
            # 가능하다면, 더 높은 높이에서도 가능할지 확인해 최댓값을 노린다
            result = pc            # 현 시점의 후보 정답 갱신
            pl = pc + 1            # 더 큰 높이(오른쪽)로 탐색 범위 이동
        else:
            # 불가능하다면, 높이가 너무 높다는 뜻 → 낮춰야 함
            pr = pc - 1            # 더 작은 높이(왼쪽)로 탐색 범위 이동

    # 루프 종료 시 result에는 f(h) ≥ M 를 만족하는 최대 h가 저장되어 있음
    return result
    
print(bin_search())