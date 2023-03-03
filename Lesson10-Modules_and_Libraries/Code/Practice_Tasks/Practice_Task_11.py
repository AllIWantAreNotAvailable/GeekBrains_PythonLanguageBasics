# Практическое задание 11:
# Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из
# которой запущен данный код. Затем создайте вторую функцию удаляющую эти папки.
# Проверьте работу функций в этом же модуле.


import os
import time


def make_dirs_list():
    dirs_paths = []
    for i in range(1, 9):
        dirs_paths.append(os.path.join(os.getcwd(), f'dir_{i}'))
    print(dirs_paths)
    return dirs_paths


def make_dirs(paths):
    for path in paths:
        os.mkdir(path)


def remove_dirs(paths):
    for path in paths:
        os.rmdir(path)


def main():
    list_of_paths_to_dirs = make_dirs_list()
    make_dirs(list_of_paths_to_dirs)
    time.sleep(5)
    remove_dirs(list_of_paths_to_dirs)


if __name__ == '__main__':
    main()
