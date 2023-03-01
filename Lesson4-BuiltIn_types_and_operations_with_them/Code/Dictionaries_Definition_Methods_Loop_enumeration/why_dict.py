friends = ['Max', 'Leo', 'Kate']

print(f'Список friends == {friends}\n'
      f'type(friends) == {type(friends)}\n'
      f'Первый элемент списка == {friends[0]}\n'
      f'type(friends[0]) == {type(friends[0])}')
print()


# Как добавить другу возраст?

# Пустой словарь может быть инициализирован {}
empty_dict = {}

print(f'Словарь empty_dict == {empty_dict}\n'
      f'type(empty_dict) == {type(empty_dict)}')
print()

# Инициализация словаря с элементами:
friend = {
    'name': 'Max',
    'age': 23
}

print(f'Словарь friends == {friend}\n'
      f'type(friend) == {type(friend)}')
print()


# Обращение по ключу:
print('Значение элемента можно получить по ключу:\n'
      f'friend["name"] == {friend["name"]}\n'
      f'friend["age"] == {friend["age"]}')
print()


# Добавление пары ключ-значение
print('Добавление пары ключ-значение:\n'
      'friend["has_car"] = True')
friend['has_car'] = True

print(f'Словарь friends == {friend}\n'
      f'type(friend) == {type(friend)}')
print()


# Изменени значения элемента словаря:
print('Изменени значения элемента словаря'
      'friend["has_car"] = False')
friend['has_car'] = False

print(f'Словарь friends == {friend}\n'
      f'type(friend) == {type(friend)}')
print()


# Удаление элемента словаря
print('Удаление элемента словаря'
      'del friend["age"]')
del friend["age"]

print(f'Словарь friends == {friend}\n'
      f'type(friend) == {type(friend)}')
print()


# Оператор in проверяет есть ли ключ в словаре
print('Оператор in проверяет есть ли ключ в словаре\n'
      f'"age" in friend --> {"age" in friend}\n'
      f'"has_car" in friend --> {"has_car" in friend}')
