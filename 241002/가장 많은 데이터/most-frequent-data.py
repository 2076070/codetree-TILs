n = int(input())
myDict = {}
for _ in range(n):
    word = input()
    if (word in myDict):
        myDict[word] += 1
    else: myDict[word] = 1

print(max(myDict.values()))