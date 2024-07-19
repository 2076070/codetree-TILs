a, b, c = map(str, input().split("-"))
tmp = b
b = c
c = tmp
print(f"{a}-{b}-{c}")