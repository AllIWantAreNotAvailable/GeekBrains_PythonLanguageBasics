user_input = input('Введите число:\n>>> ')

try:
    number = int(user_input)
    result = 100 / number
except ZeroDivisionError as e:
    print('Попытка деления на 0!\n'
          f'Информация об исключении: "{e}"')
except Exception as e:
    print('Непредвиденная ошибка ;(\n'
          f'Информация об исключении: "{e}"')

print('Конец программы')
