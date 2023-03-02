# Пользователь вводит 3 числа.
# Необходимо найти: максимальное, минимальное их сумму и вывести результаты на экран

numbers = []

for i in range(3):
    number = int(input(f'Введите {i+1}-е число:\n>>> '))
    numbers.append(number)
print()

print(f'Пользователь ввел числа: {numbers}\n'
      f'Максимальное число --> {max(numbers)}\n'
      f'Минимальное число --> {min(numbers)}\n'
      f'Сумма числа --> {sum(numbers)}')
