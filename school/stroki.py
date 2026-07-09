"""
#1
world1 = input("Ведите любое слово: ")
world2 =input("Ведите любое слово: ")

if world1[0] == world2[-1]:
    print("True")
else:
    print("False")
#2
a="яблоко"
b= a[1:5] #блок
c= a[3:] #око

print(b) 
print(c)
#3
a="строка"
b= a.replace("к","ф")
print(b)

#4
sentanse=input("Введи предложение: ")
m=sentanse.lower().count("м")
n=sentanse.lower().count("н")
if m>n:
    print(f"Букв м больше, их {m}")
else:
    print(f"Букв н больше, их {n}")

#5
sentanse=input("Введи предложение: ")
abc="уеыаоэяиюё"
count=0
for k in sentanse.lower():
    if k in abc:
        count+=1
print(count)
"""
#6
c1=input("Введи любой город: ")
c2=input("Введи любой город: ")
c3=input("Введи любой город: ")

long=c1
if len(c2)> len(long):
    long = c2
if len(c3)>len(long):
    long =c3


