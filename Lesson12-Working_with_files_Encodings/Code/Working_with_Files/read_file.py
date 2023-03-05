# Открываем файл на чтение, директива 'r' – файл существует
file = open('first..txt', 'r')

# Получаем содержимое файла как 1 строчку
# print(file.read())

# Получаем содержимое файла построчно
# for line in file:
#     print(line.replace('\n', ''))

# Получаем строки файла списком
print(file.readlines())
