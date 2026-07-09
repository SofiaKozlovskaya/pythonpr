#file = open("test.txt", "w")
#a=111

#file.write(str(111) + "\n")
#file.write(f"{a}")

#file.close()

all_test = ""

with open("test.txt", "r", encoding="utf-8") as file:
    all_text = file.read()

print(all_text)