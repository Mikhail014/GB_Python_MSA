"""""""""
Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов.
Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""""""""

from random import random

size = int(input("Количество элементов в списке: "))
arr_nums = [round(random() * 10, 3) for i in range(0, size)]

print("Список:")
print(arr_nums)

max = arr_nums[0] % 1
min = arr_nums[0] % 1

for i in arr_nums:
    frac_num = i % 1
    if frac_num > max:
        max = frac_num
    elif frac_num < min:
        min = frac_num

print(f"Разница: {round(max % 1 - min % 1, 3)}")


