
arr = [10,11,12]
try:
    num = int(input("enter a number"))
    print(arr[num])
    num2 = int(input("enter number2"))
    print(arr[num]/num2)
except (ValueError,IndexError,ZeroDivisionError) as e :
    print(e,"exception handled")
