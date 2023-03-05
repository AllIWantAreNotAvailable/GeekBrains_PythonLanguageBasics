import json


def obj_to_json_file(friends):
    with open('friends.json', 'w') as file:
        # преобразуем объект в json и сохраняем в файл
        json.dump(friends, file)


def load_obj_from_json_file():
    with open('friends.json', 'r') as file:
        friends = json.load(file)
    return friends


def obj_to_json(friends):

    json_friends = json.dumps(friends)
    # проверим, что мы получили
    print(json_friends, '->', type(json_friends))
    return json_friends


def load_obj_from_json(json_friends):
    return json.loads(json_friends)


def main():
    # Создадим структуру данных
    friends = [
        {
            'name': 'Max',
            'age': 23,
            'phones': [123, 234]
        },
        {
            'name': 'Leo',
            'age': 33
        }
    ]
    # Посмотрим как выглядит Наша структура и ее тип
    print(friends, '->', type(friends))

    # Преобразуем структуру friends в формат json
    json_friends = obj_to_json(friends)

    # Преобразуем json в объект
    load_obj_from_json(json_friends)
    #  посмотрим как теперь выглядит Наша структура и ее тип
    print(friends, '->', type(friends))

    # Запишем json в файл
    obj_to_json_file(friends)

    # Считаем json-файл и восстановим объект
    friends = load_obj_from_json_file()
    #  посмотрим как теперь выглядит Наша структура и ее тип
    print(friends, '->', type(friends))


if __name__ == '__main__':
    main()
