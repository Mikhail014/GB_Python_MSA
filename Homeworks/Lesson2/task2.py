num = int(input("Введите число: "))

arrNums = []

for i in range(1, num + 1):
    n = 1
    for j in range(1, i + 1):
        n *= j
    arrNums.append(n)

print(arrNums)

