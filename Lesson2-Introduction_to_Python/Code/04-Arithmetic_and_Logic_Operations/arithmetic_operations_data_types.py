# Математические операции
# Программа "Расчеты нашей жизни#

# Средняя продолжительность жизни в России, лет
ale = 71
age = int(input('Сколько Вам лет?\n>>> '))

# +
after20 = age + 20
print('Через 20 лет Вам будет', after20, 'лет.', '\ntype(after) ==', type(after20))

# -
alive = ale - age
print('По статистике Вам осталось', alive, 'лет жизни', '\ntype(alive) ==', type(alive))

# *
count = 144000000
all_alive = count * ale
print('Среднее время жизни всех людей', all_alive, 'лет', '\ntype(all_alive) ==', type(all_alive))

# /
live_part = age / ale
print('Часть прожитой жизни', live_part * 100, '%', '\ntype(live_part) ==', type(live_part))
# Результат деления всегда будет возвращать тип данных float
