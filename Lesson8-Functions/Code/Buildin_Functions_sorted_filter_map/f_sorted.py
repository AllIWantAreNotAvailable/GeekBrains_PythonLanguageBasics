def show(intro: str, sours_list: list, sorted_list: list):
    print(intro)
    print(f'{sours_list} -> {sorted_list}')
    print()


def by_count(city):
    return city[1]


# набор чисел ->
numbers = [1, 5, 3, 5, 9, 7, 11]

# сортировка по возрастанию:
show(intro='Сортировка по возрастанию:',
     sours_list=numbers,
     sorted_list=sorted(numbers)
     )

# сортировка по убыванию:
show(intro='Сортировка по убыванию:',
     sours_list=numbers,
     sorted_list=sorted(numbers, reverse=True)
     )


# Набор строк ->
names = ['Leo', 'Max', 'Kate', 'Anna', 'Ron', 'Alex']

# сортировка по алфавиту:
show(intro='Сортировка по алфавиту:',
     sours_list=names,
     sorted_list=sorted(names)
     )

# Города и численности населения ->
cities = [
    ('Москва', 1000),
    ('Лас-Вегас', 500),
    ('Антверпен', 2000)
]

# такая сортировка сработает по алфавиту:
show(intro='Такая сортировка сработает по алфавиту:',
     sours_list=cities,
     sorted_list=sorted(cities)
     )


# Как отсортировать по численности?
show(intro='Такая сортировка использует функцию в качестве ключа сортировки:',
     sours_list=cities,
     sorted_list=sorted(cities, key=by_count)
     )

show(intro='Аналогично, только в качестве ключа lambda:',
     sours_list=cities,
     sorted_list=sorted(cities,
                        key=lambda city: city[1]
                        )
     )
