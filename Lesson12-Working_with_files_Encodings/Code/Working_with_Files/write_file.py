# Открываем файл на запись, директива 'w' – файла не существует
file = open('first..txt', 'w')

file.write('1. Hello')
file.write(' ')
file.write('2. world')
file.write('\n')

file.write('3. Hello\n')
file.write('4. world\n')

file.writelines(['5. Hello', 'Python'])
file.write('\n')

file.writelines(['6. Hello\n', 'Python\n'])
