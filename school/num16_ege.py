"""
#1
def f(n):
    if n == 1:
        return 1
    elif n%2==0:
        s = n+f(n-1)
        return s
    elif n>1 and n%2!=0:
        k = 2*f(n-2)
        return k

print(f(26))

#2
def f(n):
    if n >= 2025:
        return n
    elif n<2025:
        s = n+3 +f(n+3)
        return s

print(f(23)-f(21))

#3
def f(n):
    if n ==1:
        return 0
    elif n>1:
        s = f(n-1)+n
        return s

def g(i):
    if i==1:
        return 1
    elif i >1:
        k=g(i-1)*i
        return k
    
print(f(5)+g(5))

#4
def f(n):
    if n ==1:
        return 1
    elif n>1:
        s = f(n-1)+2*n-1
        return s
    
print(f(10))

#5
import sys
sys.setrecursionlimit(2100)

def f(n):
    if n ==1:
        return 1
    elif n>2 and n%2==0:
        return 2*n*f(n-1)+f(n-3)
        
    elif n>1 and n%2!=0:
        return f(n-2)*3
a= int(input())
b=int(input())
print(f(a)/f(b))

#6
import sys
sys.setrecursionlimit(2250)
def f(n):
    if n<11:
        return 10
    elif n>= 11:
        return n+f(n-1)
a= int(input())
b=int(input())
print(f(a)-f(b))
"""