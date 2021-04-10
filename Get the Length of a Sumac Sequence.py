# Sumac sequence begins with two positive integers; t_n = t_(n-2)-t_(n-1)
# terminates when the next term would be non-positive
# code golf to write shortest possible code

def F(I):
    i=1
    if I[0]<0:
        return ([],0)
    if I[1]<0:
        return ([I[0]],1)
    while I[i-1]-I[i]>0:
        I.append(I[i-1]-I[i])
        i+=1
    return I,i+1


# test cases

print(F([120,71]))
print(F([101,42]))
print(F([500,499]))
print(F([387,1]))
print(F([3,-128]))
print(F([-2,3]))
print(F([3,2]))
