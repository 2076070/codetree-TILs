n, m = map(int, input().split())
A = [0]
A.extend(list(map(int, input().split())))
li = []
for i in range(m) :
    li.append(list(map(int, input().split())))

for j in range(m):
    result = sum(A[li[j][0]:li[j][1]+1])
    print(result)