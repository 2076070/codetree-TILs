def cm(n,m):
    tmp=n
    while(True):
        if (tmp%18==0): break
        tmp+=n
    print(tmp)


n, m = map(int, input().split())
cm(n,m)