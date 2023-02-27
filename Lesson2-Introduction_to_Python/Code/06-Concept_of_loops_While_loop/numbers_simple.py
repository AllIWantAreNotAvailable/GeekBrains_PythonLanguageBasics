# 1. Вывести числа от 0 до 100
increment = 0
upper_bound = 100
while increment <= upper_bound:
    print(increment, end=' ')
    increment += 1
else:
    print()


# 2. Вывести числа от 0 до n, где n вводит пользователь
increment = 0
upper_bound = int(input('Введите верхнюю границу диапазона:\n>>> '))
while increment <= upper_bound:
    print(increment, end=' ')
    increment += 1
else:
    print()


# 3. Вывести четные числа от 0 до n, где n вводит пользователь
increment = 0
upper_bound = int(input('Введите верхнюю границу диапазона:\n>>> '))
while increment <= upper_bound:
    if increment % 2 == 0:
        print(increment, end=' ')
    increment += 1
else:
    print()
