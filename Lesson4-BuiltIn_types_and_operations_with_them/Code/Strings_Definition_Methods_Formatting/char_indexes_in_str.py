friends_name = 'Максим'

first_char = friends_name[0]
print('В Python отсутсвует тип для символа, отдельный символ будет иметь тип строка.\n'
      f'Первая буква в имени друга "{friends_name}" -–> "{first_char}"; type(first_char) == {type(first_char)}')

print(f'Вторая буква "{friends_name}" -–> "{friends_name[1]}"; type(first_char) == {type(friends_name[1])}')
print(f'Четвертая буква "{friends_name}" -–> "{friends_name[3]}"; type(first_char) == {type(friends_name[3])}')
print(f'Последняя буква "{friends_name}" -–> "{friends_name[-1]}"; type(first_char) == {type(friends_name[-1])}')
print(f'Предпоследняя буква "{friends_name}" -–> "{friends_name[-2]}"; type(first_char) == {type(friends_name[-2])}')
