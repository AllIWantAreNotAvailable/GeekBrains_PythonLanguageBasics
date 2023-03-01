# Программа принимает на вход кол-во участников от пользователя. Затем, спрашивает кто занял места от последнего к
# первому. После, выводит список участников отсортированный по алфавиту на экран. В конце, поздравляет победителей,
# которые заняли места с 3 по 1.

print('Соревнования по Python'.upper())
participant_count = int(input('Введите количество участников:\n>>> '))
participant_list = []

while 0 < participant_count:
    participant_list.append(input(f'Кто занял {participant_count} место?\n>>> '))
    participant_count -= 1

print(f'В соревнованиях участвовали: {sorted(participant_list)}')
participant_list.reverse()
print(f'Победители: {participant_list[:3]}. Поздравляем!')
