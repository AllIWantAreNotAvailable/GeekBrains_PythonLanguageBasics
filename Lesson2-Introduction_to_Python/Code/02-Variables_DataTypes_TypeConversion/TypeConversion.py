birthday_year = '1988'
print(type(birthday_year))

period = 20
print(type(period))

# Такая инструкция вызовет ошибку: "TypeError: can only concatenate str (not "int") to str"
#  age = birthday_year + period
# Такая инструкция вызовет ошибку: "TypeError: unsupported operand type(s) for +: 'int' and 'str'
#  age = period + birthday_year

# Причина ошибок: несоответсвие типов данных для операции. Интерпритатор не может выбрать самостоятельно, какую из
# операций проводить: конкатенацию или сложение. В связи с чем, необходимо явлно преобразовать один из операндов к
# нужному типу данных.

age = period + int(birthday_year)
print('Сложение -->', age)
some_string = birthday_year + str(period)
print('Конкатенация --> ', age)
