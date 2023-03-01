friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')

# Типы данных
print('\nТипы данных:\n'
      f'type(friend_name) == {type(friend_name)}\n'
      f'type(friends) == {type(friends)}\n'
      f'type(roles) == {type(roles)}')

# Индексация
print('\nИндексация:\n'
      f'friend_name[1] == {friend_name[1]}\n'
      f'friends[1] == {friends[1]}\n'
      f'roles[1] == {roles[1]}')

# Срезы
print('\nСрезы:\n'
      f'friend_name[1:] == {friend_name[1:]}\n'
      f'friends[1:] == {friends[1:]}\n'
      f'roles[1:] == {roles[1:]}')

# Длина
print('\nДлина:\n'
      f'len(friend_name) == {len(friend_name)}\n'
      f'len(friends) == {len(friends)}\n'
      f'len(roles) == {len(roles)}')
