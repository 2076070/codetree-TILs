import sys
N = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

min_val = -sys.maxsize
for i in range(N):
    for j in range(N-3+1):
        temp = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        min_val = min_val if(min_val > temp) else temp
print(min_val)