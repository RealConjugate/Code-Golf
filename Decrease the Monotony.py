def f(L):
    z=0
    for i in range(0,len(L)-1):
        if L[i]-L[i+1]<0:
            return 2
        if L[i]-L[i+1]==0:
            z=1
    return z

# outputs
# 0: strictly decreasing
# 1: weakly decreasing
# 2: none of the above

# test cases
print(f([7,5,4,3,1]))
print(f([27,19,19,10,3]))
print(f([78,89,3,-1,3]))
