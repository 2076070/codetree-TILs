n, m = map(int, input().split())
def rect(n, m):
    for _ in range(n):
        for _ in range(m):
            print(1, end="")
        print("")

rect(n,m)