s = input("enter a string: ")
d = {}
for e in s:
    if e not in d.keys():
        d[e] = s.count(e)
print(d)



# output:
# enter a string: python programming
# {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}