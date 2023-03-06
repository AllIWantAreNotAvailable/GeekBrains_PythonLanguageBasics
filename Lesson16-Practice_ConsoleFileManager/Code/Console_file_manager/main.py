import sys
import os
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info

save_info('[START] - Начало работы программы')
try:
    save_info('[info] - Попытка считать команду')
    command = sys.argv[1]
except IndexError:
    save_info('[!] - Ошибка при попытке считать команду')
    print('Чтобы начать работу с менеджером, введите команду.\n'
          'Чтобы узнать все команды введите "help".')
else:
    if command == 'list':
        save_info('[info] - Была считана команда "list"')
        print(get_list())
        save_info(f'[info] - {command} была выполнена')
    elif command == 'create_file':
        save_info('[info] - Была считана команда "create_file"')
        try:
            save_info('[info] - Попытка считать имя создаваемого файла')
            name = sys.argv[2]
            temp = name.split('.')
            if not (1 < len(temp) < 3 and 0 < len(temp[1])):
                raise NameError('[!] - Неверный формат имени файла.'
                                'необходимо ввести имя файла в формате *имя_файла*.*расширение*')
        except IndexError:
            save_info('[!] - Ошибка при попытке считать имя создаваемого файла')
            print('Для создания файла, после команды "create_file" необходимо ввести имя файла '
                  'в формате *имя*.*расширение*')
        except NameError as e:
            save_info('[!] - Неверный формат имени файла.')
            print(e)
        else:
            save_info(f'[info] - Начато создание файла "{name}"')
            create_file(name=name)
            save_info(f'[info] - {command} была выполнена')
    elif command == 'create_folder':
        save_info('[info] - Была считана команда "create_folder"')
        try:
            save_info('[info] - Попытка считать имя создаваемой папки')
            name = sys.argv[2]
        except IndexError:
            save_info('[!] - Ошибка при попытке считать имя создаваемой папки')
            print('Для создания папки, после команды "create_folder" необходимо ввести имя папки')
        else:
            save_info(f'[info] - Начато создание папки "{name}"')
            create_folder(name=name)
            save_info(f'[info] - {command} была выполнена')
    elif command == 'delete':
        save_info('[info] - Была считана команда "delete"')
        try:
            save_info('[info] - Попытка считать имя файла (папки) для удаления')
            if len(sys.argv) == 3:
                name = sys.argv[2]
            else:
                name = ''
                for string in sys.argv[2:]:
                    name += f'{string} '
                else:
                    name = name.strip()
        except IndexError:
            save_info('[!] - Ошибка при попытке считать имя для удаления файла (папки)')
            print('Для для удаления файла (папки), после команды "delete" необходимо ввести имя файла (папки)')
        else:
            save_info(f'[info] - Начато удаление файла "{name}"')
            delete_file(name=name)
            save_info(f'[info] - {command} была выполнена')
    elif command == 'copy':
        save_info('[info] - Была считана команда "copy"')
        try:
            save_info('[info] - Попытка считать имя файла (папки) для копирования')
            name = sys.argv[2]
        except IndexError:
            save_info('[!] - Ошибка при попытке считать имя файла (папки) для копирования')
            print('Для для копирования файла (папки), после команды "copy" необходимо ввести имя файла (папки)')
        else:
            try:
                save_info('[info] - Попытка считать имя копии файла (папки)')
                new_name = sys.argv[3]
                if not os.path.isdir(name):
                    temp = new_name.split('.')
                    if not (1 < len(temp) < 3 and 0 < len(temp[1])):
                        raise NameError('[!] - Неверный формат имени файла.'
                                        'необходимо ввести имя файла в формате *имя_файла*.*расширение*')
            except IndexError:
                save_info('[!] - Ошибка при попытке считать имя копии файла (папки)')
                print('[info] - Вы не указали имя копии файла (папки), будет использовано имя по умолчанию')
                save_info(f'[info] - Начато копирование файла (папки) "{name}" с использованием имени по умолчанию')
                copy_file(name=name)
                save_info(f'[info] - {command} была выполнена')
            except NameError as e:
                save_info('[!] - Неверный формат имени файла.')
                print(e)
            else:
                save_info(f'[info] - Начато копирование файла (папки) "{name}" -> {new_name}')
                copy_file(name=name, name_of_copy=new_name)
                save_info(f'[info] - {command} была выполнена')
    elif command == 'help':
        save_info('[info] - Была считана команда "help"')
        print('Консольный файловый менеджер.\n'
              'Список команд:\n'
              '1) help - помощь, список команд\n'
              '2) list - показать список файлов и папок;\n'
              '3) create_file - создание файла;\n'
              '4) create_folder - создание папки;\n'
              '5) delete - удаление файла или папки;\n'
              '6) copy - копирование файла или папки;\n')
        save_info(f'[info] - {command} была выполнена')
    else:
        save_info(f'[info] - Считана неизвестная команда -> "{command}"')
        print('Неизвестная команда.\n'
              'Чтобы узнать все команды введите "help".')
finally:
    save_info('[END] - Завершение работы программы')
    print('Завершение работы программы')
