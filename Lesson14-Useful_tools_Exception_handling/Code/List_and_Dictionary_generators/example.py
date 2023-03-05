import random


# 1. Создать список состоящий из случайных чисел от 1 до 100:
result_rand = [random.randint(1, 100) for i in range(10)]
print(f'Список состоящий из случайных чисел от 1 до 100 -> {result_rand}')


# 2. Создать список квадратов чисел:
numbers = [1, 2, 3, -4]
result_numbers = [number ** 2 for number in numbers]
print(f'Список квадратов чисел {numbers} -> {result_numbers}')


# 3. Создать список имен на букву "А":
names = ['Руслан', 'Дмитрий', 'Алексей', 'Андрей']
result_names = [name for name in names if name.startswith('А')]
print(f'Список имен на букву "А" из {names} -> {result_names}')
