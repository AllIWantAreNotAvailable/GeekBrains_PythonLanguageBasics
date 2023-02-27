# Математические операции
# Программа "Расчеты нашей жизни#

# Средняя продолжительность жизни в России, лет
ale = 71
age = int(input('Сколько Вам лет?\n>>> '))

# /
live_part = age / ale
# Результат деления всегда будет возвращать тип данных float
print('Часть прожитой жизни', live_part * 100, '%', '\ntype(live_part) ==', type(live_part))

# // – целая часть от деления
integer_part = age // ale
print('integer_part ==', integer_part, '\ntype(integer_part) ==', type(integer_part))

# % – остаток от деления
float_point_of_division = 3 % 2
print('float_point_of_division ==', float_point_of_division, '; type(float_point_of_division) ==',
      type(float_point_of_division))
float_point_of_division = 4 % 2
print('float_point_of_division ==', float_point_of_division, '; type(float_point_of_division) ==',
      type(float_point_of_division))
float_point_of_division = 5 % 3
print('float_point_of_division ==', float_point_of_division, '; type(float_point_of_division) ==',
      type(float_point_of_division))

# ** – возведение в степень
powered = 2 ** 10
print('powered ==', powered, '; type(powered) ==', type(powered))
powered = 2 ** 2
print('powered ==', powered, '; type(powered) ==', type(powered))
