# Новые встроенные функции:

# abc – позволяет получить модуль числа
number = -7
modul = abs(number)
print(f'модуль числа {number} --> {modul}\n'
      f'type(modul) --> {type(modul)}')
print()


# min() и max() – позволяют получить минимальное и максимальное значение последовательности
numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
min_num = min(numbers)
max_num = max(numbers)
print(f'numbers --> {numbers}\n'
      f'минимальный элемент --> {min_num}\n'
      f'максимальный элемент --> {max_num}')
print()


# sum() – позволяет просуммировать все элементы последовательности
sum_of_numbers = sum(numbers)
print(f'numbers --> {numbers}\n'
      f'sum(numbers) --> {sum_of_numbers}')
print()


# enumerate()
winners = ['Leo', 'Max', 'Kate']
print(winners)
for number, winner in enumerate(winners, 1):
    print(number, winner)
print()


# round() – позволяет огруглить число с плавающей точкой до указанного знака после запятой
float_num = 123.123456
rounded_num = round(float_num, 2)
print(f'{float_num} --> {rounded_num}')
print()

