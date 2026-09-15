"""
for x in "0123456789abcdefghijkl":
    a=int(f"27{x}98876",22)
    b=int(f"26{x}51",22)
    c=int(f"711{x}5",22)
    if (a+b+c)%21==0:
        print((a+b+c)//21)
        break
"""
k=[]
for x in range(2030,0,-1):
    s=7**170+7**100-x
    temp=""
    while s!=0:
        temp = str(s%7)+temp 
        s//=7
    if temp.count("0")==70:
        


