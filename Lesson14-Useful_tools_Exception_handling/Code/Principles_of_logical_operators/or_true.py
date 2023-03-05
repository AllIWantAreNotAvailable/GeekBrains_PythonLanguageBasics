# Добавление элемента в список

def add_to_list(input_list=None):
    """
    1. Классический способ
    :param input_list:
    :return:
    """
    if input_list is None:
        input_list = []
    input_list.append(2)
    return input_list


def add_to_list_logic(input_list=None):
    """
    Используем свойства логического ИЛИ (or) вместо условия
    :param input_list:
    :return:
    """
    input_list = input_list or []
    input_list.append(2)
    return input_list


def main():
    # 1. Классический способ:
    result = add_to_list([0, 1])
    print(result)

    result = add_to_list()
    print(result)

    # 2. Используя особенности логического ИЛИ (or)
    result = add_to_list_logic([0, 1])
    print(result)

    result = add_to_list_logic()
    print(result)


if __name__ == '__main__':
    main()
