# Открываем файл для записи байтов:
with open('bytes.txt', 'wb') as file:
    # пишем строку байт:
    file.write(b'Hello, bytes!')

# Читаем как текст:
with open('bytes.txt', 'r', encoding='ascii') as file:
    # читаем строку байт:
    print(file.read())

# Открываем файл для записи байтов:
with open('bytes.txt', 'wb') as file:
    # пишем строку байт:
    output_string = 'Привет мир'
    file.write(output_string.encode('utf-8'))

# Читаем как текст с кодировкой UTF-8:
with open('bytes.txt', 'r', encoding='utf-8') as file:
    # читаем строку байт:
    print(file.read())
