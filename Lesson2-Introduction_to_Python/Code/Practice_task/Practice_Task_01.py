# Практическое задание №1:
# Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран. Если
# возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

user_number = int(input('Введите число:\n>>> '))
number_plus_two = user_number + 2
print(f'Вы ввели {user_number}.\n{user_number} + 2 = {number_plus_two}')