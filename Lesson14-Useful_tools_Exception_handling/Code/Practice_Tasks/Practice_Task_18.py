# Практическое задание №17:
# Напишите функцию, которая принимает на вход список. Функция создает из этого списка новый
# список из квадратных корней чисел (если число положительное) и самих чисел (если число
# отрицательное) и возвращает результат (желательно применить генератор и тернарный оператор
# при необходимости). В результате работы функции исходный список не должен измениться.

# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]

# Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить
# туда отрицательные числа. 10-20 чисел в списке вполне достаточно.


import math
import random


def get_list_satisfying_conditions(source_list) -> list:
    return [number if number < 0 else int(math.sqrt(number)) for number in source_list]


def get_numbers_sequence(l_bound: int = -100, u_bound: int = 100, length: int = 20) -> list:
    return [random.randint(l_bound, u_bound) for i in range(length)]


def main():
    my_list = get_numbers_sequence(-16, 16, 5)
    # my_list = [1, -3, 4]
    print(f'Source list[{my_list}]')
    result = get_list_satisfying_conditions(my_list)
    print(f'Source list[{my_list}] -> do not changed!'
          f'\nResult list[{result}]')


if __name__ == '__main__':
    main()
