Y, M , D = map(int, input().split())

def invalid_i(Y,M,D):
    if ((Y<1)|(Y>3000)): return True
    if ((M<1)|(M>12)): return True
    day=30
    if (M in [1,3,5,7,8,10,12]): day = 31
    if (M==2):
        if (Y%4==0):
            day=29
            if (Y%100==0):
                day=28
                if (Y%400==0) : day=29
    if ((D<1)|(D>day)): return True

def season(M):
    if (invalid_i(Y,M,D)) : return -1
    if (M in [3,4,5]): return "Spring"
    if (M in [6,7,8]): return "Summer"
    if (M in [9,10,11]): return "Fall"
    if (M in [12,1,2]): return "Winter"

print(season(M))