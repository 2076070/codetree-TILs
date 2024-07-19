a, b = map(int, input().split())

prod=1
for i in range(b) :
    if ((i+1)%a): continue
    prod *= (i+1)

print(prod)