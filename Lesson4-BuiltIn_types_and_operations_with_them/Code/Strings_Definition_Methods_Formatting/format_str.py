# Форматирование строк

name = 'Leo'
age = 30

# 1. Конкатенация (склеивание) строк – не рекомендуется к использованию
hello_str = 'Привет, ' + name + '! Тебе ' + str(age) + ' лет.'
print(hello_str)

# 2. Оператор %
hello_str = 'Привет, %s! Тебе %d лет.' % (name, age)
print(hello_str)

# 3. str.format() – рекомендуется
hello_str = 'Привет, {}! Тебе {} лет.'.format(name, age)
print(hello_str)

# 4. fstring - рекомедуется
hello_str = f'Привет, {name}! Тебе {age} лет.'
print(hello_str)
