# Практическое задание №14:
# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей
# любимой музыкальной группы, например:

# my_favourite_group = {
#                       ‘name’: ‘Г.М.О.’,
#                       ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
#                       ‘Albums’: [
#                                   {
#                                        ‘name’: ‘Делать панк-рок’,
#                                        ‘year’: 2016
#                                    },
#                                   {
#                                        ‘name’: ‘Шапито’,
#                                        ‘year’: 2014
#                                    }
#                                   ]
#                       }

# С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
# вывести результаты в терминал. Записать результаты в файлы group.json, group.pickle
# соответственно. В файле group.json указать кодировку utf-8.


import pickle
import json


def serialize_json(obj):
    file_name = 'groups.json'
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(obj, file)
    print(file_name, 'was created with "json"')


def serialize_pickle(obj):
    file_name = 'groups.pickle'
    with open(file_name, 'wb') as file:
        pickle.dump(obj, file)
    print(file_name, 'was created with "pickle"')


def get_my_music():
    my_favorite = [
        {
            'name': {'rus': 'Океан Ельзы', 'eng': 'Okean Elzy'},
            'formed': 1994,
            'discography': [
                {'studio_albums': [
                    {
                        'name': {'rus': 'Там, де нас нема', 'eng': "There, Where We Aren't"},
                        'released': 1998
                    },
                    {
                        'name': {'rus': 'Я на небі був', 'eng': 'I Was In Heaven'},
                        'released': 2000
                    }
                ],
                    'acoustic_albums': [
                        {
                            'name': {'rus': 'Tviy format', 'eng': 'Your format'},
                            'released': 2003
                        }
                    ]
                }
            ]
        },
        {
            'name': {'rus': 'Машина времени', 'eng': 'Mashina Vremeni'},
            'formed': 1969,
            'discography': [
                {'studio_albums': [
                    {
                        'name': {'rus': 'Это было так давно', 'eng': "It was so long ago't"},
                        'released': 1978
                    },
                    {
                        'name': {'rus': 'Маленький принц', 'eng': 'The Little Prince'},
                        'released': 1979
                    }
                ]
                }
            ]
        }
    ]

    return my_favorite


def main():
    groups = get_my_music()
    serialize_pickle(groups)
    serialize_json(groups)


if __name__ == '__main__':
    main()
