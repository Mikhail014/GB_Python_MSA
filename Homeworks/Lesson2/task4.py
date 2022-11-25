from random import randint

num = int(input("Введите положительное число для генерации списка: "))
mn1 = int(input("Первый множитель (индекс): "))
mn2 = int(input("Второй множитель (индекс): "))

arrNums = [i for i in range(-num, num + 1)]

res = arrNums[mn1] * arrNums[mn2]

print(f"Список: {arrNums}")
print(f"Произведение чисел: {res}")