GLOBAL_VAR = 2


def my_f():
    result = GLOBAL_VAR ** 5
    print(result)


def my_change_f():
    global GLOBAL_VAR
    GLOBAL_VAR = 'Какая-то строка'


# my_change_f()
my_f()