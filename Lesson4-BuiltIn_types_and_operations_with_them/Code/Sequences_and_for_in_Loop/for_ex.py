char_m = 'M'
friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')

# operator in
print('i')
if char_m in friend_name:
    print(f'Буква "{char_m}" есть в слове "{friend_name}"')

if friend_name in friends:
    print(f'У меня есть друг {friend_name}!')


# for..in loop
print('\nfor...in loop:')
for char in friend_name:
    print(char)
else:
    print('End for...in\n')

for friend in friends:
    print(friend)
else:
    print('End for...in\n')

for role in roles:
    print(role)
else:
    print('End for...in\n')

# while loop
print('while loop:')
i = 0
while i < len(friend_name):
    char = friend_name[i]
    print(char)
    i += 1
else:
    print('end while\n')

i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1
else:
    print('end while\n')

i = 0
while i < len(roles):
    role = roles[i]
    print(role)
    i += 1
else:
    print('end while\n')
