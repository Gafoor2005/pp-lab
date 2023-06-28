class ShortIntException(Exception):
    pass
string = input("enter a string")
try:
    if(len(string)<3):
        raise ShortIntException
    print("string is ",string," length is",len(string))
except ShortIntException:
    print("string length is lessthan 3")
    
