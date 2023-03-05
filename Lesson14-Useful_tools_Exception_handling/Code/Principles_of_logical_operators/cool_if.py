# строка
some_string = 'abc'

# Классический способ проверки пустой строки
if len(some_string) != 0:
    print('Строка не пустая')
else:
    print('Строка пустая ;(')


# Удобный способ, который обеспечивает 'логика' Python
if some_string:
    print('Строка не пустая')
else:
    print('Строка пустая ;(')

# Аналогично работает со списками, словарями и др. типами, например:
number = 0
dictionary = {}
listing = []

if number:
    print('Не ноль')
else:
    print('Ноль')

if dictionary:
    print('В словаре что-то есть')
else:
    print('Пустой словарь')

if listing:
    print('В списке что-то есть')
else:
    print('Пустой список')

# А с заполненными
number = 123
dictionary = {1: 'A'}
listing = [1, 2, 3, 4, 5]

if number:
    print('Не ноль')
else:
    print('Ноль')

if dictionary:
    print('В словаре что-то есть')
else:
    print('Пустой словарь')

if listing:
    print('В списке что-то есть')
else:
    print('Пустой список')

