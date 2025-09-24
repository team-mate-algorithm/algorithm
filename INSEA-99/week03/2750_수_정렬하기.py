# 시간(ms) : 92
# 공간(KB) : 109412
#
# 공유 :
# 1) * 는 리스트, 튜플, 문자열 등의 요소를 함수 인자로 풀어서 전달
#     ex) 
#     nums = [1, 2, 3]
#     print(*nums) = print(1, 2, 3)
#
# 2) print()의 sep 매개변수 (defult = ' ')
#     ex) 
#     print('a', 'b', 'c')
#     -> 'a' 'b' 'c'
#     print('a', 'b', 'c', sep='!')
#     -> 'a'!'b'!'c'


import sys
input = sys.stdin.readline

nums = [int(sys.stdin.readline().strip()) for _ in range(int(input()))]
print(*sorted(nums), sep='\n')
