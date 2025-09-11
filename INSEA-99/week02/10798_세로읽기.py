import sys
from itertools import zip_longest
input = sys.stdin.readline

lines = [input().rstrip() for _ in range(5)]
vertical_chars = [''.join(filter(None, chars)) for chars in zip_longest(*lines)]
print(''.join(vertical_chars))


# - filter(function, iterable)
# iterable의 각 요소를 차례로 function에 넣고 반환값이 True면 사용, False면 제거
# function 대산 None을 넣는 경우 None을 제거해줌

# - zip
# 여러 iterable(리스트, 문자열 등) 을 병렬로 묶어서 튜플을 만들어줌
# 가장 짧은 iterable 길이에 맞춰 묶음이 생성됨
# 예시)
# a = [1, 2, 3]
# b = ['x', 'y']
# zip(a, b) -> [(1, 'x'), (2, 'y')]
#
# - zip_longest
# zip과 기능이 동일하지만 가장 긴 iterable 길이에 맞추고 그것보다 짧은 iterable은 None으로 채움(None 대신 다른 값으로 설정 가능. 인자에 fillvalue=?)

# - * (언패킹)
# 리스트, 튜플, 문자열 등 iterable을 개별 요소로 풀어서 함수 인자나 다른 자료구조에 전달
# ex) 
# lst1 = [1, 2]
# lst2 = [3, 4]
# combined = [*lst1, *lst2]  # [1, 2, 3, 4]
