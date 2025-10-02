# 시간(ms) : 104
# 공간(KB) : 110064
#
# 공유 : 
# - counter는 내부적으로 dictionary로 구현됨
# - counter['a']는 dict에서 'a'의 개수를 반환 

import sys
from collections import Counter
input = sys.stdin.readline

books = [input().strip() for _ in range(int(input().strip()))]
counter = Counter(books)
print(sorted(counter, key=lambda x : (-counter[x], x), reverse=True)[-1])