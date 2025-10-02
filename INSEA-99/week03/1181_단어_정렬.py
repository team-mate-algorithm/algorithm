# 시간(ms) : 156
# 공간(KB) : 115768

import sys
input = sys.stdin.readline

nums = set([sys.stdin.readline().strip() for _ in range(int(input()))])
print(*sorted(nums, key=lambda x : (len(x), x)), sep='\n')
