friend = 'Максим Леонид'
print(friend)

# Длину итерируемых объектов (коллекций) можно получить при помощи глобальной функции len()
print(f'Длина строки "{friend}" ==', len(friend))

# Чтобы найти подстроку в строке, можно воспользоваться методом str.find()
print(f'Подстрока "Лео" в строке "{friend}" начинается с индекса: {friend.find("Лео")}')
print('Если искомой подстроки нет в строке поиска, то str.find() вернет индекс -1\n'
      f'Например, найдем подстроку "Николай" в строке "{friend}" -> {friend.find("Николай")}')

# Метод str.split() разделяет строку в list() подстрок по указанному разделителю,
# если разделитель не указан, то по умолчанию в качестве разделителя используется символ пробела.
print(friend.split())

# Метод str.isdigit() определяет, состоит ли строка только из цифр
int_string = '123'
int_below_zero_string = '-123'
float_string = '123.123'
float_below_zerow_string= '-123.123'

print('Метод str.isdigit() определяет, состоит ли строка только из цифр, например:\n'
      f'"Максим Леонид" --> {friend.isdigit()}\n'
      f'"123" --> {int_string.isdigit()}\n'
      f'"-123" --> {int_below_zero_string.isdigit()}\n'
      f'"123.123" --> {float_string.isdigit()}\n'
      f'"-123.123" --> {float_string.isdigit()}\n')

# Метод str.upper() приводит строку к верхнему регистру
print(friend.upper())

# Метод str.lower() приводит строку к нижнему регистру
print(friend.lower())