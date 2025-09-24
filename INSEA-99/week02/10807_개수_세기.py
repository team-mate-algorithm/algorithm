import sys
input = sys.stdin.readline

ans = 0

# 입력
input() # 다른 언어는 리스트 입력 받을 때 몇개인지 정보가 필요한 경우가 있는데, 파이썬은 필요없어서 그냥 받기만 하고 사용 안함
nums = map(int, input().split())
v = int(input())

# 풀이
for n in nums:
    if(n==v): ans+=1

# 출력
print(ans)