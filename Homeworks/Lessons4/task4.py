from random import randint

k = int(input("Натуральная степень: "))
nums = [randint(0, 101) for i in range(3)]

math_op = ["+", "-"]

with open("task4text.txt", "w") as file:
    file.write(f"{nums[0]}x**{k} {math_op[randint(0, 1)]} "
               f"{nums[1]}x**{randint(1, k)} {math_op[randint(0, 1)]} "
               f"{nums[2]}")


# task4text.txt
# task5text1.txt
# task5text2.txt