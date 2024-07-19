N = int(input())
arr = []
for i in range(N) :
    n = int(input())
    if ((n%2==1)&(n%3==0)) : arr.append(n)
    i+=1

for j in range(len(arr)) :
    print(arr[j])