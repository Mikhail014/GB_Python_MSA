num = int(input("Введите число: "))

if num > 5 and num < 8:
    print(f"{num} - выходной")
elif num < 1 or num > 7:
    print(f"{num} - это не день недели")
else:
    print(f"{num} - это будний день")
