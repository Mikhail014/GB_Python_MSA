n = int(input("Введите натуральное число: "))
res = []
i = 2

while n != 1:
    if n % i == 0:
        res.append(i)
        n //= i
    else:
        i += 1

print("Список простых множителей:")
print(res)