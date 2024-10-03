n, k = map(int, input().split())
arr = list(map(int, input().split()))
myDict = {}

# k-number 는 unique...

for i in range(n):
    if (arr[i] not in myDict): myDict[arr[i]] = 0
    if (k-arr[i] in myDict):
        myDict[arr[i]] += 1
    
print(sum(myDict.values()))