# Практическое задание №3:
# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
#
# Поэкспериментируйте со значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.


import random


def take_damage(damage: float, health: int) -> int:
    return int(health - damage)


def fight(player1: dict, player2: dict):
    attacker = player1
    victim = player2
    flag = True

    while 0 < attacker["health"] and 0 < victim["health"]:
        if flag:
            attacker = player1
            victim = player2
        else:
            attacker = player2
            victim = player1
        flag = not flag

        victim["health"] = take_damage(damage=attacker["damage"],
                                       health=victim["health"])
        print(f'Персонаж {attacker["name"]} нанес(а) {victim["name"]} -> {attacker["damage"]} урона,')
        if victim["health"] < 1:
            print(f'этот удар был смертельным для {victim["name"]}...\n')
            return
        print(f'у {victim["name"]} осталось {victim["health"]} HP!\n')


def get_player(bot: bool = False) -> dict:
    """
    Функция возвращает структуру персонажа типа:\n
    - имя ("name");\n
    - здоровье ("health");\n
    - урон ("damage").\n
    :param bot: Если значение True, то возвращает случайного бота, иначе персонажа пользователя.
    :return: type(Структура персонажа) -> <class 'dict'>.
    """
    player = {}
    min_health, max_health = 80, 200
    min_damage, max_damage = 25, 75

    if not bot:
        player["name"] = input('Задайте имя Вашему персонажу:\n>>> ')
    else:
        bot_names = ['Leo', 'Max', 'Anna', 'Alex', 'Ron', 'Kate']
        name_index = random.randint(0, len(bot_names) - 1)
        player["name"] = bot_names[name_index]

    player["health"] = random.randint(min_health, max_health)
    player["damage"] = random.randint(min_damage, max_damage)

    low_health = player["health"] < 130
    show_health = 'На вид ты какой-то хилый, всего-то' if low_health else 'Да, таких здоровых еще поискать, целых'
    low_damage = player["damage"] < 55
    show_damage = 'Ты меч в руках удержать сможешь?' if low_damage else 'Интересно, твой оппонент не испугается?'

    print(f'Приветствуем тебя, {player["name"]}!\n'
          f'{show_health} {player["health"]} HP!\n'
          f'{show_damage} Урон -> {player["damage"]}\n')
    return player


def main() -> None:
    """
    Программа создает 2-х персонажей:\n
    - одного для пользователя;\n
    - другого для бота.\n
    Персонажи сражаются пока здоровье одного из них не достигнет 0.
    :return: None
    """
    player = get_player()
    enemy = get_player(bot=True)

    fight(player, enemy)

    player_alive = 0 < player["health"]
    enemy_alive = 0 < enemy["health"]

    if player_alive or enemy_alive:
        if player_alive:
            winner = player
        else:
            winner = enemy
        print(f'Поздравляем с победой, {winner["name"]}!')
    else:
        print('В схватке пали оба ;(')


if __name__ == '__main__':
    main()
