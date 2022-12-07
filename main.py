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

# from time import time
#
# n1 = int(input("Введите первое число: "))
# n2 = int(input("Введите второе число: "))
#
# def rand_num(num1, num2):
#     return round((time() % 1) * (num2 - num1)) + num1
#
# print(rand_num(n1, n2))


# arr = ["22", "33", "123", "fert", "ytyy", "55"]
#
# num = int(input("Введите число: "))
#
# def is_there_a_number_in_arr(n):
#     for i in arr:
#         if i.isdigit():
#             if n == int(i):
#                 return True
#     return False
#
# res = is_there_a_number_in_arr(num)
#
# if res:
#     print(f"Число {num} присуствует в данном списке")
# else:
#     print(f"Числа {num} в данном списке нет")


# str = input("Введите строку: ")
# arrStr = ["qwe", "ser", "fdr", "fdr", "gtredf", "qwe", "ktg", "ser"]
#
# def get_index_second_occur_of_str(text, arr):
#     count_entry = 0
#     for i, v in enumerate(arr):
#         if text == v:
#             count_entry += 1
#             if count_entry == 2:
#                 return i
#     return -1
#
# res = get_index_second_occur_of_str(str, arrStr)
# print(res)

# file = open('file1')
#
# # print(1, file.read())
# # print(2, file.readline())
# # print(3, file.readlines())
#
# # file.write('text4')
# file.close()

#with open('file1') as file:
#     print(1, file.read())
#     # file.seek(0)
#     print(1, file.read())

#import second
#
# print(second.a)




# Task 1

# str1 = input("Enter string of nums: ")
#
# nums = str1.split(" ")
#
# max = int(nums[0])
# min = int(nums[0])
#
# for i in nums:
#     n = int(i)
#     if n > max:
#         max = n
#     elif n < min:
#         min = n
#
# print(max, min)


# a1 = int(input("A: "))
# b1 = int(input("B: "))
# c1 = int(input("C: "))
#
# def discriminant(a, b, c):
#     d = b**2 - (4 * a * c)
#     print(d)
#     if d < 0:
#         return -1
#     elif d >= 0:
#         return d
#
# res = discriminant(a1, b1, c1)
#
# if res == -1:
#     print("Корней нет")
# elif res == 0:
#     print("Один корень: ")
#     print(f"x = {-b1 / (a1 * 2)}")
# else:
#     print("Два корня:")
#     print(f"x1 = {(-b1 - res**0.5) / (a1 * 2)}")
#     print(f"x2 = {(-b1 + res**0.5) / (a1 * 2)}")


# print(discriminant(a1, b1, c1))







# num1 = int(input("Num 1: "))
# num2 = int(input("Num 2: "))
#
# def foundLCM(n1, n2):
#     count = n1 if n1 > n2 else n2
#     while True:
#         count += 1
#         if count % n1 == 0 and count % n2 == 0:
#             return count
#
# res = foundLCM(num1, num2)
# print(f"Наименьшее общее кратное чисел {num1} и {num2}: {res}")

# nums = []
#
# with open("file.txt", "r") as file:
#     nums = file.readline().split(" ", )
#
# for i, v in enumerate(nums):
#     nums[i] = int(v)
#
# res = [(i, i * i) for i in nums if i % 2 == 0]
#
# print(res)

# Task 1

# nums = []
#
# with open("file1", "r") as file:
#     nums = file.readline().split()
#
# nums = list(map(int, nums))
# res = None
#
# for i, v in enumerate(nums):
#     if i > 0 and nums[i] - 1 != nums[i - 1]:
#         res = v - 1
#
# print(res)
