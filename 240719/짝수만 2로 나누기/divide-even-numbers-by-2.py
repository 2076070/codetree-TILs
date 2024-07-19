def my_func(x):
    x = int(x)
    if (x%2==0): return x/2
    else: return x

N = int(input())
li = list(map(my_func, input().split())
)
for i in range(len(li)):
    print(f"{li[i]:.0f}", end=" ")