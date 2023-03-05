# Обычная строка:
some_string = 'Hello, world!'

# Переводим строку в байт с кодировкой ASCII:
byte_string = some_string.encode('ascii')
print(byte_string, '->', type(byte_string))

# При попытке перевода строки в байты важно использовать кодировку,
# которая поддерживает (имеет) символы содержащиеся в строке, например:
rus_str = 'Привет, мир!'
# 1) кодировка ASCII не содержит русских литералов и следующий код
# вызовет исключение 'UnicodeEncodeError':
# byte_string = rus_str.encode('ascii')
# print(byte_string, '->', type(byte_string))
# 2) кодировка UTF-8 содержит русские литералы и следующий код
# не вызовет исключений:
byte_string = rus_str.encode('utf-8')
print(byte_string, '->', type(byte_string))
