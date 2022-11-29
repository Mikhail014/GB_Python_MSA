# n1 = int(input("Первое число: "))
# n2 = int(input("Второе число: "))
#
# def checkQuad(num1, num2):
#     if num1 < num2:
#         if num1 ** 2 == num2:
#             print(f"{num2} является квадратом числа {num1}")
#         else:
#             print(f"{num2} не является квадратом числа {num1}")
#     else:
#         if num2 ** 2 == num1:
#             print(f"{num1} является квадратом числа {num2}")
#         else:
#             print(f"{num1} не является квадратом числа {num2}")
#
# checkQuad(n1, n2)

# n1 = int(input("Первое число: "))
# n2 = int(input("Второе число: "))
# n3 = int(input("Третье число: "))
# n4 = int(input("Четвертое число: "))
# n5 = int(input("Пятое число: "))
#
# arrNums = [n1, n2, n3, n4, n5]
#
# def findMaxNum(arr):
#     max = arr[0]
#     for i in arr:
#         if i > max: max = i
#     return max
#
# res = findMaxNum(arrNums)
# print(res)

# n = int(input("Введите число: "))
#
# def printNumsInARange(num):
#     nums = str()
#     for i in range(-num, num + 1):
#         if i != num: nums += f"{str(i)}, "
#         else: nums += f"{str(i)}"
#     return nums
#
# res = printNumsInARange(n)
# print(res)

# nf = float(input("Введите дробное число: "))
#
# def firstDigitFloatNumber(nf):
#     return int((nf * 10) % 10)
#
# res = firstDigitFloatNumber(nf)
#
# if res != 0: print(f"Первая цифра дробной части числа {nf} = {res}")
# else: print("Вы ввели целое число!!!")

# n = int(input("Введите число: "))
# res = [1]
#
# for i in range(1, n):
#     res.append(res[-1] * -3)
#
# print(res)

# n = int(input("Введите число: "))
# res = [1]
#
# for i in range(1, n):
#     res.append(3 * i + 1)
#
# print(res)

# s1 = input("Str 1: ")
# s2 = input("Str 2: ")
# entry = 0
#
# len_s2 = len(s2)
# count = len(s1) - len_s2 + 1
#
# for i in range(count):
#     if s1[i : i+len_s2] == s2:
#         entry += 1
#
# print(f"Количество вхождений: {entry}")

from time import time

n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))

def rand_num(num1, num2):
    return round((time() % 1) * (num2 - num1)) + num1

print(rand_num(n1, n2))
