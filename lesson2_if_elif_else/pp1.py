
symbol = input("введите любой символ с клавиатуры: ")

if len(symbol) == 0:
    print("Ошибка ввода. Вы ничего не ввели. Программа будет закрыта.")
    exit()

if len(symbol) > 1:
    print("Ошибка ввода. Вы ввели не символ, а строку. Программа будет закрыта.")
    exit()

#TODO проверка на длину вводимой строки

if symbol >= "a" and symbol <= "z" or symbol >= "A" and symbol <= "Z":
    print("это английская буква")
    if symbol >= "a" and symbol <= "z":
        print("маленькая")
    else:
        print("большая")

elif symbol >= "0" and symbol <= "9":
    print("это цифра")
    if int(symbol)%2==0:
        print("чётная")
    else:
        print("нечётная")
else:
    print("это неизвестный символ")
