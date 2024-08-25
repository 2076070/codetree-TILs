def insertion_sort(arr):
    arr_len = len(arr)
    for i in range(1, arr_len):
        j = i-1
        key = arr[i]
        while ((j>=0)and(arr[j]>=key)):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

n = int(input())
arr1 = list(input().split())

for e in insertion_sort(arr1):
    print(e, end=" ")