# 3. Вывод четных от 0 до n

number = 0
n = int(input('Введите n:\n>>> '))

while number <= n:
    if number % 2 != 0:
        number += 1
        continue
    print(number, end=' ')
    number += 1
