offset = 1000
arr = [
    [
        0
        for _ in range(2000)
    ]
    for _ in range(2000)
]
result = 0

# 첫번째 사각형
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2): # -2 ~ 1 = -2 -1 0
    for j in range(y1, y2): # -2 ~ 1 = -2 -1 0
        arr[i+offset][j+offset] = 1

# 두번째 사각형
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2): # 0 ~ 3 = 0 1 2
    for j in range(y1, y2): # 0 1 2
        arr[i+offset][j+offset] = 0

x_list = []
y_list = []

for i in range(0, 2000) :
    for j in range(0, 2000) :
        if (arr[i][j] == 1) :
            x_list.append(i-offset)
            y_list.append(j-offset)

if (x_list and y_list): # 둘 다 비어있지 않을 것
    result = (max(x_list) - min(x_list) + 1) * (max(y_list) - min(y_list) + 1)
print(result)