# 시간(ms) : 216
# 공간(KB) : 137716
#
# 공유 : 
# - 파이썬에서 문자(str)와 정수(int)는 비교 방식이 다르므로 정렬 시 주의
#     ex)
#     2 < 10
#     '2' > '10' # 문자열 "2"의 첫 글자 '2'와 "10"의 첫 글자 '1'을 비교

import sys
input = sys.stdin.readline

def bs(arr, target) :
    left = 0
    right = len(arr) - 1
    
    while(left <= right) :
        mid = (left + right) // 2
        if(arr[mid] < target) : left = mid + 1
        elif(arr[mid] > target) : right = mid - 1 
        else : return 1
    return 0

input()
nums = sorted(list(map(int, input().strip().split())))
input()
for t in list(map(int, input().strip().split())):
    print(bs(nums, t))
