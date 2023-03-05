# Практическое задание №17:
# Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих
# следующим условиям:
# 1) Элемент кратен 3,
# 2) Элемент положительный,
# 3) Элемент не кратен 4.

# Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
# 10-20 чисел в списке вполне достаточно.


import random


def get_numbers_sequence(l_bound: int = -100, u_bound: int = 100, length: int = 20) -> list:
    return [random.randint(l_bound, u_bound) for i in range(length)]


def get_list_satisfying_conditions(source_list) -> list:
    return [number for number in source_list if number % 3 == 0 and number % 4 != 0 < number]


def main():
    my_randints = get_numbers_sequence(-16, 16, 10)
    print(f'Source list[{my_randints}]')
    result = get_list_satisfying_conditions(my_randints)
    print(f'result list[{result}]')


if __name__ == '__main__':
    main()
