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

    with open(path, 'a', encoding='UTF-8') as file:
        json.dump(contact, file, ensure_ascii=False)

def show_on_screen(contacts: list) -> None:
        decode_key = dict(
            first_name = 'Имя',
            second_name = 'Фамилия',
            contacts = 'Телефон'
        )
        pretty_text = str()
        for num, elem in enumerate(contacts, 1):
            pretty_text += f'Контакт #{num}:\n'
            pretty_text += '\n'.join(f'{decode_key[k]}: {v}' for k, v in elem.items())
            pretty_text += '\n________\n'
        print(pretty_text)
def new_contact() -> dict:
    return dict(
        first_name = input('Введите имя контакта:\n>>>'),
        second_name = input('Введите фамилию контакта:\n>>>'),
        contacts = input('Введите номер телефона:\n>>>')
    )

def change_contact(ind: int, contact: dict) -> None:
    global phone_book
    phone_book.pop(ind-1)
    phone_book.insert(ind-1, contact)

def delete_contact() -> None:


def main() -> None:
    data = load_from_file()
    show_on_screen(data)

if __name__ == '__main__':
    main()