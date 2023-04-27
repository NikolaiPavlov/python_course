# Телефонный справочник
# Time code: 48:49/2:11:22
import os
import json

def find_contact(contacts: list) -> dict:
    what = input('Кого ищем?\n>>> ')
    found = filter(lambda el: what in el['first_name'] or what in el['second_name'], contacts)
    show_on_screen(list(found))

def file_path(file_name = 'contact_list'):
    return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')

def load_from_file():
    path = file_path()

    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data

def save_to_file(contact: list) -> None:
    path = file_path()

    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(contact, file, ensure_ascii=False)
    print('Saved')

def show_on_screen(contacts: list) -> None:
        decode_key = dict(
            first_name = 'Имя',
            second_name = 'Фамилия',
            contacts = 'Телефон'
        )
        pretty_text = str()
        for num, elem in enumerate(contacts, 0):
            pretty_text += f'Контакт №{num}:\n'
            pretty_text += '\n'.join(f'{decode_key[k]}: {v}' for k, v in elem.items())
            pretty_text += '\n________\n'
        print(pretty_text)

def new_contact() -> dict:
    return dict(
        first_name = input('Введите имя контакта:\n>>>'),
        second_name = input('Введите фамилию контакта:\n>>>'),
        contacts = input('Введите номер телефона:\n>>>')
    )

def delete_contact() -> None:
    enumerate(load_from_file(), 0)
    show_on_screen(load_from_file())

    d = int(input('Введите номер контакта для удаления:\n>>> '))

    contacts = load_from_file()
    contacts.pop(d)
    save_to_file(contacts)

def change_contact() -> None:
    enumerate(load_from_file(), 0)
    show_on_screen(load_from_file())

    d = int(input('Введите номер контакта для изменения:\n>>> '))

    contacts = load_from_file()

def main() -> None:
    contacts = load_from_file()
    #contacts.append(new_contact())
    #show_on_screen(contacts)
    #save_to_file(contacts)
    delete_contact()

if __name__ == '__main__':
    main()