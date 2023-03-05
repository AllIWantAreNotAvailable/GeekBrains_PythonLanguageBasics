# Открываем файл для записи байтов:
with open('bytes.txt', 'wb') as file:
    # пишем строку байт
    output_string = 'Привет мир'
    file.write(output_string.encode('utf-8'))

# Открываем файл в режиме чтения байтов
with open('bytes.txt', 'rb') as file:
    # читаем байты:
    result = file.read()
    print(result, '->', type(result))
    # декодируем для получения строки
    some_string = result.decode('utf-8')
    print(some_string, '->', type(some_string))

# Открываем файл для записи:
with open('bytes.txt', 'w', encoding='utf-8') as file:
    # пишем строку:
    output_string = 'Привет мир'
    file.write(output_string)

# Открываем файл в режиме чтения байтов
with open('bytes.txt', 'rb') as file:
    # читаем байты:
    result = file.read()
    print(result, '->', type(result))
    # декодируем для получения строки
    some_string = result.decode('utf-8')
    print(some_string, '->', type(some_string))
