# Когда поможет range()

winners = ['Max', 'Leo', 'Kate']
print(winners)
print()
# Простой перебор
for winner in winners:
    print(winner)
print()

# Что делать, если нужно вывести позицию победителя?
# Использовать while loop или есть способ лучше?

# while loop
i = 0
print('winners with place and while loop:')
while i < len(winners):
    print(f'{i+1}. {winners[i]}')
    i += 1
else:
    print('End while')
print()

# for...in range() loop
print('for...in range() loop:')
for i in range(len(winners)):
    print(f'{i + 1}. {winners[i]}')
else:
    print('End for...in')
print()


# Вывести нечетные цифры от 1 до 5
numbers = [1, 3, 5]
print(numbers)
print()
for number in numbers:
    print(number)
print()

# Как это сделать, если цифр будет 100 или 1000?
# Использовать while loop или есть способ лучше?
print('odd numbers below 5 with while loop:')
upper_bound = 5
i = 0
while i <= upper_bound:
    if i % 2 != 0:
        print(i)
    i += 1
else:
    print('End while')
print()

print('for...in range() loop:')
for i in range(upper_bound + 1):
    if i % 2 != 0:
        print(i)
else:
    print('End for...in')
print()

# альтернатива:
print('Более красивый способ с использованием range() и приведением к типу list\n'
          f'list(range(1, 100, 2) --> {list(range(1, 50, 2))}')
