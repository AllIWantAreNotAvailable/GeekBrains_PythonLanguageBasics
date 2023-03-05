# Организуем запись и чтение данных (объектов) с помощью встроенного модуля pickle


import pickle


def save_to_file(obj: dict):
    # Открываем файл:
    with open('person.dat', 'wb') as file:
        # сразу записываем объект целиком с помощью pickle
        pickle.dump(obj, file)
    print(f'{obj} -> Объект был записан')


def read_from_file() -> dict:
    # Открываем файл:
    with open('person.dat', 'rb') as file:
        person = pickle.load(file)
        return person


def main():
    person = {
        'name': 'Max',
        'phones': [
            123,
            345
        ],
        'age': 20
    }

    save_to_file(person)
    read_obj = read_from_file()
    print(f'{read_obj} -> Объект считан')


if __name__ == '__main__':
    main()
