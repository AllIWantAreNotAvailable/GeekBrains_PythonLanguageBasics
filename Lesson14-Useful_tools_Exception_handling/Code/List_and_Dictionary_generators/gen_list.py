# записать в список только положительные числа
numbers = [1, 2, 3, 4, 5, -1, -2, -3]
result = []

# с использованием цикла (классический способ):
for number in numbers:
    if 0 < number:
        result.append(number)

print(f'С помощью цикла -> {result}')
result.clear()

# через функцию filter():
result = list(filter(lambda x: 0 < x, numbers))
print(f'С помощью функции filter() -> {result}')
result.clear()

# через генератор:
result = [number for number in numbers if 0 < number]
print(f'С использование генератора -> {result}')


