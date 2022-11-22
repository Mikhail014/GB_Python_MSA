n1 = int(input("Первое число: "))
n2 = int(input("Второе число: "))

def checkQuad(num1, num2):
    if num1 < num2:
        if num1 ** 2 == num2:
            print(f"{num2} является квадратом числа {num1}")
        else:
            print(f"{num2} не является квадратом числа {num1}")
    else:
        if num2 ** 2 == num1:
            print(f"{num1} является квадратом числа {num2}")
        else:
            print(f"{num1} не является квадратом числа {num2}")

checkQuad(n1, n2)