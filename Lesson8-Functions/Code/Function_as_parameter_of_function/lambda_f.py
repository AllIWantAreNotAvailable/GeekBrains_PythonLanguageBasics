def my_filter(numbers: list, condition) -> list:
    """
    Отберет числа из списка согласно переданному условию отбора и вернет их списком.
    :param numbers: Список чисел.
    :param condition: Функция с условием отбора значений.
    :return: Вернет list заполненный только четными числами из параметра numbers.
    """
    result = []
    for number in numbers:
        if condition(number):
            result.append(number)
    return result


def get_list_of_numbers(length: int) -> list:
    """
    Возвращает числовой ряд от 0 до N не включительно.
    :param length: Длина диапазона целых чисел.
    :return: Вернет list заполненный диапазоном целых чисел [0...length).
    """
    return list(range(length))


def main() -> None:
    """
    Главная функция.
    :return: None
    """
    length_of_list = int(input('Введите длину списка:\n>>> '))

    print('Отбираем только четные:')
    my_list_of_numbers = get_list_of_numbers(length_of_list)
    print(f'{my_list_of_numbers}', end=' -> ')
    even_numbers = my_filter(numbers=my_list_of_numbers,
                             condition=lambda number: number % 2 == 0
                             )
    print(even_numbers)

    print('Отбираем только нечетные:')
    my_list_of_numbers = get_list_of_numbers(length_of_list)
    print(f'{my_list_of_numbers}', end=' -> ')
    even_numbers = my_filter(numbers=my_list_of_numbers,
                             condition=lambda number: number % 2 != 0
                             )
    print(even_numbers)

    print('Отбираем только больше чем 4:')
    my_list_of_numbers = get_list_of_numbers(length_of_list)
    print(f'{my_list_of_numbers}', end=' -> ')
    even_numbers = my_filter(numbers=my_list_of_numbers,
                             condition=lambda number: 4 < number
                             )
    print(even_numbers)


if __name__ == '__main__':
    main()
