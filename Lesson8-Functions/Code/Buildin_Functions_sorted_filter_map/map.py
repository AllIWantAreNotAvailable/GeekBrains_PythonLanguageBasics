numbers = list(range(2, 9))

# получить список элементов возведенных в квадрат:
print(list(map(lambda x: x ** 2, numbers)))

# привести числа к строке:
print(list(map(lambda el: str(el), numbers)))
