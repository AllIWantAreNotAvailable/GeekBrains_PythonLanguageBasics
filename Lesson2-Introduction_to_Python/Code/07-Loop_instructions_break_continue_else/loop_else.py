# Цикл while
# Вывести числа от 0 до 100

number = 0

while number <= 100:
    print(number, end=' ')
    number += 1
    if number == 33:
        break
else:
    # Блок else в цикле будет выполнятся тогда и только тогда, когда условие цикла стало ложным. Иначе говоря, блок else
    # не будет выполнен, если цикл был прерван инструкцией break
    print()
    print('EndLoop')
print()
print('EndProgram')
