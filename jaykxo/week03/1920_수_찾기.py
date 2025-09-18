# 1920 수 찾기
# 메모리: 50412 KB, 시간: 504 ms

import sys
input = sys.stdin.readline
from typing import Any, Sequence

N = int(input())
A = list(map(int, input().split()))
A.sort()  # 이분 탐색을 위해 반드시 정렬 필요
M = int(input())
K = list(map(int, input().split()))

def bin_search(A: Sequence, key: Any):
    pl = 0
    pr = len(A) - 1  # 탐색 범위 오른쪽 끝 (리스트 마지막 인덱스)

    while pl <= pr:
        pc = (pl + pr) // 2  # 현재 탐색 구간의 중간 인덱스

        if A[pc] == key:  
          print("1")  
          return pc       # 찾으면 인덱스 반환 (실제 문제에서는 출력만 필요)
        
        elif A[pc] < key:
            pl = pc + 1  # 찾는 값이 더 크면 오른쪽 반으로 탐색 범위 좁힘
        else:
            pr = pc - 1  # 찾는 값이 더 작으면 왼쪽 반으로 탐색 범위 좁힘

    print("0")  # 끝까지 못 찾으면 0 출력

# 찾을 숫자들을 하나씩 이분 탐색 실행
for key in K:
    bin_search(A, key)
    

############ 번외 ############
# node.js 제출 버전
# 메모리: 39068 KB, 시간: 324 ms

# const fs = require("fs");
# const input = fs.readFileSync(0).toString().trim().split("\n");

# const N = Number(input[0]);
# const A = input[1].split(" ").map(Number).sort((a, b) => a - b);
# const M = Number(input[2]);
# const targets = input[3].split(" ").map(Number);

# function binarySearch(arr, target) {
#   let start = 0, end = arr.length - 1;
#   while (start <= end) {
#     let mid = Math.floor((start + end) / 2);
#     if (arr[mid] === target) return 1;
#     if (arr[mid] < target) start = mid + 1;
#     else end = mid - 1;
#   }
#   return 0;
# }

# console.log(targets.map(t => binarySearch(A, t)).join("\n"));