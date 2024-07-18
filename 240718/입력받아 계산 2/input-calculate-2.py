arr = input().split()

prod = 1
for i in range(len(arr)):
    arr[i] = int(arr[i])
    prod *= arr[i]

print(prod)