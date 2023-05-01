s = input("enter a string : ")
s2 = ""
for e in s:
    if(e in "AEIOUaeiou"):
        continue
    s2 += e
print("result is",s2)