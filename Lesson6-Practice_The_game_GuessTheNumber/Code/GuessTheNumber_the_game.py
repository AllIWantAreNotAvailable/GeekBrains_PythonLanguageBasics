# Шаг 1. Загадать случайное число от 1 до 100
import random
number = random.randint(1, 100)  # [1, 100] -> [1, 2, 3...98, 99, 100]


# Шаг 5. Добавили уровни сложности и возможность выбора уровня сложности
levels = {
    1: 10,
    2: 5,
    3: 3
}
level = int(input('Выбирете уровень сложности: 1, 2 или 3?\n>>> '))
max_count = 1 if level < 1 or 3 < level else level
count = 0


# Шаг 6. Добавляем несколько пользователей (игроков)
players_count = int(input('Введите количество игроков:\n>>> '))
players = []
for i in range(players_count):
    player_name = input(f'Введите имя {i + 1}-го пользователя:\n>>> ')
    players.append(player_name)
is_winner = False
winner_name = ''


# Шаг 4. Организовать цикл до победы пользователя
while not is_winner:
    # Реализация уровней сложности
    count += 1
    if levels[max_count] < count:
        print('\nВы все проиграли... ;\'(')
        break

    # Реализация нескольких пользователей
    for player in players:
        print(f'\nПопытка №{count},', end=' ')
        print(f'ход игрока {player}.\n'
              f'{player},', end=' ')


        # Шаг 2. Предложить пользователю ввести число
        users_number = int(input('введите число:\n>>> '))


        # Шаг 3. Сравнение числе. Вывод результата
        if users_number < number:
            print('Загаданное больше ;\'(')
        elif number < users_number:
            print('Загаданное меньше ;\'(')
        else:
            is_winner = True
            winner_name = player
            break
else:
    print('Победа! :-)\n'
          f'Поздравляем, {winner_name}! <3')
