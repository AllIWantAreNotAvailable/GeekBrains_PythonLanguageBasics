def show(intro: str, sours_list: list, filtered_list: list):
    print(f'{intro}\n{sours_list} --> {filtered_list}\n')


# набор чисел от 1 до 8 -->
numbers = list(range(9))

# получить только четные числа:
filtered_numbers = filter(lambda el: el % 2 == 0, numbers)
print(filtered_numbers, type(filtered_numbers))

show(intro='Отфильтруем только четные:',
     sours_list=numbers,
     filtered_list=list(filtered_numbers)
     )


# Набор строк -->
names = ['Max', 'Leo', 'Kate']

# получить строки длиннее 3-х символов:
show(intro='Строки длиннее 3-х символов:',
     sours_list=names,
     filtered_list=list(filter(lambda el: 3 < len(el),
                               names)
                        )
     )
