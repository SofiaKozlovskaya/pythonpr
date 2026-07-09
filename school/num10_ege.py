def d(n):
    A=[]
    for i in range(2, int(n**0.5)+1):
        if n%i ==0:
            A.append(i)
            if i !=n//i:
                