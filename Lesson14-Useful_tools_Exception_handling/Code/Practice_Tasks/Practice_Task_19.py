# Практическое задание №19:
# Написать функцию, которая принимает на вход число от 1 до 100. Если число равно 13,
# функция поднимает исключительную ситуации ValueError иначе возвращает введенное число,
# возведенное в квадрат.
# Далее написать основной код программы:
# 1) Пользователь вводит число.
# 2) Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция.
# 3) Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.


def get_square_o_number_between_one_and_hundred(number: int) -> int:
    if number == 13:
        raise ValueError('Число равно 13')
    else:
        return number ** 2


def get_user_number() -> int:
    user_input = input('Введите число от 1 до 100:\n>>> ')
    user_number = int(user_input)
    if not (1 <= user_number <= 100):
        raise ValueError('Пользователь ввел число за пределами диапазона [0...100]')
    else:
        return user_number


def main():
    try:
        num = get_user_number()
        sqrt_num = get_square_o_number_between_one_and_hundred(num)
    except Exception as e:
        print('Что-то пошло не так:', e)
    else:
        print(f'{num}^2 = {sqrt_num}')
    finally:
        print('Конец программы')


if __name__ == '__main__':
    main()
