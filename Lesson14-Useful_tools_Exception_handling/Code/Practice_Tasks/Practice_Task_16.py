# Практическое задание №16:
# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

# Примечание: Списки фруктов создайте вручную в начале файла.


def get_list_intersections(first_list: list, second_list: list) -> list:
    return [fruit for fruit in first_list if fruit in second_list]


def get_fruits_lists() -> tuple:
    output = (
        ['Авокадо', 'Киви', 'Груша', 'Ананас', 'Банан', 'Яблоко', 'Айва', 'Манго'],
        ['Мандарин', 'Апельсин', 'Гранат', 'Киви', 'Яблоко', 'Груша', 'Банан', 'Виноград', 'Манго',
         'Дыня', 'Нектарин', 'Маракуйя', 'Айва', 'Кокос']
    )
    return output


def main():
    magnit, perekrestok = get_fruits_lists()
    print(f'Фрукты в магазине Магнит: {magnit}\n'
          f'Фрукты в магазине Перекресток: {perekrestok}')
    result = get_list_intersections(magnit, perekrestok)
    print(f'Фрукты, которые есть в обоих магазинах: {result}')


if __name__ == '__main__':
    main()
