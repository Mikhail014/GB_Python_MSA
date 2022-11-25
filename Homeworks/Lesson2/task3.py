num = int(input("Введите число: "))
arrNums = []
sum = 0

for n in range(1, num + 1):
    arrNums.append((1 + 1 / n) ** n)

for i in arrNums:
    sum += i

print(f"Сумма: {round(sum, 3)}")