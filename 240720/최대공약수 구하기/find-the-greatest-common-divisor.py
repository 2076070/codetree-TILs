n, m = map(int, input().split())

def gcd(a, b):
    ans = 1
    if(a>=b): small=a
    else: small=b
    for i in range(2, small+1, 1):
        if (a%i==0):
            if (b%i==0): ans = i
    return ans

print(gcd(n,m))