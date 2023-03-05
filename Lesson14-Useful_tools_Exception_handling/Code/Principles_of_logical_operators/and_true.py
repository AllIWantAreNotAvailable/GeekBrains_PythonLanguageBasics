import math


# Есть список чисел
numbers = [4, 1, 2, 3, -4, -2, 7, 16]

# создать список из тех чисел, которые имеют квадратный корень меньше 2 [1, 2, 3]
result =[]

# 1. Обычный способ:
for number in numbers:
    if 0 < number:
        sqrt = math.sqrt(number)
        # проверяем условие sqrt < 2
        if sqrt < 2:
            result.append(number)
print(result)

result.clear()

# 2. С применением логического И (and):
for number in numbers:
    if 0 < number and math.sqrt(number) < 2:
        result.append(number)
print(result)

result.clear()

# в то числе с помощью генератора:
print([number for number in numbers if 0 < number and math.sqrt(number) < 2])
