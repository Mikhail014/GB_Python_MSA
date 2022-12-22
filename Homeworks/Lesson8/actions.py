import data

def write_to_the_head_of_the_company(text):
    message = f"{data.selected_role}: {text}"
    data.mail_head_company.append(message)
    data.export_to_file("mail_head_company", message)

def write_to_the_dep_manager(text):
    message = f"{data.selected_role}: {text}"
    data.mail_manager.append(message)
    data.export_to_file("mail_manager.txt", message)

def write_to_an_employee(text):
    message = f"{data.selected_role}: {text}"
    data.mail_employee.append(message)
    data.export_to_file("mail_employee", message)
