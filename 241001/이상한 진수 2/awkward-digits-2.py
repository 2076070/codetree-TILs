a = list(input()) # 2진법 수
arr = [ 0 for _ in range(len(a))]

# 원래 숫자의 2진법 표현을 찾는다
for i in range(len(a)):
    N_bi = []
    for k in range(len(a)):
        N_bi.append(a[k])
    if (a[i]=="0"): N_bi[i] = "1"
    else : N_bi[i] = "0"
    for j in range(len(a)):
        arr[i] += int(N_bi[j]) * (2**(len(a)-1-j))
print(max(arr))