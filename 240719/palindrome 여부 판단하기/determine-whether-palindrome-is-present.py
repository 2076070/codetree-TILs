def isPalindrome(s):
    for i in range (len(s)//2):
        if (s[i]==s[len(s)-i-1]) : continue
        else:
            print("No")
            return
    print("Yes")

A = input()
isPalindrome(A)