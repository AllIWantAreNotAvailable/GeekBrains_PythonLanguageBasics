# Чтобы объявить пустой список
empty_list = []

# Можно инициализировать списк с элементами
friends = ['Max', 'Leo', 'kate']

# Тип списка – list
print(f'Список friends == {friends}; type(friends) == {type(friends)}')

# Как и строка, список является итерируемым объектом
print('Второй друг:', friends[1])
print('Первый друг с конца:', friends[-1])

# Для списка также доступны срезы
print(friends[1:2])
print(friends[:2])
print(friends[1:])
