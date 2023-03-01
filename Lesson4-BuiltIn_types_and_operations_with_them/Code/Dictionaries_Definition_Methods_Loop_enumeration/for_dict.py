# for..in loop with Dict
friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}

# Перебор по ключам
print('Перебор по ключам\n'
      'for var in dict.keys():')
for key in friend.keys():
    print('\tkey -->', key)
    print('\tfriend[key] ==', friend[key])
print()

print('Перебор по ключам\n'
      'for var in dict:')
for key in friend:
    print('\tkey -->', key)
    print('\tfriend[key] ==', friend[key])
print()
print()

# Перебор по значениям
print('Перебор по значениям\n'
      'for var in dict.values():')
for value in friend.values():
    print('\tvalues -->', value)
print()

# Перебор по ключам и значениям
print('Перебор по ключам и значениям с помощью переменной типа tuple\n'
      'for var in dict.items():')
for item in friend.items():
    print(f'\t{item}')
    print(f'\titem[0] --> {item[0]} == item[1] --> {item[1]}')
print()

print('Перебор по ключам и значениям с помощью 2-х переменных\n'
      'for var1, var2 in dict.items():')
for key, value in friend.items():
    print(f'\tkey --> {key} == value --> {value}')