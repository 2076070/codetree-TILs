offset = 1000
arr = [
    [
        0
        for _ in range(2000)
    ]
    for _ in range(2000)
]

# A 칠하기
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2) :
    for j in range(y1, y2) :
        arr[i+offset][j+offset] = 1

# B 칠하기
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2) :
    for j in range(y1, y2) :
        arr[i+offset][j+offset] = 1

# M 칠하기
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2) :
    for j in range(y1, y2) :
        arr[i+offset][j+offset] = 0

# 출력
result = 0
for k in range(2000) :
    result += sum(arr[k]) 
print(result)