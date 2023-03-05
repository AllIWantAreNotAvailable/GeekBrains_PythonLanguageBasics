user_input = input('Введите число:\n>>> ')

try:
    number = int(user_input)
    result = 100 / number
except ZeroDivisionError:
    print('Попытка деления на 0!')
except ValueError:
    print(f'Не удалось преобразовать строку "{user_input}" к числу типа int()!')
except Exception:
    print('Непредвиденная ошибка ;(')

print('Конец программы')
