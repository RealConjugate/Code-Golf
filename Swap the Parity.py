# Attempt at the shortest possible program to do the following:
# Given positive integer n, output n+1 if n is odd and n-1 if n is even.

def f(n):
    return n+(-1)**(n%2+1)
