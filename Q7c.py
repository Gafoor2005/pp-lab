n = int(input("How many strings you will enter? "))
d = {}
for i in range(n):
    s = input(f"enter string {i+1} : ")
    d[s] = len(s)
print(d)

# output:
# How many strings you will enter? 3
# enter string 1 : gec
# enter string 2 : python
# enter string 3 : programming
# {'gec': 3, 'python': 6, 'programming': 11}
