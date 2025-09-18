# 1181 단어 정렬
# 메모리: 37692 KB, 시간: 80 ms

import sys
input = sys.stdin.readline

N = int(input())

# 단어들을 입력받아 리스트에 저장
words = [input().strip() for _ in range(N)]

# 중복 제거 후 길이 → 사전순으로 정렬
words = sorted(set(words), key=lambda x: (len(x), x))

for word in words:
  print(word)