planeNum = int(input("Номер плоскости: "))

if planeNum == 1:
    print("x = +inf, y = +inf")
elif planeNum == 2:
    print("x = -inf, y = +inf")
elif planeNum == 3:
    print("x = -inf, y = -inf")
elif planeNum == 4:
    print("x = +inf, y = -inf")
else:
    print("Введите число от 1 до 4")