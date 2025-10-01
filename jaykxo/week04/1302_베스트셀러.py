# 1302 베스트셀러
# PyPy3, 메모리: 110064 KB, 시간: 112 ms
# Python3, 메모리: 34908 KB, 시간: 56 ms

import sys
input = sys.stdin.readline
from collections import Counter

N = int(input().strip())
books = [input().strip() for _ in range(N)]

counter = Counter(books)         # books 리스트 안의 각 책 제목을 key로, 등장 횟수를 value로 세어 Counter 객체 생성
best = sorted(
    counter.items(),             # Counter를 (책제목, 등장횟수) 쌍들의 리스트로 변환
    key=lambda x: (-x[1], x[0])  # 첫 번째 기준: 등장 횟수 내림차순(-x[1]), 두 번째 기준: 책 제목 오름차순(x[0])
)[0][0]                          # 정렬된 결과의 첫 번째 요소(가장 많이 팔린 책)에서 제목만 추출

print(best)