# 3: Дан список заполненный произвольными целыми числами. Получите новый список,
# элементами которого будут только уникальные элементы исходного.

# Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
# В этом случае ответ будет:
# [5, 8]

numbers_list = [2, 2, 5, 12, 8, 2, 12]
uniq_numbers = []

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number in numbers_list[i + 1:] or number in numbers_list[:i]:
        continue
    else:
        uniq_numbers.append(number)

print(f'{numbers_list} --> {uniq_numbers}')
