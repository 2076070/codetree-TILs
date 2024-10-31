n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    min_idx = i
    for j in range(i, n):
        if (arr[min_idx] > arr[j]):
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

for e in arr:
    print(e, end=" ")