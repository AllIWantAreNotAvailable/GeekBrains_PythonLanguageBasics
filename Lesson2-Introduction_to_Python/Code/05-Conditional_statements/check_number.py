number = 43
value = int(input('Введите число от 1 до 100:\n>>> '))

if 1 <= value <= 100:
    if value == number:
        print('Вы угадали!')
    else:
        if value < number:
            print('Нужно больше')
        else:
            print('Нужно меньше')
else:
    print('Введенное число не входит в оговоренный диапазон')