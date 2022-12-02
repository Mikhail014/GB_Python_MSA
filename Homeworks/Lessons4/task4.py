from random import randint

k = int(input("Натуральная степень: "))
nums = [randint(0, 101) for i in range(3)]

with open("task4text.txt", "w") as file:
    file.write(f"{nums[0]}x**{k} + {nums[1]}x + {nums[2]} = 0")