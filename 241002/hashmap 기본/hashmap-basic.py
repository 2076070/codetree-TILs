hashmap = {}
def add(k, v):
    hashmap[k] = v

def remove(k):
    hashmap.pop(k)

def find(k):
    if (k in hashmap): print(hashmap[k])
    else: print("None")

n = int(input())
for _ in range(n):
    arr = input().split()
    cmd = arr[0]
    if (cmd == 'add'):
        key = arr[1]
        value = arr[2]
        add(key, value)
    elif (cmd == 'remove'):
        key = arr[1]
        remove(key)
    elif (cmd == 'find'):
        key = arr[1]
        find(key)