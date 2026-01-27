import random

def otvet():
    return f"НЕТ, НИ РАЗУ С {random.randint(1930, 1950)} ГОДА!"

bye_streak = 0

govor = input("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?! ")

while True:
    govor = govor.strip()

    if govor == "ПОКА!":
        bye_streak += 1

        if bye_streak == 3:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
            break
        else:
            print(otvet())

    else:
        bye_streak = 0

        if govor.isupper() and govor != "":
            print(otvet())
        else:
            print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")

    govor = input()
