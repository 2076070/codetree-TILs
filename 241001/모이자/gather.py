import sys

n = int(input())
arr = list(map(int, input().split()))
result = [ 0 for _ in range(n) ]

min_val = sys.maxsize
for i in range(n):
    for j in range(n):
        result[i] += arr[j] * abs(j-i)

print(min_val if(min_val<min(result)) else min(result))
# 구한 값 중에서 최소값이, 상한선보다 높다면 오류
# 상한선보다 낮은 값이라면, 구한 값 중 최소값을 반환할 것