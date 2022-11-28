"""""""""
Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов списка, 
стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""""""""

from random import randint

arr_nums = [randint(1, 10) for i in range(0, 10)]

print("Список:")
print(arr_nums)

sum_items = 0
size = len(arr_nums)

for i, v in enumerate(arr_nums):
    if i % 2 != 0:
        sum_items += v

print(f"Сумма: {sum_items}")