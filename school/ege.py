"""
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F=(x and y and not(z))==(y or z or not(w))
                if F == 1:
                    print(x,y,z,w)

def f(n):
    s=""
    while n >0:
        s=str(n%3)+s
        n//=3
    return s
c=[]
for n in range(1,1000):
    s= f(n)
    s=s + str(n%3)
    r=int(s,3)
    if r>= 100 and r<=999:
        c.append(r)
print(min(c))

k=0
for a1 in "1234567":
    for a2 in "01234567":
        for a3 in "01234567":
            for a4 in "01234567":
                for a5 in "01234567":
                    s= a1+a2+a3+a4+a5
                    if s.count("6")==1:
                        if '16' not in s and '36' not in s and '56' not in s and '76' not in s:
                            if '61' not in s and '63' not in s and '65' not in s and '67' not in s:
                                k+=1
print(k)

x = 9**7 + 3**21 - 9
s = ''
while x != 0:
    s += str(x % 3) 
    x //= 3
s = s[::-1]
print(s.count("2"))

def f(n):
    if n == 1:
        return 3
    elif n >1:
        return f(n-1)*(n-1)
print(f(6))
"""
def f(x,y):
    if x>y or x==18:
        return 0
    elif x == y:
        return 1
    else:
        return f(x+1,y)+f(x*2,y)
print(f(1,10)*f(10,21))



