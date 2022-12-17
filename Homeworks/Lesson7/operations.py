import data

def add_contact(lastname, firstname, phone, about):
    data.list_data.append({
        "Фамилия": lastname,
        "Имя": firstname,
        "Телефон": phone,
        "Описание": about
    })

def print_contacts():
    contacts = ""
    for contact in data.list_data:
        for key, value in contact.items():
            contacts += f"{key}: {value}\n"
    return contacts

def search_contact():
    pass

def delete_contact():
    pass