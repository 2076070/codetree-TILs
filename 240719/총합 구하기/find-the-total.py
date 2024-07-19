a, b = map(int, input().split())
tmp = 0

a = a + (6-a%6)
while(a<=b):
    if (a%8) : tmp+=a
    a+=6

print(tmp)