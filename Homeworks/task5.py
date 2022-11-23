from math import sqrt

print("Координаты первой точки:")
x1 = int(input("x = "))
y1 = int(input("y = "))

print("Координаты второй точки:")
x2 = int(input("x = "))
y2 = int(input("y = "))

dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"\nРасстояние между точками: {dist}")