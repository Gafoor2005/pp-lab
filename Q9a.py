fp = open('txt1.txt','r')
for e in fp:
    print(e.split('\n')[0][::-1])
fp.close()

# output:
# rutetcesnoc tema tis rolod muspi meroL
# 54321 cba