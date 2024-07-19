while(True) :
    a, b = map(int, input().split())
    if ((1<=a)&(a<=b)&(b<=100)) : break;

if (a%2) : # a가 홀수
    for i in range(a,b+1,2) : print(i, end=" ")
else :
    for i in range(a+b, b+1, 2) : print(i, end=" ")