n = int(input())
arr = list(map(int, input().split()))

for i in range(0, n):
    for j in range(0, n-1):
        if (arr[j] > arr[j+1]):
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp

for k in range(0, n):
    print(arr[k], end=" ")