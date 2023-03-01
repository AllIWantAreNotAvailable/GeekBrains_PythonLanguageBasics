friends = ['Max', 'Leo', 'Kate']

# Глобальная функция len() используется со всеми итерируемыми объектами
print(f'Список friends == {friends}; len(friends) --> {len(friends)}')

# Чтобы добавить новый элемент в имеющийся список, используется метод list.append()
friends.append('Ron')
print(f'Список friends == {friends}; len(friends) --> {len(friends)}')

# Есть 3 способа удалени элементов из списка:
# 1) Метод list.pop() – удаляет последний из списка и возвращает его значение
last_friend = friends.pop()
print(f'{last_friend} – был удален')
print(f'Список friends == {friends}; len(friends) --> {len(friends)}')

# 2) Метод list.remove() – позволяет удалить элемент "по значению"
friends.remove('Kate')
print(f'Список friends == {friends}; len(friends) --> {len(friends)}')

# 3) Глобальная функция del позволяет удалить элемент из списка "по индексу элемента"
del friends[1]
print(f'Список friends == {friends}; len(friends) --> {len(friends)}')

# Чтобы очистить весь список используется метод list.clear()
friends.clear()
print(f'Список friends == {friends}; len(friends) --> {len(friends)}')
