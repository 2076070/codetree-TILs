a = list(map(int, input().split()))
print(f"{sum(a)}")
print(f"{sum(a)/len(a):.0f}")
print(f"{sum(a)-sum(a)/len(a):.0f}")