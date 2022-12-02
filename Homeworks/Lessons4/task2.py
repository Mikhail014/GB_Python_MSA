n = int(input("Введите натуральное число: "))
res = []

for i in range(2, n):
    if n % i == 0:
        res.append(i)

print("Список простых множителей:")
print(res)