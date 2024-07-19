# def cm(n,m):
#     tmp=n
#     while(True):
#         if (tmp%m==0): break
#         tmp+=n
#     print(tmp)


# n, m = map(int, input().split())
# cm(n,m)

def cm(a,b):
    if(a>=b):
        bigger=a
        smaller=b
    else:
        bigger=b
        smaller=a
    for i in range(smaller,a*b+1,smaller):
        if(i%bigger==0): return i



# 실행 부분
n, m = map(int, input().split())
print(cm(n,m))