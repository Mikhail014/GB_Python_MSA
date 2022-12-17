import operations
import data

def action_choice():
    print("Телефонная книга")
    print("----------------")
    print("Выберите действие:")
    print("1. Добавить запись;")
    print("2. Вывод записей на экран;")
    print("3. Экспорт записей;")
    print("4. Импорт записей;")
    print("5. Поиск записи;")
    print("6. Удаление записи.")
    print("----------------")
    return int(input("Ответ: "))

def start_action(num_action):
    if num_action == 1:
        ln = input("Введите фамилию: ")
        fn = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        about = input("Введите описание: ")
        operations.add_contact(ln, fn, phone, about)
        return f"Данные контакта {ln} {fn} добавлены!"
    elif num_action == 2:
        return operations.print_contacts()
    elif num_action == 3:
        fn = input("Введите имя файла: ")
        print("Выберите формат экспорта:")
        print("1. Данные одного пользователя на разных строках;")
        print("2. Данные одного пользователя на одной строке.")
        mode = int(input("Ответ: "))
        while mode < 1 or mode > 2:
            mode = input("Введите 1 или 2: ")
        data.export_to_file(fn, mode)
        return f"Данные экспортированы в файл {fn}!"
    elif num_action == 4:
        fn = input("Введите имя файла: ")
        data.import_from_file(fn)
        return f"Данные импортированы из файла {fn}!"