import random

player_hp = 100
enemy_hp = 100
player_mana = 50
enemy_mana = 50
fireball_count = 0
heal_count = 0
mana_count = 0
shield_count = 0
miss_count = 0
critical_hit_count = 0
turn_number = 1


while True: #цикл, чтобы начать заново

    player_name = input("\nПривет! Чтобы вступить в игру введи своё имя: ")

    print(f"\nДобро пожаловать в игру 'Дуэль магов', {player_name}!")
    print("\nДоступные заклинания:")
    print("1. Огненный шар: урон 25, стоимость 15 маны")
    print("2. Щит: защита на 1 ход, стоимость 10 маны")
    print("3. Восстановление маны: +15 маны, стоимость 5 маны")
    print("4. Лечение: +20 здоровья, стоимость 20 маны")
    print("\nТак же есть шанс промаха, который равен 10%, а критического удара(урон х2) - 20%")


    while player_hp > 0 and enemy_hp > 0:
        print(f"\n-----------РАУНД {turn_number}-----------")
        print(f"\n{player_name}: hp {player_hp}/100, мана {player_mana}/50")
        print(f"Враг: hp {enemy_hp}/100, мана {enemy_mana}/50")

        player_shield_on = False
        enemy_shield_on = False

        if player_mana == 0:
            player_mana = 15
            print("\nУ вас нет маны. Вы пропускаете ход и восстанавливаете 15 маны.")
        else:
            player_action = 0
            
            while player_action not in [1, 2, 3, 4]:
                player_action = input("\nВыберите заклинание (1-4): ")

                if not player_action.isdigit():
                    print("Ошибка. Введите число от 1 до 4.")
                    player_action = 0

                player_action = int(player_action)

                if player_action not in [1, 2, 3, 4]:
                    print("Ошибка. Выберите число от 1 до 4.")
                    player_action = 0

                if player_action == 1 and player_mana < 15:
                    print("Недостаточно маны для огненного шара. Выберите другое заклинание.")
                    player_action = 0
                elif player_action == 2 and player_mana < 10:
                    print("Недостаточно маны для щита. Выберите другое заклинание.")
                    player_action = 0
                elif player_action == 3 and player_mana < 5:
                    print("Недостаточно маны для восстановления маны.Выберите другое заклинание.")
                    player_action = 0
                elif player_action == 4 and player_mana < 20:
                    print("Недостаточно маны для лечения. Выберите другое заклинание.")
                    player_action = 0

        #ход игрока
            if player_action == 1:
                fireball_count += 1
                if random.random() < 0.1: #шанс промаха 10%
                    miss_count += 1
                    print("\nВы использовали огненный шар, но вы промахнулись:(")
                else:
                    damage = 25
                    if random.random() < 0.2: #шанс крит удара 20 % и урон x2
                        damage *= 2
                        print(f"\nВы использовали огненный шар и нанесли критический удар! Урон по врагу равен {damage}.")
                        critical_hit_count +=1
                    if enemy_shield_on: #учёт щита
                        damage -= 10
                    enemy_hp -= damage
                    print(f"\nВы использовали огненный шар. Урон по врагу равен {damage}.")
                player_mana -= 15
            elif player_action == 2:
                player_shield_on = True
                player_mana -= 10
                shield_count += 1
                print("\nВы поставили щит.")
            elif player_action == 3:
                player_mana += 15
                if player_mana > 50:
                    player_mana = 50
                player_mana -= 5
                mana_count += 1
                print("\nВы восстановили ману.")
            elif player_action == 4:
                player_hp += 20
                if player_hp > 100:
                    player_hp = 100
                player_mana -= 20
                heal_count += 1
                print("\nВы исцелились.")

        #ход врага
        if enemy_mana == 0:
                enemy_mana = 15
                print("\nУ врага нет маны. Он пропускает ход и восстанавливает 15 маны.")
        else:
            enemy_action = random.randint(1, 4)

            if enemy_action == 1 and enemy_mana >= 15:
                if random.random() < 0.1: #шанс промаха 10%
                    print("Враг использовал огненный шар и промахнулся!")
                else:
                    damage = 25
                    if random.random() < 0.2: #шанс крит удара 20 % и урон x2
                        damage *= 2
                        print(f"Враг использовал огненный шар и нанёс критический удар! Урон по вам {damage}")
                    if player_shield_on:  #учёт щита
                        damage -= 10
                    player_hp -= damage
                    print(f"Враг использовал огненный шар и нанёс вам {damage} урона.")
                enemy_mana -= 15
            elif enemy_action == 2 and enemy_mana >= 10:
                enemy_shield_on = True
                enemy_mana -= 10
                print("Враг поставил щит.")
            elif enemy_action == 3 and enemy_mana >= 5:
                enemy_mana += 15
                if enemy_mana > 50:
                    enemy_mana = 50
                enemy_mana -= 5
                print("Враг восстановил ману.")
            elif enemy_action == 4 and enemy_mana >= 20:
                enemy_hp += 20
                if enemy_hp > 100:
                    enemy_hp = 100
                enemy_mana -= 20
                print("Враг исцелился.")

        turn_number += 1

    if player_hp <= 0 and enemy_hp <= 0:
        winner = "Ничья."
    elif player_hp <= 0:
        winner = "Враг победил:( Ничего, в следующий раз повезёт"
    else:
        winner = f"Вы победили, маг {player_name}! Поздравляю!"

    print(f"\n-----------ИГРА ОКОНЧЕНА!-----------")
    print(winner)
    print("\nСтатистика боя:")
    print(f"Использовано огненных шаров: {fireball_count}")
    print(f"Использовано лечения: {heal_count}")
    print(f"Восстановили ману: {mana_count}")
    print(f"Использовали щит: {shield_count}")
    print(f"Было промахов: {miss_count}")
    print(f"Нанесено критических ударов: {critical_hit_count}")
    print(f"Всего ходов: {turn_number - 1}")
    

    fin = input("\nХотите начать заново? да/нет: ").lower()
    if fin == "да" or fin == "lf":
        print("Начинаем заново!")
        continue
    elif fin == "нет" or fin == "ytn":
        print("Игра завершена. До встречи!")
        break
    else:
        print("Неправильный ввод. Введите 'да' или 'нет'.")
