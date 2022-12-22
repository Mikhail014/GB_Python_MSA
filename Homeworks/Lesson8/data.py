mail_head_company = []
mail_manager = []
mail_employee = []
selected_role = ""
is_active_program = True

def export_to_file(filename, message):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{message}\n")

def import_from_file(filename, arr):
    with open(filename, "r", encoding="utf-8") as file:
        for i in file.readlines():
            arr.append(i)

def all_data_import():
    import_from_file("mail_head_company", mail_head_company)
    import_from_file("mail_manager.txt", mail_manager)
    import_from_file("mail_employee", mail_employee)