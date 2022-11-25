num = float(input("Введите число: "))
sum = 0

while num != 0:
    sum += num % 10
    num //= 10

print(f"Сумма цифр: {int(sum)}")