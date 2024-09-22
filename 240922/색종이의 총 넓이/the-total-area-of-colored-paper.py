arr = [
    [
        0
        for _ in range(200)
    ]
    for _ in range(200)
]
offset = 100

N = int(input())
for _ in range(N) :
    x, y = map(int, input().split())
    for i in range(x, x+8):
        for j in range(y, y+8):
            arr[i+offset][j+offset] = 1

result = 0
for k in range(200) :
    result += sum(arr[k])

print(result)