"""
def tri(n):
    s=""
    while n>0:
        s=str(n%3)+s
        n//=3
    return s

best = 0
best_diff = 999999

for n in range(1,1000):
    r=tri(n)
    if n%3!=0:
        r="1"+ r + r[-3:]
    else:
        r+= tri((r.count("1") + r.count("2")*2)*8)
    R=int(r,3)

    diff=abs(R-1220)
    if diff < best_diff:
        best_diff = diff
        best = R
print(best)



def tri(n):
    s=""
    while n>0:
        s=str(n%3)+s
        n//=3
    return s

s=[]

for n in range(1,1000):
    r=tri(n)
    sum=r.count("1") + r.count("2")*2
    if sum%9==0:
        r+="2"
    else:
        r+=tri(sum%9)
    R=int(r,3)

    if n>166:
        s.append(R)
        
print(min(s))
"""
k=[]
for n in range(1,1000):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    s += str(s.count("1") % 2)
    s += str(s.count("1") % 2)
    r = int(s, 2)  # перевод в десятичную систему
    if r>170:
        k.append(n)

print(min(k))