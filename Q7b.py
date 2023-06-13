def mean(l):
    return sum(l)/len(l)

def median(l):
    l.sort()
    if len(l)%2 != 0 :
        return l[int(len(l)/2)]
    else:
        return (l[int(len(l)/2)] + l[int((len(l)/2)-1)])/2
    
def mode(l):
    mode = None
    for e in l :
        if  (mode != None) and (l.count(e) > mode):
            mode = e
        elif (mode == None) and (l.count(e)>1) :
            mode = e
    return mode

n = int(input("enter no of elements in list : "))
l = []
for i in range(0,n):
    l.append(int(input(f"enter {i+1} element :")))
print("list is ",l)
print("mean is ",mean(l))
print("median is ",median(l))
print("mode is ",mode(l))


# output:
# enter no of elements in list : 6 
# enter 1 element :10
# enter 2 element :20
# enter 3 element :51
# enter 4 element :20
# enter 5 element :15
# enter 6 element :32
# list is  [10, 20, 51, 20, 15, 32]
# mean is  24.666666666666668
# median is  20.0
# mode is  20