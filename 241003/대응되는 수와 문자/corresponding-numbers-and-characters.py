n, m = map(int, input().split())

hash1 = {}
hash2 = {}
for i in range(n):
    string = input()
    hash1[str(i+1)] = string # key는 숫자(문자열), value는 받은 문자
    hash2[string] = str(i+1) # key는 받은 문자, value는 숫자(문자열)
for _ in range(m):
    cmd = input()
    if (cmd in hash1): print(hash1[cmd])
    elif (cmd in hash2): print(hash2[cmd])