# Given positive integer n, return the sum of the reverses of 1,2,...,n

def f(n):
    s=0
    for i in range(1,n+1):
        r=""
        k=str(i)
        for j in range(0,len(k)):
            r=r+k[len(k)-1-j]
        s+=int(r)
    return s
        
# test cases
print(f(10))
print(f(5))
print(f(21))
print(f(58))
print(f(75))
print(f(999))
