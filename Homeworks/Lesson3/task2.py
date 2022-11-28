"""""""""
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""""""""

from random import randint
from  math import ceil

size = int(input("Количество элементов в списке: "))
arr_nums = [randint(1, 10) for i in range(0, size)]

print("Список:")
print(arr_nums)

res = []

for i in range(ceil(size / 2)):
    res.append(arr_nums[i] * arr_nums[-i - 1])

print(f"Результат: {res}")