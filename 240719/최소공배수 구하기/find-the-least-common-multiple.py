def cm(n,m):
    tmp=n
    while(True):
        if (tmp%m==0): break
        tmp+=n
    print(tmp)


n, m = map(int, input().split())
cm(n,m)