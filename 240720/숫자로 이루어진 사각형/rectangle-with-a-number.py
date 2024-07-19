N = int(input())

def rect(n):
    e = 1
    for i in range(n*n):
        print(e, end=" ")
        if(i%n==n-1): print("")
        if (e==9): e=1
        else: e += 1

rect(N)