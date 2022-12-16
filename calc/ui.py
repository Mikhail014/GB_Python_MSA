import operations

def choice_operation():
    print("Это калькулятор!\n")
    print("Введи число от 1 до 4, чтобы выбрать операцию:")
    print("1. Сложение;")
    print("2. Вычитание;")
    print("3. Умножение;")
    print("4. Деление.")

    return int(input("Операция: "))


def get_result():
    enter_num = choice_operation()

    print("Теперь введи числа, над которыми нужно провести операции:")
    n1 = int(input("Первое число: "))
    n2 = int(input("Второе число: "))

    if enter_num == 1:
        return f"Результат: {operations.sum(n1, n2)}"
    elif enter_num == 2:
        return f"Результат: {operations.sub(n1, n2)}"
    elif enter_num == 3:
        return f"Результат: {operations.mul(n1, n2)}"
    elif enter_num == 4:
        return f"Результат: {operations.divis(n1, n2)}"
