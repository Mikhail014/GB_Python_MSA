import data

def add_contact(lastname, firstname, phone, about):
    data.list_data.append({
        "Фамилия": lastname,
        "Имя": firstname,
        "Телефон": phone,
        "Описание": about
    })
    data.export_to_file("contacts")

def print_contacts():
    contacts = "\n"
    for contact in data.list_data:
        for key, value in contact.items():
            contacts += f"{key}: {value}\n"
        contacts += "\n"
    return contacts