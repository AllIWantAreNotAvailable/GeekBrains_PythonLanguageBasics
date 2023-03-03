# Практическое задание №2:
# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.


def show_biggest(numbers: list) -> None:
    """
    Показывает переданные аргументом числа в консоль и указывает на наибольшее число.
    :param numbers: Список чисел.
    :return: None
    """
    print(f'Получены: {numbers}, наибольшее значение -> {max(numbers)}')


def user_input(numbers_count: int = 3) -> list:
    """
    Считывает "numbers_count" чисел введенных пользователем и возвращает кортеж введенных чисел.
    :param numbers_count: Количество чисел, которое должен будет ввести пользователь.
    :return: Список (list) содержащий числа введенные пользователем.
    """
    users_numbers = []
    for i in range(numbers_count):
        users_numbers.append(int(input(f'Введите {i+1}-е число:\n>>> ')))
    return users_numbers


def main():
    """
    Программа запрашивает у пользователя 3 числа, после чего выводит в консоль наибольшее из них.
    :return: None
    """
    show_biggest(user_input())


if __name__ == '__main__':
    main()
