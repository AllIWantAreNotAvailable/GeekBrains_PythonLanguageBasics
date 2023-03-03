def f():
    print('hello from other f!')


def to(f_param):
    # Параметром будет функция, поэтому в теле функции мы её вызовем
    f_param()


# Проверим
to(f)
