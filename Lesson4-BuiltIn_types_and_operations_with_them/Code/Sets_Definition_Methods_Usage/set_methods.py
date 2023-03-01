# Ининциализация множества
cities = {'Las Vegas', 'Paris', 'Moscow'}
print(cities)
print()

# Добавление элемента во множество
cities.add('Burma')
print(cities)
print()

# Если попытаться добавить значение, которое уже содержится во множестве, то ничего не произойдет
cities.add('Moscow')
print(cities)
print()

# Удалиение элемента из множества
cities.remove('Moscow')
print(cities)
print()