# Lynch-Bell number has unique digits 1-9 and each digit divides the number

def f(n):
    s=""
    for i in n:
        if i in s or int(n)%int(i)!=0:
            return False
        s=s+i
    return True

# test cases
print(f("7"))
print(f("126"))
print(f("54"))
print(f("55"))
print(f("3915"))
    
# without whitespace removed
# def f(n): s="" for i in n: if i in s or int(n)%int(i)!=0: return False s=s+i return True
