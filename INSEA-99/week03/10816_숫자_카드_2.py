# Dict 풀이 시간: 
# 시간(ms) : 720
# 공간(KB) : 266652
#
# Counter 풀이 시간:
# 시간(ms) : 672
# 공간(KB) : 266708
#
# 공유 : 
# - Counter는 collections 모듈에 포함된 dict의 특수 버전. 내부는 사실상 dict 기반이지만, 추가 메서드와 연산자 지원


import sys
from collections import Counter
input = sys.stdin.readline


# 1. dictionary 사용
input()
nums = list(input().strip().split())    # 숫자 카드 입력 받기

dic = {}
for n in nums :    # dictionary로 입력 받은 숫자 카드 개수 카운드
    dic[n] = dic.get(n, 0) + 1

input()
ans = []
for m in list(input().strip().split()) :    # dic에서 숫자 카드 개수 가져오기
   ans.append(dic.get(m, 0))
print(*ans) 



# 2. Counter 사용
input()
nums = list(input().strip().split())    # 숫자 카드 입력 받기
counter = Counter(nums)

input()
ans = []
for m in list(input().strip().split()) :    # dic에서 숫자 카드 개수 가져오기
   ans.append(counter[m])
print(*ans) 

