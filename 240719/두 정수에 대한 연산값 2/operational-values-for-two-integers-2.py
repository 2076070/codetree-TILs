def myCalc(x, y):
    if (x>y):
        x *= 2
        y += 10
    else :
        x += 10
        y *= 2
    return x, y

x, y = map(int, input().split())
x, y = myCalc(x, y)
print(x, y)