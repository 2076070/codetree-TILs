n = int(input())
offset = 100
arr = [
    [
        0
        for _ in range(200)
    ]
    for _ in range(200)
]

for i in range(1, n+1):
    x1, y1, x2, y2 = map(int, input().split())
    if(i%2==1): #빨간색
        for j in range(x1, x2):
            for k in range(y1, y2):
                arr[j+offset][k+offset] = 0
    if(i%2==0): #파란색
        for j in range(x1, x2):
            for k in range(y1, y2):
                arr[j+offset][k+offset] = 1

# 넓이 구하기
result = 0
for i in range(0, 200):
    result += sum(arr[i])
print(result)