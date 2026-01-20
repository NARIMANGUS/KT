import random
def otvet_babushki():
    return f"НЕТ, НИ РАЗУ С {random.randint(1930, 1950)} ГОДА!"


# БЕСКОНЕЧНЫЙ ЦИКЛ ПОД ТЗ, ДЛЯ ВЫХОД ИЗ ЦИКЛ ВВЕСТИ ПОДРЯД "ПОКА!"  - 3 РАЗА
govor = str(input("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ,МИЛОК?!"))
while True:
    # ДОРОГА НА ВЫХОД ИЗ ПРОГРАММЫ
    if govor == "ПОКА!":
        print(otvet_babushki())
        govor = str(input(""))
        if govor == "ПОКА!":
            print(otvet_babushki())
            import random


            def otvet_babushki():
                return f"НЕТ, НИ РАЗУ С {random.randint(1930, 1950)} ГОДА!"


            # БЕСКОНЕЧНЫЙ ЦИКЛ ПОД ТЗ, ДЛЯ ВЫХОД ИЗ ЦИКЛ ВВЕСТИ ПОДРЯД "ПОКА!"  - 3 РАЗА
            govor = str(input("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ,МИЛОК?!"))
            while True:
                # ДОРОГА НА ВЫХОД ИЗ ПРОГРАММЫ
                if govor == "ПОКА!":
                    print(otvet_babushki())
                    govor = str(input(""))
                    if govor == "ПОКА!":
                        print(otvet_babushki())
                        govor = str(input(""))
                        if govor == "ПОКА!":
                            print("ДО СВИДАНИЯ, МИЛЫЙ!")
                            break
                        else:
                            continue
                    else:
                        continue
                elif govor.isupper():
                    print(otvet_babushki())
                else:
                    print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
                govor = str(input(""))

            if govor == "ПОКА!":
                print("ДО СВИДАНИЯ, МИЛЫЙ!")
                break
            else:
                continue
        else:
            continue
    elif govor.isupper():
        print(otvet_babushki())
    else:
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
    govor = str(input(""))
