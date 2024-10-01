R, C = map(int, input().split())
arr = [
    list(input().split())
    for _ in range(R)
]

# 조건에 맞는 경로 세기
cnt = 0

for i in range(1, R):
    for j in range(1, C):
        if (arr[0][0] != arr[i][j]):
            for ii in range(i+1, R):
                for jj in range(j+1, C):
                    if(arr[i][j] != arr[ii][jj]):
                        for iii in range(ii+1, R):
                            for jjj in range(jj+1, C):
                                if((iii==R-1)and(jjj==C-1)and(arr[ii][jj] != arr[iii][jjj])):
                                    # print(f"({i+1},{j+1}) ({ii+1},{jj+1}) ({iii+1},{jjj+1})")
                                    cnt+=1

print(cnt)