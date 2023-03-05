# Практическое задание №2:
# Создать модуль music_deserialize.py. В этом модуле открыть файлы: group.json и group.pickle.
# Прочитать из них информацию. И получить объект: словарь из предыдущего задания.


import pickle
import json


def deserialize_json():
    file_name = 'groups.json'
    with open(file_name, 'r', encoding='utf-8') as file:
        music_groups = json.load(file)
    return music_groups


def deserialize_pickle():
    file_name = 'groups.pickle'
    with open(file_name, 'rb') as file:
        music_groups = pickle.load(file)
    return music_groups


def main():
    print('Deserialize from pickle:')
    print(deserialize_pickle())
    print()
    print('Deserialize from json')
    print(deserialize_json())


if __name__ == '__main__':
    main()
