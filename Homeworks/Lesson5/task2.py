from random import randint

print("------------------------------------------------------")
print("Добро пожаловать в игру '2021 конфета'!!!")
print("------------------------------------------------------")
print("За один ход можно забрать не более 28 конфет!")
print("------------------------------------------------------")
print("Играю два игрока, делая ход друг после друга.")
print("------------------------------------------------------")
print("Первый ход определяется жеребьевкой.")
print("------------------------------------------------------")
print("Все конфеты достаются тому, кто сделает последний ход.")
print("------------------------------------------------------")

print()

candies = 202
isEnd = False
modeBot = False
players = []

user1 = input("Введи свое имя: ")
user2 = None

print("С кем будешь играть?")
print("1. С человеком")
print("2. С ботом")
askBot = input("Ответ: ")

if askBot == "1":
    print("Хорошо! Настроена игра с человеком")
    user2 = input("Введи его имя: ")
else:
    modeBot = True
    print("Хорошо! Настроена игра с ботом")
    user2 = "Бот"

players.append(user1 if randint(0, 9) % 2 == 0 else user2)
players.append(user2 if players[0] != user2 else user1)

print("\n---------------------------------")
print(f"Игру начинает - {players[0]}")
print("---------------------------------\n")

while not isEnd:
    for pl in players:
        if pl == "Бот" and modeBot:
            entered_num = 28 if candies > 28 else candies
            print(f"Бот взял конфет: {entered_num}")
        else:
            entered_num = int(input(f"{pl}, возьми конфеты, но не более 28: "))
            while entered_num > 28 or entered_num < 1:
                entered_num = int(input(f"Ошибка! Введи число от 1 до 28 включительно: "))
        candies -= entered_num
        if candies <= 0:
            print("\n---------------------------------")
            print(f"{pl} одержал победу!!!")
            print("---------------------------------\n")
            isEnd = True
            break
        else:
            print(f"Осталось конфет: {candies}\n")