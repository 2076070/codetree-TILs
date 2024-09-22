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
for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i+offset][j+offset] = 1

# 두번째 사각형
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i+offset][j+offset] = 0

a1, a2, b1, b2 = (0, 0, 0, 0)
# 좌측하단 끝점
searching = True
for i in range(0, 2000):
    for j in range(0, 2000):
        if((arr[i][j]==1) and (searching==True)):
            a1, b1 = (i-offset, j-offset) # (2,1)
            searching = False

# 우측상단 끝점
searching = True
for i in range(1999, -1, -1):
    for j in range(1999, -1, -1):
        if((arr[i][j]==1) and (searching==True)):
            a2, b2 = (i-offset+1, j-offset+1)
            searching = False

# test
# print(a1, b1, a2, b2)

# 양단 끝점으로 정사각형 넓이 출력하기
result = abs(a2-a1) * abs(b2-b1)
print(result)