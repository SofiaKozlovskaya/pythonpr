"""
def f(x,y):
    if x>y:
        return 0
    elif x ==y:
        return 1
    elif x < y:
        return f(x**2,y)+ f(x+4, y)+ f(x+3, y)
print(f(2,33))

def f(x,y):
    if x>y or x==10:
        return 0
    elif x ==y:
        return 1
    elif x < y:
        return f(x+1,y)+ f(x+2, y)+ f(x*2, y)
print(f(3,7)*f(7,20))

def f(x,y):
    if x<y or x ==15:
        return 0
    elif x ==y:
        return 1
    elif x >y:
        return f(x-2,y)+f(x-3,y)+f(x//3,y)
    
print(f(48,25)*f(25,17)*f(17,4))

def f(x,y):
    if x<y or x==28:
        return 0
    if x==y:
        return 1
    if x>y:
        if x%2==0:
            return f(x-2,y)+f(x/2,y)
        elif x%2!=0:
            return f(x-2,y)+f(x-3,y)

print(f(98,1))

def f(x,y,s):
    if x<y:
        return 0
    elif x ==y and "AAA" not in s and "BBB" not in s:
        return 1
    else:
        if x%2==0:
            return f(x-2,y, s+"A")+f(x//2,y, s+"B")
        else:
            return f(x-2,y, s+"A")+f(x-7,y,s+"B")

print(f(40,1,""))
"""

