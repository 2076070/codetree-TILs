b2 = list(input())
b3 = list(input())

# base2에서 하나 변환한 것 list로
base2_list = []
for i in range(len(b2)):
    base2 = []
    for b in b2:
        base2.append(b)
    base2[i] = "0" if(base2[i]=="1") else "1"
    v = 0
    for j in range(0, len(base2)):
        v += (2**(len(base2)-1-j)) * int(base2[j])
    base2_list.append(v)
#print(base2_list)

# base3에서 하나 변환한 것 list로
base3_list = []
for i in range(len(b3)):
    base3 = []
    for b in b3:
        base3.append(b)
    base3[i] = "0" if(base3[i]=="1") else "1"
    v = 0
    for j in range(0, len(base3)):
        v += (3**(len(base3)-1-j)) * int(base3[j])
    base3_list.append(v)
for i in range(len(b3)):
    base3 = []
    for b in b3:
        base3.append(b)
    base3[i] = "1" if(base3[i]=="2") else "2"
    v = 0
    for j in range(0, len(base3)):
        v += (3**(len(base3)-1-j)) * int(base3[j])
    base3_list.append(v)
for i in range(len(b3)):
    base3 = []
    for b in b3:
        base3.append(b)
    base3[i] = "2" if(base3[i]=="0") else "0"
    v = 0
    for j in range(0, len(base3)):
        v += (3**(len(base3)-1-j)) * int(base3[j])
    base3_list.append(v)


result = 0
for e2 in base2_list:
    for e3 in base3_list:
        if(e2==e3): result = e2
print(result)