# В зависимости от параметра вызвать различные функции скрипта:
# 1) Параметр ping -> функция выводит pong;
# 2) Параметры name <Имя> -> функция приветсвует пользователя по имени;
# 3) Параметр list -> функция показывает содержимое текущей директории.


import sys, os


def ping():
    print('pong')


def hello(name):
    print(f'Hello, {name}!')


def get_info():
    print(os.listdir())


command = sys.argv[1]

if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[2]
    hello(name)
