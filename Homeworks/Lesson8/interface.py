import roles
import data
import actions

def select_role():
    print("\nПожалуйста, выберите роль:")
    for i, v in enumerate(roles.roles_list):
        print(f"{i+1}: {v}")
    num_role = int(input("Ответ: "))
    while num_role < 1 or num_role > 3:
        num_role = int(input("Введите число от 1 до 3 включительно: "))
    roles.set_role(roles.roles_list[num_role - 1])

def action_mode(role):
    print(f"\nВы вошли как: {data.selected_role}!")
    print("Выберите действие:")
    if role != roles.roles_list[0]:
        print("1. Написать руководителю компании")
    if role != roles.roles_list[1]:
        print("2. Написать менеджеру отдела")
    if role != roles.roles_list[2]:
        print("3. Написать рядовому сотруднику")
    print("4. Проверить почту")
    print("5. Изменить роль")
    print("6. Выход из программы")
    print("---\n")
    choice = input("Ответ: ")
    if choice == "1" and role != roles.roles_list[0]:
        send_a_message(actions.write_to_the_head_of_the_company)
    elif choice == "2" and role != roles.roles_list[1]:
        send_a_message(actions.write_to_the_dep_manager)
    elif choice == "3" and role != roles.roles_list[2]:
        send_a_message(actions.write_to_an_employee)
    elif choice == "4":
        print("\n---Почта---")
        check_email(role)
        print("\n")
    elif choice == "5":
        select_role()
    elif choice == "6":
        data.is_active_program = False
        print("Вы вышли из программы!")
    else:
        print("\nПожалуйста, выберите другое действие!\n")


def check_email(role):
    arr = []
    if role == roles.roles_list[0]:
        arr = data.mail_head_company
    elif role == roles.roles_list[1]:
        arr = data.mail_manager
    elif role == roles.roles_list[2]:
        arr = data.mail_employee
    for i in arr:
        print(i)

def send_a_message(func):
    message = input("\nНапишите сообщение: ")
    func(message)
    print("Сообщение отправлено!\n")