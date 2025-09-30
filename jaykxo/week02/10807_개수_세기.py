import sys
input = sys.stdin.readline

N = int(input())  # 숫자 개수 입력 받기
num = list(map(int, input().split()))  # 숫자 리스트 입력 받기
v = int(input())  # 찾을 숫자 입력 받기

count = 0  # 찾은 숫자 개수 초기화

for i in range(N):
    if num[i] == v :  # 현재 숫자가 찾는 숫자와 같은지 확인
        count += 1  # 같으면 개수 증가

print(count)  # 결과 출력 (찾은 숫자의 개수)