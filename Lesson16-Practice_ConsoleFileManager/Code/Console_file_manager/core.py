import os
import shutil
import datetime


# Шаг 1. Функция для создания файла.
def create_file(name: str, text: str = None) -> None:
    """
    Создает файл с именем "name" и записывает в него переданные данные (text).
    :param name: Имя файла, которое будет присвоено ему при создании (включая расширение), например: "test.txt".
    :param text: Текст, который будет записан в созданный файл.
    :return: None
    """
    name = name.strip()
    with open(name, 'w', encoding='utf-8') as file:
        if text:
            file.write(text)
    save_info(f'[info] - Была создан файл с именем "{name}"')
    print(f'[info] - Была создан файл с именем "{name}"')


# Шаг 2. Функция для создания папки.
def create_folder(name: str = 'new_folder') -> None:
    """
    Функция создает папку с именем "name", по умолчанию "new_folder".
    :param name: Имя, которое будет присвоено новой папке, по умолчанию "new_folder". Если
    папка с таким именем уже существует, то ничего не произойдет.
    :return: None
    """
    name = name.strip()
    try:
        os.mkdir(name)
    except FileExistsError:
        save_info(f'[!] - Папка с именем "{name}" уже есть')
        print(f'[!] - Папка с именем "{name}" уже есть')
    else:
        save_info(f'[info] - Была создана папка с именем "{name}"')
        print(f'[info] - Была создана папка с именем "{name}"')


# Шаг 3. Функция для просмотра файлов и папок.
def get_list(folders_only: bool = False) -> str:
    """
    Функция возвращает нумерованный список файлов (папок) строкой.
    :param folders_only: Если Истина, выводит только папки
    :return: Строка с нумерованным списком файлов (папок).
    """
    result = os.listdir()
    if folders_only:
        result = [file for file in result if os.path.isdir(file)]

    files_string = ''
    for number, file in enumerate(result, start=1):
        files_string += f'{number}. {file}\n'
    return files_string


# Шаг 4. Удаление файлов(папок)
def delete_file(name) -> None:
    """
    Функция удаляет файл (папку) по имени "name".
    :param name: Имя файла (папки) которая будет удалена.
    :return: None
    """
    try:
        if os.path.isdir(name):
            os.rmdir(name)
            save_info(f'[info] - папка "{name}" была удалена с компьютера')
            print(f'[info] - папка "{name}" была удалена с компьютера')
        else:
            os.remove(name)
            save_info(f'[info] - файл "{name}" была удален с компьютера')
            print(f'[info] - файл "{name}" была удален с компьютера')
    except FileNotFoundError:
        save_info(f'[!] - Файл (папка) с именем "{name}" не найдена')
        print(f'[!] - Файл (папка) с именем "{name}" не найдена')

# Шаг 5. Копирование файла (папки)
def copy_file(name: str, name_of_copy: str = '') -> None:
    """
    Функция создает копию папки с именем "name", с учетом всех вложенных файлов (папок).
    :param name: Имя копируемой папки.
    :param name_of_copy: Имя создаваемой копии, по умолчанию "{name} – copy.*". Если
    папка с таким именем уже существует, то ничего не произойдет.
    :return: None
    """
    if os.path.isdir(name):
        # Если имя копии не задано, то по умолчанию добавляем к имени файла "– copy"
        if not name_of_copy:
            name_of_copy = f'{name.strip()} – copy'
        else:
            name_of_copy = name_of_copy.strip()

        try:
            shutil.copytree(name, name_of_copy)
        except FileExistsError:
            save_info(f'[!] - Не удалось создать копию {name}, папка с именем "{name_of_copy}" уже существует')
            print(f'[!] - Не удалось создать копию {name}, папка с именем "{name_of_copy}" уже существует')
    else:
        if not name_of_copy:
            # Если имя копии не задано, то по умолчанию добавляем к имени файла "– copy"
            temp = name.strip().split('.')
            temp[0] = f'{temp[0]} - copy'
            temp.insert(-1, '.')
            name_of_copy = ''.join(temp)
        else:
            name_of_copy = name_of_copy.strip()
        try:
            shutil.copy(name, name_of_copy)
        except FileNotFoundError:
            save_info(f'[!] - Файл с указанным именем "{name}" не найден')
            print(f'[!] - Файл с указанным именем "{name}" не найден')
        else:
            save_info(f'[info] - создана копия файла {name} с именем {name_of_copy}')
            print(f'[info] - создана копия файла {name} с именем {name_of_copy}')


# Шаг 6. Сохранение логов
def save_info(message):
    """
    Создает запись лога формата "ДатаВремя – Сообщение (message)" в файл log.txt
    :param message: Сообщение, которое будет записано в файл-лога
    :return: None
    """
    current_time = datetime.datetime.now()
    result = f'{current_time} – {message}'

    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{result}\n')


if __name__ == '__main__':
    pass
