# Функция простой разделитель

def get_sep(sep: str, length: int):
    return sep * length


# Меняем знак разделителя (был "-", стал "*")
print(get_sep('-', 100))
print(get_sep('*', 100))


# Меняем знак и длину разделителя (было "-" * 100, стало "*" * 50)
print(get_sep('*', 50))

# Используем разделитель в тексте
sep = get_sep('-', 50)
text = 'Hello {} Func {}'.format(sep, sep)
print(text)
