def change_number_in_list(input_list: list):
    input_list[1] = 200


def main():
    numbers = [1, 2, 3]
    print('Список имеет ссылочный тип данных, это значит, если мы изменим переданный как '
          'аргумент список в функции то он изменится и в месте инициализации:')
    print('Исходный список ->', numbers)
    change_number_in_list(numbers)
    print('Список после работы функции ->', numbers)


if __name__ == '__main__':
    main()
