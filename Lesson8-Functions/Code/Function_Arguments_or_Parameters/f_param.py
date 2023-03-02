def hello_max():
    """
    Функция hello_max() – эта функция относится к первому типу: ничего не принимает и ничего не возвращает.
    Данная функция приветствует пользователя по имени 'Max'.
    """
    print('Hello, Max!')


def hello(who: str):
    """
    Функция hello() – эта функция относится ко второму типу: что-то принимает, но ничего не возвращает.
    Данная функция приветствует пользователя по имени, которое передается в параметр функции.
    :param who: Имя пользователя, которого нужно поприветствовать.
    :return: None
    """
    print(f'Hello, {who}!')


def greeting(say: str, who: str):
    """
    Функция greeting() – эта функция относится ко второму типу: что-то принимает, но ничего не возвращает.
    Эта функция приветствует пользователя по имени и определенным образом. Как приветствовать и имя пользователя
    передаются параметрами функции.
    :param say: Как приветствует функция.
    :param who: Имя пользователя, которого приветствует функция.
    :return: None
    """
    print(f'{say}, {who}!')


def main():
    """Функция main() – является главной управляющей функцией из которой запускаются другие.
    Наименование является "общепринятым", но не обязательным.
    :return: None
    """
    hello_max()
    hello('Leo')
    greeting('Привет', 'Мир')


# Точка входа – место, которое определяет начало программы.
# Почему такое условие: __name__ == '__main__'?
# Глобальная переменная __name__ хранит в себе имя запущенного модуля. Если, # текущий модуль не является импортируемым,
# то в переменной __name__ хранится значение "__main__", иначе имя модуля.
# Таким образом, можно определить функции которые должны/не должны работать при импорте данного модуля в другой
# исполняемый модуль.
if __name__ == '__main__':
    main()
