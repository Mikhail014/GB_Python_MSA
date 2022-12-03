from random import randint

k1 = int(input("Натуральная степень: "))
k2 = randint(1, k1 - 1) if k1 > 2 else 1
nums = [randint(0, 101) for i in range(3)]

math_op = ["+", "-"]

# with open("task5text1.txt", "w") as file:
# with open("task5text2.txt", "w") as file:
with open("task4text.txt", "w") as file:
    file.write(f"{nums[0]}x**{k1} {math_op[randint(0, 1)]} "
               f"{nums[1]}x**{k2} {math_op[randint(0, 1)]} "
               f"{nums[2]}")

# task4text.txt
# task5text1.txt
# task5text2.txt