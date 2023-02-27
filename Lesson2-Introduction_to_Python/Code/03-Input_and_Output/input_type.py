name = input('Как Вас зовут?\n>>> ')
print(type(name))
is_love = input('Вы любите Python?\n>>> ')
print(type(is_love))
age = input('Сколько Вам лет?\n>>> ')
print(type(age))

period = 20
age_period = int(age) + period
print('Через', period, 'Вам будет', age_period)
