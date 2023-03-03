# Практическое задание №4:
# Давайте усложним предыдущее задание.
# Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон
# по формуле:

# damage = damage / armor

# Следовательно, у вас должно быть 2 функции:
# 1) Наносит урон. Это улучшенная версия функции из задачи 3.
# 2) Вычисляет урон по отношению к броне.

# Примечание: Функция номер 2 используется внутри функции номер 1 для вычисления урона
# вычитания его из здоровья персонажа.


import random


def damage_calculation(damage: int, armor: float) -> float:
    return damage / armor


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

        critical_strike = random.randint(0, 50) / 100 + 1
        is_critical_damage = True if 70 < random.randint(0, 100) else False
        player_hit = round(attacker["damage"] * critical_strike if is_critical_damage else attacker["damage"])
        damage = round(damage_calculation(damage=player_hit,
                                          armor=victim["armor"]))
        damage_blocked = player_hit - damage

        victim["health"] = take_damage(damage=damage,
                                       health=victim["health"])
        print(f'Персонаж {attacker["name"]} нанес(а) {victim["name"]} -> '
              f'{player_hit} {"критического " if is_critical_damage else ""}урона.\n'
              f'{victim["name"]} удалось заблокировать {damage_blocked} урона.')
        if victim["health"] < 1:
            print(f'Но этот удар был смертельным для {victim["name"]}...\n')
            return
        print(f'{victim["name"]} потерял {damage} HP, у него(неё) осталось {victim["health"]} HP!\n')


def get_player(bot: bool = False) -> dict:
    """
    Функция возвращает структуру персонажа типа:\n
    - имя ("name");\n
    - здоровье ("health");\n
    - урон ("damage");\n
    - броня ("armor").\n
    :param bot: Если значение True, то возвращает случайного бота, иначе персонажа пользователя.
    :return: type(Структура персонажа) -> <class 'dict'>.
    """
    player = {}
    min_health, max_health = 100, 300
    min_damage, max_damage = 50, 100
    min_armor,  max_armor = 0, 50

    if not bot:
        player["name"] = input('Задайте имя Вашему персонажу:\n>>> ')
    else:
        bot_names = ['Leo', 'Max', 'Anna', 'Alex', 'Ron', 'Kate']
        name_index = random.randint(0, len(bot_names) - 1)
        player["name"] = bot_names[name_index]

    player["health"] = random.randint(min_health, max_health)
    player["damage"] = random.randint(min_damage, max_damage)
    player["armor"] = random.randint(min_armor, max_armor) / 100 + 1

    low_health = player["health"] < 130
    show_health = 'На вид ты какой-то хилый, всего-то' if low_health else 'Да, таких здоровых еще поискать, целых'
    low_damage = player["damage"] < 55
    show_damage = 'Ты меч в руках удержать сможешь?' if low_damage else 'Интересно, твой оппонент не испугается?'
    protection_rate = int(player["armor"] * 100 - 100)

    print(f'Приветствуем тебя, {player["name"]}!\n'
          f'{show_health} {player["health"]} HP!\n'
          f'{"Модный костюмчик!" if 10 < protection_rate else "Какой срам..."} {protection_rate}% защиты.\n'
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
