def c(x):
    p=0
    for i in range(2,x+1):
        P=1
        for d in range(1,i):
            if i%d==0 and d!=1:
                P=0
        p+=1*P
    return p


# test cases

print(0,1,2,2,3,3,4,4,4,4,5)

for i in range(1,12):
    print(c(i))
