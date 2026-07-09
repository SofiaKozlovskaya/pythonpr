"""
#1
k=0
for a1 in "123456":
    for a2 in "0123456":
        for a3 in "0123456":
            for a4 in "0123456":
                for a5 in "0123456":
                    s=a1+a2+a3+a4+a5
                    if s.count("0") == 1 and s.count("1")<=2:
                        k+=1
print(k)

#2
k=0
l=[]        

for a1 in "ИРСТУЦ":
    for a2 in "ИРСТУЦ":
        for a3 in "ИРСТУЦ":
            for a4 in "ИРСТУЦ":
                for a5 in "ИРСТУЦ":
                    s=a1+a2+a3+a4+a5
                    k+=1
                    if s.count("И") ==2 and "ЦЦ" not in s:
                        l.append(k)

print(l)

#3
p=5
q=7
e=11
f=(p-1)*(q-1)
for d in range(40,1,-1):
    if (d*e)%f ==1:
        print(d)
        break

"""
#4
def check_no_adjacent_duplicates(number):
    # Превращаем число в строку, чтобы можно было перебирать цифры
    s = str(number)
    
    # Проходим циклом до предпоследнего элемента
    for i in range(len(s) - 1):
        # Если текущая цифра совпадает со следующей — возвращаем False
        if s[i] == s[i+1]:
            return False
            
    # Если цикл дошел до конца и совпадений не нашел — возвращаем True
    return True

k=0
for a1 in "123456789ABC":
    for a2 in "0123456789ABC":
        for a3 in "0123456789ABC":
            for a4 in "0123456789ABC":
                for a5 in "0123456789ABC":
                    s=a1+a2+a3+a4+a5
                    if s.count("0")==1 and check_no_adjacent_duplicates(s) is True:
                        k+=1
print(k)
"""
#5
k=0
k1=0
for a1 in "АЖИМНУЧ":
    for a2 in "АЖИМНУЧ":
        for a3 in "АЖИМНУЧ":
            for a4 in "АЖИМНУЧ":
                for a5 in "АЖИМНУЧ":
                    for a6 in "АЖИМНУЧ":
                        s=a1+a2+a3+a4+a5+a6
                        k+=1
                        if k%2==0 and s.count("Ч")<=1 and s[0]!="Ж":
                            k1+=1
print(k1)
"""