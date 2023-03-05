# Организуем собственную систему записи-чтения данных (объектов) в файлы

def save_to_file(obj: dict):
    # Открываем файл в режиме записи байт:
    with open('person.dat', 'wb') as file:
        # например, записываем объект в файл построчно:
        # 1) начнем с поля 'name':
        name = obj['name']
        # для того чтобы отделить поле от других, добавим перенос каретки:
        file.write(f'{name}\n'.encode('utf-8'))
        # 2) получим список телефонов:
        phones = obj['phones']
        # запишем телефоны через '; ':
        for phone in phones:
            file.write(f'{phone}; '.encode('utf-8'))
    print(f'Объект {obj} записан')


def read_from_file() -> dict:
    # Открываем файл в режиме чтения байт:
    with open('person.dat', 'rb') as file:
        # для того чтобы правильно считать объект, необходимо знать как он был записан:
        # 1) прочитаем файл и сохраним содержимое в список строк:
        result = file.readlines()
    # 2) весь файл был считан, нет необходимости держать его открытым
    # 3) восстановим исходный объект:
    # - помним, поля делили по строкам, первая была 'name':
    person = {'name': result[0].decode('utf-8').replace('\n', '')}
    # - далее идет строка с 'phones', они разделены '; ':
    phones = result[1].decode('utf-8').replace(';', '').strip().split(' ')
    person['phones'] = phones

    return person


def main():
    person = {
        'name': 'Max',
        'phones': [
            123,
            345
        ]
    }

    save_to_file(person)
    read_obj = read_from_file()
    print(read_obj)


if __name__ == '__main__':
    main()
