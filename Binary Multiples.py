# Given positive integer n, finds smallest binary multiple of n
# A binary multiple is a number in base 10 with only digits 0 and 1 that n divides

def f(n):
    s="1"
    while 2>1:
        if int(s)%n==0:
            return s
        if "0" in s:
            for j in range(0,len(s)):
                if s[j]=="0":
                    q=j
            t=s[:q]
            for k in range(q,len(s)):
                t=t+str(1-int(s[k]))
            s=t
        else:
            s=str(10**len(s))

# test cases
print(f(2))
print(f(3))
print(f(4))
print(f(5))
print(f(6))
print(f(7))
print(f(8))
print(f(9))
print(f(10))
print(f(11))
print(f(12))
print(f(13))
print(f(14))
print(f(15))
print(f(16))
print(f(17))
print(f(18))
print(f(19))
print(f(20))
print(f(100))
