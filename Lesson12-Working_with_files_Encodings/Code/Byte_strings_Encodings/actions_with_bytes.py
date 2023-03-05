# Обычная строка:
some_string = 'Hello, world'

# Строка байт:
byte_string = b'Hello, bytes'

# Обращение по индексу:
print(f'Обращение по индексу [1] к строке "{some_string}" -> {some_string[1]}')
print(f'Обращение по индексу [1] к строке байт {byte_string} -> {byte_string[1]}')

# Стрезы:
print(f'Срез [1:3] строки "{some_string}" -> {some_string[1:3]}')
print(f'Срез [1:3] строки байт {byte_string} -> {byte_string[1:3]}')

# Перебор в цикле:
print(f'Перебор в цикле строки {some_string} ->', end=' ')
for char in some_string:
    print(char, end='')
print()

print(f'Перебор в цикле строки байт {byte_string} ->', end=' ')
for char in byte_string:
    print(char, end=' ')
print()
