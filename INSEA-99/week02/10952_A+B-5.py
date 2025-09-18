import sys
input = sys.stdin.readline

while(True):
    a, b = map(int, input().split())
    if(a==0 and b==0):
        break
    print(a+b)

# [입력 받는 로직 설명]
# a, b = map(int, input().split())
# 예시) 만약 "1 1" 입력이 들어왔다면
# 1. input()을 통해 "1 1"을 가져옴
# 2. input().split()를 통해 공백을 기준으로 쪼갠 리스트를 얻음["1", "1"] (쪼개는 기준 split에 인자 줘서 바꿀 수 있음)
# 3. map을 통해 list의 원소마다 int를 적용시켜줌 -> [1, 1]
# 4. a, b = [1, 1]를 하면 파이썬에서 제공하는 시퀀스 언패킹 기능으로 a=1, b=1이 할당됨