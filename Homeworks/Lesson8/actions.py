import data

def write_to_the_head_of_the_company(text):
    data.mail_head_company.append(f"{data.selected_role}: {text}")
    data.export_to_file("mail_head_company", data.mail_head_company)

def write_to_the_dep_manager(text):
    data.mail_manager.append(f"{data.selected_role}: {text}")
    data.export_to_file("mail_manager.txt", data.mail_manager)

def write_to_an_employee(text):
    data.mail_employee.append(f"{data.selected_role}: {text}")
    data.export_to_file("mail_employee", data.mail_employee)
