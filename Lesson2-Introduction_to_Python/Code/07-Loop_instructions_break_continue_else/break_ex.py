# Цикл while
# Задавать вопросы, пока пользователь не введет правильный ответ

name = None

while True:
    name = input('Кто создатель Python?\n>>> ')
    if name == 'Гвидо':
        break
    print('НЕ верно')

print('Верно')
