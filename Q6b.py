def length(s):
    if s=="":
        return 0
    return length(s[1:]) + 1
def palindrome(s):
    n = int(length(s)/2)
    for i in range(0,n):
        if s[i] != s[-i-1] :
            return False
    return True
s = input("enter a string : ")
print("string length is",length(s))
print("string is palindrome",palindrome(s))