# Открываем файл для записи байтов:
with open('bytes.txt', 'wb') as file:
    pass

with open('bytes.txt', 'rb') as file:
    pass

# Открываем файл в текстовом режиме с указанием кодировки
with open('bytes.txt', 'r', encoding='utf-8') as file:
    pass
