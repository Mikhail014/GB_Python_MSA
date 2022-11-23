x = int(input("X = "))
y = int(input("Y = "))

if x == 0 and y == 0:
    print("X и Y не должны быть равны нулю")
elif x > 0 and y > 0:
    print(f"Точка находится в первой четверти")
elif x < 0 and y > 0:
    print(f"Точка находится во второй четверти")
elif x < 0 and y < 0:
    print(f"Точка находится в третьей четверти")
elif x > 0 and y < 0:
    print(f"Точка находится в четвертой четверти")
elif x != 0 and y == 0:
    print(f"Точка находится на оси X")
elif y != 0 and x == 0:
    print(f"Точка находится на оси Y")

