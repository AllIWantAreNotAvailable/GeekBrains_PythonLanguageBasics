# Обычная строка:
rus_str = 'Привет, мир!'

byte_string = rus_str.encode('utf-8')
print(byte_string, '->', type(byte_string))

# При декодировании важно использовать туже систему кодировке,
# которая использовалась при кодировании:
decoded_string = byte_string.decode('utf-8')
print(decoded_string, '->', type(decoded_string))
