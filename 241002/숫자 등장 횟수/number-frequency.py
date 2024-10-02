n, m = map(int, input().split())
arr = list(map(int, input().split()))
cmd = list(map(int, input().split()))

myDict = {}
# 2번째 입력으로 사전 만들기
for i in range(n):
    if (arr[i] in myDict): myDict[arr[i]] += 1
    else: myDict[arr[i]] = 1

for c in cmd:
    if (c in myDict): print(myDict[c], end=" ")
    else: print(0, end=" ")